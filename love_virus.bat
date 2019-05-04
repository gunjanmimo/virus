@echo off
color 67
echo Hey,do you love me(only answe in yes or no)
set /p love=
if %love%==yes goto love
if %love%==no goto hate
:love
echo I love you too...
echo meet you soom :0
pause exit
:hate
echo BUt i love you...hehehehe
echo you are hacked...
echo your pc will crach in 10 seconds
timeout 10
shutdown -s -t 100

