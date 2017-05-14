#!/usr/bin/env python
# coding: utf-8 

proginf = "drawrof 0.1, may 2017 mn"

# license:

############################################################​####################

# Copyright © 2015, 2016, 2017 mn
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

############################################################​####################

import sys
import os
from sys import stdin, stdout

buf = []

cmdhelp = [("timer", "input (shared-line) change main variable to number of seconds past midnight")
,("time", "input (shared-line) change main variable to string of current time: hh:mm:ss")
,("arropen filepath", "input (shared-line) change main variable to array of file lines in filepath")
,("date", "input (shared-line) change main variable to string of the date: mm/dd/yyyy")
,("sleep seconds", "input (shared-line) wait for number of seconds before continuing with program")
,("command", "input (shared-line) change main variable to array of command line parameters")
,("display", "output (shared-line) 1st time: stop automatic graphx update. 2nd, etc: update.")
,("cls", "output (shared-line) clear the screen. currently only affects text screen")
,("pset x y c", "output (shared-line) draw dot at location (x, y) in colourcode c (0 - 15)")
,("line x1 y1 x2 y2 c", "output (shared-line) draw line from (x1, y1) to (x2, y2) in colourcode c (0-15)")
,("break", "loop --\\own\\line put in the middle of a loop to exit (stop looping)")
,("for var strt stop step", "loop --\\own\\line start a for loop, changing var from strt to stop, by step")
,("forin var array", "loop --\\own\\line loop through each item in array; for each, set var to item")
,("iftrue ckvar", "conditional --\\own\\line run lines between iftrue and ne if ckvar is \"non-zero\"")
,("ifequal var1 var2", "conditional --\\own\\line run lines between ifequal and ne if var1 equals var2")
,("ifmore var1 var2", "conditional --\\own\\line run lines between ifmore and ne if var1 is > var2")
,("ifless var1 var2", "conditional --\\own\\line run lines between ifless and ne if var1 is < var2")
,("try", "conditional --\\own\\line put code that might not work between try and except")
,("except", "conditional --\\own\\line if code between try/except fails, run the code after except")
,("resume", "conditional --\\own\\line mark the end of try / except / resume command block")
,("else", "conditional --\\own\\line after if- line, before ne. run lines if condition isnt true")
,("func name p1 p2 ..?", "function --\\own\\line define function named name with optional params p1,p2, etc")
,("get parametername", "function (shared-line) copy parametername value to main var")
,("ne", "function --\\own\\line finalise a block (started by if/while/function/for/forin")
,("pass", "function --\\own\\line blocks (for/, etc) require something inside lines; pass works / does nothing")
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
,("arreverse", "function (shared-line) change main variable from array to reverse order of array")
,("reverse", "function (shared-line) like arreverse (which might be faster for array) for strings")
,("arrsort", "function (shared-line) change main variable from array to sorted array")
,("():|=,. ( ) : ; | = , .", "optional (shared-line) use in a shared line (and some others) for aesthetics/notation")
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
,("end", "function (shared-line) interchangeable with system which ends the program")
,("return var", "function (shared-line) (optional) exit current function, returning value var")
,("swap var1 var2", "function (shared-line) change contents of var1 to contents of var2 and vice-versa")
,("plus numstrarr", "math (shared-line) change main variable to itself plus num or string or arr")
,("minus numeric", "math (shared-line) change main variable to itself minus numeric")
,("divby numeric", "math (shared-line) change main variable to itself divided by numeric")
,("times numeric", "math (shared-line) change main variable to itself times numeric")
,("abs", "math (shared-line) change main variable to its absolute value")
,("oct", "math (shared-line) change main variable from numeric decimal to octal")
,("hex", "math (shared-line) change main variable from  numeric decimal to hexadecimal")
,("cos", "math (shared-line) change numeric main variable to the cosine of itself")
,("sin", "math (shared-line) change numeric main variable to the sine of itself")
,("tan", "math (shared-line) change numeric main variable to its tangent")
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

def colour(f, b):
    return ""

def bcolour(b):
    return ""

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

def nefsp(p):
    pp = "" ; flg = 0 
    fsp = nefsplit(p)    
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

def nefsplit(p):
    px = [] 
    pxc = -1 # could use len(px) -1 instead?

    inquotes = 0
    remarked = 0
    inspc = "" ; vnspc = ""

    for l in p:
        if inquotes == 0 and remarked == 0 and l == "#":
            remarked = 1
            pxc += 1 ; px += [""]
        if remarked == 1:
            px[pxc] += l

        if remarked == 0:
            if l == "'":
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
    pne = ""
    try: pne = left(p[s], 2)
    except: pne = ""
    if pne.lower() == "ne" and p[s].lower() != "ne": return "ne."
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
    try: pqt = left(p[s], 2)
    except: pqt = ""
    if pqt.lower() == "ne" and p[s].lower() != "ne": return "ne."
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
    pne = ""
    try: pne = left(p[s], 2)
    except: pne = ""
    if pne.lower() == "ne" and p[s].lower() != "ne": return "ne."
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

def lc():
    global linecount
    global flen
    es = " "
    return "# " + right(chr(32) * flen + str(linecount), flen) + es

def wr(p):
    global buf
    buf += [p + "\n"]

#colour(11, None) ; print proginf; colour(7, None) ; print

addtoout = [0]
addto = [0]

addtoout[0] = """import sys, os
from sys import stdin, stdout
from sys import argv as neargv
from random import randint
from time import sleep\n\n
from os import chdir as neoch
from os import system as nesh
from os import name as neosname
nesysteme = 0
"""

addtoout += [0] ; addto += [0]

addtoout[1] = """from sys import stdout

import time

def nenonz(p, n=None):
    if n==None:
        if p == 0: return 1
    else:
        if p == 0: return n
    return p

def nenot(p):
    if p: return 0
    return -1

nebac = None
neprsbac = None
sub = None
def nenone(p, nebac):
    if p == None: return nebac
    return p
    return -1

def stopgraphics():
    global yourscreen
    global neraphics
    neraphics = 0
    try: pygame.quit()
    except: pass\n
\n"""
addtoout += [0] ; addto += [0]

addtoout[2] = ""
addtoout += [0] ; addto += [0]

addtoout[3] = """neraphics = -1
nerupd = 1
try: import pygame
except: neraphics = 0
yourscreen = ""
try: pygame.init()
except: quit() #neraphics = 0 ; ph = 'unable to init pygame, just use text'

def nepset(z, x, y, c):
    global neraphics, nerupd
    global yourscreen
    global necgapal ; #print "pset", x, y, c
    if neraphics == -1:
        #pygame.init()
        try:
            yourscreen = pygame.display.set_mode((800, 600))
            pygame.display.set_caption("drawrof 0.1")
            neraphics = 1
        except:
            stopgraphics() ; neraphics = 0
    if neraphics == 1:
        if x > -1 and y > -1:
            yourscreen.set_at((x, y), necgapal[int(c)])
            #pygame.draw.circle(yourscreen,(255, 255, 255),(int(x), int(y)), 1, 0)
            if nerupd: pygame.display.update()
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:  
                    neraphics = 0
                    stopgraphics()

def necircle(z, x, y, r, c):
    global neraphics, nerupd
    global yourscreen
    global necgapal  #; print "circle", x, y, r, c
    if neraphics == -1:
        try:
            yourscreen = pygame.display.set_mode((800, 600))
            pygame.display.set_caption("drawrof 0.1")
            neraphics = 1
        except:
            stopgraphics() ; neraphics = 0
    if neraphics == 1:
        if x > -1 and y > -1:
            pygame.draw.circle(yourscreen, necgapal[int(c) % 16], (int(x), int(y)), r, 0)
            if nerupd: pygame.display.update()
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:  
                    neraphics = 0
                    stopgraphics()

def rect(x, y, x2, y2, c):
    if x > x2: x2, x = x, x2
    if y > y2: y2, y = y, y2
    x2 = x2 - x # width, not coord
    y2 = y2 - y # height, not coord
    global neraphics, nerupd
    global yourscreen
    global necgapal ; #print "r", x, y, x2, y2, c
    if neraphics == -1:
        try:
            yourscreen = pygame.display.set_mode((800, 600))
            pygame.display.set_caption("drawrof 0.1")
            neraphics = 1
        except:
            stopgraphics() ; neraphics = 0
    if neraphics == 1:
        if x > -1 and y > -1:
            pygame.draw.rect(yourscreen, necgapal[int(c)], [int(x),int(y), int(x2), int(y2)], 0)
            if nerupd: pygame.display.update()
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:  
                    neraphics = 0
                    stopgraphics()

def neline(z, x, y, x2, y2, c):
    global neraphics, nerupd
    global yourscreen
    global necgapal ; #print "line", x, y, x2, y2, c
    if neraphics == 1:
        if x > -1 and y > -1 and x2 > -1 and y2 > -1:
            yourscreen.set_at((int(x), int(y)), necgapal[int(c)])
            pygame.draw.line(yourscreen, necgapal[int(c)], (x, y), (x2, y2), 1)
            if nerupd: pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    neraphics = 0
                    stopgraphics()

def anykeypyg():
    global yourscreen
    global neraphics, nerupd
    p = 0
    while not p: 
        if neraphics == 0: break
        time.sleep(0.001)
        for event in pygame.event.get():   
            if event.type == pygame.KEYDOWN: 
                if nerupd: pygame.display.update() 
                p = 1\n\n"""

addtoout += [0] ; addto += [0]

# -2: print(variable, etc)
# -1: print(variable), 0: variable = int(variable), 1: variable=left(variable, etc)

cmds = {"ltrim":0, "len":0, "asc":0, "atn":0, "str":0,
"get":1, "chr":0, "sleep":-2, "arrsort":-1,
"arreverse":-1, "reverse":0, "display":-1, "system":-1, "end":-1, 
 "arrset":-3,
"split":2, "left":1, "join":2, "arrget":2, "mid":2, "right":1, 
"plus":1, "times":1, "close":-1, "cls":-1, "arropen":1, "divby":1, "hex":0, "rtrim":0,  "timer":0, "command":0, "ta":-2, "tp":-2, "u":-2, "d":-2, "l":-2, "r":-2, "time":0, "date":0, "tan":0, "oct":0, "abs":0, "val":0, "minus":1, "lcase":0, "ucase":0, "pc":-2,
"int":0, "left":1, "swap":-3, "locate":-3, "pset":-4, "line":-6, 
"return":-2, "randint":2, "topwr":1, "arr":0, "mod":1, "cos":0, "cu":-2, "cd":-2, "cl":-2, "cr":-2,
"not":0, "sin":0, "instr":2, "sgn":0, "sqr":0}

funcs = {"func" : -1, "iftrue" : -2, "ifequal" : -3, "ifless" : -3, 
"ifmore" : -3, "try":0, "except":0, "resume":0, "else":0}

ufunc = {}

#addfuncs = addtoout[0] + addtoout[1] + addtoout[3] + """
addfuncs = """
z = 0
nexv = 400
neyv = 300
cv = 15
ta = 0

necgapal = [(0, 0, 0), (0, 0, 170), (0, 170, 0), (0, 170, 170),
(170, 0, 0), (170, 0, 170), (170, 85, 0), (170, 170, 170), 
(85, 85, 85), (85, 85, 255), (85, 255, 85), (85, 255, 255), 
(255, 85, 85), (255, 85, 255), (255, 255, 85), (255, 255, 255)]



def neget(p, s): return s

def neta(p, x): global ta ; ta = x

def netp(p, x): global ta ; ta += x

def nepc(p, x): global cv ; cv = x

from math import cos, sin, pi

def neradians(dg): rd = dg * pi / 180 ; print "#",pi,rd ; return rd

def neu(p, x): global nexv, neyv, cv, ta ; ox, oy = nexv, neyv ; nexv = int(ox + x * cos(neradians((ta + 270.25) % 360))) ; neyv = int(oy + x * sin(neradians((ta + 270.25) % 360))) ; neline(z, ox, oy, nexv, neyv, cv)

def ned(p, x): global nexv, neyv, cv, ta ; ox, oy = nexv, neyv ; nexv = int(ox + x * cos(neradians((ta + 90) % 360))) ; neyv = int(oy + x * sin(neradians((ta + 90) % 360))) ; neline(z, ox, oy, nexv, neyv, cv)

def nel(p, x): global nexv, neyv, cv, ta ; ox, oy = nexv, neyv ; nexv = int(ox + x * cos(neradians((ta + 180) % 360))) ; neyv = int(oy + x * sin(neradians((ta + 180) % 360))) ; neline(z, ox, oy, nexv, neyv, cv)

def ner(p, x): global nexv, neyv, cv, ta ; ox, oy = nexv, neyv ; nexv = int(ox + x * cos(neradians((ta) % 360))) ; neyv = int(oy + x * sin(neradians((ta) % 360))) ; neline(z, ox, oy, nexv, neyv, cv)



def necu(p, x):
    global nexv, neyv, cv, ta ; ox, oy = nexv, neyv ; nexv = int(ox + (x / 2) * cos(neradians((ta + 270.25) % 360))) ; neyv = int(oy + (x / 2) * sin(neradians((ta + 270.25) % 360))) ; necircle(z, nexv, neyv, int(x / 2),cv)
    nexv = int(ox + x * cos(neradians((ta + 270.25) % 360))) ; neyv = int(oy + x * sin(neradians((ta + 270.25) % 360)))

def necd(p, x):
    global nexv, neyv, cv, ta ; ox, oy = nexv, neyv ; nexv = int(ox + (x / 2) * cos(neradians((ta + 90) % 360))) ; neyv = int(oy + (x / 2) * sin(neradians((ta + 90) % 360))) ; necircle(z, nexv, neyv, int(x / 2),cv)
    nexv = int(ox + x * cos(neradians((ta + 90) % 360))) ; neyv = int(oy + x * sin(neradians((ta + 90) % 360)))

def necl(p, x):
    global nexv, neyv, cv, ta ; ox, oy = nexv, neyv ; nexv = int(ox + (x / 2) * cos(neradians((ta + 180) % 360))) ; neyv = int(oy + (x / 2) * sin(neradians((ta + 180) % 360))) ; necircle(z, nexv, neyv, int(x / 2),cv)
    nexv = int(ox + x * cos(neradians((ta + 180) % 360))) ; neyv = int(oy + x * sin(neradians((ta + 180) % 360)))

def necr(p, x):
    global nexv, neyv, cv, ta ; ox, oy = nexv, neyv ; nexv = int(ox + (x / 2) * cos(neradians((ta) % 360))) ; neyv = int(oy + (x / 2) * sin(neradians((ta) % 360))) ; necircle(z, nexv, neyv, int(x / 2),cv)
    nexv = int(ox + x * cos(neradians((ta) % 360))) ; neyv = int(oy + x * sin(neradians((ta) % 360)))






def neinstr(x, p, e):
    try: return p.index(e) + 1
    except: return 0

def neabs(p):
    return abs(p)

def nesgn(p):
    p = float(p)
    if p > 0: return 1
    if p < 0: return -1
    return 0

def nestr(p): return str(p)
def neprint(p): print p
def nechr(p): 
    if type(p) == str:
        if len(p) > 0:
            return p[0]
    return chr(p)
def neprints(p): stdout.write(str(p)) ; sys.stdout.flush()
def neleft(p, s): return p[:s]
def nemid(p, s, x):
    arr = 0
    if type(p) == list or type(p) == tuple: arr = 1
    rt = p[s - 1:x + s - 1]
    if arr and len(rt) == 1: rt = rt[0]
    return rt
def neright(p, s): return p[-s:]
def nerandint(x, s, f):
    return randint(s, f)
def nelcase(p): return p.lower()

def neucase(p): return p.upper()
def neint(p): return int(p)

def nearrset(x, p, s): 
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

def necls(x):
    if neosname == "nt": cls = nesh("cls") 
    else: stdout.write("\x1b[2J\x1b[1;1H") ; sys.stdout.flush()

def nearropen(x, s):
    x = open(s).read().replace(chr(13) + chr(10), chr(10)).replace(chr(13), 
    chr(10)).split(chr(10))
    return x[:]

def nearrget(x, p, s): 
    if 1:
        return p[s - 1]

def neplus(p, s): 
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

def nejoin(p, x, s):
    t = ""
    if len(x) : t = str(x[0])
    for c in range(len(x)):
        if c > 0: t += str(s) + str(x[c]) 
    return t # s.join(x)

def nearr(p):
    if type(p) in (float, int, str): 
        p = [p]
    else:
        p = list(p)
    return p

def nesplit(p, x, s):
    return x.split(s)

def neval(n): 
    n = float(n) 
    if float(int(n)) == float(n): n = int(n) 
    return n    
def netimes(p, s):
    if type(p) in (float, int):
        p = p * s # float(s) if you want it easier
        if p == float(int(p)): p = int(p)
    else:
        if type(p) == list:
            p = p[:] * s # neval(s)
        else:
            p = p * s # neval(s) if you want it easer
    return p
def nedivby(p, s):
    p = float(p) / s
    if p == float(int(p)): p = int(p)
    return p
def neminus(p, s): return p - s

def netopwr(p, s): 
    p = p ** s
    if p == float(int(p)): p = int(p)
    return p
def nemod(p, s): 
    return p % s
def necos(p): 
    from math import cos ; p = cos(p)
    if p == float(int(p)): p = int(p)
    return p
def nesin(p): 
    from math import sin ; p = sin(p)
    if p == float(int(p)): p = int(p)
    return p
def nesqr(p): 
    from math import sqrt ; p = sqrt(p)
    if p == float(int(p)): p = int(p)
    return p

def neltrim(p): return p.lstrip() 
def nelineinput(p): return raw_input() 
def nelen(p): 
    if type(p) == list: return len(p)
    elif type(p) == str: return len(p)
    else: return len(str(p))

def neasc(p): return ord(p[0])
def neatn(p):
    from math import atan ; p = atan(p)
    if p == float(int(p)): p = int(p)
    return p

def nehex(p): return hex(p)
def nertrim(p): return p.rstrip() 

def netimer(p):
    from time import strftime
    return int(strftime("%H"))*60*60+int(strftime("%M"))*60+int(strftime("%S"))

def netime(p): from time import strftime ; return strftime("%H:%M:%S")

def nedate(p): from time import strftime ; return strftime("%m/%d/%Y")

def necommand(p): return neargv[1:]

def netan(p): 
    from math import tan ; p = tan(p)
    if p == float(int(p)): p = int(p)
    return p

def neoct(p): return oct(p)

def nesleep(p, s): 
    sleep(s)

def nearrsort(p): 
    p.sort()

def nedisplay(x): 
    global neraphics, nerupd
    nerupd = 0
    if neraphics == 1:
        pygame.display.update()

def nereverse(p): 
    if type(p) == list: p.reverse() ; return p
    elif type(p) == str:
        p = map(str, p) ; p.reverse()
        p = "".join(p)
        return p

def nearreverse(p): 
    p.reverse()

def neend(x): quit()
def nesystem(x): quit()
\n"""

demo = ";angle 7 ;func ppp angle ;z 32 chr ta angle  pc 1 cu 50 cu 50 cu 50 cu 50 cu 50 pc 2 cr 200 pc 5 cd 50 cd 50 cd 50 cd 50 cd 50  pc 8 cl 200 ;ne ; for angle 125 5 -25 ; p ppp angle ; ne" 

p = ""
try: p = right(sys.argv, 1)[0]
except: pass
if not ".ne" in p.lower():
    if p.lower() == "help":
        stdout.write("\n    type (any) part of the command you want help on." +
        "\n\n    ne will show all matches.\n\n\n    ")
        helpf = chelp(raw_input())
        if not helpf: print(colour(14,0)+"\n    no commands match your search.") ; print("")
        colour(7,0)
        quit()
    else:
        print "#using built-in demo source, translating to demo.ne.py..." ; print
        p = "demo.ne" ; demo = "now pset 0 0 0;" + demo
        inputfile = demo.replace(chr(13), "").replace(";", "\n").split("\n")
else:
    try:
        inputfile = open(p).read().replace(chr(13) + chr(10), 
        chr(10)).replace(chr(13), chr(10)).split(chr(10))
    except: print "couldn't open \"" + p + "\", exiting." ; print ; quit()
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
neraphics = -1 # -1 = uninitialised, 0 = textmode, 1 = initialised
vrs = []
vr = ""
outb = []
ofwr = ""
ingfx = 0
linesoutc = 0

for p in inputfile:
    linecount += 1 ; vrop = 0 ; vrcl = 0

    if mode == 0:
        x = nefsplit(p.lstrip())
        lp = p.lower()
        if not len(p):
            print lc() + ""
            #% write copied blank lines from inline python
            outfilewrite(outb, "\n")

        if len(p.lstrip()):

            e = 0

            if p.lstrip()[0] == ";":
                if linecount == 1:
                    es = 0
                    try: 
                         if p.lstrip()[1] == "!": es = 1
                    except: es = 0
                    if not es:
                        wr(p)
                        print lc(), nefsp(p)
                    else: print lc() + "[this first comment isn't copied over]"
                    es = 0 
                else:
                    #% write comments
                    #print colour(14, 0) + p + colour(7,0) ; znul = raw_input()  #$ 
                    outfilewrite(outb, chr(32) * atleast(0, indent) + p + "\n")
                    print lc(), nefsp(p)

            elif lnob(x, 0) == "ne.":
                 e = 2

            else:
                if not lnob(x, 0) == "ne.":
                    if lnob(x, 0) != "ne" and not lnob(x, 
                    0) in cmds.keys() and not lnob(x, 
                    0) in funcs.keys() + ["forin", "for", "func", "nextin",
                    "next"] + ["break", "pass"]: 
                        if not lnob(x, 0) in vrs: vrs += [lnob(x, 0)[:]] # main vars, also func params, etc
                        #% write variable
                        outfilewrite(outb, "\n")
                        outfilewrite(outb, chr(32) * atleast(0, indent) + 
                        "nelist = 0\n") 

                        outfilewrite(outb, chr(32) * atleast(0, indent) + 
                        "try: nelist = int(type(" + lnob(x, 0) + ") == list)\n")

                        outfilewrite(outb, chr(32) * atleast(0, indent) + 
                        "except NameError: pass\n")
                        outfilewrite(outb, chr(32) * atleast(0, indent) + 
                        "if not nelist: " + lnob(x, 0) + " = 0 \n")

                    if lnob(x, 0) == "ne":
                        #print lc () + p
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
                    if lnob(x, 0) == "func" and len(getmore(x, 1)) > 0:
                        #print lc () + p
                        mkf = []
                        funcname = getlmore(x, 1)[0]
                        prm = 1
                        while 1:
                            try:
                                aprm = getlmore(x, 1)[prm]
                                if len(aprm): 
                                    if aprm[0] != ";":
                                        mkf += [aprm]
                                        if aprm not in vrs: vrs += [aprm[:]]
                                prm += 1
                            except: break
                        ufunc[funcname] = mkf[:] #; print ufunc # #
                        #print ufunc
                        #print len(ufunc[funcname])
                        #% write func def
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
                            ")), int(float(" + gmrh + ")) + nesgn(" + gmrf + 
                            "), nenonz(int(float(" + gmrf + ")))):\n")
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
                        gmro + " in " + gmrt + ":\n")
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
                        outfilewrite(outb, chr(32) * atleast(0, indent) + "if " + 
                        snob(x, 1) + ":\n") ; indent += 4

                    if lnob(x, 0) == "ifequal" and len(getmore(x, 1)) == 2:
                        #print lc () + p
                        #% write ifequal
                        outfilewrite(outb, chr(32) * atleast(0, indent) + "if " + 
                        snob(x, 1) + " == " + snob(x, 2) + ":\n") ; indent += 4

                    if lnob(x, 0) == "ifless" and len(getmore(x, 1)) == 2:
                        #print lc () + p
                        #% write ifless
                        outfilewrite(outb, chr(32) * atleast(0, indent) + "if " +
                        snob(x, 1) + " < " + snob(x, 2) + ":\n") ; indent += 4

                    if lnob(x, 0) == "ifmore" and len(getmore(x, 1)) == 2:
                        #print lc () + p
                        #% write ifmore
                        outfilewrite(outb, chr(32) * atleast(0, indent) + "if " + 
                        snob(x, 1) + " > " + snob(x, 2) + ":\n") ; indent += 4

                    if lnob(x, 0) in cmds.keys(): # + ufunc.keys():
                        e = 4 ; shln = lnob(x, 0) 

                    if lnob(x, 0) != "ne" and lnob(x, 
                    0) not in funcs.keys() + ["forin", "for", "func", 
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
                            if "ne" in prs:
                                if prs[:3] == "ne": e = 2 ; break ; break
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

                                        if neprsbac in ufunc.keys():
                                            #% write parametered func call 
                                            outfilewrite(outb, chr(32) * atleast(0,
                                            indent) + vrcs + ") ; " + lnob(x, 0) +
                                            " = nenone(" + lnob(x, 0) +
                                            ", nebac) ; ") ; vrcl += 1
                                        else:
                                            #% write builtin func call assignment
                                            outfilewrite(outb, chr(32) *
                                            atleast(0, indent) + vrcs + ") ; ") ; vrcl += 1
                                else:
                                    vrcs += ", " #; print "*"
                                    #if 
                                continue

                            if prs.lower() in funcs.keys() + ["forin", "for",
                            "func", "nextin", "next"] + ["break", "pass"]:
                                e = 3
                            neprsbac = None

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

                            if prs[0] == ";": 
                                #% write trailing comments 
                                outfilewrite(outb, prs + "\n") ; break

                            if prs.lower() in ufunc.keys():
                                #% write pre-func-call var backup for sub-style behavior
                                outfilewrite(outb, chr(32) * atleast(0, indent) +
                                "nebac = " + lnob(x,0) + " ; " ) # ##
                                neprsbac = prs.lower()	

                                cstrctr = len(ufunc[prs])
                                #print cstrctr
                                if cstrctr == 0:
                                    #% write zero-param func/?sub call
                                    outfilewrite(outb, chr(32) * 
                                    atleast(0, indent) + 
                                    vr + " = " + prs.lower() + "() ; " + lnob(x, 0) +
                                            " = nenone(" + lnob(x, 0) + ", nebac) ; ") # #
                                else:
                                    #print "y"
                                    vrop += 1
                                    vrcs = vr + " = " + prs.lower() + "(" 
                                    #multiparameter  

                            if prs.lower() in cmds.keys():
                                if prs.lower() in ["display", "pset", "line"]: 
                                    ingfx = 1
                                cstrctr = cmds[prs]

                                if cstrctr == -1:
                                    #% write zero-param subs
                                    outfilewrite(outb, chr(32) * 
                                    atleast(0, indent) + "ne" + 
                                    prs.lower() + "(" + vr + ") ; " ) ; vrcl += 1

                                if cstrctr == 0:
                                    #% write zero-param functions 
                                    outfilewrite(outb, chr(32) * atleast(0,
                                    indent) + vr +
                                    " = ne" + prs.lower() + "(" + vr + ") ; " ) ; vrcl += 1

                                if cstrctr < -1:
                                    if prs == "return":
                                        cstrctr = abs(cstrctr) - 1
                                        vrcs = "return " #parameter
                                    else:
                                        cstrctr = abs(cstrctr) - 1
                                        if prs == "swap": vrcs = "swap "
                                        else:
                                            vrop += 1
                                            vrcs = "ne" + prs.lower() + "(" + vr 
                                            vrcs += ", " #multiparameter  
                                else:
                                    vrop += 1
                                    vrcs = vr + " = ne" + prs.lower() + "(" + vr 
                                    vrcs += ", " #multiparameter  

                        if vrop == vrcl and e == 0: 
                            print lc(), nefsp(p)

                        outfilewrite(outb, "\n")
                    else:
                        print lc() + p
                else:
                    e = 2

if ingfx == 0: addtoout[3] = ""
ofwr += addtoout[0] + addtoout[1] + addtoout[3] + addfuncs + "\n"

for outsb in outb: ofwr += outsb + "\n"
print
print ofwr
try: exec(ofwr + """\ntry:
    if neraphics == 1:
        while 1:
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:  
                    neraphics = 0
                    stopgraphics()
            sleep(.1)
except: pass""")
except: pass
