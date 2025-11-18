# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 11:46:55 2025

@author: HP
"""

import os

with os.scandir("./files") as f:
    for file in f:
        print(file.name)