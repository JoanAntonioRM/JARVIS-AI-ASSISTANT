@echo off
setlocal

python -m pip install --upgrade pip
python -m pip install pyinstaller

REM Build jarvis.exe (main app)
pyinstaller --noconfirm --onefile --windowed --name jarvis --add-data "face.png;." main.py

REM Build jarvisinstall.exe (installer)
pyinstaller --noconfirm --onefile --windowed --name jarvisinstall installer.py

echo Done. Exes are in dist\
endlocal
