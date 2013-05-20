#!/usr/bin/env python

from __future__ import division
import numpy
import pylab
import XKCDify
import random

#solution_dict = {'b': 15.962500000000082, 'f': 0.0015407986111111336, 'a': 1.0, 'd': 1.040190972222232, 'e': -0.06762152777777858, 'c': -6.605555555555604}
solution_dict = {"b": 5.066533383144606, "f": 4.727668830513914e-05, "a": 1.1390753899407047, "d": 0.14775993667161155, "e": -0.006081742122895637, "c": -1.285639984558238}


def prob_say_yes(cs):
    a = solution_dict["a"]
    b = solution_dict["b"]
    c = solution_dict["c"]
    d = solution_dict["d"]
    e = solution_dict["e"]
    f = solution_dict["f"]
    return a + b * cs + c * cs ** 2 + d * cs ** 3 + e * cs ** 4 + f * cs ** 5

ax = pylab.axes()

x = numpy.linspace(0, 15, 100)
y = [prob_say_yes(e) + random.random() / 5 for e in x]
ax.plot(x, y, 'b', lw=1)
x = numpy.linspace(15.1, 16, 100)
y = [prob_say_yes(e) + random.random() / 5 for e in x]
ax.plot(x, y, 'b--', lw=1)
x = numpy.linspace(16.1, 35, 100)
y = [9 - (e - 16) / 5 + random.random() / 10 for e in x]
ax.plot(x, y, 'b--', lw=1)

# set labels/title
ax.set_title('Prob of saying "Yes" to academic responsabilities')
#ax.set_xlabel('Career stage')
ax.set_ylabel('%')

# set legend position
#ax.legend(loc='upper right')

ax.annotate("Wow, that\n was tough!", xy=(4, 9), xytext=(1, 14), arrowprops=dict(facecolor='black', shrink=0.01),)
ax.annotate("Oh ***t!\n That was the easy part!", xy=(6, 9.5), xytext=(7, 2), arrowprops=dict(facecolor='black', shrink=0.01))
ax.annotate("I miss the sun...", xy=(13, 18), xytext=(8, 8), arrowprops=dict(facecolor='black', shrink=0.01))
ax.annotate("I think I remember what\n my partner looks like...", xy=(15, 16), xytext=(16, 20), arrowprops=dict(facecolor='black', shrink=0.01))
ax.annotate("Ignorance is bliss...", xy=(25, 8), xytext=(20, 10), arrowprops=dict(facecolor='black', shrink=0.01))


# set x/y limits
ax.set_xlim(-2, 30)
ax.set_ylim(-4, 26)

# No x/yticks
ax.set_xticks([4, 8, 16])
ax.set_xticklabels(["PhD", "Postdoc", "Permanent position\n/tenure"], rotation=2)
ax.set_yticks([16])
ax.set_yticklabels(["100"])

# modify all the axes elements in-place
XKCDify.XKCDify(ax, xaxis_loc=0.0, yaxis_loc=0.0, xaxis_arrow='+', yaxis_arrow='+', expand_axes=True)

# save to file
pylab.savefig('Probability_of_saying_yes_to_academic_responsabilities.png')
