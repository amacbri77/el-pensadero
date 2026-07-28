# EL PENSADERO · kit v1.1 (2026-07-27)

Un pensadero es una carpeta de archivos de texto donde tus ideas quedan
guardadas como fichas conectadas —con su fuente, su confianza y su estado—
mantenida por la inteligencia artificial que ya usas, bajo reglas que tu defines.

## Esta carpeta es la INSTALACION, no tu pensadero

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
Documentos, con lo que haya ahi dentro.

**Un solo pensadero para todos tus proyectos.** El valor esta en los cruces.
El proyecto se distingue con el primer tag de cada ficha, no con carpetas.

## Que hay aqui

| Archivo | Que es |
|---|---|
| `REGLAS.md` | La constitucion de tu pensadero. **Copia este archivo** dentro de tu `Mi_Pensadero/`. No hace falta copiarlo desde el PDF. |
| `PROMPTS.md` | Los tres prompts, listos para pegar. |
| `COMO REVISAR TUS FICHAS.md` | Tres formas de revisar, y ninguna exige saber de terminales. |
| `Verificar (Mac).command` · `Verificar (Windows).bat` | Doble clic. Unas doce lineas cada uno: abrelos y leelos antes. |
| `verificador.py` | El revisor. Solo lee: no escribe, no borra, no usa internet. |
| `ejemplo/` | Un pensadero de dos fichas que funciona. Sirve de plantilla. |
| `EL PENSADERO — guia rapida.pdf` | Seis pasos para instalarlo. **Empieza aqui.** |
| `EL PENSADERO — guia completa.pdf` | La explicacion entera, para leer con calma. |

## Empieza aqui

1. Abre **`EL PENSADERO — guia rapida.pdf`**. Seis pasos, media hora.
2. Crea tu carpeta `Mi_Pensadero` **junto a tus proyectos**, con `Fuentes` y `Fichas` dentro.
3. Copia `REGLAS.md` ahi.
4. Abre `PROMPTS.md` y usa el prompt A con tu IA.

## Sobre seguridad

`verificador.py` solo lee archivos, no usa red y no sale de la carpeta que le
indiques. Puedes comprobarlo abriendolo: son unas 300 lineas comentadas. Los dos
lanzadores tienen doce lineas cada uno, a proposito, para que los leas enteros
en diez segundos antes de ejecutarlos.

**Da a tu IA una carpeta acotada**, no el disco completo ni el escritorio, y no
guardes ahi material que no pueda salir. Lo que le pasas a una IA sale de tu
computador.

Antes de creerle al revisor, pidele que se pruebe a si mismo: crea fichas rotas
a proposito y te muestra que las detecta. Esta al final de
`COMO REVISAR TUS FICHAS.md`. Un revisor que solo se ha visto decir SANO no
esta probado.

## Que NO hace este kit

El verificador comprueba la **forma** de tus fichas, no si lo que escribiste es
verdad. Una ficha perfectamente formada puede contener un error y dira SANO.

## Donde se explica todo esto

- **Canal en YouTube** — el video *El Pensadero* cuenta el porque del metodo:
  https://www.youtube.com/channel/UCF8EaEZ4kVPQ9bD6idZvSsQ
- **Boletin «Inteligencia que queda»** — ahi se anuncian las versiones nuevas:
  https://www.linkedin.com/newsletters/inteligencia-que-queda-7473916679656247298
- **LinkedIn** — donde suele empezar la conversacion:
  https://www.linkedin.com/in/andrew-mac-gregor/

## Version

Kit v1.1, 2026-07-27. Las versiones futuras se publican en el boletin
**Inteligencia que queda**. Compara este numero con el de la ultima edicion.
