# CTS-TRADE-IT
A trial program for a job interview.
This program downloads all job listings from (https://www.cts-tradeit.cz/kariera/) and saves them as individual files in the program root directory.

Author: Jiří Madeja

### Running the program (the easy way)
The program can be executed with run_script.exe or (for better clarity) run_exe.bat
Run run_exe.bat

### Running the program (from source code)
Before you run the source code, it's a good idea to create virtual environment for Python execution.


#### Installation (Windows 10)
```bash
# Install Python 3.7 (64-bit)
# Open command-line from the root directory of this project

# Create new virtual environment (notice: use correct version of Python)
python -m venv cts_venv

# Activate the virtual environment
cts_venv\Scripts\activate

# Install requirements to the virtual environment
pip install -r requirements.txt
```
#### Running
You can manually activate the virtual environment and run the .py script or just run the batch file.
```bash
run_script.bat
```