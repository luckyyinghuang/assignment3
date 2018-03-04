'''
Created on 27 Feb 2018

@author: 25142
'''
""" Console Script for test"""
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
                
        else:
            # use open(uri) 
            uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
            r = requests.get(uri).text
            print('\n'.join(r.split('\n')[:5]))
            
        return 
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
              
    


















