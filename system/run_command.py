# -*- coding: UTF-8 -*-
import subprocess

if __name__ == '__main__':
    val = subprocess.run("pwd")
    print(type(val))
    print(val)
    subprocess.run(["ls", "-l"])
