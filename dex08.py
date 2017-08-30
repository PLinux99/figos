#!/usr/bin/env python
# coding: utf-8 
## license: creative commons cc0 1.0 (public domain) 
## http://creativecommons.org/publicdomain/zero/1.0/ 
proginf = "dex 0.8, aug 2017 mn" # with lots of design help
import sys ; from sys import stdout
import os ; from os import system as dexsh
from os import name as dexosname
from random import randint

demo = """
  rollem rps 1 3
  ifeql rps 1
    rps "rock"
    nxt
  ifeql rps 2
    rps "paper"
    nxt
  ifeql rps 3
    rps "scissors"
    nxt
  
  fr rtr 1 10 1

    rtr 1
    cmts "rock, paper or scissors?"

    slinpt psr
    lwr psr
    ifeql psr "rock"
      rtr 100
      ifeql rps "rock"
        cmts "tie!"
        nxt
      ifeql rps "paper"
        cmts "paper defeats your rock (somehow)"
        nxt
      ifeql rps "scissors"
        cmts "your rock breaks scissors!"
        nxt
      nxt

    ifeql psr "paper"
      rtr 100
      ifeql rps "rock"
        cmts "your paper defeats rock! (somehow)"
        nxt
      ifeql rps "paper"
        cmts "tie!"
        nxt
      ifeql rps "scissors"
        cmts "scissors cut your paper"
        nxt
      nxt

    ifeql psr "scissors"
      rtr 100
      ifeql rps "rock"
        cmts "rock breaks your scissors"
        nxt
      ifeql rps "paper"
        cmts "your scissors cut paper!"
        nxt
      ifeql rps "scissors"
        cmts "tie!"
        nxt
      nxt

    ifeql rtr 1
      cmts "no, you need to spell the answer correctly and not use spaces"
      nxt

    nxt  

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

#### slinpt: get keyboard input
def dexslinpt(): return raw_input()

#### cap wot: capitalise wot
def dexcap(dx): return dx.upper()

#### cmts wot: put wot on the screen
def dexcmts(dx): print dexdelpz(dx)

#### slcmts wot: put wot on the screen; stay on the same line
def dexslcmts(dx): stdout.write(str(dexdelpz(dx))) ; sys.stdout.flush()

#### lft wot howmany: get howmany leftmost characters from wot
def dexlft(dx, howmany): return dx[:howmany]

#### rt wot howmany: get howmany rightmost characters from wot
def dexrt(dx, howmany): return dx[-howmany:]

#### rollem variable lower higher: get howmany rightmost characters from wot
def dexrollem(dx, dl, dh): return randint(dl, dh)

#### chg: change colour
def dexchg(dx): 
    colours = ["blk", "blu", "grn", "trq", "red", "mag", "brn", "wht"]
    colours += ["gry", "lt blu", "lt grn", "lt trq", "slmn", "pnk", "ylw", "brt wht"]
    f = colours.index(dx)
    x = 0
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

def dexdelpz(p):
    if type(p) in (int, float):
        if float(int(p)) == float(p): return int(p)
    return p

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
def gm(dx):
    while " " * 2 in dx: dx = dx.replace(" " * 2," ")
    dx = dx.strip().split(" ")
    return dx
def dc(dx):
    while " " * 2 in dx: dx = dx.replace(" " * 2," ")
    dx = dx.strip().replace(" ", ", ")
    return dx
def atleast(s, p):
    if p < s: return s
    else: return p
indent = 0
for each in inputfile:
    allch = ""
    cmd = ""
    for ch in each:
        allch = allch + ch
        if (ch == " " or allch == each) and len(allch.strip()):
            if allch.lower().strip() == "clr":
                dxtfile.write(chr(32) * atleast(0, indent) + """dexclr()""" + nl)
                allch = ""
                break # stop parsing this line, go to next line
            elif allch.lower().strip() == "cmts":
                allch = "dexcmts(" + dexrt(each, len(each) - len(allch)).strip() + ")"
                dxtfile.write(chr(32) * atleast(0, indent) + allch + nl)
                break
            elif allch.lower().strip() == "slcmts":
                allch = "dexslcmts(" + dexrt(each, len(each) - len(allch)).strip() + ")"
                dxtfile.write(chr(32) * atleast(0, indent) + allch + nl)
                break
            elif allch.lower().strip() == "cap":
                capwot = dexrt(each, len(each) - len(allch)).strip().split(" ")[0]
                allch = capwot + " = dexcap(" + dexrt(each, len(each) - len(allch)).strip() + ")"
                dxtfile.write(chr(32) * atleast(0, indent) + allch + nl)
                break
            elif allch.lower().strip() == "lwr":
                lwrwot = dexrt(each, len(each) - len(allch)).strip().split(" ")[0]
                allch = lwrwot + " = dexlwr(" + dexrt(each, len(each) - len(allch)).strip() + ")"
                dxtfile.write(chr(32) * atleast(0, indent) + allch + nl)
                break
            elif allch.lower().strip() == "slinpt":
                inptwot = dexrt(each, len(each) - len(allch)).strip().split(" ")[0]
                allch = inptwot + " = dexslinpt()"
                dxtfile.write(chr(32) * atleast(0, indent) + allch + nl)
                break
            elif allch.lower().strip() == "lft":
                lftwot = dexrt(each, len(each) - len(allch)).strip().split(" ")[0]
                allch = lftwot + " = dexlft(" + dc(dexrt(each, len(each) 
                - len(allch)).strip()) + ")"
                dxtfile.write(chr(32) * atleast(0, indent) + allch + nl)
                break
            elif allch.lower().strip() == "rt":
                rtwot = dexrt(each, len(each) - len(allch)).strip().split(" ")[0]
                allch = rtwot + " = dexrt(" + dc(dexrt(each, len(each) 
                - len(allch)).strip()) + ")"
                dxtfile.write(chr(32) * atleast(0, indent) + allch + nl)
                break
            elif allch.lower().strip() == "rollem":
                rollemwot = dexrt(each, len(each) - len(allch)).strip().split(" ")[0]
                allch = rollemwot + " = '' ; " + rollemwot + " = dexrollem(" + dc(dexrt(each, len(each) 
                - len(allch)).strip()) + ")"
                dxtfile.write(chr(32) * atleast(0, indent) + allch + nl)
                break
            elif allch.lower().strip() == "chg":
                allch = "dexchg(" + dexrt(each, len(each) - len(allch)).strip() + ")"
                dxtfile.write(chr(32) * atleast(0, indent) + allch + nl)
                break # stop parsing this line, go to next line
            #### fr variable start stop step - for loop
            elif allch.lower().strip() == "fr":
                #lftwot = dexrt(each, len(each) - len(allch)).strip().split(" ")[0]
                #allch = lftwot + " = dexlft(" + dc(dexrt(each, len(each) 
                #- len(allch)).strip()) + ")"
                gmro = gm(dexrt(each, len(each) - len(allch)).strip())[0]
                gmrt = gm(dexrt(each, len(each) - len(allch)).strip())[1]
                gmrh = gm(dexrt(each, len(each) - len(allch)).strip())[2]
                gmrf = gm(dexrt(each, len(each) - len(allch)).strip())[3]
                dxtfile.write(chr(32) * atleast(0, indent) + gmro 
                + " = float(" + gmrt + ") - float(" + gmrf + ")" + chr(10) + 
                chr(32) * atleast(0, indent) + "while 1:" + chr(10) + chr(32) *
                atleast(0, indent + 4) + gmro + " += float(" + gmrf +
                ") ; " + gmro + " = dexdelpz(" + gmro + ")" + chr(10) + chr(32) * 
                atleast(0, indent + 4) + "if " + gmrf +
                " > 0 and " + gmro + " > float(" + gmrh + "): break" + chr(10) + 
                chr(32) * atleast(0, indent + 4) + "elif " + gmrf + 
                " <= 0 and " + gmro + 
                " < float(" + gmrh + "): break" + nl)
                indent += 4
                break
            #### ifeql compare1 compare2
            elif allch.lower().strip() == "ifeql":
                gmro = gm(dexrt(each, len(each) - len(allch)).strip())[0]
                gmrt = gm(dexrt(each, len(each) - len(allch)).strip())[1]
                dxtfile.write(chr(32) * atleast(0, indent) + "if " + gmro + 
                " == " + gmrt + ":" + chr(10)) 
                indent += 4
                break
            #### els - if conditional is not true
            elif allch.lower().strip() == "els":
                indent -= 4
                dxtfile.write(chr(32) * atleast(0, indent) + "else:" + chr(10)) 
                indent += 4
                break
            #### nxt - mark the bottom of a for loop or conditional or other command block
            elif allch.lower().strip() == "nxt":
                indent -= 4
                break
            else:
                allch = allch.strip() + " = " + dexrt(each, len(each) - len(allch)).strip()
                dxtfile.write(chr(32) * atleast(0, indent) + allch + nl)
                break
dxtfile.close() ; p = dexsh("chmod +x " + outname)
print nl + "your program is compiled to: " + outname
print "now running: " + outname + nl
## run actual program
prog = nl.join(open(outname).readlines())
exec(prog)
