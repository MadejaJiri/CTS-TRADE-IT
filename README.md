# CTS-TRADE-IT
A trial program for a job interview.
This program downloads all job listings from (https://www.cts-tradeit.cz/kariera/) and saves them as individual files in the program root directory.

Author: Jiří Madeja

### Running the program (the easy way)
Run run_script.exe

### Running the program (from source code)
Before you run the source code, it's a good idea to create virtual environment for Python execution.


#### Installation (Windows 10)
```bash
#Install Python 3.7 (64-bit)
#Open command-line from the root directory of this project
python -m venv venv_new
venv_new\Scripts\activate
pip install -r requirements.txt
```
#### Running
```bash
#With the virtual environment activated (assumed continuation of the installation part)
python CTS_TRADEIT_TRIAL.py
```