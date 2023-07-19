@echo off
echo Ejemplo de host 4.2.2.2 o puede ser tambien google.com
set /p input="Ingrese el host: "
ping %input%
pause