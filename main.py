'''
Created on 27 Feb 2018

@author: 25142
'''
from fileinput import filename
from numpy.distutils.conv_template import file
def main(filename,N):
    lights=LightTester(N)
    instructions=parse-file(filename())
    for cmd in instructions:
        lights.apply(cmd)
        print("#occupied: ", light.count())


if __name__ == '__main__':
    pass