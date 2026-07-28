# -*- coding: utf-8 -*-
"""
verificador.py — El Pensadero · verificador oficial de fichas
Version 1.1 · 2026-07-27

QUE HACE
    Revisa las fichas de tu pensadero contra REGLAS.md y te dice si alguna
    incumple. Termina con SANO o con la lista de problemas. Ademas imprime
    un tablero: cuantas fichas hay y como se reparten.

QUE NO HACE
    No dice si lo que escribiste es VERDAD. Comprueba la FORMA de la ficha:
    que tenga fuente, que los valores sean del vocabulario, que los enlaces
    apunten a fichas que existen. Una ficha perfectamente formada puede
    contener una mentira y este programa dira SANO.

SEGURIDAD — puedes comprobarlo leyendo el codigo
    - Solo LEE archivos. No escribe, no borra, no renombra.
    - No usa red. No importa ninguna libreria de red.
    - No sale de la carpeta que le indiques.
    - Solo usa la libreria estandar de Python.

COMO SE USA
    python3 verificador.py <ruta a Mi_Pensadero>
    python3 verificador.py --autoprueba     comprueba que el propio
                                            verificador detecta fallos

Si quieres estar seguro de que funciona, corre --autoprueba: crea fichas
rotas a proposito en una carpeta temporal y te muestra que las detecta.
Un verificador que solo se ha visto decir SANO no esta probado.
"""
import os, re, sys, tempfile, shutil
from collections import Counter

# En Windows, cuando la salida se guarda en un archivo (que es justo lo que hace
# el lanzador: > ultimo-resultado.txt), Python no escribe en UTF-8 sino en la
# codificacion del sistema, que no conoce caracteres como — o →. El programa
# reventaba con un error de Python EN LUGAR de mostrar los problemas: quien
# tenia las fichas sanas veia SANO, y quien las tenia rotas veia un choque.
# Justo al reves de lo util. Detectado el 2026-07-27 probando el camino de fallo
# con la codificacion real de un Windows en espanol. Se fuerza UTF-8 y, por si
# algun entorno raro lo impide, se sustituye el caracter en vez de reventar.
for _f in (sys.stdout, sys.stderr):
    try:
        _f.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

VERSION = "1.1"
FECHA   = "2026-07-27"

TIPOS   = {"hecho", "definicion", "regla", "procedimiento",
           "decision", "observacion", "principio", "pregunta_abierta"}
ESTADOS = {"tentativo", "vigente", "caduco", "en_conflicto"}
CONF    = {"alta", "media", "baja"}
RELT    = {"apoya", "contradice", "refina", "depende_de", "parte_de", "relacionado"}
FTIPOS  = {"documento", "conversacion", "url", "referencia"}
CAMPOS  = ["id", "tipo", "estado", "confianza", "creado", "actualizado",
           "fuentes", "relaciones", "tags", "reemplazado_por"]


def leer_fichas(raiz):
    carpeta = os.path.join(raiz, "Fichas")
    if not os.path.isdir(carpeta):
        return None, "No encuentro la carpeta 'Fichas' dentro de %s" % raiz
    fichas = {}
    for nombre in sorted(os.listdir(carpeta)):
        if not nombre.endswith(".md"):
            continue
        texto = open(os.path.join(carpeta, nombre), encoding="utf-8").read()
        # El Bloc de notas y varios editores guardan una marca invisible al
        # principio del archivo (BOM). Con ella, la ficha esta perfectamente
        # bien y el revisor decia "no tiene frontmatter": un callejon sin
        # salida, porque lo que sobra no se ve. Se ignora. (2026-07-27)
        texto = texto.lstrip("﻿").replace("\r\n", "\n")
        m = re.match(r"^---\n(.*?)\n---\n?(.*)$", texto, re.S)
        fichas[nombre] = {"fm": m.group(1) if m else None,
                          "cuerpo": (m.group(2) if m else texto)}
    return fichas, None


def campo(fm, nombre):
    m = re.search(r"^%s:[ \t]*(.*)$" % re.escape(nombre), fm, re.M)
    return None if not m else m.group(1).strip()


