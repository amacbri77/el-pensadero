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
Se descarga todo el kit, versión 1.3.

---

## Antes de descargar, puedes leerlo todo aquí

Esto no es un adorno: **el propio kit te dice que no ejecutes nada que no puedas
leer.** Aquí puedes revisarlo sin bajar nada.

| Archivo | Qué es |
|---|---|
| [`REGLAS.md`](REGLAS.md) | La constitución de tu pensadero. Dos páginas. |
| [`PROMPTS.md`](PROMPTS.md) | Los tres prompts, listos para pegar. |
| [`verificador.py`](verificador.py) | El revisor de fichas. **Sobre tu pensadero solo lee**: no escribe, no borra, no usa internet. La autoprueba es la única que escribe, y lo hace en una carpeta temporal del sistema. Unas 487 líneas comentadas. |
| [`COMO REVISAR TUS FICHAS.md`](COMO%20REVISAR%20TUS%20FICHAS.md) | Tres caminos para revisar. El más simple: pedírselo a tu IA. |
| [`Verificar (Windows).bat`](Verificar%20(Windows).bat) | El único archivo que se ejecuta, y solo en Windows. **Veinte líneas**: léelo entero antes. |
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

**Esta carpeta es la instalación, no tu pensadero.** Tu pensadero se crea aparte,
junto a tus proyectos, y no dentro del kit: si algún día reemplazas el kit por una
versión nueva, lo que guardaste sigue donde estaba.

---

## Dos herramientas distintas

Conviene saber en qué se diferencian antes de elegir.

Una **LLM Wiki** al estilo Karpathy son archivos de texto enlazados. La escribes,
la lees, y no te pide nada más: simple, barata de mantener, y para mucha gente es
exactamente lo que hace falta.

Un **pensadero** añade gobierno —procedencia, confianza, reemplazo trazable,
conflictos a la vista— y a cambio pide mantenimiento: unos diez minutos al cierre
de cada sesión que valga la pena, y ninguna ficha entra sin decir de dónde salió.

**Ninguna de las dos es mejor: resuelven cosas distintas.** Y la buena es la que
vas a usar de verdad — una wiki que mantienes vale más que un pensadero
abandonado.

El gobierno cuesta, y solo compensa si te hace falta. Te hace falta si decides con
esto y no solo tomas notas, si alguien te va a preguntar de dónde salió, o si
necesitas creerle a la IA cuando te responde sobre tu propio material.

---

## Quién hizo esto, y qué hacer si lo mejoras

**No lo hizo un programador.** Lo hizo alguien con un problema: el criterio que
se gana trabajando se pierde entre conversaciones, y no hay dónde dejarlo. El kit
se construyó **conversando con una IA**, no escribiendo código a mano — que es,
de paso, la prueba de su propia tesis.

Por eso es **un punto de partida, no un producto cerrado**: está hecho para que lo
ajustes a tu oficio, a tu vocabulario y a tu nivel de exigencia. Lo que recibes es
una base que funciona. Lo que hagas con ella es tuyo.

Si algo aquí no te calza, cámbialo. Tú conoces tu trabajo mejor que este documento.

**Pero mejóralo con método.** La IA hace igual de rápido el acierto y el error:

1. **Una cosa a la vez.** Si cambias tres y algo se rompe, no sabrás cuál fue.
2. **Escribe antes qué esperas que pase.** Si no puedes decirlo, todavía no sabes qué estás cambiando.
3. **Prueba el camino que falla**, no solo el que funciona. Lo que solo se ha visto salir bien no está probado.
4. **Comprueba en el resultado, no en la fuente.** Que el archivo diga lo correcto no significa que lo diga lo que tú recibes.
5. **Deja escrito por qué lo cambiaste.** Tú dentro de tres meses eres otra persona, y va a querer deshacerlo.

Y una que las resume: **si tu cambio no se puede comprobar, no lo hagas.**

Son archivos de texto y tienes copia. Romper algo no es grave; romperlo sin
enterarte, sí.

---

## Requisitos

Un computador —esto se instala en el computador, no en el teléfono—, una IA que
pueda leer tus carpetas, y **Python instalado** si vas a usar el revisor. El
revisor es opcional: el pensadero funciona sin él.

---

## De dónde viene

Desciende del patrón **LLM Wiki**, propuesto por Andrej Karpathy: pedirle a la IA
que mantenga una wiki personal de archivos de texto enlazados. Y es justo decirlo.

Y ese es, de paso, el punto: hoy puedes tomar una idea ajena y ajustarla a tu forma
de trabajar conversando con una IA. **Ajusta este kit también.** Las reglas son un
punto de partida, no un destino.

---

## Dónde se explica todo esto

- 🎥 **[Cómo construir un segundo cerebro a tu medida sin saber programar](https://www.youtube.com/watch?v=Qh4DhR4-cK4)** — el video cuenta el porqué del método, en menos de siete minutos.
- 📬 **[Boletín «Inteligencia que queda»](https://www.linkedin.com/newsletters/inteligencia-que-queda-7473916679656247298)** — las versiones nuevas del kit se anuncian ahí.
- 💼 **[LinkedIn](https://www.linkedin.com/in/andrew-mac-gregor/)** — donde suele empezar la conversación.

---

## Versiones

**v1.3** · 2026-07-28 — las dos guías dicen dónde sigue esto: el canal de YouTube
y el boletín, y que por ahí irán saliendo las versiones nuevas y otras herramientas.

**v1.2** · 2026-07-28 — la regla 4b se comprueba de verdad: antes bastaba con que
existiera cualquier `pregunta_abierta` viva para dar por descrito un choque, y
ahora se exige la que enlaza a las dos fichas en conflicto. El revisor comprueba
además cuatro reglas más (que el reemplazo apunte a una ficha que existe, que solo
se llene al caducar, que `relaciones` no quede suelto y que las fechas estén bien
escritas) y avisa cuando le das la carpeta equivocada. Las dos guías cuentan ahora
los mismos seis pasos, y el ejemplo de la guía se lee de las fichas que trae el kit
en vez de estar copiado a mano. Correcciones de redacción en todo el kit.

**v1.1** · 2026-07-27 — primera versión pública.

El número de versión va dentro de `REGLAS.md`. Si tienes el kit guardado y quieres
saber si cambió, compara ese número con el de aquí.

---

*Andrew Mac Gregor B. — Inteligencia que queda*
