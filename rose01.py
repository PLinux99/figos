#!/usr/bin/env python
# coding: utf-8 
#### license: creative commons cc0 1.0 (public domain) 
#### http://creativecommons.org/publicdomain/zero/1.0/ 
proginf = "rose 0.1, oct 2017 mn"
import sys
import os
from sys import stdin, stdout
from os import popen
try: from colorama import init ; init()
except: pass

buf = []
nl = chr(10)
if os.name == "nt": nl = chr(13) + nl

cmdhelp = [("timer", "input (shared-line) change main variable to number of seconds past midnight")

,("cdxin", "input (shared-line) change main variable to codex containing lines of stdin")
,("input", "input (shared-line) change main variable to string input from keyboard")
,("time", "input (shared-line) change main variable to string of current time: hh:mm:ss")
,("cdxload filepath", "input (shared-line) change main variable to codex of file lines in filepath")
,("date", "input (shared-line) change main variable to string of the date: mm/dd/yyyy")
,("cdxcurl url", "input (shared-line) like cdxload, except downloading url into the codex")
,("sleep seconds", "input (shared-line) wait for number of seconds before continuing with program")
,("cdxcmd", "input (shared-line) change main variable to codex of command line parameters")
,("display", "output (shared-line) output main variable to the screen (aka stdout)")
,("displays", "output (shared-line) put main var to screen; like print but (s)tays on line.")
,("esc", "output (shared-line) clear the screen. currently only affects text screen")
,("colourtext colourcode", "output (shared-line) change colour of upcoming text to colourcode from 0 - 15")
,("colortext colorcode", "output (shared-line) change color of upcoming text to colorcode from 0 - 15")
,("highlight colourcode", "output (shared-line) change background colour of upcoming text tocolourcode 0-15")
,("locate row column", "output (shared-line) move to textmode position at row, column")
,("pset x y c", "output (shared-line) draw dot at location (x, y) in colourcode c (0 - 15)")
,("line x1 y1 x2 y2 c", "output (shared-line) draw line from (x1, y1) to (x2, y2) in colourcode c (0-15)")
,("while", "loop --\\own\\line mark the start of a loop (will keep going without break)")
,("break", "loop --\\own\\line put in the middle of a loop to exit (stop looping)")
,("for var strt stop step", "loop --\\own\\line start a for loop, changing var from strt to stop, by step")
,("forin var codex", "loop --\\own\\line loop through each item in codex; for each, set var to item")
,("iftrue ckvar", "conditional --\\own\\line run lines between iftrue and next if ckvar is \"non-zero\"")
,("ifequal var1 var2", "conditional --\\own\\line run lines between ifequal and next if var1 equals var2")
,("ifmore var1 var2", "conditional --\\own\\line run lines between ifmore and next if var1 is > var2")
,("ifless var1 var2", "conditional --\\own\\line run lines between ifless and next if var1 is < var2")
,("try", "conditional --\\own\\line put code that might not work between try and except")
,("except", "conditional --\\own\\line if code between try/except fails, run the code after except")
,("resume", "conditional --\\own\\line mark the end of try / except / resume command block")
,("else", "conditional --\\own\\line after if- line, before next. run lines if condition isnt true")
,("function name p1 p2 â#Š", "function --\\own\\line define function named name with optional params p1,p2, etc")
,("get parametername", "function (shared-line) (no longer required) copy parametername value to main var")
,("next/nextin/wend", "next (interchangeable) function --\\own\\line finalise a block (started by if/while/function/for/forin")
,("pass", "function --\\own\\line blocks (for/next, etc) require something inside lines; pass works / does nothing")
,("lcase", "function (shared-line) change main variable to all-lower-case copy of own value")
,("ucase", "function (shared-line) change main variable to all-upper-case copy of own value")
,("str", "function (shared-line) convert main variable from number to string")
,("shell", "function (shared-line) run main variable contents   in a command shell (os specific)")
,("asc", "function (shared-line) change main variable from string to ascii code of 1st char")
,("val", "function (shared-line) change main variable from string to numeric (int if whole)")
,("len", "function (shared-line) change main variable to  numeric length of main var")
,("not", "function (shared-line) change main variable to zero if non-zero; or -1 if zero")
,("ltrim", "function (shared-line) strip whitespace from left side of main variable")
,("rtrim", "function (shared-line) strip whitespace from right side of main variable")
,("chr", "function (shared-line) change main variable from numeric to ascii/uni string")
,("cdxshell", "function (shared-line) change main var to codex of shell output (from main var)")
,("cdxreverse", "function (shared-line) reverse a codex")
,("cdxsort", "function (shared-line) change main variable from codex to sorted codex")
,("#", "comment (can\\share) place at beginning (or end) of line, prior to a comment")
,("():;|=,. ( ) : ; | = , .", "optional (shared-line) use in a shared line (and some others) for aesthetics/notation")
,("left numofcharsoritems", "function (shared-line) change main variable to __ leftmost group of chars/items")
,("right numofchrsoritems", "function (shared-line) change main variable to __ rightmost group of chars/items")
,("cdxget codex position", "function (shared-line) change main variable to position-th item from codex")
,("cdxset position setto", "function (shared-line) change item in codex in main variable to value of setto")
,("mid position len", "function (shared-line) change main variable to range of len items from position")
,("cdxsplit string splitby", "function (shared-line) split string by separator splitby into codex, to main var")
,("cdxjoin codex usestring", "function (shared-line) change main var to string by joining codex using usestring")
,("instr lookin lookfor", "function (shared-line) change main var to numeric position of lookfor in lookin")
,("add cdxnumstr", "math (shared-line) change main variable to itself plus cdx or num or string")
,("subtract numeric", "math (shared-line) change main variable to itself minus numeric")
,("divby numeric", "math (shared-line) change main variable to itself divided by numeric")
,("times numeric", "math (shared-line) change main variable to itself times numeric")
,("cdxsave filepath", "function (shared-line) write codex to filepath")
,("chdir", "function (shared-line) change current folder to path string from main variable")
,("exit", "function (shared-line) put on (usually at the end of) a line to stop the program")
,("close", "function (shared-line) close the open file designated by main variable")
,("return var", "function (shared-line) (optional) exit current function, returning value var")
,("swap var1 var2", "function (shared-line) change contents of var1 to contents of var2 and vice-versa")
,("oct", "math (shared-line) change main variable from numeric decimal to octal")
,("hex", "math (shared-line) change main variable from  numeric decimal to hexadecimal")
,("cos", "math (shared-line) change numeric main variable to the cosine of itself")
,("sin", "math (shared-line) change numeric main variable to the sine of itself")
,("pi", "math (shared-line) change numeric main variable to 3.14159265359")
,("int", "math (shared-line) change main variable from decimal (aka \"float\") to integer")
,("mod denominator", "math (shared-line) change main variable to: main var modulus denominator")
,("exp n", "math (shared-line) raise numeric main variable to n-th power")
,("random smallst largst", "input (shared-line) change main var to random number from smallst to largst")
,("cdx", "function (shared-line) change main var to codex (starting with same contents)") ]

