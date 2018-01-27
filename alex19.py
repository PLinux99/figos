#!/usr/bin/env python
# coding: utf-8 
#### license: creative commons cc0 1.0 (public domain) 
#### http://creativecommons.org/publicdomain/zero/1.0/ 
proginf = "alex 1.9, jan 2018 mn"
try: import readline 
except: p = 0
import sys
import os
from datetime import datetime
from hashlib import sha256
from sys import stdin, stdout
from os import popen
from os import name as alexosname
if alexosname == "nt":
    try: from colorama import init ; init()
    except: pass
try: from sys import exit as quit
except: pass

cmdhelp = [("timer", "input (shared-line) change main variable to number of seconds past midnight")

,("arrstdin", "input (shared-line) change main variable to array containing lines of stdin")
,("flineinput filepath", "input (shared-line) change main var to string of line from open file filepath")
,("arropen filepath", "input (shared-line) change main variable to array of file lines in filepath")
,("arrcurl url", "input (shared-line) like arropen, except downloading url into the array")
,("sleep seconds", "input (shared-line) wait for number of seconds before continuing with program")
,("command", "input (shared-line) change main variable to array of command line parameters")
,("print", "output (shared-line) output main variable to the screen (aka stdout)")
,("prints", "output (shared-line) put main var to screen; like print but (s)tays on line.")
,("fprint filepath", "output (shared-line) write main variable to open file designated by filepath")
,("while", "loop --\\own\\line mark the start of a loop (will keep going without break)")
,("break", "loop --\\own\\line put in the middle of a loop to exit (stop looping)")
,("for var strt stop step", "loop --\\own\\line start a for loop, changing var from strt to stop, by step")
,("forin var array", "loop --\\own\\line loop through each item in array; for each, set var to item")
,("iftrue ckvar", "conditional --\\own\\line run lines between iftrue and fig if ckvar is \"non-zero\"")
,("ifequal var1 var2", "conditional --\\own\\line run lines between ifequal and fig if var1 equals var2")
,("ifmore var1 var2", "conditional --\\own\\line run lines between ifmore and fig if var1 is > var2")
,("ifless var1 var2", "conditional --\\own\\line run lines between ifless and fig if var1 is < var2")
,("try", "conditional --\\own\\line put code that might not work between try and except")
,("except", "conditional --\\own\\line if code between try/except fails, run the code after except")
,("resume", "conditional --\\own\\line mark the end of try / except / resume command block")
,("else", "conditional --\\own\\line after if- line, before fig. run lines if condition isnt true")
,("function name p1 p2 â€¦", "function --\\own\\line define function named name with optional params p1,p2, etc")
,("get parametername", "function (shared-line) (no longer required) copy parametername value to main var")
,("python", "function --\\own\\line put inline python code between lines python and fig")
,("fig/next/nextin/wend", "fig (interchangeable) function --\\own\\line finalise a block (started by if/while/function/for/forin")
,("pass", "function --\\own\\line blocks (for/next, etc) require something inside lines; pass works / does nothing")
,("lcase", "function (shared-line) change main variable to all-lower-case copy of own value")
,("ucase", "function (shared-line) change main variable to all-upper-case copy of own value")
,("str", "function (shared-line) convert main variable from number to string")
,("asc", "function (shared-line) change main variable from string to ascii code of 1st char")
,("val", "function (shared-line) change main variable from string to numeric (int if whole)")
,("len", "function (shared-line) change main variable to  numeric length of main var")
,("not", "function (shared-line) change main variable to zero if non-zero; or -1 if zero")
,("ltrim", "function (shared-line) strip whitespace from left side of main variable")
,("rtrim", "function (shared-line) strip whitespace from right side of main variable")
,("chr", "function (shared-line) change main variable from numeric to ascii/uni string")
,("arrshell", "function (shared-line) change main var to array of shell output (from main var)")
,("arreverse", "function (shared-line) change main variable from array to reverse order of array")
,("reverse", "function (shared-line) like arreverse (which might be faster for array) for strings")
,("arrsort", "function (shared-line) change main variable from array to sorted array")
,("#", "comment (can\\share) place at beginning (or end) of line, prior to a comment")
,("():;|=,. ( ) : ; | = , .", "optional (shared-line) use in a shared line (and some others) for aesthetics/notation")
,("left numofcharsoritems", "function (shared-line) change main variable to __ leftmost group of chars/items")
,("right numofchrsoritems", "function (shared-line) change main variable to __ rightmost group of chars/items")
,("arrget array position", "function (shared-line) change main variable to position-th item from array")
,("arrset position setto", "function (shared-line) change item in array in main variable to value of setto")
,("mid position len", "function (shared-line) change main variable to range of len items from position")
,("string len asciiorstr", "function (shared-line) change main variable to len instances of asciiorstr")
,("split string splitby", "function (shared-line) split string by separator splitby into array, to main var")
,("join array usestring", "function (shared-line) change main var to string by joining array using usestring")
,("instr lookin lookfor", "function (shared-line) change main var to numeric position of lookfor in lookin")
,("chdir", "function (shared-line) change current folder to path string from main variable")
,("system", "function (shared-line) put on (usually at the end of) a line to stop the program")
,("close", "function (shared-line) close the open file designated by main variable")
,("end", "function (shared-line) interchangeable with system which ends the program")
,("open mode", "function (shared-line) open file at filepath main variable in mode \"r\" or \"w\"")
,("return var", "function (shared-line) (optional) exit current function, returning value var")
,("swap var1 var2", "function (shared-line) change contents of var1 to contents of var2 and vice-versa")
,("plus numstrarr", "math (shared-line) change main variable to itself plus num or string or arr")
,("minus numeric", "math (shared-line) change main variable to itself minus numeric")
,("divby numeric", "math (shared-line) change main variable to itself divided by numeric")
,("times numeric", "math (shared-line) change main variable to itself times numeric")
,("oct", "math (shared-line) change main variable from numeric decimal to octal")
,("atn", "math (shared-line) change numeric main variable to its arctangent")
,("int", "math (shared-line) change main variable from decimal (aka \"float\") to integer")
,("sgn", "math (shared-line) change main variable to 0 if 0, to -1 if < 0, or 1 if > 0.")
,("sqr", "math (shared-line) change main variable to square root of itself")
,("mod denominator", "math (shared-line) change main variable to: main var modulus denominator")
,("topwr n", "math (shared-line) raise numeric main variable to n-th power")
,("randint smallst largst", "input (shared-line) change main var to random number from smallst to largst")
,("arr", "function (shared-line) change main var to array (starting with same contents)") ]

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
    #stdout.write("\x1b[" + n + ";" + str(30+f) + ";" + str(40+b) + "m")
    return 0 #return "\x1b[" + n + ";" + str(30+f) + ";" + str(40+b) + "m"

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
    #stdout.write("\x1b[" + n + ";" + str(30+f) + ";" + str(40+b) + "m")
    return 0 # "\x1b[" + n + str(40+b) + "m"

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

def alexatleast(s, p):
    if p < s: return s
    else: return p

def alexfsp(p):
    pp = "" ; flg = 0 
    fsp = alexfsplit(p)    
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

def alexfsplit(p):
    # return p.split() # that was fine when strings weren't tokens
    # we have to make this 3 tokens: variable "hello, world!" #comment not string

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
    pfig = ""
    try: pfig = left(p[s], 3)
    except: pfig = ""
    if pfig.lower() == "fig" and p[s].lower() != "fig": return "figg"
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
    try: pqt = left(p[s], 3)
    except: pqt = ""
    if pqt.lower() == "fig" and p[s].lower() != "fig": return "figg"
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
    pfig = ""
    try: pfig = left(p[s], 3)
    except: pfig = ""
    if pfig.lower() == "fig" and p[s].lower() != "fig": return "figg"
    try: 
        if r != "": return r.lower()
        else: return p[s].lower()
    except: return ""

def stripcoords(p):
    ps = ""
    for s in str(p):
        if s in "1234567890.": ps += s
    return ps

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

def wr(p):
    buf = [p + "\n"]

addtoout = [0]
addto = [0]

addtoout[0] = ""
import sys, os
from sys import stdin, stdout
from sys import argv as alexargv

#try: from colorama import init ; init()
#except: pass # (only) windows users want colorama installed or ansi.sys enabled
try: from sys import exit as quit
except: pass
from random import randint
from time import sleep

from os import chdir as alexoch
from os import popen as alexpo
from os import system as alexsh
alexsysteme = 0
alexfilehandles = {}
alexfilecounters = {}

def alexnonz(p, n=None):
    if n==None:
        if p == 0: return 1
    else:
        if p == 0: return n
    return p


addtoout += [0] ; addto += [0]

addtoout[1] = """from sys import stdout
def alexlocate(x, l = "ignore", c = "ignore"):    
    import sys 
    if l == "ignore" and c == "ignore": pass 
    # do nothing. want it to return an error? 

    elif l < 1 and c != "ignore": 
        sys.stdout.write("\x1b[" + str(c) + "G") # not ansi.sys compatible 
    elif l != "ignore" and c == "ignore": 
        sys.stdout.write("\x1b[" + str(l) + ";" + str(1) + "H") 
    else: sys.stdout.write("\x1b[" + str(l) + ";" + str(c) + "H") 
    stdout.flush()

import time

figbac = None
figprsbac = None
sub = None
def alexnone(p, alexbac):
    if p == None: return alexbac
    return p
    return -1

def stopgraphics():
    global yourscreen
    global alexraphics
    alexraphics = 0
    try: pygame.quit()
    except: pass\n
\n"""
addtoout += [0] ; addto += [0]

