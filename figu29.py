#!/usr/bin/env python
# coding: utf-8 
#### license: creative commons cc0 1.0 (public domain) 
#### http://creativecommons.org/publicdomain/zero/1.0/ 
proginf = "figueira 2.9, oct 2016 mn"
import sys
import os
from sys import stdin, stdout
from os import popen
try: from colorama import init ; init()
except: pass

buf = []

cmdhelp = [("crono", "input (shared-line) change var principal to number of seconds past midnight")

,("ordstdin", "input (shared-line) change var principal to array containing lines of stdin")
,("linhaentra", "input (shared-line) change var principal to string input from keyboard")
,("alinhaentra arquivo", "input (shared-line) change var principal to string of line from open file arquivo")
,("hora", "input (shared-line) change var principal to string of current time: hh:mm:ss")
,("ordaberto arquivo", "input (shared-line) change var principal to array of file lines in arquivo")
,("data", "input (shared-line) change var principal to string of the date: mm/dd/yyyy")
,("ordcurl url", "input (shared-line) like ordaberto, except downloading url into the array")
,("pausa segundos", "input (shared-line) wait for number of seconds before continuing with program")
,("comando", "input (shared-line) change var principal to array of command line parameters")
,("impress", "output (shared-line) output var principal to the screen (aka stdout)")
,("impressha", "output (shared-line) put var principal to screen; like print but stays on the line.")
,("aimpress arquivo", "output (shared-line) write var principal to open file designated by arquivo")
,("display", "output (shared-line) 1st time: stop automatic graphx update. 2nd, etc: update.")
,("lmp", "output (shared-line) clear the screen. currently only affects text screen")
,("graficos", "output --\\own\\line dont(or stop) suppress(ing) graphics. this is the default.")
,("textomodo", "output --\\own\\line suppress graphics; force graphics commands to use text.")
,("cortexto corcodigo", "output (shared-line) change color of upcoming text to colorcode from 0 - 15")
,("realcar corcodigo", "output (shared-line) change background color of upcoming text to colorcode 0-15")
,("localiz linha coluna", "output (shared-line) move to textmode position at linha, coluna")
,("ppus x y c", "output (shared-line) draw dot at location (x, y) in colorcode c (0 - 15)")
,("linha x1 y1 x2 y2 c", "output (shared-line) draw line from (x1, y1) to (x2, y2) in colorcode c (0-15)")
,("enquant", "loop --\\own\\line mark the start of a loop (will keep going without saida)")
,("saida", "loop --\\own\\line put in the middle of a loop to exit (stop looping)")
,("para vc de para quanto", "loop --\\own\\line start a for loop, changing vc from de to para, by quanto")
,("paraem itemv ordem", "loop --\\own\\line loop through each item in ordem; for each, set itemv to item")
,("severd cfvar", "conditional --\\own\\line run lines between severd and fig if cfvar is \"non-zero\"")
,("seigual var1 var2", "conditional --\\own\\line run lines between seigual and fig if var1 equals var2")
,("semais var1 var2", "conditional --\\own\\line run lines between semais and fig if var1 is > var2")
,("semenos var1 var2", "conditional --\\own\\line run lines between semenos and fig if var1 is < var2")
,("tentar", "conditional --\\own\\line put code that might not work between tentar and exceto")
,("exceto", "conditional --\\own\\line if code between tentar/exceto fails, run the code after exceto")
,("retomar", "conditional --\\own\\line mark the end of tentar/exceto/retomar command block")
,("outra", "conditional --\\own\\line after se- line, before fig. run lines if condition isnt true")
,("funcao nome p1 p2 …", "function --\\own\\line define function named nome with optional params p1,p2, etc")
,("obter parametro", "function (shared-line) (no longer required) copy parametro value to var principal")
,("python", "function --\\own\\line put inline python code between lines python and fig")
,("fig/seg/segem/efim", "fig (interchangeable) function --\\own\\line finalize a block (started by se/enquant/funcao/para/paraem")
,("passar", "function --\\own\\line blocks (for/next, etc) require something inside lines; passar works / does nothing")
,("mincula", "function (shared-line) change var principal to all-lower-case copy of own value")
,("maicula", "function (shared-line) change var principal to all-upper-case copy of own value")
,("cad", "function (shared-line) convert var principal from number to string")
,("shell", "function (shared-line) run var principal contents   in a command shell (os specific)")
,("asc", "function (shared-line) change var principal from string to ascii code of 1st char")
,("val", "function (shared-line) change var principal from string to numeric (int if whole)")
,("comprim", "function (shared-line) change var principal to  numeric length of var principal")
,("estanao", "function (shared-line) change var principal to zero if non-zero; or -1 if zero")
,("ecorta", "function (shared-line) strip whitespace from left side of var principal")
,("dcorta", "function (shared-line) strip whitespace from right side of var principal")
,("car", "function (shared-line) change var principal from numeric to ascii/uni string")
,("ordshell", "function (shared-line) change var principal to array of shell output (from var principal)")
,("ordreverso", "function (shared-line) change var principal from array to reverse order of array")
,("reverso", "function (shared-line) like ordreverso (which might be faster for array) for strings")
,("ordordena", "function (shared-line) change var principal from array to sorted array")
,("#", "comment (can\\share) place at beginning (or end) of line, prior to a comment")
,("():;|=,. ( ) : ; | = , .", "optional (shared-line) use in a shared line (and some others) for aesthetics/notation")
,("esquerdo numdecaras", "function (shared-line) change var principal to __ leftmost group of caras/items")
,("direito numdecaras", "function (shared-line) change var principal to __ rightmost group of caras/items")
,("ordobter ordem posicao", "function (shared-line) change var principal to posicao-nth item from ordem")
,("ordpus posicao que", "function (shared-line) change item in array in var principal to value of que")
,("meio posicao comprimento", "function (shared-line) change var principal to range of comprimento items from posicao")
,("cadeia n asciiorcad", "function (shared-line) change var principal to n instances of asciiorcad")
,("separar cadeia comcadeia", "function (shared-line) split cadeia by separator comcadeia into array, to var principal")
,("juntar ordem comcadeia", "function (shared-line) change var principal to string by joining ordem using comcadeia")
,("incad cadeia olharpara", "function (shared-line) change var principal to numeric position of olharpara in cadeia")
,("mudar", "function (shared-line) change current folder to path string from var principal")
,("sistema", "function (shared-line) put on (usually at the end of) a line to stop the program")
,("fechar", "function (shared-line) close the open file designated by var principal")
,("fim", "function (shared-line) interchangeable with sistema which ends the program")
,("aberto modo", "function (shared-line) open file at arquivo var principal in modo \"r\" or \"w\"")
,("retorno var", "function (shared-line) (optional) exit current function, returning value var")
,("troca var1 var2", "function (shared-line) change contents of var1 to contents of var2 and vice-versa")
,("mais numcadord", "math (shared-line) change var principal to itself plus num or cadeia or ord")
,("menos numerico", "math (shared-line) change var principal to itself minus numerico")
,("divipor numerico", "math (shared-line) change var principal to itself divided by numerico")
,("multipor numerico", "math (shared-line) change var principal to itself times numerico")
,("oct", "math (shared-line) change var principal from numeric decimal to octal")
,("hex", "math (shared-line) change var principal from  numeric decimal to hexadecimal")
,("cosseno", "math (shared-line) change numeric var principal to the cosine of itself")
,("seno", "math (shared-line) change numeric var principal to the sine of itself")
,("tan", "math (shared-line) change numeric var principal to its tangent")
,("atan", "math (shared-line) change numeric var principal to its arctangent")
,("int", "math (shared-line) change var principal from decimal (aka \"float\") to integer")
,("smb", "math (shared-line) change var principal to 0 if 0, to -1 if < 0, or 1 if > 0.")
,("raizquadr", "math (shared-line) change var principal to square root of itself")
,("mod denominador", "math (shared-line) change var principal to: var principal módulo denominador")
,("apoten n", "math (shared-line) raise numeric var principal to n-th power")
,("aleatint menor maior", "input (shared-line) change var principal to random number from menor to maior")
,("ordem", "function (shared-line) change var principal to array (starting with same contents)") ]

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
            stdout.write("    " + color(14,0)+ cde[0])
            cda = cde.remove(cde[0])
            for c in cde:
                stdout.write(" " + color(0, 7)+ " " + c + " " + color(7,0)+" ") ; stdout.flush()
            print "" 
            print "" 
            print color(3,0) + "        category:", rcat, rt.replace("\\", " ") 
            print "" 
            print "        " + color(7,0) + " ".join(rd) 
            print "" 
        color(7,0);
    return ck

