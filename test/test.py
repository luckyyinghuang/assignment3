'''
Created on 27 Feb 2018

@author: 25142
'''

import sys
sys.path.append('.')
import pytest
from click.testing import CliRunner
import main
import re
help(re.match)                   
pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+) \s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
result=pat.match("")
class LightTest:
    lights=None
    def __init__(self,N):
        self.lights=[[False]*N for _ in range(N)]
    
    def apply(self,cmd):
        if cmd is 'turn on':
            for false in list turn true or turn from 1 to 0 ; 1 means false
            print("turn on")
                 
        elif cmd is 'switch':
            for 1 turns to 0
            for 0 turns to 1
            
            print("switch")
        
        elif cmd is 'turn off':
            for 0 turns on 1
            print("turn off")
                
            
        
    def count(self):
        count=0
        for row in lights:
            for light in row:
                if(light==True):
                    count=count+1
        print("The number of lights on is ", count)
        return count
    

