# Drisy
A Google Drive Manager

### [ Work In Progress ]

![demo image](resources/images/new-demo.png?raw=true)

### Setup

**Google App**

- Create a Google [Console](https://console.developers.google.com) Project
- Add Google Drive API to the list of APIs used
- Configure `Oauth Consent` screen (Only the APP Name will do)
- Select the `Credentials` Tab and click `Create Credentials`
- > Oauth client ID >> Desktop app
- Download the credentials json file


**Project**

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

### Different UI Framework
*So, you're the rebel?*

```
from drisy.core.drive import DriveManager

dm = DriveManager()
drive_objects = dm.list_files()

```
To see what properties are available, introspect on a DriveObject or check out the schema file :see_no_evil:

### Known Issues
![Google Cop](resources/images/google-cop.PNG?raw=true)
- Did you see the red circle above? You might need it at some point.
- If you're having trouble installing WxPython, you must be using linux. I'll leave you with [link 1](https://shanemcd.org/2020/05/03/how-to-install-wxpython-in-a-python-virtual-environment-on-debian-buster/) and [link 2](https://wiki.wxpython.org/How%20to%20install%20wxPython). 
Unfortunately I might not be of much use beyond that. *Google?*
- On some OS and Python versions, WxPython doesn't want to be run from a virtual environment. *Latest Python Version? Different OS? Virtual Machine?*
- The app won't shutdown when you click the "close button" on the form. It will remain in the system tray. You'll have click the "Exit" option on the system tray menu to shut it down (designed that way).
- The threading is still horrible. You'll notice it if your Google Drive has many files. *Don't you want to play hero?*

## Credits
Icons: https://www.iconarchive.com/show/flatwoken-icons-by-alecive.html