def outfilewrite(outb, p):
    outb += [p]
    #global vrck 
    #vrck += p.strip()
    #if inle: print color(5, 0) + p.rstrip() ; p=raw_input() ; quit()

def color(f, b):
    if f == None: f = 0
    if b == None: b = 0
    n = "0"
    if f > 7: n = "1" ; f = f - 8
    if f == 1: f = 4 ## switch ansi colors for qb colors
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

def bcolor(b):
    f = None
    if f == None: f = 0
    if b == None: b = 0
    n = "0"
    if f > 7: n = "1" ; f = f - 8
    if f == 1: f = 4 ## switch ansi colors for qb colors
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

def figfsp(p):
    pp = "" ; flg = 0 
    fsp = figfsplit(p)    
    for fp in enumerate(fsp):
        if flg == 0 and fp[1] in cmds.keys():
            pp += color(8,0) + "_" + color(7,0) + " " ; flg = cmds[fp[1]]
            if flg < 0: flg = flg * -1
            else: flg = flg + 1
        pp += fp[1] + " "
        if flg > 0:
            flg -= 1 
            if flg == 0 and fp[0] + 1 < len(fsp):
                pp += color(8,0) + "_" + color(7,0) + " "
    return pp.rstrip().replace(color(8,0) + "_" + color(7,0) + " " + color(8,0) + 
    "_" + color(7,0), color(8,0) + "__" + color(7,0)).replace(color(8,0) + "_" + 
    color(7,0),color(8,0) + "__" + color(7,0))

def figfsplit(p):
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
    return "\x1b[0;37;44m" + right(chr(32) * flen + str(linecount), flen) + es

def wr(p):
    global buf
    buf += [p + "\n"]

color(11, None) ; print proginf; color(7, None) ; print

addtoout = [0]
addto = [0]

addtoout[0] = """import sys, os
from sys import stdin, stdout
from sys import argv as figargv
try: from colorama import init ; init()
except: pass # (only) windows users want colorama installed or ansi.sys enabled
from random import randint
from time import sleep\n\n
from os import chdir as figoch
from os import popen as figpo
from os import system as figsh
from os import name as figosname
figsysteme = 0
figfilehandles = {}
figfilecounters = {}
"""

addtoout += [0] ; addto += [0]

addtoout[1] = """from sys import stdout
def figlocaliz(x, l = "ignore", c = "ignore"):    
    import sys 
    if l == "ignore" and c == "ignore": pass 
    # do nothing. want it to return an error? 

    elif l < 1 and c != "ignore": 
        sys.stdout.write("\x1b[" + str(c) + "G") # not ansi.sys compatible 
    elif l != "ignore" and c == "ignore": 
        sys.stdout.write("\x1b[" + str(l) + ";" + str(1) + "H") 
    else: sys.stdout.write("\x1b[" + str(l) + ";" + str(c) + "H") 

import time

def fignonz(p, n=None):
    if n==None:
        if p == 0: return 1
    else:
        if p == 0: return n
    return p

def figestanao(p):
    if p: return 0
    return -1

figbac = None
figprsbac = None
sub = None
def fignone(p, figbac):
    if p == None: return figbac
    return p
    return -1

def stopgraphics():
    global yourscreen
    global figraphics
    figraphics = 0
    try: pygame.quit()
    except: pass\n
\n"""
addtoout += [0] ; addto += [0]

