REM ��f�B���N�g����T��

echo off
for /R %%d in ( . ) do call :sub "%%d"
exit /b

:sub
for /f "tokens=1-3" %%a in ('dir %1 ^| find "�̃t�@�C��"') do set fnum=%%a & set fsize=%%c
set fsize=%fsize:,=%
for /f "tokens=1" %%a in ('dir %1 ^| find "�̃f�B���N�g��"') do set dir=%%a
if %fnum% EQU 0 if %fsize% EQU 0 if %dir% EQU 2 echo %1
goto :EOF