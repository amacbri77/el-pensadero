# EL PENSADERO · kit v1.1 (2026-07-27)

Un pensadero es una carpeta de archivos de texto donde tus ideas quedan
guardadas como fichas conectadas —con su fuente, su confianza y su estado—
mantenida por la inteligencia artificial que ya usas, bajo reglas que tú defines.

## Esta carpeta es la INSTALACIÓN, no tu pensadero

Tu pensadero vive **aparte**, junto a tus proyectos:

```
Mis Proyectos/          <- lo unico que le das a la IA
   Mi_Pensadero/        <- tu pensadero, hermano de los proyectos
      Fuentes/
      Fichas/
   Proyecto A/
   Proyecto B/
```

Un solo permiso cubre el proyecto en el que trabajas y el pensadero donde
guardas lo aprendido. Y no tienes que abrirle a la IA toda tu carpeta de
Documentos, con lo que haya ahí dentro.

**Un solo pensadero para todos tus proyectos.** El valor está en los cruces.
El proyecto se distingue con el primer tag de cada ficha, no con carpetas.

## Qué hay aquí

| Archivo | Qué es |
|---|---|
| `REGLAS.md` | La constitución de tu pensadero. **Copia este archivo** dentro de tu `Mi_Pensadero/`. No hace falta copiarlo desde el PDF. |
| `PROMPTS.md` | Los tres prompts, listos para pegar. |
| `COMO REVISAR TUS FICHAS.md` | Tres caminos para revisar. El más simple: pedírselo a tu IA. |
| `Verificar (Windows).bat` | Doble clic, solo Windows. Veinte líneas: ábrelo y léelo antes. En Mac se usa la IA o la terminal, sin bloqueos. |
| `verificador.py` | El revisor. **Sobre tu pensadero solo lee**: no escribe, no borra, no usa internet. La autoprueba es la única que escribe, y lo hace en una carpeta temporal del sistema. |
| `ejemplo/` | Un pensadero de dos fichas que funciona. Sirve de plantilla. |
| `EL PENSADERO — guia rapida.pdf` | Seis pasos para instalarlo. **Empieza aquí.** |
| `EL PENSADERO — guia completa.pdf` | La explicación entera, para leer con calma. |

## Empieza aquí

1. Abre **`EL PENSADERO — guia rapida.pdf`**. Seis pasos, media hora.
2. Crea tu carpeta `Mi_Pensadero` **junto a tus proyectos**, con `Fuentes` y `Fichas` dentro.
3. Copia `REGLAS.md` ahí.
4. Abre `PROMPTS.md` y usa el prompt A con tu IA.

## Sobre seguridad

`verificador.py` **sobre tu pensadero solo lee**: no escribe, no borra, no usa
red y no sale de la carpeta que le indiques. La única excepción es la autoprueba
(`--autoprueba`), que crea fichas rotas a propósito en una carpeta temporal del
sistema y la borra al terminar; nunca toca tus archivos. Si no la corres, el
programa no escribe nada en ningún sitio. Puedes comprobarlo abriéndolo: las
únicas líneas que escriben están dentro de la función `autoprueba`. Son unas 360
líneas comentadas. El lanzador de Windows tiene veinte líneas, a propósito, para que lo leas entero en medio minuto
antes de ejecutarlo. En Mac no hay lanzador: macOS bloquea los ejecutables
descargados con un aviso que asusta, y preferimos no ponerte en esa situación.

**Da a tu IA una carpeta acotada**, no el disco completo ni el escritorio, y no
guardes ahí material que no pueda salir. Lo que le pasas a una IA sale de tu
computador.

Antes de creerle al revisor, pídele que se pruebe a sí mismo: crea fichas rotas
a propósito y te muestra que las detecta. Está al final de
`COMO REVISAR TUS FICHAS.md`. Un revisor que solo se ha visto decir SANO no
está probado.

## Quién hizo esto, y qué hacer si lo mejoras

**No lo hizo un programador.** Lo hizo alguien con un problema: el criterio que
se gana trabajando se pierde entre conversaciones, y no hay dónde dejarlo. Se
construyó conversando con una IA, no escribiendo código a mano. Por eso es un
punto de partida y no un producto cerrado: está hecho para que lo ajustes a tu
oficio, a tu vocabulario y a tu nivel de exigencia. Lo que recibes es una base
que funciona; lo que hagas con ella es tuyo.

**Pero mejórala con método.** La IA hace igual de rápido el acierto y el error:

1. Una cosa a la vez. Si cambias tres y algo se rompe, no sabrás cuál fue.
2. Escribe antes qué esperas que pase. Si no puedes decirlo, todavía no sabes qué estás cambiando.
3. Prueba el camino que falla, no solo el que funciona.
4. Comprueba en el resultado, no en la fuente.
5. Deja escrito por qué lo cambiaste.

Y una que las resume: **si tu cambio no se puede comprobar, no lo hagas.**

## Qué necesitas

Un computador (esto se instala en el computador, no en el teléfono), una IA que
pueda leer tus carpetas, y **Python instalado** si vas a usar el revisor. El
revisor es opcional: el pensadero funciona sin él.

## Qué NO hace este kit

El verificador comprueba la **forma** de tus fichas, no si lo que escribiste es
verdad. Una ficha perfectamente formada puede contener un error y dirá SANO.

## Dónde se explica todo esto

- **El video** «Cómo construir un segundo cerebro a tu medida sin saber
  programar» cuenta el porqué del método, en menos de siete minutos:
  https://www.youtube.com/watch?v=Qh4DhR4-cK4
- **Boletín «Inteligencia que queda»** — ahí se anuncian las versiones nuevas:
  https://www.linkedin.com/newsletters/inteligencia-que-queda-7473916679656247298
- **LinkedIn** — donde suele empezar la conversación:
  https://www.linkedin.com/in/andrew-mac-gregor/

## Versión

Kit v1.1, 2026-07-27. Las versiones futuras se publican en el boletín
**Inteligencia que queda**. Compara este número con el de la última edición.