addtoout[2] = """palette = {}
palette["black"] = (0, 0, 0)
palette["gray"], palette["grey"] = (0, 0, 0), (85, 85, 85)
palette["blue"], palette["lightblue"] = (0, 0, 170), (85, 85, 255)
palette["green"], palette["lightgreen"] = (0, 170, 0), (85, 255, 85)
palette["cyan"], palette["lightcyan"] = (0, 170, 170), (85, 255, 255)
palette["red"], palette["lightred"] = (170, 0, 0), (255, 85, 85)
palette["magenta"], palette["lightmagenta"] = (170, 0, 170), (255, 85, 255)
palette["brown"], palette["yellow"] = (170, 85, 0), (255, 255, 85)
palette["white"], palette["lightwhite"] = (170, 170, 170), (255, 255, 255)\n"""
addtoout += [0] ; addto += [0]

addtoout[3] = """figraphics = -1
figrupd = 1
try: import pygame
except: figraphics = 0
yourscreen = ""
try: pygame.init()
except: figraphics = 0 # unable to init pygame, just use text
def figppus(z, x, y, c):
    global figraphics, figrupd
    global yourscreen
    global figcgapal
    if figraphics == -1:
        #pygame.init() 
        try:
            yourscreen = pygame.display.set_mode((800, 600))
            pygame.display.set_caption("fig graphics screen")
            #pygame.quit()
            figraphics = 1
        except: 
            stopgraphics() ; figraphics = 0
    if figraphics == 0:
        if x > -1 and y > -1:
            figcortexto(c, c)
            figlocaliz(0, int(y) + 1, int(x) + 1) ; stdout.write(unichr(9608))
            sys.stdout.flush()
    if figraphics == 1:
        if x > -1 and y > -1:
            yourscreen.set_at((x, y), figcgapal[c]) 
            #pygame.draw.circle(yourscreen,(255, 255, 255),(int(x), int(y)), 1, 0) 
            if figrupd: pygame.display.update()
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:  
                    figraphics = 0
                    stopgraphics()

def figlinha(z, x, y, x2, y2, c):
    global figraphics, figrupd
    global yourscreen
    global figcgapal
    if figraphics == -1:
        #pygame.init() 
        try:
            yourscreen = pygame.display.set_mode((800, 600))
            pygame.display.set_caption("fig graphics screen")
            #pygame.quit()
            figraphics = 1
        except: 
            stopgraphics() ; figraphics = 0
    if figraphics == 0:
        if x > -1 and y > -1 and x2 > -1 and y2 > -1:
            figcortexto(c, c)
            if x2 < x: x, y, x2, y2 = x2, y2, x, y
            figliney = [y, y2]
            figlinec = 0
            figlinestep = int(y2 - y)
            if figlinestep < 0: figlinestep = int(y - y2) ; figlinec = 0
            if figlinestep < 1: figlinestep = 1
            figlinestep = float(1) / figlinestep
            figlinex = x
            while 1:
                if figlinex > x2: break
                if y2 - y == 0:
                    figlocaliz(0, int(y) + 1, int(figlinex) + 1)
                    stdout.write(unichr(9608)) 
                elif y2 < y:
                    figlinec -= figlinestep 
                    figlocaliz(0, int(y + int(float(y - y2) / fignonz(x2 - x,.1) *
                    fignonz(figlinec,.1) ) ) + 1, int(figlinex) + 1)
                    stdout.write(unichr(9608)) 
                else:
                    figlocaliz(0, int(y + int(float(y2 - y) / fignonz(x2 - x,.1) *
                    fignonz ( figlinec,.1) ) ) + 1, int(figlinex) + 1) ; 
                    stdout.write(unichr(9608)) 
                    figlinec += figlinestep 
                    #[0] = figliney[0]+float(figliney[1] - figliney[0]) / (x2 - x) 
                figlinex += figlinestep
            figlocaliz(0, int(y) + 1, int(x) + 1) ; stdout.write(unichr(9608))
            figlocaliz(0, int(y2) + 1, int(x2) + 1) ; stdout.write(unichr(9608))
            sys.stdout.flush()
    if figraphics == 1:
        if x > -1 and y > -1 and x2 > -1 and y2 > -1:
            yourscreen.set_at((x, y), figcgapal[c]) 
            pygame.draw.line(yourscreen, figcgapal[c], (x, y), (x2, y2), 1) 
            if figrupd: pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    figraphics = 0
                    stopgraphics()

def anykeypyg():
    global yourscreen
    global figraphics, figrupd
    p = 0
    while not p: 
        if figraphics == 0: break
        time.sleep(0.001)
        for event in pygame.event.get():   
            if event.type == pygame.KEYDOWN: 
                if figrupd: pygame.display.update() 
                p = 1\n\n"""

addtoout += [0] ; addto += [0]

palette = {}
palette["black"] = (0, 0, 0)
palette["gray"], palette["grey"] = (0, 0, 0), (85, 85, 85)
palette["blue"], palette["lightblue"] = (0, 0, 170), (85, 85, 255)
palette["green"], palette["lightgreen"] = (0, 170, 0), (85, 255, 85)
palette["cyan"], palette["lightcyan"] = (0, 170, 170), (85, 255, 255)
palette["red"], palette["lightred"] = (170, 0, 0), (255, 85, 85)
palette["magenta"], palette["lightmagenta"] = (170, 0, 170), (255, 85, 255)
palette["brown"], palette["yellow"] = (170, 85, 0), (255, 255, 85)
palette["white"], palette["lightwhite"] = (170, 170, 170), (255, 255, 255)

