# Drisy
A Google Drive Manager

### [ Work In Progress ]

![demo image](resources/images/drisy_demo_image.png?raw=true)

### Setup

Google App

- Create a Google [Console](https://console.developers.google.com) Project
- Add Google Drive API to the list of APIs used
- Configure `Oauth Consent` screen (Only the APP Name will do)
- Select the `Credentials` Tab and click `Create Credentials`
- > Oauth client ID >> Desktop app
- Download the credentials json file


Project

- make sure you have a working Python3 installation on your system
- `git clone https://github.com/Edward-K1/Drisy.git`
- `CD` into Project
- copy the json credentials file you downloaded into the project dir
- rename it to `credo.json`
- run `python scripts/config.py` to generate a configuration file (assuming `python`==`python3`)
- add a `.env` file to the project and make its contents equal to those of `.env.config`
- create a python virtual environment: `virtualenv venv` or `python -m venv venv`
- activate the virtual environment: `venv/bin/activate` or `venv\Scripts\activate`
- install requirements: `pip install -r requirements.txt`
- run project: `python drisy.py`

### Known Issues
- If you're having trouble installing WxPython, you must be using linux. I'll leave you with [link 1](https://shanemcd.org/2020/05/03/how-to-install-wxpython-in-a-python-virtual-environment-on-debian-buster/) and [link 2](https://wiki.wxpython.org/How%20to%20install%20wxPython). 
Unfortunately I might not be of much use beyond that. *Google?*
- On some OS and Python versions, WxPython doesn't want to be run from a virtual environment. *Latest Python Version? Different OS? Virtual Machine?*
- The threading is still horrible. You'll notice it if your Google Drive has many files. *Don't you want to play hero?*
