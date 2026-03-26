; Inno Setup Script for JARVIS
#define MyAppName "JARVIS"
#define MyAppVersion "0.1.2"
#define MyAppPublisher "JARVIS"
#define MyAppExeName "jarvis.exe"

[Setup]
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={localappdata}\JarvisAI
DefaultGroupName={#MyAppName}
OutputBaseFilename=jarvisinstall
SetupIconFile=icon_jarvis.png
Compression=lzma
SolidCompression=yes
WizardStyle=modern
DisableDirPage=yes

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional tasks:"; Flags: unchecked
Name: "startup"; Description: "Start {#MyAppName} with Windows"; GroupDescription: "Additional tasks:"; Flags: unchecked

[Files]
Source: "dist\jarvis.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "face.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "icon_jarvis.png"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Registry]
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "JARVIS"; ValueData: "\"{app}\{#MyAppExeName}\" --minimized"; Tasks: startup

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch {#MyAppName}"; Flags: nowait postinstall skipifsilent
