@echo off
echo Installing requirements...
pip install -r requirements.txt
echo Done.

echo starting the script

python main.py 6a 
python main.py 5a
python main.py 4a
pause