def chelp(f):
    ck = 0 ; print ""
    for p in cmdhelp:
        rcmd = p[0]
        if f in rcmd.split()[0]:
            ck = 1
            rd = p[1].split()
            rcat = rd[0] ; rd.remove(rd[0])
            rt = rd[0] ; rd.remove(rd[0])

            cde = rcmd.split(" ")
            print ""
            stdout.write("    " + colour(14,0)+ cde[0])
            cda = cde.remove(cde[0])
            for c in cde:
                stdout.write(" " + colour(0, 7)+ " " + c + " " + colour(7,0)+" ") ; stdout.flush()
            print ""
            print ""
            print colour(3,0) + "        category:", rcat, rt.replace("\\", " ")
            print ""
            print "        " + colour(7,0) + " ".join(rd)
            print ""
        colour(7,0);
    return ck

def outfilewrite(outb, p):
    outb += [p]
    #global vrck
    #vrck += p.strip()
    #if inle: print colour(5, 0) + p.rstrip() ; p=raw_input() ; quit()

def colour(f, b):
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
    stdout.write("\x1b[" + n + ";" + str(30+f) + ";" + str(40+b) + "m")
    return "\x1b[" + n + ";" + str(30+f) + ";" + str(40+b) + "m"

def bcolour(b):
    f = None
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
    stdout.write("\x1b[" + n + ";" + str(30+f) + ";" + str(40+b) + "m")
    return "\x1b[" + n + str(40+b) + "m"

def sgn(p):
    p = float(p)
    if p > 0: return 1
    if p < 0: return -1
    return 0

def left(p, s):
    return p[:s]

def right(p, s):
    return p[-s:]

def leftfour(p):
    try:
        if left(p, 4) == chr(32) * 4: p = right(p, len(p) - 4)
    except:
        pass
    return p

def atleast(s, p):
    if p < s: return s
    else: return p

def rosefsp(p):
    pp = "" ; flg = 0
    fsp = rosefsplit(p)    
    for fp in enumerate(fsp):
        if flg == 0 and fp[1] in cmds.keys():
            pp += colour(8,0) + "_" + colour(7,0) + " " ; flg = cmds[fp[1]]
            if flg < 0: flg = flg * -1
            else: flg = flg + 1
        pp += fp[1] + " "
        if flg > 0:
            flg -= 1
            if flg == 0 and fp[0] + 1 < len(fsp):
                pp += colour(8,0) + "_" + colour(7,0) + " "
    return pp.rstrip().replace(colour(8,0) + "_" + colour(7,0) + " " + colour(8,0) +
    "_" + colour(7,0), colour(8,0) + "__" + colour(7,0)).replace(colour(8,0) + "_" +
    colour(7,0),colour(8,0) + "__" + colour(7,0))

def rosefsplit(p):
    # return p.split() # that was fine when strings weren't tokens
    # we have to make this 2 tokens: "hello, world!" #comment not string

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
            if right(px[p], 1) == ":":
                lenpx = len(px[p]) - 1
                if lenpx > 0:
                    px[p] = left(px[p], lenpx)
    return px[:]

def nob(p, s):
    r = ""
    if s == len(p) - 1:
        if len(p):
            if p[s].rstrip() != ".": r = p[s].rstrip()
        if len(r):
            if r[-1:] == ".": r = left(r, len(r) - 1)
    prose = ""
    try: prose = left(p[s], 4)
    except: prose = ""
    if prose.lower() == "rose" and p[s].lower() != "rose": return "roseg"
    try:
        if r != "": return r
        else: return p[s]
    except: return ""

def snobl(p):
    if "\"" in p: return p
    else: return p.lower()

def snob(p, s):
    r = ""
    if s == len(p) - 1:
        if len(p):
            if p[s].rstrip() != ".": r = p[s].rstrip()
        if len(r):
            if r[-1:] == ".": r = left(r, len(r) - 1)
    pqt = ""
    try: pqt = left(p[s], 4)
    except: pqt = ""
    if pqt.lower() == "rose" and p[s].lower() != "rose": return "roseg"
    try:
        if r != "": return snobl(r)
        else: return snobl(p[s])
    except: return ""

def lnob(p, s):
    r = ""
    if s == len(p) - 1:
        if len(p):
            if p[s].rstrip() != ".": r = p[s].rstrip()
        if len(r):
            if r[-1:] == ".": r = left(r, len(r) - 1)
    prose = ""
    try: prose = left(p[s], 4)
    except: prose = ""
    if prose.lower() == "rose" and p[s].lower() != "rose": return "roseg"
    try:
        if r != "": return r.lower()
        else: return p[s].lower()
    except: return ""

def getmore(p, s):
    try:
        for t in range(1, s + 1):
            if len(p) == 1: p = []
            p = right(p, len(p) - 1)
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
            p = right(p, len(p) - 1)
        while "" in p: p.remove("")
        return p
    except: return []

def getpairs(p, s):
    r = ""
    if len(p):
        if p[len(p) - 1].rstrip() != ".": r = p[len(p) - 1].rstrip()
    if len(r):
        if r[-1:] == ".":
            r = left(r, len(r) - 1)
            p[len(p) - 1] = r    
    try:
        p = right(p, len(p) - s)
        if not len(p) % 2: return p
        else: return []
    except: return []

def lc():
    global linecount
    global flen
    es = " \x1b[0;37;40m"
    return "\x1b[0;37;41m" + right(chr(32) * flen + str(linecount), flen) + es

def wr(p):
    global buf
    buf += [p + "\n"]

colour(13, None) ; print proginf; colour(7, None) ; print

addtoout = [0]
addto = [0]

