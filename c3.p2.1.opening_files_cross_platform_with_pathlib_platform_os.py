# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 16:17:20 2025

@author: HP
"""

import os, pathlib, platform

print(os.getcwd())
folder = pathlib.Path.cwd()
print(folder)
#my_file = folder/'example'/'example.txt'
my_file = folder/'game.html'

print(my_file)
if platform.system() =='Windows':
    os.system(f"explorer {my_file}")
elif platform.system()=='Darwin':
    os.system(f'open {my_file}')
else:
    os.system(f"xdg-open {my_file}")