"""
File: <sin2_plus_cos2.py>

Copyright (c) 2016 <Francis Agustin>

License: MIT

<Find the erroneous statements that are causing the program bug.>
"""

print "a)"
from math import sin, cos, pi
x = pi/4
val = sin(x)**2 + cos(x)**2
print val

print "b)"
v0 = 3 #m/s
t = 1 #m/s
a = 2**2 #m/s
s = (v0*t) + 0.5*a*(t**2)
print s

print "c)"
a = 3.3; b = 5.3

a2 = a**2
b2 = b**2

eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2

eq1_pow = (a + b)**2
eq2_pow = (a - b)**2

print 'First equation: %f = %f' % (eq1_sum, eq1_pow)
print 'Second equation: %f = %f' % (eq2_sum, eq2_pow)
