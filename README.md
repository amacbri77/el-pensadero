# El Pensadero

**Un kit para construir tu segundo cerebro a medida, con la IA que ya usas.**
Gratis, abierto, sin registro y sin correo.

Un pensadero es una carpeta de archivos de texto en tu computador donde tus ideas
quedan guardadas como fichas conectadas —con su fuente, su nivel de confianza y su
estado— mantenida por la inteligencia artificial que ya usas, bajo reglas que tú
defines.

No hace falta saber programar.

---

## Descargar

Pulsa el botón verde **Code** aquí arriba y elige **Download ZIP**.
Se descarga todo el kit, versión 1.1.

---

## Antes de descargar, puedes leerlo todo aquí

Esto no es un adorno: **el propio kit te dice que no ejecutes nada que no puedas
leer.** Aquí puedes revisarlo sin bajar nada.

| Archivo | Qué es |
|---|---|
| [`REGLAS.md`](REGLAS.md) | La constitución de tu pensadero. Dos páginas. |
| [`PROMPTS.md`](PROMPTS.md) | Los tres prompts, listos para pegar. |
| [`verificador.py`](verificador.py) | El revisor de fichas. **Solo lee**: no escribe, no borra, no usa internet. Unas 300 líneas comentadas. |
| [`COMO REVISAR TUS FICHAS.md`](COMO%20REVISAR%20TUS%20FICHAS.md) | Tres formas de revisar, ninguna exige saber de terminales. |
| [`ejemplo/`](ejemplo) | Un pensadero de dos fichas que funciona. |

Y si quieres comprobar que el revisor hace lo que dice, córrelo contra sí mismo:

```
python3 verificador.py --autoprueba
```

Crea fichas rotas a propósito y te muestra que detecta cada fallo.
**Un revisor que solo se ha visto decir SANO no está probado.**

---

## Por dónde empezar

1. Descarga y descomprime.
2. Abre **`EL PENSADERO — guia rapida.pdf`**: seis pasos, media hora.
3. Si quieres el porqué de cada regla, está en **`EL PENSADERO — guia completa.pdf`**.

---

## ¿Es para ti?

**Probablemente no, y conviene decirlo antes de que inviertas un fin de semana.**

Una LLM Wiki al estilo Karpathy es más simple y más barata
de mantener. Un pensadero agrega gobierno —procedencia, confianza, reemplazo
trazable, conflictos a la vista— y **eso cuesta**: unos diez minutos al cierre de
cada sesión que valga la pena, y ninguna ficha entra sin decir de dónde salió.

Si eso te parece mucho, probablemente lo sea. **Una wiki que usas vale más que un
pensadero que abandonaste.**

Vale la pena si decides con esto y no solo tomas notas, si alguien te va a preguntar
de dónde salió, o si necesitas creerle a la IA cuando te responde sobre tu propio
material.

---

## De dónde viene

Desciende del patrón **LLM Wiki**, propuesto por Andrej Karpathy: pedirle a la IA
que mantenga una wiki personal de archivos de texto enlazados. Y es justo decirlo.

Aquella idea es más general y más simple. Esta adaptación agrega gobierno para quien
necesita **confiar** en lo que su cerebro le responde, no solo leerlo. Ninguna es
mejor: son herramientas para propósitos distintos.

Y ese es, de paso, el punto: hoy puedes tomar una idea ajena y ajustarla a tu forma
de trabajar conversando con una IA. **Ajusta este kit también.** Las reglas son un
punto de partida, no un destino.

---

## Dónde se explica todo esto

- 🎥 **[Canal en YouTube](https://www.youtube.com/channel/UCF8EaEZ4kVPQ9bD6idZvSsQ)** — el video *El Pensadero* cuenta el porqué del método, en siete minutos.
- 📬 **[Boletín «Inteligencia que queda»](https://www.linkedin.com/newsletters/inteligencia-que-queda-7473916679656247298)** — las versiones nuevas del kit se anuncian ahí.
- 💼 **[LinkedIn](https://www.linkedin.com/in/andrew-mac-gregor/)** — donde suele empezar la conversación.

---

## Versiones

**v1.1** · 2026-07-27 — primera versión pública.

El número de versión va dentro de `REGLAS.md`. Si tienes el kit guardado y quieres
saber si cambió, compara ese número con el de aquí.

---

*Andrew Mac Gregor B. — Inteligencia que queda*
