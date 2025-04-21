import os
import sys


for filename in os.listdir("Tests/"):
    print("Running test on file: " + filename)
    os.system("py MainRunner.py Tests/" + filename)

