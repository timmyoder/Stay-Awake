set root=C:\Users\yode049\Anaconda3

call %root%\Scripts\activate.bat %root%

call conda activate work

call python "C:\Users\yode049\repos\Stay-Awake\src\awake.py" 300

call conda list pyautogui
