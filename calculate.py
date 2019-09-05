import sys
import math_lib

operation = sys.argv[1]
a = int(sys.argv[2])
b = int(sys.argv[3])

if operation == 'div':
    print(math_lib.div(a,b))
elif operation == 'add':
    print(math_lib.add(a,b))