textpalette = {}
textpalette["black"],textpalette["gray"], palette["grey"] = 0, 8, 8
textpalette["blue"], textpalette["lightblue"] = 1, 9
textpalette["green"], textpalette["lightgreen"] = 2, 10
textpalette["cyan"], textpalette["lightcyan"] = 3, 11
textpalette["red"], textpalette["lightred"] = 4, 12
textpalette["magenta"], textpalette["lightmagenta"] = 5, 13
textpalette["brown"], textpalette["yellow"] = 6, 14
textpalette["white"], textpalette["lightwhite"] = 7, 15

# -2: print(variable, etc)
# -1: print(variable), 0: variable = int(variable), 1: variable=left(variable, etc)

cmds = {"ecorta":0, "linhaentra":0, "comprim":0, "asc":0, "aatn":0, "cad":0,
"obter":1, "car":0, "impressha":-1, "pausa":-2, "ordordena":-1,
"ordreverso":-1, "reverso":0, "display":-1, "sistema":-1, "fim":-1, 
"impress":-1, "ordpus":-3,
"separar":2, "esquerdo":1, "juntar":2, "ordobter":2, "meio":2, "direito":1, 
"mais":1, "multipor":1, "fechar":-1, "lmp":-1, "alinhaentra":1, "aimpress":-2, 
"aberto":-2, "ordaberto":1, "ordstdin":0, "ordcurl":1, "cortexto":-2, 
"realcar":-2, "divipor":1, "hex":0, "dcorta":0, "cadeia":2, "crono":0, "comando":0,
"hora":0, "data":0, "tan":0, "oct":0, "val":0, "menos":1, "mincula":0, "maicula":0, 
"int":0, "esquerdo":1, "troca":-3, "localiz":-3, "ppus":-4, "linha":-6, 
"retorno":-2, "aleatint":2, "apoten":1, "ordem":0, "mod":1, "cosseno":0, 
"estanao":0, "seno":0, "incad":2, "mudar":-1, "shell":-1, "ordshell":0,
"smb":0, "raizquadr":0}

funcs = {"funcao" : -1, "severd" : -2, "seigual" : -3, "semenos" : -3, 
"semais" : -3, "tentar":0, "exceto":0, "retomar":0, "outra":0}

ufunc = {}

