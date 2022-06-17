import os

os.run("pip install pyinstaller requests")

os.run("pyinstaller hang.py --one-file --name=main")
