@echo off
REM Abre el launcher registrando en last_run.log como se acomoda cada elemento del HUD.
set BB_HUD_LOG=1
cd /d "%~dp0"
powershell -NoProfile -Command "Start-Process -FilePath (Get-ChildItem -LiteralPath '%~dp0' -Filter 'Crash*Nitro-Fueled.exe')[0].FullName -WorkingDirectory '%~dp0'"
