python -m pip install --upgrade pip
python -m pip install pyinstaller

# Build jarvis.exe (main app)
pyinstaller --noconfirm --onefile --windowed --name jarvis --icon icon_jarvis.png --add-data "face.png;." --add-data "icon_jarvis.png;." main.py

# Build jarvisinstall.exe (installer)
pyinstaller --noconfirm --onefile --windowed --name jarvisinstall installer.py

Write-Host "Done. Exes are in dist/"
