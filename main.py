'''
Created on 27 Feb 2018

@author: 25142
'''
from test.test import LightTest
""" Console Script for test"""
import sys
import click
import re
help(re.match)

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
    sys.exit(main())  # pragma: no cover


import urllib.request
help(urllib.request.urlopen)
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
    


















