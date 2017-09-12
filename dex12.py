#!/usr/bin/env python
# coding: utf-8 
## license: creative commons cc0 1.0 (public domain) 
## http://creativecommons.org/publicdomain/zero/1.0/ 
proginf = "dex 1.2, sep 2017 mn" # with lots of design help
import sys ; from sys import stdout
import os ; from os import system as dexsh
from os import name as dexosname
from random import randint

demo = """

text "the quick brown fox jumped the fence and got the heck out of there."
len l text
locpstn p text "fox"

slcmts "the text: '" 
slcmts text
cmts "'"

slcmts "the length of the text: "
cmts l

slcmts "the position of the 'fox' in the text: " 
cmts p

"""

def dexlft(dx, howmany): return dx[:howmany]
def dexrt(dx, howmany): return dx[-howmany:]
top = """
import sys ; from sys import stdout
import os ; from os import system as dexsh
from os import name as dexosname
from random import randint
from os import name as dexosname

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

#### add dx howmany: add howmany to dx
def dexadd(dx, howmany): return dx + howmany

#### add dx howmany: subt howmany from dx
def dexsubt(dx, howmany): return dx - howmany

#### mltply dx howmany: multiply dx times howmany
def dexmltply(dx, howmany): return dx * howmany

#### divd dx howmany: divide dx by howmany
def dexdivd(dx, howmany): return dexval(float(dx) / howmany)

#### save v dx: save array v to filepath dx
def dexsave(v, dx):
    sep = chr(10)
    if dexosname == "nt": sep = chr(13) + chr(10)
    try: 
        if len(v) > 1 and v[-1:] == "": v = v[:-1]
    except: pass
    dexfilehandle = open(dx, "w")
    dexfilehandle.write(dexjoin(v, sep) + sep)
    dexfilehandle.close()

#### load v dx: load filepath dx to array v
def dexload(v, dx):
    v = open(dx).read().replace(chr(13) + chr(10), chr(10)).replace(chr(13), 
    chr(10)).split(chr(10))
    return v[:]

#### len v dx: set v to length of dx
def dexlen(v, dx): return len(dx)

#### load v dx s: set v to position of s in dx
def dexlocpstn(v, dx, s):
    try: return dx.index(s) + 1
    except: return 0

#### val dx: convert dx from string to numeric
def dexval(dx):
    n = float(dx)
    if float(int(n)) == float(n): n = int(n) 
    return n

#### splt dx wth: split string dx by wth
def dexsplt(dx, wth): return dx.split(wth)

#### join dx wth: make string from array dx by joining wth
def dexjoin(dx, wth):
    t = ""
    if len(dx) : t = str(dx[0])
    for c in range(len(dx)):
        if c > 0: t += str(wth) + str(dx[c]) 
    return t

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
fnclist = []

def fsplit(p):
    px = [] 
    pxc = -1 # could use len(px) -1 instead?

    inquotes = 0
    remarked = 0
    inspc = "" ; vnspc = ""

    #print "->", p

    for l in p:
        if inquotes == 0 and remarked == 0 and l == "#":
            remarked = 1
            pxc += 1 ; px += [""]
        if remarked == 1:
            px[pxc] += l

        if remarked == 0:
            if l == "\"":
                if inquotes == 0:
                    inquotes = 1 ; pxc += 1 ; px += [""]
                else: inquotes = 0 #; px[pxc] += l
        if inquotes == 1: px[pxc] += l

        if remarked == 0 and inquotes == 0:
            if vnspc not in "1234567890-" + chr(32) and l[0] == ".": l = " "
            vnspc = l
            if l[0] in "():;|=,": l = " "
            if inspc != " " and l == " ": pxc += 1 ; px += [""]
            if l != " ":
                if pxc == -1: pxc += 1 ; px += [""]
                px[pxc] += l.lower() 
            inspc = l
    #print "->", px[:]
    while ('') in px: px.remove('')
    while (':') in px: px.remove(':')
    for p in range(len(px)):
        if px[p][0] != "#":
            if dexrt(px[p], 1) == ":":
                lenpx = len(px[p]) - 1
                if lenpx > 0:
                    px[p] = left(px[p], lenpx)
    return px[:]

def getmore(p, s):
    try:
        for t in range(1, s + 1):
            if len(p) == 1: p = []
            p = dexrt(p, len(p) - 1)
        while "" in p: p.remove("")
        for prx in range(len(p)):
            if p[prx][0] == "#":
                p.remove(p[prx])
        return p
    except: return []

def getlmore(p, s):
    try:
        for t in range(1, s + 1):
            if len(p) == 1: p = []
            p = dexrt(p, len(p) - 1)
        while "" in p: p.remove("")
        return p
    except: return []

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
            elif allch.lower().strip() in fnclist:
                mkfncname = allch.lower().strip()
                mkfncwot = getlmore(fsplit(each.lstrip()), 1)[0]
                funcp = getlmore(fsplit(each.lstrip()), 2)
                try: funcps = ", ".join(funcp)
                except: funcps = ""
                allch = "dexfnc = " + mkfncname + "(" + funcps + ")"
                dxtfile.write(chr(32) * atleast(0, indent) + allch + nl)
                allch = "if dexfnc != None: " + mkfncwot + " = dexfnc"
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
            elif allch.lower().strip() == "val":
                valwot = dexrt(each, len(each) - len(allch)).strip().split(" ")[0]
                allch = valwot + " = dexval(" + dexrt(each, len(each) - len(allch)).strip() + ")"
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
            elif allch.lower().strip() == "add":
                rtwot = dexrt(each, len(each) - len(allch)).strip().split(" ")[0]
                allch = rtwot + " = dexadd(" + dc(dexrt(each, len(each) 
                - len(allch)).strip()) + ")"
                dxtfile.write(chr(32) * atleast(0, indent) + allch + nl)
                break
            elif allch.lower().strip() == "subt":
                rtwot = dexrt(each, len(each) - len(allch)).strip().split(" ")[0]
                allch = rtwot + " = dexsubt(" + dc(dexrt(each, len(each) 
                - len(allch)).strip()) + ")"
                dxtfile.write(chr(32) * atleast(0, indent) + allch + nl)
                break
            elif allch.lower().strip() == "mltply":
                rtwot = dexrt(each, len(each) - len(allch)).strip().split(" ")[0]
                allch = rtwot + " = dexmltply(" + dc(dexrt(each, len(each) 
                - len(allch)).strip()) + ")"
                dxtfile.write(chr(32) * atleast(0, indent) + allch + nl)
                break
            elif allch.lower().strip() == "divd":
                rtwot = dexrt(each, len(each) - len(allch)).strip().split(" ")[0]
                allch = rtwot + " = dexdivd(" + dc(dexrt(each, len(each) 
                - len(allch)).strip()) + ")"
                dxtfile.write(chr(32) * atleast(0, indent) + allch + nl)
                break
            elif allch.lower().strip() == "splt":
                rtwot = dexrt(each, len(each) - len(allch)).strip().split(" ")[0]
                allch = rtwot + " = dexsplt(" + dc(dexrt(each, len(each) 
                - len(allch)).strip()) + ")"
                dxtfile.write(chr(32) * atleast(0, indent) + allch + nl)
                break
            elif allch.lower().strip() == "join":
                rtwot = dexrt(each, len(each) - len(allch)).strip().split(" ")[0]
                allch = rtwot + " = dexjoin(" + dc(dexrt(each, len(each) 
                - len(allch)).strip()) + ")"
                dxtfile.write(chr(32) * atleast(0, indent) + allch + nl)
                break
            elif allch.lower().strip() == "rollem":
                rollemwot = dexrt(each, len(each) - len(allch)).strip().split(" ")[0]
                allch = rollemwot + " = '' ; " + rollemwot + " = dexrollem(" + dc(dexrt(each, len(each) 
                - len(allch)).strip()) + ")"
                dxtfile.write(chr(32) * atleast(0, indent) + allch + nl)
                break
            #### mkfnc name variable-to-set parameter parameter etc 
            elif allch.lower().strip() == "mkfnc" and len(getmore(fsplit(each.lstrip()), 1)) > 0:
                funcname = getlmore(fsplit(each.lstrip()), 1)[0]
                funcset = getlmore(fsplit(each.lstrip()), 2)[0]
                funcp = getlmore(fsplit(each.lstrip()), 3)
                try: funcps = ", ".join(funcp)
                except: funcps = ""
                allch = funcname + " = 0" + nl + chr(32) * atleast(0, indent)
                allch += "def " + funcname + "(" + funcps + "):"
                dxtfile.write(chr(32) * atleast(0, indent) + allch + nl)
                fnclist += [funcname]
                indent += 4
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
            elif allch.lower().strip() == "save":
                gmro = gm(dexrt(each, len(each) - len(allch)).strip())[0]
                gmrt = gm(dexrt(each, len(each) - len(allch)).strip())[1]
                dxtfile.write(chr(32) * atleast(0, indent) + "dexsave(" + gmro + 
                ", " + gmrt + ")" + chr(10)) 
                break
            elif allch.lower().strip() == "load":
                gmro = gm(dexrt(each, len(each) - len(allch)).strip())[0]
                gmrt = gm(dexrt(each, len(each) - len(allch)).strip())[1]
                dxtfile.write(chr(32) * atleast(0, indent) + gmro + " = [] ; " + 
                gmro + " = dexload(" + gmro + ", " + gmrt + ")" + chr(10)) 
                break
            elif allch.lower().strip() == "len":
                gmro = gm(dexrt(each, len(each) - len(allch)).strip())[0]
                gmrt = gm(dexrt(each, len(each) - len(allch)).strip())[1]
                dxtfile.write(chr(32) * atleast(0, indent) + gmro + " = -1 ; " + 
                gmro + " = dexlen(" + gmro + ", " + gmrt + ")" + chr(10)) 
                break
            elif allch.lower().strip() == "locpstn":
                gmro = gm(dexrt(each, len(each) - len(allch)).strip())[0]
                gmrt = gm(dexrt(each, len(each) - len(allch)).strip())[1]
                gmrh = gm(dexrt(each, len(each) - len(allch)).strip())[2]
                dxtfile.write(chr(32) * atleast(0, indent) + gmro + " = -1 ; " + 
                gmro + " = dexlocpstn(" + gmro + ", " + gmrt + ", " + gmrh + ")" + chr(10)) 
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
