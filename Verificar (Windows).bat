@echo off
REM Revisa tus fichas. Solo llama al verificador y guarda una copia del resultado.
REM No borra nada, no envia nada, no usa internet. Puedes leerlo entero.
cd /d "%~dp0"
set "D=%~1"
if "%D%"=="" if exist "Mi_Pensadero" set "D=Mi_Pensadero"
if "%D%"=="" set /p D="Arrastra aqui tu carpeta Mi_Pensadero y pulsa Enter: "
set "D=%D:"=%"
set "PY="
where python >nul 2>nul && set "PY=python"
if not defined PY where py >nul 2>nul && set "PY=py"
if not defined PY echo No encuentro Python en este equipo. No es un error tuyo ni del kit. Lee "COMO REVISAR TUS FICHAS.md", seccion "Si dice que Python no existe". & pause & exit /b 1
%PY% verificador.py "%D%" > ultimo-resultado.txt 2>&1
type ultimo-resultado.txt
echo.
echo (Este resultado quedo guardado en  ultimo-resultado.txt )
pause
