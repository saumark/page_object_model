set CURRENT_DIR=%~dp0

echo CURRENT_DIR=%CURRENT_DIR%

set PYTHONPATH=%PYTHONPATH%;CURRENT_DIR

pytest ".\uptake\tests\test_navigation.py" --browser=chrome

pause