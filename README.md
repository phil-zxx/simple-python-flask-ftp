# Simple Python Flask FTP

## Description

This is a simple `flask`-based server, written in `Python`, to exchange files.<br><br>

## Setup

Firstly, make sure you have Python installed: https://www.python.org/downloads.

Then, perform the following steps in the command line (in the root folder of this repo):

1. Run `python -m venv env` to **create** the virtual environment
2. Run `./env/Scripts/Activate.ps1` (for Windows), or `./env/Scripts/activate` (on Linux) to **activate** the virtual environment
3. Run `pip install -r .\requirements.txt` to **install** the required Python packages, like `flask`
<br><br>

## Usage

Run `python run_server.py` to **start** the server. Note that if you are running this server at home, you may need to open port `5023` in your home router (in order for external parties to be able to connect).

The default URL to connect to is `http://X.X.X.X:5023/file?code=dkljdfs8923dfa1`. Of course, you need to replace `X.X.X.X` with your external IPv4 address, which you can look up e.g. via https://whatismyipaddress.com.
