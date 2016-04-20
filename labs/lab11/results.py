#!/usr/bin/python
print "content-type: text/html\n"
import sys
sys.path.insert(0, "../modules")
from htmlFuncts import *

print startPage("Results")



print endPage()