addtoout[0] = """import sys, os
from sys import stdin, stdout
from sys import argv as roseargv
try: from colorama import init ; init()
except: pass # (only) windows users want colorama installed or ansi.sys enabled
from random import randint
from time import sleep\n\n
from os import chdir as roseoch
from os import popen as rosepo
from os import system as rosesh
from os import name as roseosname
rosesysteme = 0
rosefilehandles = {}
rosefilecounters = {}
"""

addtoout += [0] ; addto += [0]

addtoout[1] = """from sys import stdout
def roselocate(x, l = "ignore", c = "ignore"):    
    import sys
    if l == "ignore" and c == "ignore": pass
    # do nothing. want it to return an error?

    elif l < 1 and c != "ignore":
        sys.stdout.write("\x1b[" + str(c) + "G") # not ansi.sys compatible
    elif l != "ignore" and c == "ignore":
        sys.stdout.write("\x1b[" + str(l) + ";" + str(1) + "H")
    else: sys.stdout.write("\x1b[" + str(l) + ";" + str(c) + "H")

import time

def rosenonz(p, n=None):
    if n==None:
        if p == 0: return 1
    else:
        if p == 0: return n
    return p

def rosenot(p):
    if p: return 0
    return -1

rosebac = None
roseprsbac = None
sub = None
def rosenone(p, rosebac):
    if p == None: return rosebac
    return p
    return -1

def stopgraphics():
    global yourscreen
    global roseraphics
    roseraphics = 0

\n"""
addtoout += [0] ; addto += [0]

addtoout[2] = """\n"""
addtoout += [0] ; addto += [0]

addtoout[3] = """roseraphics = -1
roserupd = 1
roseraphics = 0
yourscreen = ""
def rosepset(z, x, y, c):
    global roseraphics, roserupd
    global yourscreen
    global rosecgapal
    roseraphics = 0
    if roseraphics == 0:
        if x > -1 and y > -1:
            rosecolourtext(c, c)
            roselocate(0, int(y) + 1, int(x) + 1) ; stdout.write(unichr(9608))
            sys.stdout.flush()

def roseline(z, x, y, x2, y2, c):
    global roseraphics, roserupd
    global yourscreen
    global rosecgapal
    roseraphics = 0
    if roseraphics == 0:
        if x > -1 and y > -1 and x2 > -1 and y2 > -1:
            rosecolourtext(c, c)
            if x2 < x: x, y, x2, y2 = x2, y2, x, y
            roseliney = [y, y2]
            roselinec = 0
            roselinestep = int(y2 - y)
            if roselinestep < 0: roselinestep = int(y - y2) ; roselinec = 0
            if roselinestep < 1: roselinestep = 1
            roselinestep = float(1) / roselinestep
            roselinex = x
            while 1:
                if roselinex > x2: break
                if y2 - y == 0:
                    roselocate(0, int(y) + 1, int(roselinex) + 1)
                    stdout.write(unichr(9608))
                elif y2 < y:
                    roselinec -= roselinestep
                    roselocate(0, int(y + int(float(y - y2) / rosenonz(x2 - x,.1) *
                    rosenonz(roselinec,.1) ) ) + 1, int(roselinex) + 1)
                    stdout.write(unichr(9608))
                else:
                    roselocate(0, int(y + int(float(y2 - y) / rosenonz(x2 - x,.1) *
                    rosenonz ( roselinec,.1) ) ) + 1, int(roselinex) + 1) ;
                    stdout.write(unichr(9608))
                    roselinec += roselinestep
                    #[0] = roseliney[0]+float(roseliney[1] - roseliney[0]) / (x2 - x)
                roselinex += roselinestep
            roselocate(0, int(y) + 1, int(x) + 1) ; stdout.write(unichr(9608))
            roselocate(0, int(y2) + 1, int(x2) + 1) ; stdout.write(unichr(9608))
            sys.stdout.flush()

def anykeypyg():
    global yourscreen
    global roseraphics, roserupd
    p = 0
    p = 1\n\n"""

addtoout += [0] ; addto += [0]

# -2: print(variable, etc)
# -1: print(variable), 0: variable = int(variable), 1: variable=left(variable, etc)

cmds = {"ltrim":0, "input":0, "len":0, "asc":0, "pi":0, "str":0,
"get":1, "chr":0, "displays":-1, "sleep":-2, "cdxsort":-1,
"cdxeverse":-1, "reverse":0, "exit":-1, "display":-1, "cdxset":-3,
"cdxsplit":2, "left":1, "cdxjoin":2, "cdxget":2, "mid":2, "right":1,
"add":1, "times":1, "close":-1, "esc":-1,
"cdxsave":-2, "cdxload":1, "cdxin":0, "cdxcurl":1, "colourtext":-2,
"highlight":-2, "divby":1, "hex":0, "rtrim":0, "cdxcmd":0,
"time":0, "date":0, "oct":0, "val":0, "subtract":1, "lcase":0, "ucase":0,
"int":0, "left":1, "swap":-3, "locate":-3, "pset":-4, "line":-6,
"return":-2, "randint":2, "exp":1, "cdx":0, "dict":0, "mod":1, "cos":0,
"not":0, "sin":0, "instr":2, "chdir":-1, "shell":-1, "cdxshell":0, "colortext":-2,}

funcs = {"function" : -1, "use" : -2, "iftrue" : -2, "ifequal" : -3, "ifless" : -3,
"ifmore" : -3, "try":0, "except":0, "resume":0, "else":0}

ufunc = {}

