import turtledemo
import tkinter as tk
import re, collections
def countnames():
    file = open('/Users/oscarestrada/Dropbox/School/Udacity/baby names of 1995.txt', 'r')
    countit = collections.Counter()
    #print(file.read())
    for line in re.findall(r'[A-Z].*,F,[0-9]*', file.read()):
        name, sex, number = line.split(',')
        countit[name] = number
        print(countit[name])
        #file.close()
    #print(list(countit))
    del countit[max(countit, key=lambda x: countit[x])]
    results = max(countit, key=lambda x: countit[x])
    return results, countit[results]


print('max', countnames())