#addfuncs = addtoout[0] + addtoout[1] + addtoout[3] + """
addfuncs = """
def figcortexto(x, f):
    b = 0
    if f == None: f = 0
    if b == None: b = 0
    n = "0"
    if f > 7: n = "1" ; f = f - 8
    if f == 1: f = 4 ## switch ansi colors for qb colors
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

figcgapal = [(0, 0, 0), (0, 0, 170), (0, 170, 0), (0, 170, 170),
(170, 0, 0), (170, 0, 170), (170, 85, 0), (170, 170, 170), 
(85, 85, 85), (85, 85, 255), (85, 255, 85), (85, 255, 255), 
(255, 85, 85), (255, 85, 255), (255, 255, 85), (255, 255, 255)]

def figobter(p, s): return s

def figrealcar(x, b):
    f = None
    if f == None: f = 0
    if b == None: b = 0
    n = "0"
    if f > 7: n = "1" ; f = f - 8
    if f == 1: f = 4 ## switch ansi colors for qb colors
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

def figincad(x, p, e):
    try: return p.index(e) + 1
    except: return 0

def figmudar(p):
    try: figoch(p)
    except: print "no such file or directory: " + str(p) ; figend(1)

def figshell(p):
    global figsysteme
    try: figsysteme = figsh(p)
    except:
        print "error running shell command: " + chr(34) + str(p) + chr(34)
        figend(1)

def figordshell(c):
    global figsysteme
    try:
        figsysteme = 0
        sh = figpo(c)
        ps = sh.read().replace(chr(13) + chr(10), 
        chr(10)).replace(chr(13), chr(10)).split(chr(10))
        figsysteme = sh.close()
    except:
        print "error running arrshell command: " + chr(34) + str(c) + chr(34) 
        figend(1)
    return ps[:]

def figsmb(p):
    p = float(p)
    if p > 0: return 1
    if p < 0: return -1
    return 0

def figcad(p): return str(p)
def figimpress(p): print p
def figcar(p): 
    if type(p) == str:
        if len(p) > 0:
            return p[0]
    return chr(p)
def figimpressha(p): stdout.write(str(p)) ; sys.stdout.flush()
def figesquerdo(p, s): return p[:s]
def figmeio(p, s, x):
    arr = 0
    if type(p) == list or type(p) == tuple: arr = 1
    rt = p[s - 1:x + s - 1]
    if arr and len(rt) == 1: rt = rt[0]
    return rt
def figdireito(p, s): return p[-s:]
def figaleatint(x, s, f):
    return randint(s, f)
def figmincula(p): return p.lower()

def figmaicula(p): return p.upper()
def figint(p): return int(p)

def figordpus(x, p, s): 
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
        #if type(p) == tuple: 
        #    if type(s) == tuple:
        #        p = tuple(list(p) + list(s))
        #    elif type(s) == list:
        #        p = tuple(list(p) + s[:])
        #    else:
        #        p = tuple(list(p) + [s])
        #if type(p) == str: p = p + s # str(s) if you want it easier

def figaberto(x, s):
    import fileinput
    if s.lower() == "w":
        if (x) not in figfilehandles.keys(): 
            figfilehandles[x] = open(x[:], s.lower())
    elif s.lower() == "r":
        if (x) not in figfilehandles.keys():
            figfilehandles[x] = fileinput.input(x[:])
            figfilecounters[x] = 0
    else:
        if (x) not in figfilehandles.keys(): figfilehandles[x] = open(x[:], s[:])

def figaimpress(x, s):
    fon = figosname
    sep = chr(10)
    if fon == "nt": sep = chr(13) + chr(10)
    figfilehandles[s].write(str(x) + sep)

def figalinhaentra(x, s):
    try:
        p = figfilehandles[s][figfilecounters[s]].replace(chr(13), 
        "").replace(chr(10), "")
        figfilecounters[s] += 1
    except:
        p = chr(10)
    return p

def figfechar(x):
    if (x) in figfilehandles.keys():
        figfilehandles[x].close() ; del figfilehandles[x]
        try: del figfilecounters[x]
        except: pass

def figlmp(x):
    if figosname == "nt": cls = figsh("cls") 
    else: stdout.write("\x1b[2J\x1b[1;1H") ; sys.stdout.flush()

def figordaberto(x, s):
    x = open(s).read().replace(chr(13) + chr(10), chr(10)).replace(chr(13), 
    chr(10)).split(chr(10))
    return x[:]

def figordcurl(x, s):
    from urllib import urlopen
    x = str(urlopen(s).read()) ; x = x.replace(chr(13) + chr(10), 
    chr(10)).replace(chr(13), chr(10)).split(chr(10))
    return x[:]

def figordstdin(x):
    ps = []
    for p in stdin: ps += [p[:-1]]
    return ps[:]

def figordobter(x, p, s): 
    if 1:
        return p[s - 1]

def figmais(p, s): 
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

def figjuntar(p, x, s):
    t = ""
    if len(x) : t = str(x[0])
    for c in range(len(x)):
        if c > 0: t += str(s) + str(x[c]) 
    return t # s.join(x)

def figordem(p):
    if type(p) in (float, int, str): 
        p = [p]
    else:
        p = list(p)
    return p

def figseparar(p, x, s):
    return x.split(s)

def figval(n): 
    n = float(n) 
    if float(int(n)) == float(n): n = int(n) 
    return n    
def figmultipor(p, s):
    if type(p) in (float, int):
        p = p * s # float(s) if you want it easier
        if p == float(int(p)): p = int(p)
    else:
        if type(p) == list:
            p = p[:] * s # figval(s)
        else:
            p = p * s # figval(s) if you want it easer
    return p
def figdivipor(p, s):
    p = float(p) / s
    if p == float(int(p)): p = int(p)
    return p
def figmenos(p, s): return p - s

def figapoten(p, s): 
    p = p ** s
    if p == float(int(p)): p = int(p)
    return p
def figmod(p, s): 
    return p % s
def figcosseno(p): 
    from math import cos ; p = cos(p)
    if p == float(int(p)): p = int(p)
    return p
def figseno(p): 
    from math import sin ; p = sin(p)
    if p == float(int(p)): p = int(p)
    return p
def figraizquadr(p): 
    from math import sqrt ; p = sqrt(p)
    if p == float(int(p)): p = int(p)
    return p

def figecorta(p): return p.lstrip() 
def figlinhaentra(p): return raw_input() 
def figcomprim(p): return len(p) 
def figasc(p): return ord(p[0])
def figatan(p):
    from math import atan ; p = atan(p)
    if p == float(int(p)): p = int(p)
    return p

def fighex(p): return hex(p)
def figdcorta(p): return p.rstrip() 
def figcadeia(x, p, n): 
    if type(n) == str: return n * p 
    return chr(n) * p 
def figcrono(p):
    from time import strftime
    return int(strftime("%H"))*60*60+int(strftime("%M"))*60+int(strftime("%S"))

def fighora(p): from time import strftime ; return strftime("%H:%M:%S")

def figdata(p): from time import strftime ; return strftime("%m/%d/%Y")

def figcomando(p): return figargv[1:]

def figtan(p): 
    from math import tan ; p = tan(p)
    if p == float(int(p)): p = int(p)
    return p

def figoct(p): return oct(p)

def figpausa(p, s): 
    #print lc () + p
    #addto[0] = 1
    sleep(s)
def figordordena(p): 
    p.sort()

def figdisplay(x): 
    global figraphics, figrupd
    figrupd = 0
    if figraphics == 1:
        pygame.display.update()

def figreverso(p): 
    if type(p) == list: p.reverse() ; return p
    elif type(p) == str:
        p = map(str, p) ; p.reverse()
        p = "".join(p)
        return p

def figordreverso(p): 
    p.reverse()

def figfuncao(p, s): return p
def figfim(x): quit()
def figif(p, s): return p
def figthen(p, s): return p
def figsistema(x): quit()
\n"""

demo = """
p 7 ordem multipor 5

x "hello, world!"
#z x impressha
#z x impress
x 5
x 5 multipor 7
x 3 mais 5 multipor 7
z x abs
x z cad asc abs int

funcao oi p           |  # function hello(p)
x "oi, "              |  # x = "hello, "
x impressha retorno 5 |  # print x; : hello = 5 : exit function
fig                   |  # end function

x oi x                |  # x = hello(x)

#x if 5```````````````` # if x = 5 then
#p "five" print```````` # p = "five" : print p
#else`````````````````` # else 
#p "not 5 or 7" print`` # p = "not 5 or 7" : print p
#fig````````````````````# end if
c comando impress
#y x````````````````````# y = x
#y chr 70 mid y 1 1```` # y = chr(70) : y = mid(y, 1, 1)
#x print sleep 2 cls````# print x : sleep 2 : cls

p impress
p impress ordpus 2 8 impress
z juntar p "(_)" impress 
x z impress
p impress fim

funcao pete
p "oi" impress
fig

funcao mais5 r
x obter r mais 5 retorno x
fig

funcao ppp
z 32 car impress
para p 1 100 1
x aleatint 0 3 
y aleatint 0 3
c aleatint 1 9
#z ppus x y c
c cortexto 7
seg
fig

z ppp
z pausa 1
#textmode
z ppp pausa 2 z ppp
"""

