# Los tres prompts
*Kit v1.1 · 2026-07-27*

Van en el orden en que los vas a usar. Son tres, no más: con una IA que lee tus carpetas, el resto sobra — ella ya tiene las reglas y las fichas a la vista.

> **Antes del primero:** dile a tu IA cuál es tu carpeta `Mi_Pensadero`. Todo lo demás lo lee sola.

---

## A · Arranque — una sola vez

> Tengo una carpeta `Mi_Pensadero` con dos subcarpetas, `Fuentes` y `Fichas`, y un archivo `REGLAS.md`. **Léelo** y actúa como el bibliotecario de mi pensadero según esas reglas, desde ahora y en cada sesión.
>
> (1) Confírmame que las entendiste y dime si ves alguna ambigüedad.
> (2) Te voy a contar un tema en el que trabajo y quiero que crees mis primeras 3 a 5 fichas. **Muéstrame cada una completa y espera mi visto bueno antes de crear el archivo.**
> (3) Dime qué conexiones ves entre ellas.

---

## E · Cuando entra un documento nuevo

*Guardar algo en `Fuentes/` no lo mete al pensadero. Hay que pedirlo.*

> Acabo de dejar `[nombre del archivo]` en `Fuentes/`. **No lo resumas:** extrae de él las ideas que merecen ficha propia según `REGLAS.md`.
>
> Muéstrame cada ficha completa y espera mi visto bueno antes de crearla. La fuente de todas es ese documento: usa tipo `documento`, su nombre y fecha en `ref`, y una cita textual cuando la haya.
>
> Si una idea ya existe entre mis fichas, dímelo y propón actualizar en vez de duplicar. Si el documento tiene datos sensibles que no convenga guardar, avísame antes de crear la ficha.

---

## B · Al cerrar la sesión — los diez minutos que sostienen todo

*Este es el hábito. Sin él, el pensadero se queda en una buena idea.*

> Antes de cerrar: revisa nuestra conversación según `REGLAS.md` y proponme qué merece guardarse.
>
> Para cada candidata, muéstrame la ficha completa y espera mi visto bueno. Fuente obligatoria y confianza honesta: si es una tesis mía y no un dato, que nazca `tentativo`.
>
> Si algo choca con una ficha que ya tengo, **aplica el protocolo de conflicto: marca el choque de inmediato y pregúntame a mí cuál vale. No lo resuelvas solo.**
>
> Al final, dime en una línea qué guardaste y qué conexiones creaste. Y antes de despedirte, **comprueba que las fichas nuevas cumplen `REGLAS.md`**: si puedes ejecutar `verificador.py`, córrelo sobre mi carpeta `Mi_Pensadero`; si no, revísalas leyendo. **Avísame solo si algo no cumple.**

---

# Anexo · Si tu IA NO puede leer tus carpetas

Todo lo anterior asume una IA de escritorio con acceso a tus archivos. **Es el camino recomendado y con diferencia el más simple.**

Si usas la IA solo en el navegador, el pensadero funciona igual, pero **el trabajo lo haces tú**, y conviene saberlo antes de empezar:

- **En cada sesión nueva tienes que pegar `REGLAS.md`.** La IA no recuerda nada de la sesión anterior. La salida cómoda: dejarlo cargado en un proyecto o asistente personalizado.
- **Para que detecte conflictos, tienes que pegarle también las fichas que puedan chocar.** Si no las ve, no hay conflicto que detectar — y te dirá que todo está bien porque no tiene con qué compararlo.
- **Las fichas las guardas tú**, copiando lo que te muestra a un archivo nuevo dentro de `Fichas/`, con el nombre del campo `id` más `.md`.
- **El revisor no lo puede ejecutar.** Tendrás que correrlo tú: doble clic si usas Windows, o la terminal —en Mac es el único camino, y está explicado paso a paso en `COMO REVISAR TUS FICHAS.md`.

En los tres prompts, agrega al principio: *«Aquí van mis reglas y las fichas relevantes: [pega REGLAS.md] [pega las fichas]»*.

**No es lo mismo y no conviene fingir que sí.** Si puedes elegir, usa una aplicación de escritorio con acceso a carpetas.

---

# Anexo · Construir tus propias herramientas (avanzado)

El kit ya trae `verificador.py`, probado y de solo lectura. **No necesitas nada más.**

Si aun así quieres que tu IA te construya herramientas a medida —otro tablero, un buscador, un exportador— este es el prompt. **Antes de ejecutar cualquier cosa que te genere, aplica todas las condiciones de seguridad del kit:** copia descartable, inventario previo de qué va a leer y escribir, sin red ni borrado, sin salir de la carpeta raíz, y respaldo.

> Quiero una herramienta simple para mi pensadero, en un solo archivo que yo pueda ejecutar, y dime exactamente cómo correrlo paso a paso. [describe qué quieres que haga]
>
> Condiciones obligatorias: trabaja sobre una copia, no accedas a internet, no borres nada, no salgas de la carpeta raíz, y antes de correrlo lístame qué archivos vas a leer y escribir.
>
> Después de construirla, **rómpela a propósito**: crea casos con cada defecto que debería detectar y muéstrame que los detecta. Una herramienta que solo se ha visto funcionar no está probada.

> ⚠️ **Pedirle a la misma IA que te explique su propio programa no es una garantía.** Es la misma que lo escribió.