#addfuncs = addtoout[0] + addtoout[1] + addtoout[3] + """
addfuncs = """
def rosecolortext(x, f):
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
    stdout.write("\\x1b[" + n + ";" + str(30+f) + "m")
    return "\\x1b[" + n + ";" + str(30+f) + ";" + str(40+b) + "m"

def rosecolourtext(x, f):
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
    stdout.write("\\x1b[" + n + ";" + str(30+f) + "m")
    return "\\x1b[" + n + ";" + str(30+f) + ";" + str(40+b) + "m"

rosecgapal = [(0, 0, 0), (0, 0, 170), (0, 170, 0), (0, 170, 170),
(170, 0, 0), (170, 0, 170), (170, 85, 0), (170, 170, 170),
(85, 85, 85), (85, 85, 255), (85, 255, 85), (85, 255, 255),
(255, 85, 85), (255, 85, 255), (255, 255, 85), (255, 255, 255)]

def roseget(p, s): return s

def rosehighlight(x, b):
    f = None
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
    stdout.write("\\x1b[" + n + str(40+b) + "m")
    return "\\x1b[" + n + str(40+b) + "m"

def roseinstr(x, p, e):
    try: return p.index(e) + 1
    except: return 0

def rosechdir(p):
    try: roseoch(p)
    except: print "no such file or directory: " + str(p) ; roseend(1)

def roseshell(p):
    global rosesysteme
    try: rosesysteme = rosesh(p)
    except:
        print "error running shell command: " + chr(34) + str(p) + chr(34)
        roseend(1)

def rosecdxshell(c):
    global rosesysteme
    try:
        rosesysteme = 0
        sh = rosepo(c)
        ps = sh.read().replace(chr(13) + chr(10),
        chr(10)).replace(chr(13), chr(10)).split(chr(10))
        rosesysteme = sh.close()
    except:
        print "error running cdxshell command: " + chr(34) + str(c) + chr(34)
        roseend(1)
    return ps[:]

def rosesgn(p):
    p = float(p)
    if p > 0: return 1
    if p < 0: return -1
    return 0

def rosestr(p): return str(p)
def rosedisplay(p): print rosearr2cdx("", p)
def rosechr(p):
    if type(p) == str:
        if len(p) > 0:
            return p[0]
    return chr(p)
def rosedisplays(p): stdout.write(str(p)) ; sys.stdout.flush()
def roseleft(p, s): return p[:s]
def rosemid(p, s, x):
    cdx = 0
    if type(p) == list or type(p) == tuple: cdx = 1
    rt = p[s - 1:x + s - 1]
    if cdx and len(rt) == 1: rt = rt[0]
    return rt
def roseright(p, s): return p[-s:]
def roserandint(x, s, f):
    return randint(s, f)
def roselcase(p): return p.lower()

def roseucase(p): return p.upper()
def roseint(p): return int(p)

def rosecdxset(x, p, s):
    if 1:
        #if type(p) == str: p = p + s # str(s) if you want it easier
        if type(x) == dict:
            if type(s) == tuple:
                if len(s) == 1: fas = s[0]
            elif type(s) == list:
                if len(s) == 1: fas = s[0]
            else:
                fas = s
            x[p] = s
        else: #type(p) == list:
            if type(s) == tuple:
                if len(s) == 1: fas = s[0]
            elif type(s) == list:
                if len(s) == 1: fas = s[0]
            else:
                fas = s
            x[p - 1] = s
        #if type(p) == tuple:
        #    if type(s) == tuple:
        #        p = tuple(list(p) + list(s))
        #    elif type(s) == list:
        #        p = tuple(list(p) + s[:])
        #    else:
        #        p = tuple(list(p) + [s])
        #if type(p) == str: p = p + s # str(s) if you want it easier

def rosefprint(x, s):
    fon = roseosname
    sep = chr(10)
    if fon == "nt": sep = chr(13) + chr(10)
    rosefilehandles[s].write(str(x) + sep)

def roseflineinput(x, s):
    try:
        p = rosefilehandles[s][rosefilecounters[s]].replace(chr(13),
        "").replace(chr(10), "")
        rosefilecounters[s] += 1
    except:
        p = chr(10)
    return p

def roseclose(x):
    if (x) in rosefilehandles.keys():
        rosefilehandles[x].close() ; del rosefilehandles[x]
        try: del rosefilecounters[x]
        except: pass

def roseesc(x):
    if roseosname == "nt": esc = rosesh("cls")
    else: stdout.write("\x1b[2J\x1b[1;1H") ; sys.stdout.flush()

def rosecdxload(x, s):
    x = open(s).read().replace(chr(13) + chr(10), chr(10)).replace(chr(13),
    chr(10)).split(chr(10))
    return x[:]

def rosecdxsave(v, dx):
    sep = chr(10)
    if roseosname == "nt": sep = chr(13) + chr(10)
    try:
        v = rosecdx2arr(v)
        if len(v) > 1 and v[-1:] == "": v = v[:-1]
    except: pass
    rosefilehandle = open(dx, "w")
    rosefilehandle.write(rosecdxjoin('', v, sep) + sep)
    rosefilehandle.close()

def rosecdxcurl(x, s):
    from urllib import urlopen
    x = str(urlopen(s).read()) ; x = x.replace(chr(13) + chr(10),
    chr(10)).replace(chr(13), chr(10)).split(chr(10))
    return x[:]

def rosecdxin(x):
    ps = []
    for p in stdin: ps += [p[:-1]]
    return ps[:]

def rosecdxget(x, p, s):
    if type(p) == dict:
        return p[s]
    else:
        return p[s - 1]

def roseadd(p, s):
    if type(p) in (float, int):
        if type(s) in (float, int):
            p = p + s
        else:
            p = p + s # float(s) if you want it easier
        if p == float(int(p)): p = int(p)
    else:
        if type(p) == str: p = p + s # str(s) if you want it easier
        if type(p) == list:
            if type(s) == tuple:
                p = p + list(s)
            elif type(s) == list:
                p = p + s[:]
            else:
                p = p + [s]
        if type(p) == dict:
            if type(s) == dict:
                for t in s.keys(): p[t] = s[t]
                p = p + s[:]
            else:
                p[len(p) + 1] = s
        if type(p) == tuple:
            if type(s) == tuple:
                p = tuple(list(p) + list(s))
            elif type(s) == list:
                p = tuple(list(p) + s[:])
            else:
                p = tuple(list(p) + [s])
    return p

def rosecdxjoin(p, x, s):
    t = ""
    if type(x) == list: x = rosearr2cdx("", x)
    k = x.keys() ; k.sort()
    if len(k) : t = str(x[k[0]])
    

    for c in range(len(k)):
        if c > 0: t += str(s) + str(x[k[c]])
    return t # s.join(x)

def rosecdx(x):
    if type(x) in (float, int, str):
        p = {} ; p[1] = x
    else:
        p = {} ; p[1] = rosecdx2arr("", x)[0]
    return p

def rosedict(x):
    if type(x) in (float, int, str):
        p = {} ; p[1] = x
    else:
        p = {} ; p[1] = rosecdx2arr("", x)[0]
    return p

def rosearr2cdx(p, x):
    if type(x) == list: 
        p = x[:]
        x = {}
        c = 0
        for t in p: c += 1 ; x[c] = t
        return x
    return x

def rosecdx2arr(p, x):
    if type(x) == dict: 
        p = {}
        for t in x.keys(): p[t] = x[t]
        x = []
        t = p.keys() ; t.sort()
        for c in t: x += [p[c],]
    return x

def rosecdxsplit(p, x, s):
    return rosearr2cdx("", x.split(s))

def roseval(n):
    n = float(n)
    if float(int(n)) == float(n): n = int(n)
    return n    
def rosetimes(p, s):
    if type(p) in (float, int):
        p = p * s # float(s) if you want it easier
        if p == float(int(p)): p = int(p)
    else:
        if type(p) == list:
            p = p[:] * s # roseval(s)
        else:
            p = p * s # roseval(s) if you want it easer
    return p
def rosedivby(p, s):
    p = float(p) / s
    if p == float(int(p)): p = int(p)
    return p
def rosesubtract(p, s): return p - s

def roseexp(p, s):
    p = p ** s
    if p == float(int(p)): p = int(p)
    return p
def rosemod(p, s):
    return p % s
def rosecos(p):
    from math import cos ; p = cos(p)
    if p == float(int(p)): p = int(p)
    return p
def rosesin(p):
    from math import sin ; p = sin(p)
    if p == float(int(p)): p = int(p)
    return p

def roseltrim(p): return p.lstrip()
def roselineinput(p): return raw_input()
def roselen(p): return len(p)
def roseasc(p): return ord(p[0])
def rosepi(p):
    return 3.14159265359

def rosehex(p): return hex(p)
def rosertrim(p): return p.rstrip()
def rosestring(x, p, n):
    if type(n) == str: return n * p
    return chr(n) * p

def rosetime(p): from time import strftime ; return strftime("%H:%M:%S")

def rosedate(p): from time import strftime ; return strftime("%m/%d/%Y")

def rosecdxcmd(p): return roseargv[1:]

def roseoct(p): return oct(p)

def rosesleep(p, s):
    #print lc () + p
    #addto[0] = 1
    sleep(s)
def rosecdxsort(p):
    p.sort()

def rosereverse(p):
    if type(p) == list: p.reverse() ; return p
    elif type(p) == str:
        p = map(str, p) ; p.reverse()
        p = "".join(p)
        return p

def rosecdxeverse(p):
    p.reverse()

def rosefunction(p, s): return p
def roseend(x): quit()
def roseif(p, s): return p
def rosethen(p, s): return p
def roseexit(x): quit()
\n"""