p = ""
try: p = right(sys.argv, 1)[0]
except: pass
if not ".figu" in p.lower():
    if p.lower() == "help":
        stdout.write("\n    type (any) part of the command you want help on." +
        "\n\n    fig will show all matches.\n\n\n    ")
        helpf = chelp(raw_input())
        if not helpf: print(color(14,0)+"\n    no commands match your search.") ; print("")
        color(7,0)
    #try: inputfile = stdin.read().replace(chr(13), "").split("\n")
    #except: 
    #print "need an input file to do anything..."; print ; quit()
        quit()
    else:
        print "using built-in demo source, translating to demo.figu.py..." ; print
        p = "demo.figu"
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
figraphics = -1 # -1 = uninitialized, 0 = textmode, 1 = initialized
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
            outfile.write("# figueira translator version: " + proginf.split(",")[0] + "\n")
    if inlinep:
        if p.lower().strip() == "fig":
            inlinep = 0
            print lc() + p
            indent = atleast(0, indent - 4)
        else:
            print lc() + color(2, None) + p + color(7, None)
            #% write copied lines of inline python
            outfilewrite(outb, chr(32) * atleast(0, indent - 4) + 
            leftfour(p) + "\n")

    elif mode == "output the following:":
        if p.lower().strip() == "display":
            mode = 0
            print lc() + p
        else:
            wr(chr(32) * atleast(0, indent) + "print \"" + p.replace(chr(34), 
            "\" + chr(34) + \"").replace(chr(92), "\" + chr(92) + \"") + "\"")
            print lc() + p.replace(chr(34), "\" + chr(34) + \"").replace(chr(92), 
            "\" + chr(92) + \"") 

    elif mode == 0:
        x = figfsplit(p.lstrip())
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
                        print lc(), figfsp(p)
                    else: print lc() + "[this first comment isn't copied over]"
                    es = 0 
                else:
                    #% write comments
                    #print color(14, 0) + p + color(7,0) ; znul = raw_input()  #$ 
                    outfilewrite(outb, chr(32) * atleast(0, indent) + p + "\n")
                    print lc(), figfsp(p)

            elif lnob(x, 0) == "figg":
                 e = 2

            elif lp.rstrip() == "python":
                indent += 4
                inlinep = 1
                print lc() + p

            else:
                if not lnob(x, 0) == "figg":
                    if lnob(x, 0) != "fig" and not lnob(x, 
                    0) in cmds.keys() and not lnob(x, 
                    0) in funcs.keys() + ["paraem", "para", "funcao", "segem",
                    "seg", "enquant", "efim"] + ["saida", "passar"]: 
                        if not lnob(x, 0) in vrs: vrs += [lnob(x, 0)[:]]
                        #% write variable
                        #var: print color(14, 0) + "variable:" + lnob(x, 0) + color(7,0) ; znul = raw_input()  #$
                        outfilewrite(outb, "\n")
                        outfilewrite(outb, chr(32) * atleast(0, indent) + 
                        "figlist = 0\n") 

                        outfilewrite(outb, chr(32) * atleast(0, indent) + 
                        "try: figlist = int(type(" + lnob(x, 0) + ") == list)\n")

                        outfilewrite(outb, chr(32) * atleast(0, indent) + 
                        "except NameError: pass\n")
                        outfilewrite(outb, chr(32) * atleast(0, indent) + 
                        "if not figlist: " + lnob(x, 0) + " = 0 \n")

                    if lnob(x, 0) == "fig":
                        #print lc () + p
                        #% write? its whitespace
                        #$
                        indent = atleast(0, indent - 4) 
                    if lnob(x, 0) == "efim":
                        #print lc () + p
                        #% write? its whitespace
                        #$
                        indent = atleast(0, indent - 4) 
                    if lnob(x, 0) == "seg":
                        #print lc () + p
                        #% write? its whitespace
                        #$
                        indent = atleast(0, indent - 4) 
                    if lnob(x, 0) == "segem":
                        #print lc () + p
                        #% write? its whitespace
                        #$
                        indent = atleast(0, indent - 4) 
                    if lnob(x, 0) == "tentar":
                        #print lc () + p
                        #% write try line
                        #$
                        outfilewrite(outb, chr(32) * atleast(0, indent) + "try:\n")
                        indent = atleast(0, indent + 4) 
                    if lnob(x, 0) == "outra":
                        #print lc () + p
                        #% write else line
                        #$
                        outfilewrite(outb, chr(32) * atleast(0, indent - 4) + 
                        "else:\n")
                    if lnob(x, 0) == "exceto":
                        #print lc () + p
                        indent = atleast(0, indent - 4) 
                        #% write except line
                        #$
                        outfilewrite(outb, chr(32) * atleast(0, indent) + 
                        "except:\n")
                        indent = atleast(0, indent + 4) 
                    if lnob(x, 0) == "retomar":
                        #print lc () + p
                        #% write? its whitespace
                        #$
                        indent = atleast(0, indent - 4) 
                    if lnob(x, 0) == "enquant":
                        #print lc () + p
                        #% write simple loop
                        #$
                        outfilewrite(outb, chr(32) * atleast(0, indent) + 
                        "while 1:\n")
                        indent += 4 
                    if lnob(x, 0) == "funcao" and len(getmore(x, 1)) > 0:
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
                        #$ print color(14,0)+ "def " +  funcname + "(" + ", ".join(mkf) + "):" + color(7,0)
                        outfilewrite(outb, chr(32) * atleast(0, indent) + "def " +
                        funcname + "(" + ", ".join(mkf) + "):\n")
                        indent += 4

                    if lnob(x, 0) == "para" and len(getmore(x, 1)) == 4:
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
                            ")), int(float(" + gmrh + ")) + figsmb(" + gmrf + 
                            "), fignonz(int(float(" + gmrf + ")))):\n")
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

                    if lnob(x, 0) == "paraem" and len(getmore(x, 1)) == 2:
                        #print lc () + p
                        gmro = getlmore(x, 1)[0]
                        gmrt = getlmore(x, 1)[1]
                        if gmro not in vrs: vrs += [gmro[:]]
                        #% write forin command with params
                        #$
                        outfilewrite(outb, chr(32) * atleast(0, indent) + "for " +
                        gmro + " in " + gmrt + ":\n")
                        indent += 4

                    if lnob(x, 0) == "saida":
                        #print lc () + p
                        #% write break command
                        #$ print
                        outfilewrite(outb, chr(32) * 
                        atleast(0, indent) + "break\n") 

                    if lp.rstrip() == "graficos":
                        ingfx = 1
                        #% write change to default mode (dont suppress gfx)
                        #$
                        outfilewrite(outb, chr(32) * atleast(0, indent) +
                        "figraphics = -1\n")
                        figraphics = -1
                        outfilewrite(outb, chr(32) * atleast(0, indent) + 
                        "figpset(0, -1, -1, 0)\n")
                        #print lc () + p

                    if lnob(x, 0) == "textomodo":
                        #print lc () + p
                        addto[3] = 1
                        #% write change to text mode (suppress graphics)
                        #$
                        outfilewrite(outb, chr(32) * atleast(0, indent) + 
                        "figraphics = 0\n")
                        outfilewrite(outb, chr(32) * atleast(0, indent) +
                        "stopgraphics()\n")
                        figraphics = 0

                    if lnob(x, 0) == "passar":
                        #print lc () + p
                        #% write pass command
                        #$ print
                        outfilewrite(outb, chr(32) *
                        atleast(0, indent) + "pass\n") 

                    if lnob(x, 0) == "severd":
                        #print lc () + p
                        #% write iftrue
                        #$ print color(14,0) + "if " +    snob(x, 1) + " > " + snob(x, 2) + ":\n"+ " ; " +color(7,0)
                        outfilewrite(outb, chr(32) * atleast(0, indent) + "if " + 
                        snob(x, 1) + ":\n") ; indent += 4

                    if lnob(x, 0) == "seigual" and len(getmore(x, 1)) == 2:
                        #print lc () + p
                        #% write ifequal
                        #$ print color(14,0) + "if " +    snob(x, 1) + " > " + snob(x, 2) + ":\n"+ " ; " +color(7,0)
                        outfilewrite(outb, chr(32) * atleast(0, indent) + "if " + 
                        snob(x, 1) + " == " + snob(x, 2) + ":\n") ; indent += 4

                    if lnob(x, 0) == "semenos" and len(getmore(x, 1)) == 2:
                        #print lc () + p
                        #% write ifless
                        #$ print color(14,0) + "if " +    snob(x, 1) + " > " + snob(x, 2) + ":\n"+ " ; " +color(7,0)
                        outfilewrite(outb, chr(32) * atleast(0, indent) + "if " +
                        snob(x, 1) + " < " + snob(x, 2) + ":\n") ; indent += 4

                    if lnob(x, 0) == "semais" and len(getmore(x, 1)) == 2:
                        #print lc () + p
                        #% write ifmore
                        #$ print color(14,0) + "if " +    snob(x, 1) + " > " + snob(x, 2) + ":\n"+ " ; " +color(7,0)
                        outfilewrite(outb, chr(32) * atleast(0, indent) + "if " + 
                        snob(x, 1) + " > " + snob(x, 2) + ":\n") ; indent += 4

                    if lnob(x, 0) in cmds.keys(): # + ufunc.keys():
                        e = 4 ; shln = lnob(x, 0) 

                    if lnob(x, 0) != "fig" and lnob(x, 
                    0) not in funcs.keys() + ["paraem", "para", "funcao", 
                    "segem", "seg", "enquant", "efim"] + ["saida", "passar"]:

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

                                    if lnob(x, prsc - 1) == "retorno":
                                        #% write return command
                                        #$ print color(14,0) +vrcs + " ; " +color(7,0)
                                        outfilewrite(outb, chr(32) * atleast(0, 
                                        indent) + vrcs)

                                    elif lnob(x, prsc - 2) == "troca":
                                        vrcs = lnob(x, prsc - 1) + ", " + lnob(x,
                                        prsc - 0) + " = " + lnob(x, 
                                        prsc - 0) + ", " + lnob(x, prsc - 1)
                                        #% write swap of 2 vars in python syntax
                                        #$ print color(14,0) +vrcs + " ; " +color(7,0)
                                        outfilewrite(outb, chr(32) * atleast(0,
                                        indent) + vrcs + " ; ")
                                    else:

                                        if figprsbac in ufunc.keys():
                                            #% write parametered func call 
                                            #$ print color(14,0)+  vrcs + ") ; " + lnob(x, 0) + " = fignone(" + lnob(x, 0) + ", figbac) ; " +color(7,0)
                                            outfilewrite(outb, chr(32) * atleast(0,
                                            indent) + vrcs + ") ; " + lnob(x, 0) +
                                            " = fignone(" + lnob(x, 0) +
                                            ", figbac) ; ") ; vrcl += 1
                                        else:
                                            #% write builtin func call assignment
                                            #$ print color(14,0)+  vr + " = " +  vrcs + ") ; "  +color(7,0)
                                            outfilewrite(outb, chr(32) *
                                            atleast(0, indent) + vrcs + ") ; ") ; vrcl += 1
                                else:
                                    vrcs += ", " #; print "*"
                                    #if 
                                continue

                            if prs.lower() in funcs.keys() + ["paraem", "para",
                            "funcao", "segem", "seg", "enquant", 
                            "efim"] + ["saida", "passar"]:
                                e = 3
                            figprsbac = None

                            if prs.lower() in vrs and cstrctr == 0: 
                                #and len(getmore(x, 1)) == 1:
                                #% write lefthand variable assignment
                                #$ print color(14,0)+  vr + " = " + prs.lower()  +color(7,0)
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
                                #% write trailing comments #$ print color(14, 0) + prs  + color(7,0)
                                outfilewrite(outb, prs + "\n") ; break


                            if prs.lower() in ufunc.keys():
                                #% write pre-func-call var backup for sub-style behavior #$ print color(14, 0) + "figbac = " + lnob(x,0) + " ; " + color(7,0)
                                outfilewrite(outb, chr(32) * atleast(0, indent) +
                                "figbac = " + lnob(x,0) + " ; " ) # ##
                                figprsbac = prs.lower()	

                                cstrctr = len(ufunc[prs])
                                #print cstrctr
                                if cstrctr == 0:
                                    #% write zero-param func/?sub call
                                    #$ print color(14, 0) + vr + " = " + prs.lower() + "() ; " + lnob(x, 0) + " = fignone(" + lnob(x, 0) + ", figbac) ; " + color(7,0)
                                    outfilewrite(outb, chr(32) * 
                                    atleast(0, indent) + 
                                    vr + " = " + prs.lower() + "() ; " + lnob(x, 0) +
                                            " = fignone(" + lnob(x, 0) + ", figbac) ; ") # #
                                else:
                                    #print "y"
                                    vrop += 1
                                    vrcs = vr + " = " + prs.lower() + "(" 
                                    #$ print color(4, 0) + vr + " = " + prs.lower() + "(" + color(7,0) #$
                                    #multiparameter  


                            if prs.lower() in cmds.keys():
                                if prs.lower() in ["display", "ppus", "linha"]: 
                                    ingfx = 1
                                ##print prs	
                                cstrctr = cmds[prs]
                                ##print cstrctr
                                if cstrctr == -1:
                                    #% write zero-param subs
                                    #print color(14, 0) + "fig" +  prs.lower() + "(" + vr 
                                    #+ ") ; " + color(7,0) ; #znul = raw_input()  #$
                                    outfilewrite(outb, chr(32) * 
                                    atleast(0, indent) + "fig" + 
                                    prs.lower() + "(" + vr + ") ; " ) ; vrcl += 1

                                if cstrctr == 0:
                                    #% write zero-param functions 
                                    #print color(14, 0) + vr + " = fig" + prs.lower() 
                                    #+ "(" + vr + ") ; "+ color(7,0) ; #znul = raw_input()  #$
                                    outfilewrite(outb, chr(32) * atleast(0,
                                    indent) + vr +
                                    " = fig" + prs.lower() + "(" + vr + ") ; " ) ; vrcl += 1

                                if cstrctr < -1:
                                    if prs == "retorno":

                                        cstrctr = abs(cstrctr) - 1
                                        vrcs = "return " #parameter
                                    else:
                                        cstrctr = abs(cstrctr) - 1
                                        if prs == "troca": vrcs = "troca "
                                        else:
                                            vrop += 1
                                            vrcs = "fig" + prs.lower() + "(" + vr 
                                            vrcs += ", " #multiparameter  
                                else:
                                    vrop += 1
                                    vrcs = vr + " = fig" + prs.lower() + "(" + vr 
                                    vrcs += ", " #multiparameter  

                        if vrop == vrcl and e == 0: 
                            print lc(), figfsp(p)

                        #% finish each line with lf
                        outfilewrite(outb, "\n")
                    else:
                        print lc() + p
                else:
                    e = 2

