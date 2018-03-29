'''
Created on 8 Mar 2018

@author: 25142
'''

""" Console Script for test"""
import sys
import click
import re

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(filename,N):
    """Console script for led_tester."""
    lights= LightTest(N)
    instructions=parsefile(filename)
    for cmd in instructions:
        lights.apply(cmd)
    print("#occupied: ",lights.count())   
if __name__ == "__main__":
    sys.exit()  # pragma: no cover


import urllib.request
# make the request
# the requests library is very useful and you will use it often:
import requests
# You will need to read files from the network too:
def parseInput(input):
        if input.startswith('http'):
            # use urllib.request.urlopen(uri)
            uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
            req = urllib.request.urlopen(uri)
            buffer = req.read().decode('utf-8')
            r = requests.get(uri).text
            print('\n'.join(r.split('\n')[:5]))
                
        else:
             # use readlines to read a line a time
            filename = "data/data.txt"
            with open(filename) as f:
                for line in f.readlines():
                    # process line        
                    values = line.strip().split()
                    
                
            # read the whole file into a buffer
            buffer = open(filename).read()
            for line in buffer.split('\n'):
                # process line
                return 
           
def parsefile(input):
    if input.startswith('http'):
        # use requests
        pass
    else:
        # read from disk
        N,instructions=None,[]
        pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+) \s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        with open(input,'r') as f:
            N=int(f.readline())
            for line in f.readlines():
                result=pat.match(line)
                instructions.append(result)
        # haven't written the code yet..
        return N,instructions
    return              
    
    
    import sys
sys.path.append('.')
import pytest
from click.testing import CliRunner


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
    