def verificar(fichas):
    problemas = []
    ids = {n[:-3] for n in fichas}

    for nombre, d in fichas.items():
        def mal(txt):
            problemas.append("%s — %s" % (nombre, txt))

        if d["fm"] is None:
            mal("no tiene frontmatter (el bloque entre --- al principio)")
            continue
        fm = d["fm"]

        for c in CAMPOS:
            if re.search(r"^%s:" % c, fm, re.M) is None:
                mal("le falta el campo '%s'" % c)

        if campo(fm, "id") != nombre[:-3]:
            mal("el 'id' no coincide con el nombre del archivo")
        if campo(fm, "tipo") not in TIPOS:
            mal("tipo invalido: '%s' (usa uno de los ocho)" % campo(fm, "tipo"))
        if campo(fm, "estado") not in ESTADOS:
            mal("estado invalido: '%s' (usa uno de los cuatro)" % campo(fm, "estado"))
        if campo(fm, "confianza") not in CONF:
            mal("confianza invalida: '%s' (alta, media o baja)" % campo(fm, "confianza"))

        if not re.search(r"^fuentes:\s*\n\s+-\s+tipo:", fm, re.M):
            mal("SIN FUENTE — la procedencia es obligatoria, sin fuente no hay ficha")

        for t in re.findall(r"^\s+-\s+tipo:\s*(\w+)\s*\n\s+ref:", fm, re.M):
            if t not in FTIPOS:
                mal("tipo de fuente invalido: '%s'" % t)

        for t in re.findall(r"^\s+-\s+tipo:\s*(\w+)\s*\n\s+ficha:", fm, re.M):
            if t not in RELT:
                mal("tipo de relacion invalido: '%s'" % t)

        for destino in re.findall(r"^\s+ficha:\s*(.+)$", fm, re.M):
            destino = destino.strip()
            if destino and destino not in ids:
                mal("enlaza a una ficha que no existe: '%s'" % destino)

        if campo(fm, "estado") == "caduco" and not campo(fm, "reemplazado_por"):
            mal("esta caduca pero no dice en 'reemplazado_por' cual la sucede")

        # --- REGLA 4: el protocolo de conflicto ---------------------------
        # Se agrego en v1.1. Antes el verificador validaba forma pero NO
        # comprobaba la regla mas importante del kit: la unica sin vigilancia.
        estado = campo(fm, "estado")
        rels = re.findall(r"^\s+-\s+tipo:\s*(\w+)\s*\n\s+ficha:\s*(.+)$", fm, re.M)
        contradice = [dst.strip() for t, dst in rels if t == "contradice"]
        if estado == "en_conflicto" and not contradice:
            mal("esta 'en_conflicto' pero no dice con cual ficha choca "
                "(le falta una relacion 'contradice')")
        # OJO con esta condicion. La regla 4d dice que al resolverse la que GANA
        # vuelve a 'vigente' y la que pierde queda 'caduco' — y la relacion
        # 'contradice' NO se borra, porque el pensadero conserva la historia.
        # La version anterior exigia 'en_conflicto' a secas y por tanto marcaba
        # como error el estado final que las propias reglas prescriben: quien
        # resolvia bien recibia un aviso de que estaba mal. Se probo el
        # 2026-07-28 simulando el protocolo entero. Ahora el conflicto solo
        # sigue abierto si la otra parte no esta 'caduco'.
        if contradice and estado not in ("en_conflicto", "caduco"):
            abiertos = [dst for dst in contradice
                        if campo((fichas.get(dst + ".md") or {}).get("fm") or "",
                                 "estado") != "caduco"]
            if abiertos:
                mal("dice que contradice a '%s' y esa ficha sigue viva, pero su "
                    "estado es '%s': hasta que decidas, ambas van 'en_conflicto'"
                    % (abiertos[0], estado))

        cuerpo = d["cuerpo"].strip()
        if not cuerpo:
            mal("no tiene cuerpo — falta la idea en una frase")
        else:
            primera = next((l for l in cuerpo.splitlines() if l.strip()), "")
            if primera.startswith("#") or primera.startswith(">"):
                mal("el cuerpo no empieza con la idea en una frase afirmativa")
        if "## Evidencia" not in cuerpo:
            mal("al cuerpo le falta la seccion '## Evidencia'")
        if "## Contexto" not in cuerpo:
            mal("al cuerpo le falta la seccion '## Contexto'")

    # --- REGLA 4, segunda parte: mirar el conjunto, no cada ficha aislada ---
    def relaciones(nombre):
        fm = fichas[nombre]["fm"] or ""
        return re.findall(r"^\s+-\s+tipo:\s*(\w+)\s*\n\s+ficha:\s*(.+)$", fm, re.M)

    en_conflicto = [n for n in fichas
                    if campo(fichas[n]["fm"] or "", "estado") == "en_conflicto"]
    for nombre in fichas:
        for t, dst in relaciones(nombre):
            if t != "contradice":
                continue
            dst = dst.strip()
            if dst + ".md" not in fichas:
                continue      # ya lo reporto el chequeo de enlaces rotos
            vuelta = [d.strip() for tt, d in relaciones(dst + ".md") if tt == "contradice"]
            if nombre[:-3] not in vuelta:
                problemas.append("%s — contradice a '%s', pero esa ficha no lo dice "
                                 "de vuelta (la contradiccion debe ser mutua)"
                                 % (nombre, dst))

    if en_conflicto:
        hay_pregunta = any(campo(fichas[n]["fm"] or "", "tipo") == "pregunta_abierta"
                           and campo(fichas[n]["fm"] or "", "estado") != "caduco"
                           for n in fichas)
        if not hay_pregunta:
            problemas.append("hay %d ficha(s) en conflicto y ninguna 'pregunta_abierta' "
                             "abierta que describa el choque (regla 4b)" % len(en_conflicto))

    return problemas


