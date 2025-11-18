# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 00:44:47 2025

@author: HP
"""

from mptpkg import print_say
import pathlib, os

#open the file..in text editor
#file = pathlib.Path.cwd()/'files'/'storm.txt'
file = r"E:\Study\22 Semester\Labs\EEE\Project Report.pdf"

with open(file) as f:
    content = f.read()
   
os.system(f'explorer {file}')
print_say(content)