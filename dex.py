#!/usr/bin/env python
# coding: utf-8 
#### license: creative commons cc0 1.0 (public domain) 
#### http://creativecommons.org/publicdomain/zero/1.0/ 
proginf = "dex 0.1, aug 2017 mn" # with design help
import sys ; from sys import stdout
import os ; from os import system as dexsh
from os import name as dexosname

demo = """

clr
  about "this is the first program written in dex"
  gr "hello, world!"
cap gr
lft gr 5
cmts gr

"""

def dexlft(dx, howmany): return dx[:howmany]
def dexrt(dx, howmany): return dx[-howmany:]
top = """
import sys ; from sys import stdout
import os ; from os import system as dexsh
from os import name as dexosname
from random import randint

#### clr: clear the screen
def dexclr():
    if dexosname == "nt": cls = dexsh("cls") 
    else: stdout.write(chr(27) + "[2J" + chr(27) + "[1;1H") ; sys.stdout.flush()

#### lwr wot: make wot lowercase
def dexlwr(dx): return dx.lower()

#### cap wot: capitalise wot
def dexcap(dx): return dx.upper()

#### cmts wot: put wot on the screen
def dexcmts(dx): print dx

#### lft wot howmany: get howmany leftmost characters from wot
def dexlft(dx, howmany): return dx[:howmany]

#### rt wot howmany: get howmany rightmost characters from wot
def dexrt(dx, howmany): return dx[-howmany:]

#### chg: change colour
def dexchg(): 
    x = 0
    f = randint(0, 15)
    b = 0
    if f == None: f = 0
    if b == None: b = 0
    n = "0"
    if f > 7: n = "1" ; f = f - 8
    if f == 1: f = 4 ## switch ansi colours for qb colours
    elif f == 4: f = 1 ## 1 = blue not red, 4 = red not blue, etc.
    if f == 3: f = 6
    elif f == 6: f = 3
    if b > 7: b = b - 8
    if b == 1: b = 4
    elif b == 4: b = 1
    if b == 3: b = 6
    elif b == 6: b = 3
    stdout.write(chr(27) + "[" + n + ";" + str(30+f) + "m")

"""
nl = chr(10) 

p = ""
try: p = dexrt(sys.argv, 1)[0]
except: pass
if not ".dxt" in p.lower():
    if 1 == 0:
        stdout.write(nl + "    type (any) part of the command you want help on." +
        nl * 2 + "    fig will show all matches." + nl * 2 +"    ")
    else:
        print "using built-in demo source, translating to demo.dxt.py..." ; print
        p = "demo.dxt"
        inputfile = demo.replace(chr(13), "").split(nl)
else:
    try:
        inputfile = open(p).read().replace(chr(13) + chr(10), 
        chr(10)).replace(chr(13), chr(10)).split(chr(10))
    except: print "couldn't open " + chr(34) + p + chr(34) + ", exiting." ; print ; quit()
try: dxtfile = open(p + ".py", "w")
except: print "couldn't write to " + chr(34) + p + ".py" "" + chr(34) + ", exiting." ; print ; quit()
outname = p + ".py"
dxtfile.write("""#!/usr/bin/env python""" + nl)
dxtfile.write("""# coding: utf-8""" + nl)
dxtfile.write("""# dex translator version: """ + proginf + nl)
dxtfile.write(top)
def dc(dx):
    while " " * 2 in dx: dx = dx.replace(" " * 2," ")
    dx = dx.strip().replace(" ", ", ")
    return dx
for each in inputfile:
    print 
    allch = ""
    cmd = ""
    for ch in each:
        allch = allch + ch
        if (ch == " " or allch == each) and len(allch.strip()):
            if allch.lower().strip() == "clr":
                dxtfile.write("""dexclr()""" + nl)
                allch = ""
                break # stop parsing this line, go to next line
            elif allch.lower().strip() == "cmts":
                allch = "dexcmts(" + dexrt(each, len(each) - len(allch)).strip() + ")"
                dxtfile.write(allch + nl)
                break
            elif allch.lower().strip() == "cap":
                capwot = dexrt(each, len(each) - len(allch)).strip().split(" ")[0]
                allch = capwot + " = dexcap(" + dexrt(each, len(each) - len(allch)).strip() + ")"
                dxtfile.write(allch + nl)
                break
            elif allch.lower().strip() == "lwr":
                lwrwot = dexrt(each, len(each) - len(allch)).strip().split(" ")[0]
                allch = lwrwot + " = dexlwr(" + dexrt(each, len(each) - len(allch)).strip() + ")"
                dxtfile.write(allch + nl)
                break
            elif allch.lower().strip() == "lft":
                lftwot = dexrt(each, len(each) - len(allch)).strip().split(" ")[0]
                allch = lftwot + " = dexlft(" + dc(dexrt(each, len(each) 
                - len(allch)).strip()) + ")"
                dxtfile.write(allch + nl)
                break
            elif allch.lower().strip() == "rt":
                rtwot = dexrt(each, len(each) - len(allch)).strip().split(" ")[0]
                allch = rtwot + " = dexrt(" + dc(dexrt(each, len(each) 
                - len(allch)).strip()) + ")"
                dxtfile.write(allch + nl)
                break
            if allch.lower().strip() == "chg":
                dxtfile.write("""dexchg()""" + nl)
                allch = ""
                break # stop parsing this line, go to next line
            else:
                allch = allch.strip() + " = " + dexrt(each, len(each) - len(allch)).strip()
                dxtfile.write(allch + nl)
                break
dxtfile.close() ; p = dexsh("chmod +x " + outname)
print nl + "your program is compiled to: " + outname
print "now running: " + outname + nl
#### run actual program
prog = nl.join(open(outname).readlines())
exec(prog)
