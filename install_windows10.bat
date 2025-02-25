
@echo off
REM =======================
REM Instalación en Windows 10
REM =======================

REM Verificar si Python está instalado
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python no está instalado. Instalando Python...
    powershell -Command "Start-Process 'https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe' -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait"
)

REM Verificar si pip está instalado
pip --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Pip no está instalado. Instalando pip...
    python -m ensurepip --upgrade
)

REM Instalar virtualenv
pip install virtualenv

REM Crear y activar entorno virtual
virtualenv venv
call venv\Scripts\activate

REM Instalar dependencias
pip install -r requirements.txt

REM Confirmar instalación completa
echo Instalación completa. El entorno está listo.
pause
