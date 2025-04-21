import os
import sys


for filename in os.listdir("NewTests/"):
    print("Running test on file: " + filename)
    os.system("py MainRunner.py NewTests/" + filename)


for filename in os.listdir("Tests/"):
    print("Running test on file: " + filename)
    os.system("py MainRunner.py Tests/" + filename)

# os.system("py MainRunner.py NewTests/n6.txt")
