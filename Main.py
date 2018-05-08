from Controller import *
import sys
from Graph import *
# Alex whole file
try:
    b = Model_Handler(sys.argv[1])
    Controller(b).Go()
except:
    b = Model_Handler(None)
    Controller(b).Go()




