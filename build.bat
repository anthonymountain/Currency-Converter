@echo off
REM Script to clean and rebuild the PyInstaller executable
echo Cleaning previous build artifacts...

REM Remove old build directory
if exist build (
    rmdir /s /q build
)

REM Remove old dist directory
if exist dist (
    rmdir /s /q dist
)

REM Remove old .spec file
if exist app\main_gui.spec (
    del /q app\main_gui.spec
)

echo Building the executable with PyInstaller...
pyinstaller --onefile --windowed application/main_gui.py

echo Build completed. Check the 'dist' folder for the executable.

pause
