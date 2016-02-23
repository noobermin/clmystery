#!/usr/bin/env python2
#requires numpy

from random import choice,randint,shuffle;
import itertools as itools;
import numpy as np;

#from 4'11" to 5'11" or 59" to 71".
heights_pool = [
    '{}\'{}"'.format(i/12, i%12)
    for i in range(59,71+1)]
heights = [ choice(heights_pool)
            for i in xrange(100) ]
#Valid License plate characters
charrange = lambda start,end: map(chr, list(range(ord(start),ord(end)+1)))
lpchars = charrange('0','9') + charrange('A','Z');
getlp   = lambda: choice(lpchars)
getlast = lambda: choice(charrange('4','9'))

LPS = ['L337'+getlp()+getlp()+getlast()
       for i in xrange(100)];
#random names from http://listofrandomnames.com/
with open("100rndnames") as f:
    names = [ line.strip() for line in f.readlines()];
#distribution of makes
# 15 Toyotas 25 Ford 20 Nissan 40 Honda
makes=15*['Toyota']+25*['Ford']+20*['Nissan']+40*['Honda'];
shuffle(makes);
#distribution of colors
# 10 Black 10 Red 5 Orange 75 Blue
colors=10*['Black']+10*['Red']+5*['Orange']+75*['Blue'];
shuffle(colors);
weights = np.random.randint(130,250,100);
linefmt="License plate {}\tMake: {}\tColor: {}\tOwner: {}\tHeight: {}\tWeight: {} lbs";
for LP, make, color, name, h, w in zip(LPS,makes,colors,names,heights,weights):
    print(linefmt.format(LP,make,color,name,h,w));
