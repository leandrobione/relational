; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{6F127615-6AD4-4BD7-8135-2444A335B5CD}
AppName=Relational
AppVerName=Relational ver. 2.3
AppPublisher=Salvo 'LtWorf' Tomaselli
AppPublisherURL=http://ltworf.github.io/relational/
AppSupportURL=http://ltworf.github.io/relational/
AppUpdatesURL=http://ltworf.github.io/relational/
DefaultDirName={pf}\Relational
DefaultGroupName=Relational
AllowNoIcons=yes
LicenseFile=COPYING
OutputBaseFilename=SetupRelational
SetupIconFile=windows\favicon.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Run]
; add the Parameters, WorkingDir and StatusMsg as you wish, just keep here
; the conditional installation Check
Filename: "{tmp}\vcredist_x86.exe";

[Files]
Source: "dist\relational_gui.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; Source: "windows\font dejavu\*"; DestDir: "{fonts}"; FontInstall: "Dejavu Sans"
Source: "samples\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "vcredist_x86.exe"; DestDir: {tmp}; Flags: deleteafterinstall
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\Relational"; Filename: "{app}\relational_gui.exe"
Name: "{group}\{cm:ProgramOnTheWeb,Relational}"; Filename: "http://ltworf.github.io/relational/"
Name: "{group}\{cm:UninstallProgram,Relational}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\Relational"; Filename: "{app}\relational_gui.exe"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\Relational"; Filename: "{app}\relational_gui.exe"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\relational_gui.exe"; Description: "{cm:LaunchProgram,Relational}"; Flags: nowait postinstall skipifsilent

