# NRB PICKLE OPTIONS 
To Edit Source Code and Work with GIT
1.	Use Git Bash
2.	`cd ../../Development`
3.	`git clone https://github.com/northriverboats/pickle-options.git`
4.	`cd pickle-options`
5.	Use windows shell
6.	`cd \Development\pickle-options`
7.	`\Python37\python -m venv .venv`
8.	`.venv\Scripts\activate`
9.	`python -m pip install pip --upgrade`
10.	Download PyQt4-4.11.4-cp37-cp37m-win_amd64.whl from https://www.lfd.uci.edu/~gohlke/pythonlibs/
11.	`pip install C:\Users\saral\Desktop\PyQt4-4.11.4-cp37-cp37m-win_amd64.whl`
12.	`pip install -r requirements.txt`
13.	Remember to Create New Branch Before Doing Any Work
# Generate UI
1.	Ues QT Creator
2.	`.venv\Lib\site-packages\PyQt4\Designer.exe`
3.	MainWindow.ui
4.	`.venv\Lib\site-packages\PyQt4\pyuic4 MainWindow.ui -o MainWindow.py`
# Build Executable
.venv\Scripts\pyinstaller.exe --onefile --windowed --icon options.ico --name "Pickle Options Folder" "pickle-options.spec" main.py

