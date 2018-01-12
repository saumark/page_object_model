if "%1"=="" (set BROWSER=chrome) else (set BROWSER=%1)

set CURRENT_DIR=%~dp0

echo CURRENT_DIR=%CURRENT_DIR%

set PYTHONPATH=%PYTHONPATH%;CURRENT_DIR

pytest ".\uptake\tests\test_navigation.py" --browser=%BROWSER%

pause