
cls
@ECHO OFF
title Folder CarpetaProtegida
if EXIST "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" goto UNLOCK
if NOT EXIST CarpetaProtegida goto MDLOCKER
:CONFIRM
echo Quiere ocultar la CarpetaProtegida? (S/N)
set/p "cho="
if %cho%==S goto LOCK
if %cho%==s goto LOCK
if %cho%==n goto END
if %cho%==N goto END
echo Invalid choice.
goto CONFIRM
:LOCK
ren CarpetaProtegida "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
attrib +h +s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
echo Folder locked
goto End
:UNLOCK
echo Introduzca la contrasena para mostrar la CarpetaProtegida
set/p "pass="
if NOT %pass%== p4ssw0rd goto FAIL
attrib -h -s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
ren "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" CarpetaProtegida
echo Folder Unlocked successfully
goto End
AIL
echo Invalid password
goto end
:MDLOCKER
md CarpetaProtegida
echo CarpetaProtegida created successfully
goto End
:End 
