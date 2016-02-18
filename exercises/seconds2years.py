"""
File: <seconds2years.py>

Copyright (c) 2016 <Francis Agustin>

License: MIT

<Can a newborn baby in Norway expect to live for one billion (10^9) seconds?>
"""

n = 60.0*60.0*24.0*365.0    #number of seconds in one year
print "Life expectancy in Norway is 81.45 years"

s = 1000000000.0    #seconds

y = s/n

print y

# See if baby can or cannot live for given time
if y <= 81.45:
    print "The norwegian baby can live for", s, "seconds."
else:
    print "The norwegian baby cannot live for", s, "seconds."