#                if not len(error):
#                    error = "error: unknown command."
#                    errorin = linecount
#                    errorsrc = p
#                print lc () + "unknown:", p

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
                print lc() + color(14, 0) + str(p) + color(7, 0)
                break

            if e == 2:
                e = 0
                if not len(error):
                    error = "error: cannot create variable or function beginning"
                    error += " with \"fig\""
                    errorin = linecount
                    errorsrc = p
                print lc() + color(14, 0) + p + color(7, 0)
                break

            if e == 3:
                e = 0
                if not len(error):
                    error = "error: single-line command \"" + shln + "\" not on own line"
                    errorin = linecount
                    errorsrc = p
                print lc() + color(14, 0) + p + color(7, 0)
                break

            if e == 4:
                e = 0
                if not len(error):
                    error = "error: shared-line function \""
                    error += shln + "\" cannot be used to start a line"
                    errorin = linecount
                    errorsrc = p
                print lc() + color(14, 0) + p + color(7, 0)
                break

    if vrcl != vrop: 
                e = 0 
                if not len(error):
                    error = "error: a command has the wrong number of parameters."
                    errorin = linecount
                    errorsrc = p
                print lc() + color(14, 0) + str(p) + color(7, 0)
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
    print error ; color(14, None) ; print "error in line " + str(errorin) + ":"
    color(7, None)
    print errorsrc
    #from os import system as stf ; p = stf("touch e") # patched jun 2016
else:
    try: os.system("chmod +x \"" + outname + "\"")
    except: pass
    color (11, None) ; print "translation complete. ", ; color(7, None)
    print "here's a python script you can run: ", 
    print color(11, None) + outname + color(7, None)
print
