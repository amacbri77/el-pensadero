@echo off
REM Revisa tus fichas. Solo llama al verificador y guarda una copia del resultado.
REM No borra nada, no envia nada, no usa internet. Puedes leerlo entero.
cd /d "%~dp0"
set "D=%~1"
REM Tu pensadero vive fuera del kit: por eso no se busca aqui, siempre se pide.
if "%D%"=="" set /p D="Arrastra aqui tu carpeta Mi_Pensadero y pulsa Enter: "
set "D=%D:"=%"
set "PY="
REM Estas tres lineas se probaron tal cual en un Windows real el 2026-07-27.
where python >nul 2>nul && set "PY=python"
if not defined PY where py >nul 2>nul && set "PY=py"
if not defined PY echo No encuentro Python en este equipo. No es un error tuyo ni del kit. Lee "COMO REVISAR TUS FICHAS.md", seccion "Si dice que Python no existe". & pause & exit /b 1
REM Consola en UTF-8 recien aqui, DESPUES de preguntar: antes estorba a la pregunta.
chcp 65001 >nul
%PY% verificador.py "%D%" > ultimo-resultado.txt 2>&1
type ultimo-resultado.txt
echo.
echo (Este resultado quedo guardado en  ultimo-resultado.txt )
pause
