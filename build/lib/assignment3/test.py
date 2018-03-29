'''
Created on 27 Feb 2018

@author: 25142
'''

import sys
sys.path.append('.')
import pytest
from click.testing import CliRunner
import main

class Point:
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
class LightTest:
    lights=None
    p1=Point(0,0)
    p2=Point(0,0)
    def __init__(self,N):
        self.lights=[[False]*N for _ in range(N)]
    
    def apply(self,cmd):
        if cmd is 'turn on':
            for i in range(self.p1.x,self.p1.y):
                for j in range(self.p2.x,self.p2.y):
                    self.lights[i][j]=True
                 
        elif cmd is 'switch':
           for i in range(self.p1.x,self.p1.y):
                for j in range(self.p2.x,self.p2.y):
                    self.lights[i][j]=not self.lights[i][j]
        
        elif cmd is 'turn off':
            for i in range(self.p1.x,self.p1.y):
                for j in range(self.p2.x,self.p2.y):
                    self.lights[i][j]=False
                
            
        
    def count(self):
        count=0
        for row in self.lights:
            for light in row:
                if(light==True):
                    count=count+1
        print("The number of lights on is ", count)
        return count