demo = """

use t 
"this is a codex; a sort of hybrid array/dictionary type" cdxsplit t ";" display 
forin x t
use x
display
next
use t
display

use p
displays
7 cdx add 7 add 7 add 7 add 7

use x
#z x 
5
5 
times 7
add 5 times 7

function hello p  |  # function hello(p)
"hello, "       |  # x = "hello, "
displays return 5 |  # print x; : hello = 5 : exit function
next               |  # end function

#hello x         |  # x = hello(x)

use c

cdxcmd display

use p

display
# sleep 1
display cdxset 2 8 display

use z
cdxjoin p "(_)" display
use x
x z display

use p
dict display
cdxset "" 10 display add 9 add 10 display

use um
cdxjoin p "" display
use uh
cdxsplit um "0" display

#0[]
#[7, 7, 7, 7, 7]
#[7, 7, 7, 7, 7]
#[7, 8, 7, 7, 7]
#7(_)8(_)7(_)7(_)7
#7(_)8(_)7(_)7(_)7
#{'': 7}
#{'': 10}
#10

use p

cdxget p "" display exit

function add5 r
use x
get r add 5 return x
next

#y 12

function ppp
use z
32 chr display
for p 1 100 1
use x
randint 0 3
use y
randint 0 3
use c
randint 1 9
#z pset x y c
colourtext 7
next
next

use z
ppp
sleep 1 display
#textmode

"""

roseusevar = "rose" ; roseunusedvar = 1

p = ""
try: p = right(sys.argv, 1)[0]
except: pass
if not ".rose" in p.lower():
    if p.lower() == "help":
        stdout.write("\n    type (any) part of the command you want help on." +
        "\n\n    rose will show all matches.\n\n\n    ")
        helpf = chelp(raw_input())
        if not helpf: print(colour(14,0)+"\n    no commands match your search.") ; print("")
        colour(7,0)
    #try: inputfile = stdin.read().replace(chr(13), "").split("\n")
    #except:
    #print "need an input file to do anything..."; print ; quit()
        quit()
    else:
        print "using built-in demo source, translating to demo.rose.py..." ; print
        p = "demo.rose"
        inputfile = demo.replace(chr(13), "").split("\n")
else:
    try:
        inputfile = open(p).read().replace(chr(13) + chr(10),
        chr(10)).replace(chr(13), chr(10)).split(chr(10))
    except: print "couldn't open \"" + p + "\", exiting." ; print ; quit()
try: outfile = open(p + ".py", "w")
except: print "couldn't write to \"" + p + ".py" "\", exiting." ; print ; quit()
outname = p + ".py"

flen = len(str(len(inputfile)))

linecount = 0
indent = 0
inlinep = 0
inle = 0
errorin = 0
errorsrc = ""
error = ""
mode = 0
roseraphics = -1 # -1 = uninitialised, 0 = textmode, 1 = initialised
vrs = []
vr = ""
outb = []
ingfx = 0
linesoutc = 0

