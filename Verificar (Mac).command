#!/bin/bash
# Revisa tus fichas. Solo llama al verificador y guarda una copia del resultado.
# No borra nada, no envia nada, no usa internet. Puedes leerlo entero: son 12 lineas.
cd "$(dirname "$0")"
D="$1"
[ -z "$D" ] && [ -d "Mi_Pensadero" ] && D="Mi_Pensadero"
[ -z "$D" ] && { echo "Arrastra aqui tu carpeta Mi_Pensadero y pulsa Enter"
                 echo "(o escribe  ejemplo/Mi_Pensadero  para probar con el ejemplo)"; read -r D; }
D="$(echo "$D" | tr -d '"' | xargs)"
PY=python3; command -v $PY >/dev/null 2>&1 || PY=python
command -v $PY >/dev/null 2>&1 || { echo "
No encuentro Python en este equipo. No es un error tuyo ni del kit.
Lee 'COMO REVISAR TUS FICHAS.md', seccion 'Si dice que Python no existe'."
  read -p "Pulsa Enter para cerrar..."; exit 1; }
$PY verificador.py "$D" 2>&1 | tee "ultimo-resultado.txt"
echo; echo "(Este resultado quedo guardado en  ultimo-resultado.txt )"
read -p "Pulsa Enter para cerrar esta ventana..."
