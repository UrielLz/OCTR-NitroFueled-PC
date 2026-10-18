@echo off
REM Abre el juego sin HUD. Ctrl+Alt+H (o doble clic de R3) lo muestra u oculta; tambien oculta los menus del juego.
set BB_HUD_HIDE=1
cd /d "%~dp0"
powershell -NoProfile -Command "Start-Process -FilePath (Get-ChildItem -LiteralPath '%~dp0' -Filter 'Crash*Nitro-Fueled.exe')[0].FullName -WorkingDirectory '%~dp0'"
