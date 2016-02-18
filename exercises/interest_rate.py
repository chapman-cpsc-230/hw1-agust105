"""
File: <interest_rate.py>

Copyright (c) 2016 <Francis Agustin>

License: MIT

<How much money 1000 euros have grown to after
three years with 5 percent interest?>
"""

A = 1000.0      #euros
P = 5.0         #pecent interest
n = 3.0         #years

x = A*pow(1+P/100, n)

print "In", n, "years,", A, "euros with", P, "percent interest will grow to", x, "euros."