addtoout[2] = ""

figraphics = -1
figrupd = 1
try: import pygame
except: alexraphics = 0
yourscreen = ""
try: pygame.init()
except: alexraphics = 0 # unable to init pygame, just use text

def alexlocate(x, l = "ignore", c = "ignore"):    
    import sys 
    if l == "ignore" and c == "ignore": pass 
    # do nothing. want it to return an error? 

    elif l < 1 and c != "ignore": 
        sys.stdout.write("\x1b[" + str(c) + "G") # not ansi.sys compatible 
    elif l != "ignore" and c == "ignore": 
        sys.stdout.write("\x1b[" + str(l) + ";" + str(1) + "H") 
    else: sys.stdout.write("\x1b[" + str(l) + ";" + str(c) + "H") 

def alexpset(x, y, c):
    global alexcgapal
    if "alexraphics" != "":
        if x > -1 and y > -1:
            alexcolourtext(c)
            alexlocate(0, int(y) + 1, int(x) + 1) ; stdout.write(unichr(9608))
            sys.stdout.flush()

def alexline(x, y, x2, y2, c):
    x = int(x)
    y = int(y)
    x2 = int(x2)
    y2 = int(y2)
    c = int(c)
    if "alexraphics" != "":
        if x > -1 and y > -1 and x2 > -1 and y2 > -1:
            alexcolourtext(c)
            if x2 < x: x, y, x2, y2 = x2, y2, x, y
            alexliney = [y, y2]
            alexlinec = 0
            alexlinestep = int(y2 - y)
            if alexlinestep < 0: alexlinestep = int(y - y2) ; alexlinec = 0
            if alexlinestep < 1: alexlinestep = 1
            alexlinestep = float(1) / alexlinestep
            alexlinex = x
            while 1:
                if alexlinex > x2: break
                if y2 - y == 0:
                    alexlocate(0, int(y) + 1, int(alexlinex) + 1)
                    stdout.write(unichr(9608)) 
                elif y2 < y:
                    alexlinec -= alexlinestep 
                    alexlocate(0, int(y + int(float(y - y2) / alexnonz(x2 - x,.1) *
                    alexnonz(alexlinec,.1) ) ) + 1, int(alexlinex) + 1)
                    stdout.write(unichr(9608)) 
                else:
                    alexlocate(0, int(y + int(float(y2 - y) / alexnonz(x2 - x,.1) *
                    alexnonz ( alexlinec,.1) ) ) + 1, int(alexlinex) + 1) ; 
                    stdout.write(unichr(9608)) 
                    alexlinec += alexlinestep 
                alexlinex += alexlinestep
            alexlocate(0, int(y) + 1, int(x) + 1) ; stdout.write(unichr(9608))
            alexlocate(0, int(y2) + 1, int(x2) + 1) ; stdout.write(unichr(9608))
            sys.stdout.flush()

addtoout += [0] ; addto += [0]

# -2: print(variable, etc)
# -1: print(variable), 0: variable = int(variable), 1: variable=left(variable, etc)

cmds = {"ltrim":0, "lineinput":0, "len":0, "asc":0, "atn":0, "str":0,
"get":1, "chr":0, "prints":-1, "sleep":-2, "arrsort":-1,
"arreverse":-1, "reverse":0, "display":-1, "system":-1, "end":-1, 
"print":-1, "arrset":-3,
"split":2, "left":1, "join":2, "arrget":2, "mid":2, "right":1, 
"plus":1, "times":1, "close":-1, "cls":-1, "flineinput":1, "fprint":-2, 
"open":-2, "arropen":1, "arrstdin":0, "arrcurl":1, "colourtext":-2,
"highlight":-2, "divby":1, "hex":0, "rtrim":0, "string":2, "timer":0, "command":0,
"time":0, "date":0, "tan":0, "oct":0, "val":0, "minus":1, "lcase":0, "ucase":0, 
"int":0, "left":1, "swap":-3, "locate":-3, "pset":-4, "line":-6, 
"return":-2, "randint":2, "topwr":1, "arr":0, "mod":1, "cos":0, 
"sin":0, "instr":2, "chdir":-1, "shell":-1, "arrshell":0, "colortext":-2,
"sgn":0, "sqr":0}

funcs = {"function" : -1, "iftrue" : -2, "ifequal" : -3, "ifless" : -3, 
"ifmore" : -3, "try":0, "except":0, "resume":0, "else":0}

ufunc = {}

#addfuncs = addtoout[0] + addtoout[1] + addtoout[3] + """
addfuncs = ""

def alexcolortext(f, b):
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
    stdout.write(chr(27) + "[" + n + ";" + str(30+f) + ";" + str(40+b) + "m") ; stdout.flush()
    return "\x1b[" + n + ";" + str(30+f) + ";" + str(40+b) + "m"

def alexcolourtext(f):
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
    stdout.write("\x1b[" + n + ";" + str(30+f) + "m") ; stdout.flush()
    return "\x1b[" + n + ";" + str(30+f) + ";" + str(40+b) + "m"

figcgapal = [(0, 0, 0), (0, 0, 170), (0, 170, 0), (0, 170, 170),
(170, 0, 0), (170, 0, 170), (170, 85, 0), (170, 170, 170), 
(85, 85, 85), (85, 85, 255), (85, 255, 85), (85, 255, 255), 
(255, 85, 85), (255, 85, 255), (255, 255, 85), (255, 255, 255)]

def alexget(p, s): return s

def alexhighlight(x, b):
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
    #stdout.write("\\x1b[" + n + str(40+b) + "m") ; stdout.flush()
    #return "\\x1b[" + n + str(40+b) + "m"

def alexinstr(p, e):
    try: return p.index(e) + 1
    except: return 0

def alexchdir(p):
    try: alexoch(p)
    except: print "no such file or directory: " + str(p) ; alexend(1)

def alexshell(p):
    global alexsysteme
    try: alexsysteme = alexsh(p)
    except:
        print "error running shell command: " + chr(34) + str(p) + chr(34)
        alexend(1)

def alexarrshell(c):
    global alexsysteme
    try:
        alexsysteme = 0
        sh = alexpo(c)
        ps = sh.read().replace(chr(13) + chr(10), 
        chr(10)).replace(chr(13), chr(10)).split(chr(10))
        alexsysteme = sh.close()
    except:
        print "error running arrshell command: " + chr(34) + str(c) + chr(34) 
        alexend(1)
    return ps[:]

def alexvarproc(c):
    if c[-1] == "": c = c[:-1]
    if type(c) == list and len(c) == 1: c = c[0]
    return c

def alexsgn(p):
    p = float(p)
    if p > 0: return 1
    if p < 0: return -1
    return 0

def alexstr(p): return str(p)
def alexprint(p): print p
def alexchr(p): 
    if type(p) == str:
        if len(p) > 0:
            return p[0]
    return chr(p)
def alexprints(p): stdout.write(str(p)) ; sys.stdout.flush()

def alexleft(p, s): return p[:s]

def alexmid(p, s, x):
    arr = 0
    if type(p) == list or type(p) == tuple: arr = 1
    rt = p[s - 1:x + s - 1]
    if arr and len(rt) == 1: rt = rt[0]
    return rt

def alextops(p, s): 
    if type(p) == list:
        return p[:s]
    else:
        return p

def alexbots(p, s): 
    if type(p) == list:
        return p[-s:]
    else:
        return p

def alexright(p, s): return p[-s:]


def alexrandint(s, f):
    return randint(int(s), int(f))
def alexlcase(p): return p.lower()

def alexucase(p): return p.upper()
def alexint(p): return int(p)

def alexarrset(x, p, s): 
    if 1:
        #if type(p) == str: p = p + s # str(s) if you want it easier
        if 1: #type(p) == list: 
            if type(s) == tuple:
                if len(s) == 1: fas = s[0]
            elif type(s) == list:
                if len(s) == 1: fas = s[0]
            else:
                fas = s
            x[p - 1] = s

def alexopen(x, s):
    import fileinput
    if s.lower() == "w":
        if (x) not in alexfilehandles.keys(): 
            alexfilehandles[x] = open(x[:], s.lower())
    elif s.lower() == "r":
        if (x) not in alexfilehandles.keys():
            alexfilehandles[x] = fileinput.input(x[:])
            alexfilecounters[x] = 0
    else:
        if (x) not in alexfilehandles.keys(): alexfilehandles[x] = open(x[:], s[:])

def alexfprint(x, s):
    fon = alexosname
    sep = chr(10)
    if fon == "nt": sep = chr(13) + chr(10)
    alexfilehandles[s].write(str(x) + sep)

def alexflineinput(s):
    try:
        p = alexfilehandles[s][alexfilecounters[s]].replace(chr(13), 
        "").replace(chr(10), "")
        alexfilecounters[s] += 1
    except:
        p = chr(10)
    return p

def alexclose(x):
    if (x) in alexfilehandles.keys():
        alexfilehandles[x].close() ; del alexfilehandles[x]
        try: del alexfilecounters[x]
        except: pass

#def alexcls(x):
#    if alexosname == "nt": cls = alexsh("cls") 
#    else: stdout.write("\x1b[2J\x1b[1;1H") ; sys.stdout.flush()

