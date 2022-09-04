import sys, re


with open("palette.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        sys.stdout.write(line)
