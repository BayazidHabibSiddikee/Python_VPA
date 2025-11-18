# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 00:27:13 2025

@author: HP
"""
import sys
sys.path.insert(0, r'E:\Study\phase-1-basics-of-programming\B4\mptpkg')


from mptpkg import voice_to_text
from mptpkg import print_say

#Ask the length of rectangle
print_say('What is the length of rectangle..??')
inp1 = voice_to_text()
print_say(f"You just said {inp1}")

#Ask the width of rectangle
print_say('What is the width of rectangle..')
inp2 = voice_to_text()
print_say(f"You just said {inp2}")

#Calculate area -_-
area = float(inp1)*float(inp2)
print_say(f"Area of the rectangle is {area}")