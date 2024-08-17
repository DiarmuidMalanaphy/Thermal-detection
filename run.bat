@echo off
echo "Running 6a"

call code\venv\Scripts\python code\main.py "code\6a"
echo "Running 5a"
call code\venv\Scripts\python code\main.py "code\5a"
echo "Running 4a"
call code\venv\Scripts\python code\main.py "code\4a"

pause