def tablero(fichas):
    tipos, estados, conf, proyectos = Counter(), Counter(), Counter(), Counter()
    sueltas = []
    for nombre, d in fichas.items():
        fm = d["fm"] or ""
        tipos[campo(fm, "tipo")] += 1
        estados[campo(fm, "estado")] += 1
        conf[campo(fm, "confianza")] += 1
        # el primer tag es el proyecto (regla del kit)
        m = re.search(r"^tags:\s*\[(.*?)\]", fm, re.M)
        if m and m.group(1).strip():
            proyectos[m.group(1).split(",")[0].strip().lower()] += 1
        if not re.search(r"^\s+ficha:\s*\S", fm, re.M):
            sueltas.append(nombre)
    print("\nTABLERO")
    print("  fichas:          %d" % len(fichas))
    print("  por tipo:        %s" % dict(tipos))
    print("  por estado:      %s" % dict(estados))
    print("  por confianza:   %s" % dict(conf))
    if proyectos:
        print("  por proyecto:    %s" % dict(proyectos))
    print("  sin conexion:    %d%s" % (len(sueltas),
          ("  → " + ", ".join(s[:40] for s in sueltas[:5])) if sueltas else ""))


def informe(raiz):
    print("=" * 72)
    print("EL PENSADERO · verificador %s (%s)" % (VERSION, FECHA))
    print("=" * 72)
    print("Leyendo (solo lectura): %s/Fichas/*.md" % raiz)
    fichas, error = leer_fichas(raiz)
    if error:
        print("\n" + error)
        return 2
    if not fichas:
        print("\nNo hay fichas todavia. Nada que revisar.")
        return 0
    problemas = verificar(fichas)
    print("\nVERIFICADOR")
    if problemas:
        print("  %d problema(s):" % len(problemas))
        for p in problemas:
            print("   - %s" % p)
    else:
        print("  SANO")
        print("  (forma correcta; este programa no juzga si el contenido es cierto)")
    tablero(fichas)
    return 1 if problemas else 0


# --------------------------------------------------------------------------
FICHA_OK = """---
id: %s
tipo: hecho
estado: vigente
confianza: alta
creado: 2026-07-27
actualizado: 2026-07-27
fuentes:
  - tipo: conversacion
    ref: "prueba interna"
relaciones:
  - tipo: relacionado
    ficha: %s
tags: [prueba]
reemplazado_por:
---

Una afirmacion de prueba.

## Evidencia
Texto de prueba.

## Contexto
Texto de prueba.
"""


