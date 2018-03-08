'''
Created on 27 Feb 2018

@author: 25142
'''
from setuptools import setup

setup(name="assignment3",
      version="0.1",
      description="assignment3 project",
      url="",
      author="ying huang",
      author_email="ying.huang@ucdconnect.ie",
      licence="GPL3",
      packages=['assignment3'],
      entry_points={'console_scripts':
                    ['solve_led=main:main'] 
                    },
      
          )