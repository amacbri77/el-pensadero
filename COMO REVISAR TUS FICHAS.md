# Cómo revisar tus fichas
*Kit v1.1 · 2026-07-27*

Hay tres formas. **Elige una.** No necesitas las otras.

> **Antes que nada: esto es opcional.** Tu pensadero funciona sin revisarlo nunca.
> El revisor sirve para detectar fichas mal formadas cuando ya tengas veinte o
> treinta y se te haga difícil mirarlas una por una. Si recién empiezas, sáltate
> esta página entera y vuelve en unas semanas.

> **Dónde está tu pensadero.** Esta carpeta es el **kit**: la instalación.
> Tu pensadero vive **aparte**, junto a tus proyectos. Cuando el revisor te
> pregunte por la carpeta, es esa la que tienes que indicarle.

---

## Forma 1 · Que lo haga tu IA (la más fácil)

Si usas una IA **con acceso a tus carpetas**, no toques nada. Pégale esto:

> En la carpeta del kit hay un archivo `verificador.py`. Léelo primero y confírmame que solo lee archivos y no usa internet. Después ejecútalo sobre mi carpeta `Mi_Pensadero` y muéstrame el resultado tal cual, sin resumirlo.

Listo. No hay paso 2.

---

## Forma 2 · Doble clic

En la carpeta del kit hay dos archivos:

| Si usas | Haz doble clic en |
|---|---|
| **Windows** | `Verificar (Windows).bat` |
| **Mac** | `Verificar (Mac).command` |

Se abre una ventana negra y **te pregunta dónde está tu pensadero**.

- **En Windows** puedes además **arrastrar tu carpeta `Mi_Pensadero` encima del archivo `.bat`** y se salta la pregunta.
- **En Mac**, cuando te pregunte, arrastra la carpeta dentro de la ventana negra y pulsa Enter. La ruta se escribe sola.
- Si prefieres probar primero con el ejemplo que trae el kit, escribe `ejemplo/Mi_Pensadero`.

Al terminar verás el resultado y **quedará guardado en `ultimo-resultado.txt`**, dentro de la carpeta del kit. Así no se pierde al cerrar la ventana: si te salieron varios problemas, los tienes ahí para irlos arreglando con calma.

**Los dos archivos tienen unas doce líneas.** Ábrelos con el Bloc de notas o TextEdit antes de usarlos: verás que solo llaman al revisor y guardan el resultado. Es exactamente lo que este kit te pide que hagas siempre antes de ejecutar algo.

### Si Windows te muestra una advertencia

Pueden salirte **dos avisos distintos**, según cómo llegó el archivo a tu computador:

**a) «Windows protegió su PC»** (pantalla azul).
Pulsa **Más información** → **Ejecutar de todas formas**.

**b) «No se pudo comprobar el editor. ¿Está seguro de que desea ejecutar este software?»**
Pulsa **Ejecutar**. Si aparece una casilla que dice *«Preguntar siempre antes de abrir este archivo»*, puedes desmarcarla para que no vuelva a preguntar.

Los dos aparecen porque el archivo vino de internet y nadie pagó una firma digital, **no porque el programa haga algo raro**. Si prefieres no ejecutarlo, usa la Forma 1 o la 3.

### Si el Mac dice que no puede abrirlo

Dirá *«no se puede abrir porque procede de un desarrollador no identificado»*. Haz **clic derecho** sobre el archivo → **Abrir** → **Abrir** otra vez en el aviso. Solo la primera vez.

---

## Forma 3 · La terminal, paso a paso

La terminal es una ventana donde escribes órdenes en vez de hacer clic. Da un poco de respeto la primera vez y luego no es nada. Aquí van los pasos, sin saltarse ninguno.

### En Mac

**1.** Pulsa `⌘` + barra espaciadora. Se abre un buscador en el centro de la pantalla.

**2.** Escribe `Terminal` y pulsa Enter. Se abre una ventana con texto.

**3.** Escribe esto, **con el espacio al final**, y **no pulses Enter todavía**:

```
cd 
```

**4.** Abre el Finder, busca **la carpeta del kit**, y **arrástrala hasta la ventana de la terminal**. La ruta se escribe sola. Ahora sí, pulsa Enter.

**5.** Escribe `python3 verificador.py ` — **con el espacio al final** — y después **arrastra tu carpeta `Mi_Pensadero`** a la ventana. Pulsa Enter.

Si quieres probar primero con el ejemplo del kit, en vez de arrastrar escribe:

```
python3 verificador.py ejemplo/Mi_Pensadero
```

### En Windows

**1.** Abre el Explorador de archivos y entra en **la carpeta del kit**.

**2.** Haz clic en la **barra de direcciones** de arriba (donde se ve la ruta), escribe `cmd` y pulsa Enter. Se abre una ventana negra **ya situada en esa carpeta**.

**3.** Escribe `python verificador.py ` — **con el espacio al final** — y después **arrastra tu carpeta `Mi_Pensadero`** a la ventana. Pulsa Enter.

Para probar con el ejemplo del kit:

```
python verificador.py ejemplo\Mi_Pensadero
```

---

## Qué vas a ver

```
VERIFICADOR
  SANO
  (forma correcta; este programa no juzga si el contenido es cierto)

TABLERO
  fichas:          7
  por tipo:        {'observacion': 3, 'principio': 1, 'decision': 2, 'pregunta_abierta': 1}
  por estado:      {'vigente': 4, 'caduco': 3}
  por proyecto:    {'circ': 5, 'personal': 2}
```

**SANO** quiere decir que tus fichas están bien formadas. **No quiere decir que lo que escribiste sea verdad** — eso ningún programa lo puede saber.

Si algo está mal, te lo dice con el nombre del archivo y qué le falta:

```
  - 20260726-cierre.md — SIN FUENTE — la procedencia es obligatoria
  - 20260726-margen.md — enlaza a una ficha que no existe: '20260726-otra'
  - 20260726-plazo.md — esta 'en_conflicto' pero no dice con cual ficha choca
```

Arreglas eso en el archivo y vuelves a correrlo.

---

## Si dice que Python no existe

Verás algo como `python no se reconoce como un comando` o `command not found`.

**Significa que ese computador no tiene Python instalado.** No es un error tuyo ni del kit.

Tienes tres salidas, de más fácil a menos:

1. **Usa la Forma 1**: pídele a tu IA que revise las fichas leyendo las reglas. No necesita Python.
2. **Sáltatelo.** El revisor es opcional. Tu pensadero sigue funcionando.
3. **Instala Python** desde [python.org](https://www.python.org/downloads/). Es gratis y son unos minutos. En Windows, **marca la casilla «Add Python to PATH»** en la primera pantalla del instalador; si no la marcas, volverá a fallar.

---

## Comprobar que el revisor es de fiar

Antes de creerle, pídele que se pruebe a sí mismo. En la terminal, dentro de la carpeta del kit:

```
python3 verificador.py --autoprueba
```

Crea fichas rotas a propósito en una carpeta temporal y te muestra que detecta cada fallo, uno por uno — incluidos los del protocolo de conflicto. Si termina en **AUTOPRUEBA: PASA**, el revisor hace lo que dice.

Un revisor que solo se ha visto decir «SANO» no está probado.