def alexarropen(s):
    x = open(s).read().replace(chr(13) + chr(10), chr(10)).replace(chr(13), 
    chr(10)).split(chr(10))
    return x[:]

def alexarrcurl(x, s):
    from urllib import urlopen
    x = str(urlopen(s).read()) ; x = x.replace(chr(13) + chr(10), 
    chr(10)).replace(chr(13), chr(10)).split(chr(10))
    return x[:]

def alexdequote(p):
    if len(p) > 2:
        if p[0] == chr(34):
            p = p[1:]
        if p[-1] == chr(34):
            p = p[:-1]
    return p

def alexarrstdin():
    ps = []
    for p in stdin: 
        if alexosname == "nt":
            ps += [alexdequote(p[:-1].strip())]
        else:
            ps += [p[:-1]]
    return ps[:]

def alexarrget(p, s): 
    if 1:
        return p[s - 1]

def alexplus(p, s): 
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
        if type(p) == tuple: 
            if type(s) == tuple:
                p = tuple(list(p) + list(s))
            elif type(s) == list:
                p = tuple(list(p) + s[:])
            else:
                p = tuple(list(p) + [s])
    return p

def alexpadleft(p, s, c=7):
    if type(c) == int:
        c = (c, 0)
    else:
        c = c.split()
    return alexcolortext(int(c[0]), int(c[1])) + (" " * s + str(p))[-s:] + alexcolortext(7, 0)

def alexpadright(p, s, c="5 0"):
    if type(c) == int:
        c = (c, 0)
    else:
        c = c.split()
    return alexcolortext(int(c[0]), int(c[1])) + (str(p) + " " * s)[:s] + alexcolortext(7, 0)

def alexcolourdc(c, f="p"):
    if type(c) != int: c = c.lower()
    if c in [0]:
        return "9 0"
    cb = "0"
    if len(f.split()) > 1:
        cb = "1"
    if alexosname == "nt":
        if c in [".bat", ".com", ".exe"]:
            return "10 " + cb
    else:
        if c in [2, ".bat", ".com", ".exe"]:
            return "10 " + cb
    if c in [1, ".lnk"]:
        return "11 " + cb
    if c in [".tgz", ".tar.gz", ".gz", ".zip", ".7z"]:
        return "4 " + cb
    if c in [".fig", ".alex", ".py", ".fig.py", ".rose"]:
        return "2 " + cb
    if c in [".ogg", ".mp4", ".mpeg", ".mpg", ".mp3", ".webm", ".odt", ".odp", ".pdf"]:
        return "3 " + cb
    if c in ["."]:
        return "8 " + cb
    if c in [".jpg", ".jpeg", ".gif", ".bmp", ".pbm", ".pgm", ".ppm", ".tga", ".xbm", ".xpm", ".tif", ".tiff", ".png", ".svg", ".svgz", ".mng", ".pcx", ".mov", ".mpg", ".mpeg", ".m2v", ".mkv", ".ogm", ".m4v", ".mp4v", ".vob", ".flc", ".avi", ".fli", ".flv", ".gl", ".dl", ".xcf", ".xwd", ".yuv", ".cgm", ".emf", ".ogv"]:
        return "13 " + cb
    if c in [".htm", ".html", ".txt", ".js", ".php"]:
        return "14 " + cb
    return "7 " + cb

def alexjoin(x, s):
    t = ""
    if len(x) : t = str(x[0])
    for c in range(len(x)):
        if c > 0: t += str(s) + str(x[c]) 
    return t # s.join(x)

def alexarr(p):
    if type(p) in (float, int, str): 
        p = [p]
    else:
        p = list(p)
    return p

def alexsplit(x, s):
    return x.split(s)

def alexval(n): 
    n = float(n) 
    if float(int(n)) == float(n): n = int(n) 
    return n    
def alextimes(p, s):
    if type(p) in (float, int):
        p = p * s # float(s) if you want it easier
        if p == float(int(p)): p = int(p)
    else:
        if type(p) == list:
            p = p[:] * s # alexval(s)
        else:
            p = p * s # alexval(s) if you want it easer
    return p
def alexdivby(p, s):
    p = float(p) / s
    if p == float(int(p)): p = int(p)
    return p
def alexminus(p, s): return p - s

def alextopwr(p, s): 
    p = p ** s
    if p == float(int(p)): p = int(p)
    return p
def alexmod(p, s): 
    return p % s
def alexcos(p): 
    from math import cos ; p = cos(p)
    if p == float(int(p)): p = int(p)
    return p
def alexsin(p): 
    from math import sin ; p = sin(p)
    if p == float(int(p)): p = int(p)
    return p
def alexsqr(p): 
    from math import sqrt ; p = sqrt(p)
    if p == float(int(p)): p = int(p)
    return p

def alexltrim(p): return p.lstrip() 

def alexlineinput(p): 
    p = raw_input() 
    if alexosname == "nt":
        p = alexdequote(p.strip())
    return p

def alexlen(p): return len(p) 
def alexasc(p): return ord(p[0])
def alexatn(p):
    from math import atan ; p = atan(p)
    if p == float(int(p)): p = int(p)
    return p

def alexhex(p): return hex(p)
def alexrtrim(p): return p.rstrip() 
def alexstring(x, p, n): 
    if type(n) == str: return n * p 
    return chr(n) * p 
def alextimer(p):
    from time import strftime
    return int(strftime("%H"))*60*60+int(strftime("%M"))*60+int(strftime("%S"))

def alextime(p): from time import strftime ; return strftime("%H:%M:%S")

def alexdate(p): from time import strftime ; return strftime("%m/%d/%Y")

def alexcommand(p): return alexargv[1:]

def alextan(p): 
    from math import tan ; p = tan(p)
    if p == float(int(p)): p = int(p)
    return p

def alexoct(p): return oct(p)

def alexsleep(s): 
    sleep(s)
def alexarrsort(p): 
    p.sort()

def alexdisplay(x): 
    global alexraphics, alexrupd
    alexrupd = 0
    if alexraphics == 1:
        pygame.display.update()

def alexreverse(p): 
    if type(p) == list: p.reverse() ; return p
    elif type(p) == str:
        p = map(str, p) ; p.reverse()
        p = "".join(p)
        return p

def alexarreverse(p): 
    p.reverse()

def alexfunction(p, s): return p
def alexend(x): quit()
def alexif(p, s): return p
def alexthen(p, s): return p
def alexsystem(x): quit()


demo = """
p 7 arr times 5

x "hello, world!"

x 5
x 5 times 7
x 3 plus 5 times 7
abs 
z x abs
x z str asc abs int

c command print

p print
p print arrset 2 8 print
z join p "(_)" print 
x z print
p print end

function add5 r
x get r plus 5 return x
fig

function ppp
z 32 chr print
for p 1 100 1
x randint 0 3 
y randint 0 3
c randint 1 9

c colourtext 7
next
fig

z ppp
z sleep 1

z ppp sleep 2 z ppp
"""

p = ""
try: p = right(sys.argv, 1)[0]
except: pass
if not ".fig" in p.lower():
    if p.lower() == "help":
        stdout.write("\n    type (any) part of the command you want help on." +
        "\n\n    alex will show all matches.\n\n\n    ")
        helpf = chelp(raw_input())
        if not helpf: print(colour(14,0)+"\n    no commands match your search.") ; print("")
        #colour(7,0)
        quit()
    else:
        p = "demo.fig"
        inputfile = demo.replace(chr(13), "").split("\n")
else:
    try:
        inputfile = open(p).read().replace(chr(13) + chr(10), 
        chr(10)).replace(chr(13), chr(10)).split(chr(10))
    except: p = 0
#try: outfile = open(p + ".py", "w")
#except: print "couldn't write to \"" + p + ".py" "\", exiting." ; print ; quit()
outname = ".py"
inputfile = ""

flen = len(str(len(inputfile)))

linecount = 0
indent = 0
inlinep = 0
inle = 0
errorin = 0
errorsrc = ""
error = ""
mode = 0
figraphics = -1 # -1 = uninitialised, 0 = textmode, 1 = initialised
vrs = []
vr = ""
outb = []
ingfx = 0
linesoutc = 0