def autoprueba():
    """Rompe el verificador a proposito. Si no detecta cada fallo, no sirve."""
    print("=" * 72)
    print("AUTOPRUEBA — el verificador debe DETECTAR fichas rotas")
    print("=" * 72)
    tmp = tempfile.mkdtemp(prefix="pensadero_autoprueba_")
    ok = True
    try:
        # (etiqueta, como romper la ficha A, como romper la B, debe detectarse)
        nada = lambda s: s
        casos = [
            ("ficha correcta",            lambda s: s,                                              False),
            # Guardada con el Bloc de notas (marca invisible) o con finales de
            # linea de Windows: la ficha esta BIEN y no debe dar problema.
            ("ficha correcta con BOM",    lambda s: "﻿" + s,                                   False),
            ("ficha correcta con CRLF",   lambda s: s.replace("\n", "\r\n"),                        False),
            ("sin fuente",                lambda s: re.sub(r'fuentes:\n  - tipo: conversacion\n    ref: "prueba interna"', "fuentes:", s), True),
            ("tipo inventado",            lambda s: s.replace("tipo: hecho", "tipo: apunte", 1),    True),
            ("estado inventado",          lambda s: s.replace("estado: vigente", "estado: borrador"), True),
            ("confianza inventada",       lambda s: s.replace("confianza: alta", "confianza: total"), True),
            ("relacion inventada",        lambda s: s.replace("tipo: relacionado", "tipo: parecida"), True),
            ("enlace a ficha inexistente", lambda s: re.sub(r"ficha: 2026\d+-b", "ficha: 20260101-no-existe", s), True),
            ("caduca sin reemplazo",      lambda s: s.replace("estado: vigente", "estado: caduco"),  True),
            ("id que no coincide",        lambda s: s.replace("id: 20260727-a", "id: 20260727-otro"), True),
            ("falta un campo",            lambda s: s.replace("tags: [prueba]\n", ""),               True),
            ("cuerpo sin Evidencia",      lambda s: s.replace("## Evidencia\nTexto de prueba.\n\n", ""), True),
            ("cuerpo sin Contexto",       lambda s: s.replace("## Contexto\nTexto de prueba.\n", ""), True),
            ("sin cuerpo",                lambda s: s.split("---\n")[0] + "---\n" + s.split("---\n")[1] + "---\n", True),
        ]
        # --- REGLA 4: cada comprobacion nueva con su prueba negativa -------
        conflicto = lambda s: s.replace("estado: vigente", "estado: en_conflicto")
        contra    = lambda s: s.replace("tipo: relacionado", "tipo: contradice")
        casos += [
            ("en_conflicto sin contradice",  conflicto,                nada,  True),
            ("contradice no mutuo",          lambda s: contra(conflicto(s)), nada, True),
            ("contradice estando vigente",   contra,                   contra, True),
            ("conflicto sin pregunta_abierta",
             lambda s: contra(conflicto(s)), lambda s: contra(conflicto(s)), True),
            # EL CAMINO BUENO DE LA REGLA 4, que nadie probaba: cuando el
            # conflicto se resuelve como manda 4d —la que pierde a 'caduco'
            # con su reemplazado_por, la que gana de vuelta a 'vigente'— el
            # verificador NO debe protestar. Hasta el 2026-07-28 protestaba:
            # castigaba a quien seguia las reglas al pie de la letra.
            ("conflicto resuelto segun la regla 4d",
             lambda s: contra(s).replace("estado: vigente", "estado: caduco")
                                .replace("reemplazado_por:", "reemplazado_por: 20260727-b"),
             contra, False),
        ]
        casos = [(c[0], c[1], nada, c[2]) if len(c) == 3 else c for c in casos]

        for etiqueta, romper, romper_b, debe_fallar in casos:
            caso = os.path.join(tmp, re.sub(r"\W+", "_", etiqueta), "Fichas")
            os.makedirs(caso)
            a = FICHA_OK % ("20260727-a", "20260727-b")
            b = FICHA_OK % ("20260727-b", "20260727-a")
            open(os.path.join(caso, "20260727-a.md"), "w", encoding="utf-8").write(romper(a))
            open(os.path.join(caso, "20260727-b.md"), "w", encoding="utf-8").write(romper_b(b))
            fichas, _ = leer_fichas(os.path.dirname(caso))
            hay = bool(verificar(fichas))
            bien = (hay == debe_fallar)
            ok = ok and bien
            print("  [%s] %-28s %s" % ("OK   " if bien else "FALLA", etiqueta,
                                       "detectado" if hay else "sin problemas"))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("-" * 72)
    # Los dos numeros se CUENTAN. Antes se restaba 1 al total dando por hecho
    # que solo habia un caso sano; al agregar dos casos sanos mas, el programa
    # empezo a anunciar 18 fallos cuando probaba 16. (2026-07-27)
    n_malos = sum(1 for c in casos if c[3])
    n_sanos = len(casos) - n_malos
    print("AUTOPRUEBA:", ("PASA — detecta los %d fallos y no marca ninguna de las %d fichas correctas"
                          % (n_malos, n_sanos)) if ok else "FALLA — el verificador no es de fiar")
    return 0 if ok else 1


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)
    if args[0] == "--autoprueba":
        sys.exit(autoprueba())
    sys.exit(informe(os.path.abspath(args[0])))