for p in inputfile:
    linecount += 1 ; vrop = 0 ; vrcl = 0

    if linecount == 1:
        outfile.write("#!/usr/bin/env python" + "\n# encoding: utf-8\n")
        if "," in proginf:
            outfile.write("# rose translator version: " + proginf.split(",")[0] + "\n")

    elif mode == 0:
        x = rosefsplit(p.lstrip())
        lp = p.lower()
        if not len(p):
            print lc() + ""
            #% write copied blank lines from inline python
            outfilewrite(outb, "\n")

        if len(p.lstrip()):

            e = 0

            if p.lstrip()[0] == "#":
                if linecount == 1:
                    es = 0
                    try:
                         if p.lstrip()[1] == "!": es = 1
                    except: es = 0
                    if not es:
                        wr(p)
                        print lc(), rosefsp(p)
                    else: print lc() + "[this first comment isn't copied over]"
                    es = 0
                else:
                    #% write comments
                    #print colour(14, 0) + p + colour(7,0) ; znul = raw_input()  #$
                    outfilewrite(outb, chr(32) * atleast(0, indent) + p + "\n")
                    print lc(), rosefsp(p)

            elif lnob(x, 0) == "use": 
                roseunusedvar = 0 
                #roseusevar = lnob(x, 1) ; outfilewrite(outb, chr(32) * atleast(0, indent) + "print \"*" + roseusevar + "*\",")
                roseusevar = lnob(x, 1)
                print lc(), colour(15, 0) + rosefsp(p) + colour(7, 0)

            elif lnob(x, 0) == "roseg":
                 e = 2

            else:
                if roseusevar != "rose" and lnob(x, 0) not in funcs.keys() + ["forin", "rose",
                    "for", "function", "nextin",
                    "next", "while", "wend"] + ["break", "pass"]: x = [roseusevar] + x
                if not roseusevar == "roseg":
                    if roseusevar != "rose" and not roseusevar in cmds.keys() and not lnob(x, 0) in funcs.keys() + ["forin", 
                    "for", "function", "nextin",
                    "next", "while", "wend"] + ["break", "pass"]:
                        if not roseusevar in vrs: vrs += [roseusevar[:]] # main vars, also func params, etc
                        #% write variable
                        #var: print colour(14, 0) + "variable:" + roseusevar + colour(7,0) ; znul = raw_input()  #$
                        outfilewrite(outb, "\n")
                        outfilewrite(outb, chr(32) * atleast(0, indent) +
                        "roselist = 0\n")

                        outfilewrite(outb, chr(32) * atleast(0, indent) +
                        "try: roselist = int(type(" + roseusevar + ") in (list, dict, float, int, str))\n")

                        outfilewrite(outb, chr(32) * atleast(0, indent) +
                        "except NameError: pass\n")
                        outfilewrite(outb, chr(32) * atleast(0, indent) +
                        "if not roselist: " + roseusevar + " = 0 \n")

                    if lnob(x, 0) == "rose":
                        #print lc () + p
                        #% write? its whitespace
                        #$
                        indent = atleast(0, indent - 4)
                    if lnob(x, 0) == "wend":
                        #print lc () + p
                        #% write? its whitespace
                        #$
                        indent = atleast(0, indent - 4)
                    if lnob(x, 0) == "next":
                        #print lc () + p
                        #% write? its whitespace
                        #$
                        indent = atleast(0, indent - 4)
                    if lnob(x, 0) == "nextin":
                        #print lc () + p
                        #% write? its whitespace
                        #$
                        indent = atleast(0, indent - 4)
                    if lnob(x, 0) == "try":
                        #print lc () + p
                        #% write try line
                        #$
                        outfilewrite(outb, chr(32) * atleast(0, indent) + "try:\n")
                        indent = atleast(0, indent + 4)
                    if lnob(x, 0) == "else":
                        #print lc () + p
                        #% write else line
                        #$
                        outfilewrite(outb, chr(32) * atleast(0, indent - 4) +
                        "else:\n")
                    if lnob(x, 0) == "except":
                        #print lc () + p
                        indent = atleast(0, indent - 4)
                        #% write except line
                        #$
                        outfilewrite(outb, chr(32) * atleast(0, indent) +
                        "except:\n")
                        indent = atleast(0, indent + 4)
                    if lnob(x, 0) == "resume":
                        #print lc () + p
                        #% write? its whitespace
                        #$
                        indent = atleast(0, indent - 4)
                    if lnob(x, 0) == "while":
                        #print lc () + p
                        #% write simple loop
                        #$
                        outfilewrite(outb, chr(32) * atleast(0, indent) +
                        "while 1:\n")
                        indent += 4
                    if lnob(x, 0) == "function" and len(getmore(x, 1)) > 0:
                        #print lc () + p
                        mkf = []
                        funcname = getlmore(x, 1)[0]
                        prm = 1
                        while 1:
                            try:
                                aprm = getlmore(x, 1)[prm]
                                if len(aprm):
                                    if aprm[0] != "#":
                                        mkf += [aprm]
                                        if aprm not in vrs: vrs += [aprm[:]]
                                prm += 1
                            except: break
                        ufunc[funcname] = mkf[:] #; print ufunc # #
                        #print ufunc
                        #print len(ufunc[funcname])
                        #% write func def
                        #$ print colour(14,0)+ "def " +  funcname + "(" + ", ".join(mkf) + "):" + colour(7,0)
                        outfilewrite(outb, chr(32) * atleast(0, indent) + "def " +
                        funcname + "(" + ", ".join(mkf) + "):\n")
                        indent += 4

                    if lnob(x, 0) == "for" and len(getmore(x, 1)) == 4:
                        #print lc () + p
                        gmro = getlmore(x, 1)[0]
                        gmrt = getlmore(x, 1)[1]
                        gmrh = getlmore(x, 1)[2]
                        gmrf = getlmore(x, 1)[3]
                        if gmro not in vrs: vrs += [gmro[:]]
                        if "." not in gmrf and (gmrf.strip()) not in ("0",
                        "0.0", "-0") and "." not in gmrt and "." not in gmrh:
                            #% write standard for loop
                            #$
                            outfilewrite(outb, chr(32) * atleast(0, indent)
                            + "for "
                            + gmro + " in range(int(float(" + gmrt +
                            ")), int(float(" + gmrh + ")) + rosesgn(" + gmrf +
                            "), rosenonz(int(float(" + gmrf + ")))):\n")
                        else:
                            #% write for loop that allows floating step
                            #$
                            outfilewrite(outb, chr(32) * atleast(0, indent) + gmro
                            + " = float(" + gmrt + ") - float(" + gmrf + ")\n" +
                            chr(32) * atleast(0, indent) + "while 1:\n" + chr(32) *
                            atleast(0, indent + 4) + gmro + " += float(" + gmrf +
                            ")\n" + chr(32) * atleast(0, indent + 4) + "if " +
                            gmrf +
                            " > 0 and " + gmro + " > float(" + gmrh + "): break\n"
                            + chr(32) * atleast(0, indent + 4) + "elif " + gmrf +
                            " <= 0 and " + gmro +
                            " < float(" + gmrh + "): break\n")
                        indent += 4

                    if lnob(x, 0) == "forin" and len(getmore(x, 1)) == 2:
                        #print lc () + p
                        gmro = getlmore(x, 1)[0]
                        gmrt = getlmore(x, 1)[1]
                        if gmro not in vrs: vrs += [gmro[:]]
                        #% write forin command with params
                        #$
                        outfilewrite(outb, chr(32) * atleast(0, indent) + "for " +
                        gmro + " in rosecdx2arr(0, " + gmrt + "):\n")
                        indent += 4

                    if lnob(x, 0) == "break":
                        #print lc () + p
                        #% write break command
                        #$ print
                        outfilewrite(outb, chr(32) *
                        atleast(0, indent) + "break\n")

                    if lnob(x, 0) == "pass":
                        #print lc () + p
                        #% write pass command
                        #$ print
                        outfilewrite(outb, chr(32) *
                        atleast(0, indent) + "pass\n")

                    if lnob(x, 0) == "iftrue":
                        #print lc () + p
                        #% write iftrue
                        #$ print colour(14,0) + "if " +    snob(x, 1) + " > " + snob(x, 2) + ":\n"+ " ; " +colour(7,0)
                        outfilewrite(outb, chr(32) * atleast(0, indent) + "if " +
                        snob(x, 1) + ":\n") ; indent += 4

                    if lnob(x, 0) == "use":
                        #print lc () + p
                        #% write iftrue
                        #$ print colour(14,0) + "use " +    snob(x, 1) + " > " + snob(x, 2) + ":\n"+ " ; " +colour(7,0)
                        #outfilewrite(outb, chr(32) * atleast(0, indent) + "if " +
                        #snob(x, 1) + ":\n") ; indent += 4
                        roseunusedvar = 0
                        roseusevar = lnob(x, 1) ; outfilewrite(outb, chr(32) * atleast(0, indent) + "print \"*" + roseusevar + "*\",")

                    if lnob(x, 0) == "ifequal" and len(getmore(x, 1)) == 2:
                        #print lc () + p
                        #% write ifequal
                        #$ print colour(14,0) + "if " +    snob(x, 1) + " > " + snob(x, 2) + ":\n"+ " ; " +colour(7,0)
                        outfilewrite(outb, chr(32) * atleast(0, indent) + "if " +
                        snob(x, 1) + " == " + snob(x, 2) + ":\n") ; indent += 4

                    if lnob(x, 0) == "ifless" and len(getmore(x, 1)) == 2:
                        #print lc () + p
                        #% write ifless
                        #$ print colour(14,0) + "if " +    snob(x, 1) + " > " + snob(x, 2) + ":\n"+ " ; " +colour(7,0)
                        outfilewrite(outb, chr(32) * atleast(0, indent) + "if " +
                        snob(x, 1) + " < " + snob(x, 2) + ":\n") ; indent += 4

                    if lnob(x, 0) == "ifmore" and len(getmore(x, 1)) == 2:
                        #print lc () + p
                        #% write ifmore
                        #$ print colour(14,0) + "if " +    snob(x, 1) + " > " + snob(x, 2) + ":\n"+ " ; " +colour(7,0)
                        outfilewrite(outb, chr(32) * atleast(0, indent) + "if " +
                        snob(x, 1) + " > " + snob(x, 2) + ":\n") ; indent += 4

                    if lnob(x, 0) in cmds.keys(): # + ufunc.keys():
                        e = 4 ; shln = lnob(x, 0)

                    if lnob(x, 0) != "rose" and lnob(x,
                    0) not in funcs.keys() + ["forin", "for", "function",
                    "nextin", "next", "while", "wend"] + ["break", "pass"]:

                        #print lc () + p
                        vr = roseusevar
                        #print vr, type(vr)
                        #print getlmore(x, 1)
                        prsc = 0
                        cstrctr = 0
                        csbuf = []
                        vrcs = ""
                        for prs in getlmore(x, 1):                            
                            #$ print prs
                            if "rose" in prs:
                                if prs[:4] == "rose": e = 2 ; break ; break
                            if prs in funcs.keys():
                                e = 3 ; shln = prs
                            prsc += 1
                            if cstrctr > 0:
                                vrcs += prs
                                cstrctr -= 1
                                if cstrctr == 0:

                                    if lnob(x, prsc - 1) == "return":
                                        #% write return command
                                        #$ print colour(14,0) +vrcs + " ; " +colour(7,0)
                                        outfilewrite(outb, chr(32) * atleast(0,
                                        indent) + vrcs)

                                    elif lnob(x, prsc - 2) == "swap":
                                        vrcs = lnob(x, prsc - 1) + ", " + lnob(x,
                                        prsc - 0) + " = " + lnob(x,
                                        prsc - 0) + ", " + lnob(x, prsc - 1)
                                        #% write swap of 2 vars in python syntax
                                        #$ print colour(14,0) +vrcs + " ; " +colour(7,0)
                                        outfilewrite(outb, chr(32) * atleast(0,
                                        indent) + vrcs + " ; ")
                                    else:

                                        if roseprsbac in ufunc.keys():
                                            #% write parametered func call
                                            #$ print colour(14,0)+  vrcs + ") ; " + lnob(x, 0) + " = rosenone(" + lnob(x, 0) + ", rosebac) ; " +colour(7,0)
                                            outfilewrite(outb, chr(32) * atleast(0,
                                            indent) + vrcs + ") ; " + lnob(x, 0) +
                                            " = rosenone(" + lnob(x, 0) +
                                            ", rosebac) ; ") ; vrcl += 1
                                        else:
                                            #% write builtin func call assignment
                                            #$ print colour(14,0)+  vr + " = " +  vrcs + ") ; "  +colour(7,0)
                                            outfilewrite(outb, chr(32) *
                                            atleast(0, indent) + vrcs + ") ; ") ; vrcl += 1
                                else:
                                    vrcs += ", " #; print "*"
                                    #if
                                continue

                            if prs.lower() in funcs.keys() + ["forin", "for",
                            "function", "nextin", "next", "while",
                            "wend"] + ["break", "pass"]:
                                e = 3
                            roseprsbac = None

                            if cstrctr == 0:
                                if not prs.lower() in vrs:
                                    if prs.lower()[0] in "abcdefghijklmnopqrstuvwxyz":
                                        if not prs.lower() in ufunc.keys():
                                            if not prs.lower() in funcs.keys():
                                                if not prs.lower() in cmds.keys():
                                                    e = 5 ; shln = prs

                            if prs.lower() in vrs and cstrctr == 0:
                                #and len(getmore(x, 1)) == 1:
                                #% write lefthand variable assignment
                                #$ print colour(14,0)+  vr + " = " + prs.lower()  +colour(7,0)
                                outfilewrite(outb, chr(32) * atleast(0, indent) +
                                vr + " = " + prs.lower() + "\n")

                            if prs[0] == "\"":
                                #% write string assignment (any place in shared line)
                                outfilewrite(outb, chr(32) * atleast(0, indent) +
                                vr + " = " + prs + " ; ")

                            if prs[0] in ".1234567890-":
                                #% write numerics
                                outfilewrite(outb, chr(32) * atleast(0, indent) +
                                vr + " = " + prs + " ; ")

                            if prs[0] == "#":
                                #% write trailing comments #$ print colour(14, 0) + prs  + colour(7,0)
                                outfilewrite(outb, prs + "\n") ; break


                            if prs.lower() in ufunc.keys():
                                #% write pre-func-call var backup for sub-style behavior #$ print colour(14, 0) + "rosebac = " + lnob(x,0) + " ; " + colour(7,0)
                                outfilewrite(outb, chr(32) * atleast(0, indent) +
                                "rosebac = " + lnob(x,0) + " ; " ) # ##
                                roseprsbac = prs.lower()    

                                cstrctr = len(ufunc[prs])
                                #print cstrctr
                                if cstrctr == 0:
                                    #% write zero-param func/?sub call
                                    #$ print colour(14, 0) + vr + " = " + prs.lower() + "() ; " + lnob(x, 0) + " = rosenone(" + lnob(x, 0) + ", rosebac) ; " + colour(7,0)
                                    outfilewrite(outb, chr(32) *
                                    atleast(0, indent) +
                                    vr + " = " + prs.lower() + "() ; " + lnob(x, 0) +
                                            " = rosenone(" + lnob(x, 0) + ", rosebac) ; ") # #
                                else:
                                    #print "y"
                                    vrop += 1
                                    vrcs = vr + " = " + prs.lower() + "("
                                    #$ print colour(4, 0) + vr + " = " + prs.lower() + "(" + colour(7,0) #$
                                    #multiparameter  


                            if prs.lower() in cmds.keys():
                                if prs.lower() in ["pset", "line"]:
                                    ingfx = 1
                                ##print prs    
                                cstrctr = cmds[prs]
                                ##print cstrctr
                                if cstrctr == -1:
                                    #% write zero-param subs
                                    #print colour(14, 0) + "rose" +  prs.lower() + "(" + vr
                                    #+ ") ; " + colour(7,0) ; #znul = raw_input()  #$
                                    outfilewrite(outb, chr(32) *
                                    atleast(0, indent) + "rose" +
                                    prs.lower() + "(" + vr + ") ; " ) ; vrcl += 1

                                if cstrctr == 0:
                                    #% write zero-param functions
                                    #print colour(14, 0) + vr + " = rose" + prs.lower()
                                    #+ "(" + vr + ") ; "+ colour(7,0) ; #znul = raw_input()  #$
                                    outfilewrite(outb, chr(32) * atleast(0,
                                    indent) + vr +
                                    " = rose" + prs.lower() + "(" + vr + ") ; " ) ; vrcl += 1

                                if cstrctr < -1:
                                    if prs == "return":

                                        cstrctr = abs(cstrctr) - 1
                                        vrcs = "return " #parameter
                                    else:
                                        cstrctr = abs(cstrctr) - 1
                                        if prs == "swap": vrcs = "swap "
                                        else:
                                            vrop += 1
                                            vrcs = "rose" + prs.lower() + "(" + vr
                                            vrcs += ", " #multiparameter  
                                else:
                                    vrop += 1
                                    vrcs = vr + " = rose" + prs.lower() + "(" + vr
                                    vrcs += ", " #multiparameter  

                        if vrop == vrcl and e == 0:
                            print lc(), rosefsp(p)

                        #% finish each line with lf
                        outfilewrite(outb, "\n")
                    else:
                        print lc() + p
                else:
                    e = 2

            #vrck = len(outb)
            #try:
            #    if "(" in vrcs and vrck == 0:
            #        e = 1
            #except: pass

            if e == 1:
                e = 0
                if not len(error):
                    error = "error: problem in command structure or details."
                    errorin = linecount
                    errorsrc = p
                print lc() + colour(14, 0) + str(p) + colour(7, 0)
                break

            if e == 2:
                e = 0
                if not len(error):
                    error = "error: cannot create variable or function beginning"
                    error += " with \"rose\""
                    errorin = linecount
                    errorsrc = p
                print lc() + colour(14, 0) + p + colour(7, 0)
                break

            if e == 3:
                e = 0
                if not len(error):
                    error = "error: single-line command \"" + shln + "\" not on own line"
                    errorin = linecount
                    errorsrc = p
                print lc() + colour(14, 0) + p + colour(7, 0)
                break

            if e == 4:
                e = 0
                if not len(error):
                    error = "error: shared-line function \""
                    error += shln + "\" cannot be used to start a line"
                    errorin = linecount
                    errorsrc = p
                print lc() + colour(14, 0) + p + colour(7, 0)
                break

            if e == 5:
                e = 0
                if not len(error):
                    error = "error: variable or function not created, but referenced... \""
                    error += shln + "\" needs to be set before first use"
                    errorin = linecount
                    errorsrc = p
                print lc() + colour(14, 0) + p + colour(7, 0)
                break

    if vrcl != vrop:
                e = 0
                if not len(error):
                    error = "error: a command has the wrong number of parameters."
                    errorin = linecount
                    errorsrc = p
                print lc() + colour(14, 0) + str(p) + colour(7, 0)
                break

#for p in range(len(addtoout)):
#    if addto[p]: outfilewrite(outb, addtoout[p])
#for p in buf:
#    outfilewrite(outb, p)

if ingfx == 0: addtoout[3] = ""
outfile.write(addtoout[0] + addtoout[1] + addtoout[3] + addfuncs)
for outsb in outb: outfile.write(outsb)
outfile.close()


print
if errorin:
    print error ; colour(14, None) ; print "error in line " + str(errorin) + ":"
    colour(7, None)
    print errorsrc
    #from os import system as stf ; p = stf("touch e")
else:
    try:
        if os.name != "nt": os.system("chmod +x \"" + outname + "\"")
    except: pass
    colour (13, None) ; print "translation complete. ", ; colour(7, None)
    print "here's a python script you can run: ",
    print colour(13, None) + outname + colour(7, None) ; print ; print
    print "now running: " + outname + nl
    ## run actual program
    prog = nl.join(open(outname).readlines())
    exec(prog)