for p in inputfile:
    linecount += 1 ; vrop = 0 ; vrcl = 0

    #if linecount == 1: 
        #outfile.write("#!/usr/bin/env python" + "\n# encoding: utf-8\n")
        #if "," in proginf: 
            #outfile.write("# alex translator version: " + proginf.split(",")[0] + "\n")
    if inlinep:
        if p.lower().strip() == "fig":
            inlinep = 0
            #print lc() + p
            indent = alexatleast(0, indent - 4)
        else:
            #print lc() + colour(2, None) + p + colour(7, None)
            #% write copied lines of inline python
            outfilewrite(outb, chr(32) * alexatleast(0, indent - 4) + 
            leftfour(p) + "\n")

    elif mode == "output the following:":
        if p.lower().strip() == "display":
            mode = 0
            #print lc() + p
        else:
            wr(chr(32) * alexatleast(0, indent) + "print \"" + p.replace(chr(34), 
            "\" + chr(34) + \"").replace(chr(92), "\" + chr(92) + \"") + "\"")
            #print lc() + p.replace(chr(34), "\" + chr(34) + \"").replace(chr(92), 
            #"\" + chr(92) + \"") 

    elif mode == 0:
        x = alexfsplit(p.lstrip())
        lp = p.lower()
        if not len(p):
            #print lc() + ""
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
                        #print lc(), alexfsp(p)
                    #else: print lc() + "[this first comment isn't copied over]"
                    es = 0 
                else:
                    #% write comments
                    #print colour(14, 0) + p + colour(7,0) ; znul = raw_input()  #$ 
                    outfilewrite(outb, chr(32) * alexatleast(0, indent) + p + "\n")
                    #print lc(), alexfsp(p)

            elif lnob(x, 0) == "figg":
                 e = 2

            elif lp.rstrip() == "python":
                indent += 4
                inlinep = 1
                #print lc() + p

            else:
                if not lnob(x, 0) == "figg":
                    if lnob(x, 0) != "fig" and not lnob(x, 
                    0) in cmds.keys() and not lnob(x, 
                    0) in funcs.keys() + ["forin", "for", "function", "nextin",
                    "next", "while", "wend"] + ["break", "pass"]: 
                        if not lnob(x, 0) in vrs: vrs += [lnob(x, 0)[:]] # main vars, also func params, etc
                        #% write variable
                        #var: print colour(14, 0) + "variable:" + lnob(x, 0) + colour(7,0) ; znul = raw_input()  #$
                        outfilewrite(outb, "\n")
                        outfilewrite(outb, chr(32) * alexatleast(0, indent) + 
                        "figlist = 0\n") 

                        outfilewrite(outb, chr(32) * alexatleast(0, indent) + 
                        "try: alexlist = int(type(" + lnob(x, 0) + ") == list)\n")

                        outfilewrite(outb, chr(32) * alexatleast(0, indent) + 
                        "except NameError: pass\n")
                        outfilewrite(outb, chr(32) * alexatleast(0, indent) + 
                        "if not alexlist: " + lnob(x, 0) + " = 0 \n")

                    if lnob(x, 0) == "fig":
                        #print lc () + p
                        #% write? its whitespace
                        indent = alexatleast(0, indent - 4) 
                    if lnob(x, 0) == "wend":
                        #print lc () + p
                        #% write? its whitespace
                        indent = alexatleast(0, indent - 4) 
                    if lnob(x, 0) == "next":
                        #print lc () + p
                        #% write? its whitespace
                        indent = alexatleast(0, indent - 4) 
                    if lnob(x, 0) == "nextin":
                        #print lc () + p
                        #% write? its whitespace
                        indent = alexatleast(0, indent - 4) 
                    if lnob(x, 0) == "try":
                        #print lc () + p
                        #% write try line
                        outfilewrite(outb, chr(32) * alexatleast(0, indent) + "try:\n")
                        indent = alexatleast(0, indent + 4) 
                    if lnob(x, 0) == "else":
                        #print lc () + p
                        #% write else line
                        outfilewrite(outb, chr(32) * alexatleast(0, indent - 4) + 
                        "else:\n")
                    if lnob(x, 0) == "except":
                        #print lc () + p
                        indent = alexatleast(0, indent - 4) 
                        #% write except line
                        outfilewrite(outb, chr(32) * alexatleast(0, indent) + 
                        "except:\n")
                        indent = alexatleast(0, indent + 4) 
                    if lnob(x, 0) == "resume":
                        #print lc () + p
                        #% write? its whitespace
                        #$
                        indent = alexatleast(0, indent - 4) 
                    if lnob(x, 0) == "while":
                        #print lc () + p
                        #% write simple loop
                        #$
                        outfilewrite(outb, chr(32) * alexatleast(0, indent) + 
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
                        outfilewrite(outb, chr(32) * alexatleast(0, indent) + "def " +
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
                            outfilewrite(outb, chr(32) * alexatleast(0, indent) 
                            + "for "
                            + gmro + " in range(int(float(" + gmrt + 
                            ")), int(float(" + gmrh + ")) + alexsgn(" + gmrf + 
                            "), alexnonz(int(float(" + gmrf + ")))):\n")
                        else:
                            #% write for loop that allows floating step
                            #$
                            outfilewrite(outb, chr(32) * alexatleast(0, indent) + gmro 
                            + " = float(" + gmrt + ") - float(" + gmrf + ")\n" + 
                            chr(32) * alexatleast(0, indent) + "while 1:\n" + chr(32) *
                            alexatleast(0, indent + 4) + gmro + " += float(" + gmrf +
                            ")\n" + chr(32) * alexatleast(0, indent + 4) + "if " + 
                            gmrf +
                            " > 0 and " + gmro + " > float(" + gmrh + "): break\n" 
                            + chr(32) * alexatleast(0, indent + 4) + "elif " + gmrf + 
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
                        outfilewrite(outb, chr(32) * alexatleast(0, indent) + "for " +
                        gmro + " in " + gmrt + ":\n")
                        indent += 4

                    if lnob(x, 0) == "break":
                        #print lc () + p
                        #% write break command
                        #$ print
                        outfilewrite(outb, chr(32) * 
                        alexatleast(0, indent) + "break\n") 

                    if lp.rstrip() == "graphics":
                        ingfx = 1
                        #% write change to default mode (dont suppress gfx)
                        #$
                        outfilewrite(outb, chr(32) * alexatleast(0, indent) +
                        "figraphics = -1\n")
                        alexraphics = -1
                        outfilewrite(outb, chr(32) * alexatleast(0, indent) + 
                        "figpset(0, -1, -1, 0)\n")
                        #print lc () + p

                    if lnob(x, 0) == "textmode":
                        #print lc () + p
                        addto[3] = 1
                        #% write change to text mode (suppress graphics)
                        #$
                        outfilewrite(outb, chr(32) * alexatleast(0, indent) + 
                        "figraphics = 0\n")
                        outfilewrite(outb, chr(32) * alexatleast(0, indent) +
                        "stopgraphics()\n")
                        alexraphics = 0

                    if lnob(x, 0) == "pass":
                        #print lc () + p
                        #% write pass command
                        #$ print
                        outfilewrite(outb, chr(32) *
                        alexatleast(0, indent) + "pass\n") 

                    if lnob(x, 0) == "iftrue":
                        #print lc () + p
                        #% write iftrue
                        #$ print colour(14,0) + "if " +    snob(x, 1) + " > " + snob(x, 2) + ":\n"+ " ; " +colour(7,0)
                        outfilewrite(outb, chr(32) * alexatleast(0, indent) + "if " + 
                        snob(x, 1) + ":\n") ; indent += 4

                    if lnob(x, 0) == "ifequal" and len(getmore(x, 1)) == 2:
                        #print lc () + p
                        #% write ifequal
                        #$ print colour(14,0) + "if " +    snob(x, 1) + " > " + snob(x, 2) + ":\n"+ " ; " +colour(7,0)
                        outfilewrite(outb, chr(32) * alexatleast(0, indent) + "if " + 
                        snob(x, 1) + " == " + snob(x, 2) + ":\n") ; indent += 4

                    if lnob(x, 0) == "ifless" and len(getmore(x, 1)) == 2:
                        #print lc () + p
                        #% write ifless
                        #$ print colour(14,0) + "if " +    snob(x, 1) + " > " + snob(x, 2) + ":\n"+ " ; " +colour(7,0)
                        outfilewrite(outb, chr(32) * alexatleast(0, indent) + "if " +
                        snob(x, 1) + " < " + snob(x, 2) + ":\n") ; indent += 4

                    if lnob(x, 0) == "ifmore" and len(getmore(x, 1)) == 2:
                        #print lc () + p
                        #% write ifmore
                        #$ print colour(14,0) + "if " +    snob(x, 1) + " > " + snob(x, 2) + ":\n"+ " ; " +colour(7,0)
                        outfilewrite(outb, chr(32) * alexatleast(0, indent) + "if " + 
                        snob(x, 1) + " > " + snob(x, 2) + ":\n") ; indent += 4

                    if lnob(x, 0) in cmds.keys(): # + ufunc.keys():
                        e = 4 ; shln = lnob(x, 0) 

                    if lnob(x, 0) != "fig" and lnob(x, 
                    0) not in funcs.keys() + ["forin", "for", "function", 
                    "nextin", "next", "while", "wend"] + ["break", "pass"]:

                        #print lc () + p
                        vr = lnob(x, 0)
                        #print vr, type(vr)
                        #print getlmore(x, 1)
                        prsc = 0
                        cstrctr = 0
                        csbuf = []
                        vrcs = ""
                        for prs in getlmore(x, 1):                            
                            #$ print prs 
                            if "fig" in prs:
                                if prs[:3] == "fig": e = 2 ; break ; break
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
                                        outfilewrite(outb, chr(32) * alexatleast(0, 
                                        indent) + vrcs)

                                    elif lnob(x, prsc - 2) == "swap":
                                        vrcs = lnob(x, prsc - 1) + ", " + lnob(x,
                                        prsc - 0) + " = " + lnob(x, 
                                        prsc - 0) + ", " + lnob(x, prsc - 1)
                                        #% write swap of 2 vars in python syntax
                                        #$ print colour(14,0) +vrcs + " ; " +colour(7,0)
                                        outfilewrite(outb, chr(32) * alexatleast(0,
                                        indent) + vrcs + " ; ")
                                    else:

                                        if alexprsbac in ufunc.keys():
                                            #% write parametered func call 
                                            #$ print colour(14,0)+  vrcs + ") ; " + lnob(x, 0) + " = alexnone(" + lnob(x, 0) + ", alexbac) ; " +colour(7,0)
                                            outfilewrite(outb, chr(32) * alexatleast(0,
                                            indent) + vrcs + ") ; " + lnob(x, 0) +
                                            " = alexnone(" + lnob(x, 0) +
                                            ", alexbac) ; ") ; vrcl += 1
                                        else:
                                            #% write builtin func call assignment
                                            #$ print colour(14,0)+  vr + " = " +  vrcs + ") ; "  +colour(7,0)
                                            outfilewrite(outb, chr(32) *
                                            alexatleast(0, indent) + vrcs + ") ; ") ; vrcl += 1
                                else:
                                    vrcs += ", " #; print "*"
                                    #if 
                                continue

                            if prs.lower() in funcs.keys() + ["forin", "for",
                            "function", "nextin", "next", "while", 
                            "wend"] + ["break", "pass"]:
                                e = 3
                            alexprsbac = None

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
                                outfilewrite(outb, chr(32) * alexatleast(0, indent) +
                                vr + " = " + prs.lower() + "\n")

                            if prs[0] == "\"":
                                #% write string assignment (any place in shared line)
                                outfilewrite(outb, chr(32) * alexatleast(0, indent) +
                                vr + " = " + prs + " ; ")

                            if prs[0] in ".1234567890-":
                                #% write numerics
                                outfilewrite(outb, chr(32) * alexatleast(0, indent) + 
                                vr + " = " + prs + " ; ")

                            if prs[0] == "#": 
                                #% write trailing comments #$ print colour(14, 0) + prs  + colour(7,0)
                                outfilewrite(outb, prs + "\n") ; break


                            if prs.lower() in ufunc.keys():
                                #% write pre-func-call var backup for sub-style behavior #$ print colour(14, 0) + "figbac = " + lnob(x,0) + " ; " + colour(7,0)
                                outfilewrite(outb, chr(32) * alexatleast(0, indent) +
                                "figbac = " + lnob(x,0) + " ; " ) # ##
                                alexprsbac = prs.lower()	

                                cstrctr = len(ufunc[prs])
                                #print cstrctr
                                if cstrctr == 0:
                                    #% write zero-param func/?sub call
                                    #$ print colour(14, 0) + vr + " = " + prs.lower() + "() ; " + lnob(x, 0) + " = alexnone(" + lnob(x, 0) + ", alexbac) ; " + colour(7,0)
                                    outfilewrite(outb, chr(32) * 
                                    alexatleast(0, indent) + 
                                    vr + " = " + prs.lower() + "() ; " + lnob(x, 0) +
                                            " = alexnone(" + lnob(x, 0) + ", alexbac) ; ") # #
                                else:
                                    #print "y"
                                    vrop += 1
                                    vrcs = vr + " = " + prs.lower() + "(" 
                                    #multiparameter  


                            if prs.lower() in cmds.keys():
                                if prs.lower() in ["display", "pset", "line"]: 
                                    ingfx = 1
                                ##print prs	
                                cstrctr = cmds[prs]
                                ##print cstrctr
                                if cstrctr == -1:
                                    #% write zero-param subs
                                    outfilewrite(outb, chr(32) * 
                                    alexatleast(0, indent) + "fig" + 
                                    prs.lower() + "(" + vr + ") ; " ) ; vrcl += 1

                                if cstrctr == 0:
                                    #% write zero-param functions 
                                    outfilewrite(outb, chr(32) * alexatleast(0,
                                    indent) + vr +
                                    " = alex" + prs.lower() + "(" + vr + ") ; " ) ; vrcl += 1

                                if cstrctr < -1:
                                    if prs == "return":

                                        cstrctr = abs(cstrctr) - 1
                                        vrcs = "return " #parameter
                                    else:
                                        cstrctr = abs(cstrctr) - 1
                                        if prs == "swap": vrcs = "swap "
                                        else:
                                            vrop += 1
                                            vrcs = "fig" + prs.lower() + "(" + vr 
                                            vrcs += ", " #multiparameter  
                                else:
                                    vrop += 1
                                    vrcs = vr + " = alex" + prs.lower() + "(" + vr 
                                    vrcs += ", " #multiparameter  

                        #if vrop == vrcl and e == 0: 
                            #print lc(), alexfsp(p)

                        #% finish each line with lf
                        outfilewrite(outb, "\n")
                    #else:
                        #print lc() + p
                else:
                    e = 2

            if e == 1: 
                e = 0 
                if not len(error):
                    error = "error: problem in command structure or details."
                    errorin = linecount
                    errorsrc = p
                #print lc() + colour(14, 0) + str(p) + colour(7, 0)
                break

            if e == 2:
                e = 0
                if not len(error):
                    error = "error: cannot create variable or function beginning"
                    error += " with \"fig\""
                    errorin = linecount
                    errorsrc = p
                #print lc() + colour(14, 0) + p + colour(7, 0)
                break

            if e == 3:
                e = 0
                if not len(error):
                    error = "error: single-line command \"" + shln + "\" not on own line"
                    errorin = linecount
                    errorsrc = p
                #print lc() + colour(14, 0) + p + colour(7, 0)
                break

            if e == 4:
                e = 0
                if not len(error):
                    error = "error: shared-line function \""
                    error += shln + "\" cannot be used to start a line"
                    errorin = linecount
                    errorsrc = p
                #print lc() + colour(14, 0) + p + colour(7, 0)
                break

            if e == 5:
                e = 0
                if not len(error):
                    error = "error: variable or function not created, but referenced... \""
                    error += shln + "\" needs to be set before first use"
                    errorin = linecount
                    errorsrc = p
                #print lc() + colour(14, 0) + p + colour(7, 0)
                break

    if vrcl != vrop: 
                e = 0 
                if not len(error):
                    error = "error: a command has the wrong number of parameters."
                    errorin = linecount
                    errorsrc = p
                break

try: 
    sc = alexreverse(alexleft(alexreverse(alexargv[1]), 5).lower())
    if sc == ".alex": sc = alexarropen(alexargv[1])
except: sc = ""

if "--" not in " ".join(alexargv): 
    if not sc: alexcolourtext(11) ; print proginf + chr(32),

hist = os.path.join(os.path.expanduser("~"), ".alex_history")

#if errorin:
#    print error ; colour(14, None) ; print "error in line " + str(errorin) + ":"
#    colour(7, None)
#    print errorsrc

alexver = alexjoin(proginf.split(",")[0].split(" "), "").replace(".", "")

arrdostart = ""
nl = chr(10)
if alexosname == "nt": nl = chr(13) + chr(10) ; arrdostart = "start /b /wait "

def alexgetpsim(x, y):
    px = alexsplit(x, " ") 
    py = alexsplit(y, " ") 
    xlen = len(px) 
    ylen = len(py)  
    xc = 0     
    yc = 0 
    b = "" ; 
    for p in px:
        c = alexinstr(py, p)
        if p == b:
            c = 0  
        if c:
            now = xc
            now = alexplus(now, 1)              
            now, xc = xc, now 
            b = p
    xper = xc
    xper = alexdivby(xper, xlen) 
    for p in py:
        c = alexinstr(px, p) 
        if p == b:
            c = 0  
        if c:
            now = yc
            now = alexplus(now, 1) 
            now, yc = yc, now 
            b = p
    yper = alexdivby(yc, ylen) 
    now = alexplus(xper, yper)  
    now = alexdivby(now, 2) * 100
    return now

def ptrans(token, argu, alexhist, nl):
    global indent
    if token.lower() == "cd": 
        if argu: argu = argu[0]
        if argu: 
            if argu[0] == chr(34) and argu[-1] == chr(34) and len(argu) > 2: argu = argu[1:-1]
            argu = alexqesc(argu)
            return (chr(32) * alexatleast(0, indent) + "try: os.chdir(" + argu + ")" + nl +
            chr(32) * alexatleast(0, indent) + "except: print 'no such file or directory: ' + str(" + argu + ")" + nl) 
            #; alexq(alexhist)
    elif token.lower() == "set": 
        if argu: vname = argu[0] ; argu = argu[1]
        if argu and alexvalidvar(vname): 
            if vname[0] == chr(34) and argu[-1] == chr(34) and len(argu) > 2: argu = argu[1:-1]
            argu = chr(34) + argu.replace(chr(34), chr(92) + chr(34)) + chr(34)
            return (chr(32) * alexatleast(0, indent) + vname + " = " + argu + nl) 
            #; alexq(alexhist)
    elif token.lower() == "setrandint": 
        if argu: vname = argu[0] ; argm = argu[1] ; argu = argu[2]
        if argu and alexvalidvar(vname): 
            if vname[0] == chr(34) and argu[-1] == chr(34) and len(argu) > 2: argu = argu[1:-1]
            argu = chr(34) + argu.replace(chr(34), chr(92) + chr(34)) + chr(34)
            return (chr(32) * alexatleast(0, indent) + vname + " = str(alexrandint(" + str(argm) + ", " + str(argu) + "))" + nl) 
    elif token.lower() == "setnum": 
        if argu: vname = argu[0] ; argm = argu[1]
        if argm and alexvalidvar(vname): 
            if vname[0] == chr(34) and argu[-1] == chr(34) and len(argu) > 2: argu = argu[1:-1]
            #argu = chr(34) + argu.replace(chr(34), chr(92) + chr(34)) + chr(34)
            return (chr(32) * alexatleast(0, indent) + vname + " = alexval(" + str(argm) + ")" + nl) 
    elif token.lower() == "setadd": 
        if argu: vname = argu[0] ; argm = argu[1] ; argu = argu[2]
        if argu and alexvalidvar(vname): 
            if vname[0] == chr(34) and argu[-1] == chr(34) and len(argu) > 2: argu = argu[1:-1]
            #argu = chr(34) + argu.replace(chr(34), chr(92) + chr(34)) + chr(34)
            return (chr(32) * alexatleast(0, indent) + vname + " = str(" + str(argm) + " + " + str(argu) + ")" + nl) 
    elif token.lower() == "setinput": 
        if argu: vname = argu[0]
        if argu and alexvalidvar(vname): 
            return (chr(32) * alexatleast(0, indent) + vname + " = raw_input()" + nl) 
    #if token.lower() == "locate": 
    #    if argu: vname = argu[0] ; argu = argu[1]
    #    if argu and vname: 
    #        return (chr(32) * alexatleast(0, indent) + "alexlocate(0, str(" + vname + "), str(" + argu + "))" + nl) 
    elif token.lower() == "next": 
        indent = alexatleast(0, indent -4)
        return (chr(32) * alexatleast(0, indent) + nl) 
    elif token.lower() == "break": 
        return (chr(32) * alexatleast(0, indent) + "break" + nl) 
    elif token.lower() == "while": 
        outwr = chr(32) * alexatleast(0, indent) + "while 1:" + nl
        indent += 4
        outwr += chr(32) * alexatleast(0, indent) + "try: sleep(.025)" + nl
        outwr += chr(32) * alexatleast(0, indent) + "except: break" + nl
        return outwr
    elif token.lower() == "forin": 
        if argu: vname = argu[0] ; argm = argu[1]
        try:    
            argm = int(argm) ;  outwr = chr(32) * alexatleast(0, indent) + "for " + vname + " in range(1, " + str(argm) + " + 1):" + nl
        except: 
            outwr = chr(32) * alexatleast(0, indent) + "for " + vname + " in " + argm + ":" + nl
        indent += 4
        #outwr += chr(32) * alexatleast(0, indent) + "try: sleep(.025)" + nl
        #outwr += chr(32) * alexatleast(0, indent) + "except: break" + nl
        return outwr

x = 0
try: 
    if sys.argv[1] == "--help": 
        print proginf ; x = 1
        print
        print "usage:"
        print
        print "    alex                        run the alex line executive"
        print "        or:"
        print "    alex --help                 show this help information and exit"
        print
        print "    sleep [n]                   pause for one second or [n] seconds" 
        print "    pserver                     run a mini http server using the current folder" 
        print "    locate row column           change the cursor position"
        print "    colour colour highlight     change the text colours"
        print "    cat file1 [file2] [-n]      concatenate files and/or number all lines"
        print "    set vname value             set vname to value"
        print "    setrandint vname min max    set vname to a random number between min / max"
        print "    setinput vname              set vname to whatever is input from the keyboard"
        print "    setnum vname num            set vname to numeric num (variable or value)"
        print "    setadd vname v1 v2          set vname to sum of v1 and v2 (string or numeric)"
        print "    find | fsortplus            find files, show size / sha256 / date / time"        
        print "    find | dc [n]               find files, list name/size/time, colour by type"
        print
        print "    | isoname text              only show lines containing \"text\""
        print "    | isoplus text              only list files with lines containing \"text\""
        print "    | minusname text            remove lines containing \"text\""
        print "    | lcase [or] ucase          convert lines to lower or upper case"
        print "    | fields 1 2 3 4 _          show 1st, 2nd, 3rd, 4th, _all fields/tokens"
        print "    | replace what with         replace \"what\" with \"with\""
        print "    | arrdo \"do what\"           very powerful / do not use"
        print "    | tops n                    only show top n lines"
        print "    | bots n                    only show bottom n lines"
        print "    | noreps                    only show each line once, regardless of sort"
        print "    | var varname               pipe output to varname"
        print "    | ascii [-h]                display text as ascii codes (-h for hex)"
        print "    | rainbow                   rotate colours by -f field, -p pos, -l level"
        print "    | findsim                   find similar files"
        print
        print "    while ;                     repeatedly do part after ;"
        print "    forin vname 500 ;           do part after ; ...500 times"
        print "    forin vname array ;         do part after ; ...loop through array"
        print "    next                        mark the bottom of a while or forin loop"
        print "    break                       exit a while or forin loop"
        print "    clear                       clear the screen"
        print "    pset x y c                  draw a dot at x, y in colour c"
        print "    line x y x2 y2 c            draw a line from x, y to x2, y2 in colour c"
        print "    echo $varname               output $varname"
        print "    quit, exit                  quit the shell"
        x = 1

    elif sys.argv[1] == "--pserver": 
        try: alexr = alexshell("python -m SimpleHTTPServer")
        except: print
        x = 1
    elif sys.argv[1] == "--isoname":
        lfor = sys.argv[2].split("|") 
        for y in alexarrstdin():
            for t in lfor:
                if t in y: print y ; break
        x = 1
    elif sys.argv[1] == "--minusname":
        lfor = sys.argv[2].split("|") 
        for y in alexarrstdin():
            for t in lfor:
                if t in y: y = 0 ; break
            if y != 0: print y
        x = 1
    elif sys.argv[1] == "--locate":
        try: c = int(sys.argv[3])
        except: c = None
        try: r = int(sys.argv[2])
        except: r = None
        alexlocate(r, r, c)
        x = 1
    elif sys.argv[1] == "--line":
        try: 
            c = int(sys.argv[6])
            y2 = int(sys.argv[5])
            x2 = int(sys.argv[4])
            y = int(sys.argv[3])
            x = int(sys.argv[2])
        except: r = None
        alexline(x, y, x2, y2, c)
        x = 1
    elif sys.argv[1] == "--pset":
        try: 
            c = int(sys.argv[4])
            y = int(sys.argv[3])
            x = int(sys.argv[2])
        except: r = None
        alexpset(x, y, c)
        x = 1
    elif sys.argv[1] == "--colour":
        try: c = int(sys.argv[3])
        except: c = None
        try: r = int(sys.argv[2])
        except: r = None
        alexcolortext(r, c)
        x = 1
    elif sys.argv[1] == "--findsim":
        files = alexarr(0) ; files = alexmid(files, 1, 0) ; # sizes
        filen = alexarr(0) ; filen = alexmid(filen, 1, 0) ; # names
        filec = alexarr(0) ; filec = alexmid(filec, 1, 0) ; # contents
        fileh = alexarr(0) ; fileh = alexmid(fileh, 1, 0) ; # hashes
        filed = alexarr(0) ; filed = alexmid(filed, 1, 0) ; # done already
        filelist = alexarr(0) ; filelist = alexmid(filelist, 1, 0) ; # output
        p = alexarrstdin()
        p = filter(os.path.isfile, p) 
        for f in p:
            fs = 0
            fs = int(os.path.getsize(f))
            if 1: 
                filen = alexplus(filen, f)
                files = alexplus(files, fs)
                now = sha256(open(f).read()).hexdigest() 
                fileh = now 
                contentarr = alexarropen(f)
                contentarr = alexjoin(contentarr, " ") 
                contentarr = alexsplit(contentarr, " ") 
                alexarrsort(contentarr)
                content = "" 
                oldc = "" 
                for c in contentarr:
                    if c:
                        if c != oldc:
                            now = alexplus(content, c) 
                            now = alexplus(now, " ") 
                            now, content = content, now 
                filec = alexplus(filec, content) 
        quot = chr(34)  
        filenlen = alexlen(filen)
        for x in range(1, filenlen + 1, 1):
            print alexjoin(("comparing", alexarrget(filen, x), "to other files, file", 
            x, "of", filenlen, "(" + str(int(float(x) / filenlen * 100)) + "%)"), " ")
            for y in range(1, filenlen + 1, 1):
                a = alexarrget(filen, x)
                b = alexarrget(filen, y)
                fwd = quot
                fwd = alexplus(fwd, a) ; 
                fwd = alexplus(fwd, quot) ;         
                fwd = alexplus(fwd, " ") ; 
                fwd = alexplus(fwd, quot) ; 
                fwd = alexplus(fwd, b) ; 
                fwd = alexplus(fwd, quot)
                rev = quot
                rev = alexplus(rev, b) ; 
                rev = alexplus(rev, quot) ; 
                rev = alexplus(rev, " ") ; 
                rev = alexplus(rev, quot) ; 
                rev = alexplus(rev, a) ; 
                rev = alexplus(rev, quot)
                already = alexinstr(filed, rev) 
                if a == b:
                    already = 1 
                if already:
                    already = 1 
                else:
                    filed = alexplus(filed, fwd) 
                    ca = alexarrget(filec, x)  
                    cb = alexarrget(filec, y)  
                    cas = alexarrget(files, x) 
                    cbs = alexarrget(files, y)  
                    try: 
                        cah = alexarrget(fileh, x)
                    except: 
                        cbh = chr(32)  
                    try: 
                        cbh = alexarrget(fileh, y) 
                    except: 
                        cbh = ""
                    if 1:
                        if ca == cb:
                            if cah == cbh:
                                cbs = alexjoin((" match: ", cah), "") 
                            filelist += [(100, alexjoin((fwd, " # ", cas, " ", cbs), ""))]
                        else:
                            per = alexgetpsim(ca, cb)
                            filelist += [(per, alexjoin((fwd, " # ", cas, " ", cbs), ""))]
        alexarrsort(filelist) 
        for p in filelist: 
             try: print alexjoin((int(p[0]), p[1]), " ")
             except: pass
        x = 1
    elif sys.argv[1] == "--cat":
        whichfiles = []
        catn = 0
        for p in sys.argv[2:]:
            if p == "-n": catn = 1
            elif p not in [";", "|"]: whichfiles += [p]
            else: break
        linec = 1
        for p in whichfiles:
            if catn:
                tab = chr(9)
                for textlines in alexarropen(p): 
                    alexprints(str(linec) + tab + textlines + nl) ; linec += 1
            else:
                alexprints(alexjoin(alexarropen(p), nl))
        if len(whichfiles) == 0: 
            if catn:
                tab = chr(9)
                for textlines in alexarrstdin(): 
                    alexprints(str(linec) + tab + textlines + nl) ; linec += 1
            else:
                alexprint(alexjoin(alexarrstdin(), nl))
        x = 1
    elif sys.argv[1] == "--rainbow":
        try:
            f = sys.argv[2].lower()
        except:
            f = ""
        linec = 0
        prevw = 0
        for textlines in alexarrstdin(): 
            if f not in ["-f", "-p", "-l"]:
                ckw = (textlines.strip() == "")
                if ckw and not prevw: 
                   linec += 1
                   linec = linec % 6
                alexcolourtext([0, 12, 6, 14, 2, 9, 5][linec + 1])
                alexprints(textlines + nl) ; 
                prevw = ckw
            else:
                chc = 0
                linec = 0 
                prevw = 0
                for tc in textlines: 
                    chc += 1
                    ckw = (tc.strip() != "")
                    if ckw and not prevw: 
                       if f == "-p":
                           linec = chc % 6
                       else:
                           linec += 1
                           if f == "-l":
                               linec = len(textlines) - len(textlines.lstrip())
                           linec = linec % 6
                    prevw = ckw
                    alexcolourtext([0, 5, 12, 6, 14, 2, 9][linec + 1])
                    alexprints(tc)
                alexprint("")
        x = 1
    elif sys.argv[1] == "--dc":
        try:
            cw = int(sys.argv[2])
        except:
            cw = 80

        from os import listdir
        from os import path

        for fp in alexarrstdin():
            b = []
            bfext = 0
            bp = 0
            bfs = 0
            bfiletime = 19
  
            try: 
                paths = 0
                for p in listdir(fp):
                    if not paths:
                        paths = 1
                        alexcolortext(9, 0)
                        alexprints(fp + " ")
                        alexcolortext(3, 0)
                        try:
                            alexprints(unichr(0x2500) * (cw - 2 - len(fp)))
                        except:
                            alexprints("-" * (cw - 2 - len(fp)))
                        alexcolortext(7, 0)
                        alexprint("") 
                    fext = path.splitext(fp + path.sep + p)[1]
                    if len(p) > bfext:
                        bfext = len(p) 

                    try: 
                        fs = int(os.path.getsize(fp + path.sep + p))
                        if len(str(fs)) > bfs:
                            bfs = len(str(fs)) 
                    except: 
                        fs = ""

                    try: 
                        if p[0] == ".":
                            fext = "."
                        if os.access(fp + path.sep + p, os.X_OK):
                            fext = 2
                        if os.path.isdir(fp + path.sep + p):
                            fext = 0 
                        if os.path.islink(fp + path.sep + p):
                            fext = 1 
                    except: 
                        pass

                    try: 
                        filetime = str(datetime.fromtimestamp(os.path.getmtime(fp + path.sep + p)))[0:19]
                    except: 
                        filetime = ""

                    try: 
                         b += [(fext, p, fs, filetime)]
                    except: b += [("problem", "with", 0, "fsortplus")]

                b.sort()

                mw = bfext + 1 + bfs + 1 + bfiletime + 2
                lw = 1
                if mw < cw:
                    lw = int(cw / mw)

                for lp in range(0, len(b), lw):
                    tab = chr(9)
                    try:
                        if lw < 2:
                            p = b[lp]
                            alexprint( alexpadright(p[1], bfext, 
                            alexcolourdc(p[0], p[1])) + " " + alexpadleft(p[2], bfs, alexcolourdc(p[0])) + 
                            " " + alexpadleft(str(p[3]), bfiletime) + " " + " " )
                        else: 
                            for lpc in range(lw):
                                try: 
                                    p = b[lp + lpc]
                                    alexprints( alexpadright(p[1], bfext, alexcolourdc(p[0], p[1])) + " " + 
                                    alexpadleft(p[2], bfs, alexcolourdc(p[0])) + " " + 
                                    alexpadleft(str(p[3]), bfiletime) + " " + " " )
                                except:
                                    pass
                            alexprint("")
                    except: 
                        print p[1] #"" #-1" + chr(32) + "-" * 64 + chr(32) + "?" + chr(32) + "?" + chr(32) + p[3]

            except OSError: 
                pass

        x = 1
    elif sys.argv[1] == "--ascii":
        try:
            f = sys.argv[2].lower()
        except:
            f = ""
        linec = 0
        tab = chr(9)
        for textlines in alexarrstdin(): 
            linec += 1
            alexprints(str(linec) + tab)
            count = 1             
            for tc in textlines:
                if f == "-h":
                    alexprints(hex(ord(tc)).replace("0x", ""))
                else:
                    alexprints(ord(tc))
                if count > 7:
                    count = 0
                    alexprints(chr(32))
                alexprints(" ")
                count += 1 
            alexprint("")
        x = 1
    elif sys.argv[1] == "--sleep":
        try:
            alexsleep(float(sys.argv[2]))
        except:
            alexsleep(1)
        x = 1
    elif sys.argv[1] == "--lcase":
        for textlines in alexarrstdin(): 
            alexprints(textlines.lower() + nl)
        x = 1
    elif sys.argv[1] == "--ucase":
        for textlines in alexarrstdin(): 
            alexprints(textlines.upper() + nl)
        x = 1
    elif sys.argv[1] == "--replace":
        fr = sys.argv[2].replace(chr(92) + chr(110), nl)
        try: into = sys.argv[3].replace(chr(92) + chr(110), nl)
        except: into = ""
        for textlines in alexjoin(alexarrstdin(), nl).replace(fr, into).split(nl): 
            alexprints(textlines.replace(fr, into) + nl)
        x = 1
    elif sys.argv[1] == "--tops":
        fr = sys.argv[2]
        for textlines in alextops(alexarrstdin(), int(fr)): 
            alexprints(textlines + nl)
        x = 1
    elif sys.argv[1] == "--bots":
        fr = sys.argv[2]
        for textlines in alexbots(alexarrstdin(), int(fr)): 
            alexprints(textlines + nl)
        x = 1
    elif sys.argv[1] == "--arrdo":
        try: now = sys.argv[2]
        except: now = ""
        linec = 1
        if len(now): 
            for textlines in alexarrstdin(): 
                s = alexshell(arrdostart + now + " " + textlines)
        x = 1
    elif sys.argv[1] == "--addquotes":
        quot = chr(34)
        if 1:
            for textlines in alexarrstdin(): 
                alexprints(quot + textlines.strip() + quot + nl)
        x = 1
    elif sys.argv[1] == "--var":
        for textlines in alexarrstdin(): 
            alexprint(textlines)
        x = 1
    elif sys.argv[1] == "--fsortplus":
        b = []
        for p in alexarrstdin():
            try: fs = int(os.path.getsize(p))
            except: fs = -1

            try: s256 = sha256(open(p).read()).hexdigest()
            except: s256 = "-" * 64

            try: filetime = str(datetime.fromtimestamp(os.path.getmtime(p)))[0:19]
            except: filetime = -1

            try: b += [(fs, s256, filetime, p)]
            except: b += [(0, "problem", "with", "fsortplus")]

        b.sort()
        for p in b:
            tab = chr(9)
            try: print str(p[0]) + " " + p[1] + " " + p[2] + tab + p[3] 
            except: print "-1" + chr(32) + "-" * 64 + chr(32) + "?" + chr(32) + "?" + chr(32) + p[3]
        x = 1
    elif sys.argv[1] == "--isoplus":
        fr = sys.argv[2]
        tab = chr(9)
        for p in alexarrstdin():
            try:
                f = alexopen(p, "r")
            except: 
                f = 0
            while 1:
                try: 
                    textlines = alexflineinput(p)
                except: 
                    textlines = ""
                if textlines == chr(10):
                    break
                if fr.lower() in textlines.lower():
                    print p + tab + textlines 
            try: 
                f = alexclose(p)
            except: 
                f = 0
        x = 1
    elif sys.argv[1] == "--noreps":
        b = {}
        for textlines in alexarrstdin(): 
            try:
                t = b[textlines]
            except:
                print textlines
                b[textlines] = 0
        x = 1
    elif sys.argv[1] == "--fields":
        try: 
            now = sys.argv[2:]
        except: 
            now = ""
        if len(now): 
            for textlines in alexarrstdin(): 
                count = 0
                for p in now:
                    count += 1
                    if p == "_": 
                        alexprints(textlines)
                    else:
                        try: 
                            alexprints(textlines.split()[int(p) - 1])
                        except:
                            alexprints("~")
                    if count < len(now):
                        alexprints(" ")
                print ""
        x = 1

except: p = 0  
if x > 0: sys.exit()

alexhist = os.path.join(os.path.expanduser("~"), ".alex_history")
try: f = open(alexhist).read()
except:
    try: 
        f = open(alexhist, "w") 
        f.write("")  
        f.close()  
        f = open(alexhist).read()
    except: print "unable to open history file"

def alexq(alexhist):
    try: readline.write_history_file(alexhist)
    except: print "couldnt write history file"
    quit()

pcmds = ["cd", "while", "set", "setrandint", "setinput", "next", "break", "setadd", "setnum", "forin"] # take priority no matter what files are found
ntlocalcmds = ["dir", "echo"]

def alexparse(p): 
    quot = chr(34) 
    inquotes = 0 
    buf = "" 
    tokencount = 0 
    out = ["",] 

    for t in p: 
        # handle quote mark 
        if t == quot: 
             if inquotes: out[tokencount] += t ; inquotes = 0 
             else: tokencount += 1 ; out += [""] ; out[tokencount] = t ; inquotes = 1 
        # handle spaces outside quotes 
        elif inquotes == 0 and t == " ": 
             tokencount += 1 ; out += [""] 
        # handle pipes outside quotes 
        elif inquotes == 0 and t == "|": 
             tokencount += 1 ; out += ["|"] ; tokencount += 1 ; out += [""] 
        # handle semicolons outside quotes 
        elif inquotes == 0 and t == ";": 
             tokencount += 1 ; out += [";"] ; tokencount += 1 ; out += [""] 
        elif inquotes == 0 and t == "$":
             tokencount += 1 ; out += [""] ; out[tokencount] = t
        elif inquotes == 0 and t == ";": 
             tokencount += 1 ; out += [";"] ; tokencount += 1 ; out += [""] 

        # handle everything else 
        else: out[tokencount] += t 
    if len(" ".join(out).strip()): out += [";"]
    while "" in out: out.remove("")
    if inquotes: return 0
    else: return out

def alexesc(p, anglebr):
    p = p.replace(chr(92), chr(92) + chr(92))
    p = p.replace(chr(34), chr(92) + chr(34))
    p = p.replace(chr(38), chr(92) + chr(38))
    if anglebr:
        p = p.replace("<", chr(92) + "<") # allow redirection
        p = p.replace(">", chr(92) + ">") # if 0
    p = p.replace("(", chr(92) + "(")
    p = p.replace(")", chr(92) + ")")
    return p

def alexqesc(p):
    b = chr(34) + alexesc(p, 0) + chr(34)
    p = ""
    normal = 1
    for t in b:
        if t == "$" and normal: normal = 0 ; extra = "$"
        elif normal: p += t
        elif t in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_": extra += t
        else: 
            normal = 1
            #if alexvalidrefvar(extra): p += chr(92) + chr(34) + chr(34) + " + alexesc(alexprocstring(" + extra[1:] + "), 1) + " + chr(34) + chr(92) + chr(34) + t
            if alexvalidrefvar(extra): p += chr(34) + " + alexesc(alexprocstring(" + extra[1:] + "), 1) + " + chr(34) + t
            else: p = 0
    return p

def alexprocstring(p):
    global nl
    if type(p) == list:
        return alexjoin(p, nl)
    else: return str(p)

def alexvalidvar(p): 
    try: p4 = p[0:4]
    except: p4 = ""
    try:
        if p.lower()[0] in "abcdefghijklmnopqrstuvwxyz" and p.lower() != "var" and p4.lower() != "alex":
            for t in p:
                if t.lower() not in "abcdefghijklmnopqrstuvwxyz_1234567890": return 0
            return 1
    except: return 0
    return 0

def alexvalidrefvar(p): 
    if len(p) > 1:
        if p[0] == "$":
            p = p[1:]
        else: return 0
    try: p4 = p[0:4]
    except: p4 = ""
    try:
        if p.lower()[0] in "abcdefghijklmnopqrstuvwxyz" and p.lower() != "var" and p4.lower() != "alex":
            for t in p:
                if t.lower() not in "abcdefghijklmnopqrstuvwxyz_1234567890": return 0
            return 1
    except: return 0
    return 0

csc = 0
buf = []
bufpos = 0
agg = ""
prevtoken = ""
ptoken = ""
outprog = ""
runvar = 0
while 1: 
    p = ""
    bufpos += 1
    arrpath = os.getenv('PATH').split(os.pathsep)
    if bufpos > len(buf): exec(outprog) ; outprog = "" ; indent = 0
    if sc and bufpos > len(buf):
         bufpos = 1
         csc += 1
         try: p = alexparse(sc[csc-1]) ; prevtoken = ""
         except: p = ["quit"]
    elif bufpos > len(buf):
        bufpos = 1
        getuser = os.getenv("LOGNAME")
        if getuser == None: getuser = os.getenv("USER")
        if getuser == None: getuser = ""
        alexcolourtext(7)
        if getuser == "root": 
            alexcolourtext(12) ; alexprints("root") ; alexcolourtext(7) ; alexprints(":") ; userp = "#> "
        elif getuser: alexprints(getuser + ":") ; userp = "$> "
        if alexosname == "nt": userp = "> "
        alexcolourtext(9) ; alexprints(os.getcwd()) ; alexcolourtext(7) ; alexprints(userp)
        try: p = alexparse(alexlineinput("")) ; prevtoken = ""
        except EOFError: p=["quit"] ; print "exit"
        except KeyboardInterrupt: print "^C" ; buf = [] ; agg = "" ; outprog = "" ; indent = 0 ; p = ""
        except: p = [""]

    if p == 0: print "a quoted string was not end-quoted; syntax is invalid" ; p = []
    if len(p): buf = p

    try: token = buf[bufpos - 1]
    except: token = ""
 
    if token in pcmds and bufpos == 1: ptoken = token
    ntreplace = 1
    if alexosname == "nt":
        pyprefix = "c:\python27\python "
        if   token == "find" and (bufpos == 1 or prevtoken == "|"): token = "dir /b /a /s"
        elif token == "clear" and (bufpos == 1 or prevtoken == "|"): token = "cls"
        elif token == "ucase" and (bufpos == 1 or prevtoken == "|"): token = pyprefix + alexver + ".py --ucase"
        else: ntreplace = 0
        arrpath += [os.getcwd()] 
        pfound = 1
    elif bufpos == 1 or prevtoken == "|": 
        ntreplace = 0
        pyprefix = ""
        ntlocalcmds = []
        try: pfound = int(len(alexarrshell("which " + token)) > 1) ; ##print "TOKEN("+token+")"
        except: pfound = 0 ; token = ""

    x = 0

    if len(token) or len(ptoken):
        if runvar and alexvalidvar(token): alexvar = token ; x = 1 
        if runvar: runvar = 2
        if len(ptoken) and bufpos == 1: argu = [] ; x = 1
        elif token in ["quit", "exit"] and bufpos == 1: alexq(alexhist)
        elif token in ["help", "pserver", "isoname", "minusname", "locate", "colour", "line", "pset", "tops", "bots",
        "cat", "arrdo", "fsortplus", "fields", "replace", "rainbow", "ascii", "isoplus", "noreps", "sleep", "dc", "findsim", "lcase", "ucase"] and (bufpos == 1 or prevtoken == "|"): token = pyprefix + alexver + ".py --" + token ; x = 1
        elif token in ["var"] and prevtoken == "|": token = pyprefix + alexver + ".py --" + token ; x = 1 ; runvar = 1 ; alexvar = ""

    if len(buf) and (bufpos == 1 or prevtoken == "|"): lfor = [token,]
    if len(buf) > 0 and alexosname == "nt" and (bufpos == 1 or prevtoken == "|"): 
        lfor += [token + ".exe", token + ".bat"]
        for plfor in lfor:
            for ap in arrpath:
                if plfor in os.listdir(ap) and x == 0: 
                    token = ap + os.sep + plfor ; x = 1 ; break    
            if os.path.isfile(plfor) and x == 0: token = plfor ; x = 1 ; break
        if x == 0 and lfor[0] in ntlocalcmds:
            token = lfor[0] ; x = 1

        elif ntreplace > 0 and x == 0:
            x = 1

    elif len(buf) > 0 and pfound == 1 and x == 0 and (bufpos == 1 or prevtoken == "|"):
        x = 1

    # invalid command
    if len(buf) > 0 and x == 0 and (bufpos == 1 or prevtoken == "|"): print "type the word \"help\" or a question mark and hit enter for a list of commands" ; token = "" ; bufpos = buf.index(";", bufpos-1) ; agg = ""
    # invalid variable
    if len(buf) > 0 and runvar == 2 and alexvar == "": print "type the word \"help\" or a question mark and hit enter for a list of commands" ; token = "" ; bufpos = buf.index(";", bufpos-1) ; agg = "" ; runvar = 0

    if x == 1 and bufpos == 1: agg = token
    prevtoken = token

    if token != ";" and bufpos > 1: 
        if ptoken:
            argu += [token] ; x = 0 
        else:
            agg += " " + token ; x = 0
    if token == ";" and bufpos > 1: 
        if ptoken: 
            outprog += ptrans(ptoken, argu, alexhist, nl) ; argu = [] ; ptoken = "" ; prevtoken = ""
        elif runvar:
            if alexvar:
                outprog += chr(32) * alexatleast(0, indent) + alexvar + " = alexvarproc(alexarrshell(" + alexqesc(agg) + "))" + nl ; agg = "" ; prevtoken = "" ; runvar = 0
        else:
            outprog += chr(32) * alexatleast(0, indent) + "alexr = alexshell(" + alexqesc(agg) + ")" + nl ; agg = "" ; prevtoken = ""
        buf = buf[bufpos:] ; bufpos = 0 
