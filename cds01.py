#!/usr/bin/env python
# coding: utf-8 
## license: creative commons cc0 1.0 (public domain) 
## http://creativecommons.org/publicdomain/zero/1.0/ 
proginf = "codeschl 0.1, oct 2017 mn" # with lots of design help
import sys ; from sys import stdout
import os ; from os import system as cdssh
from os import name as cdsosname
from random import randint

demo = """

esc
display hello
sleep 2
display now we clear the screen
sleep 5
esc
display tada!

"""

def cdsdisplay_dc(dx): return "put " + chr(34) + dx + chr(34) + " on the screen"
def cdssldisplay_dc(dx): return "put  " + dx + " on the screen without a newline"
def cdsmkfnc_dc(funcname, funcset, funcps):
    return ("make function named " + funcname + ", setting variable " + 
    funcset + ", with parameters " + funcps)

def outverb(each, allch, allcd):
    if len(allch): cdsfile.write(chr(32) * atleast(0, indent) + allch + nl)
    cdsfile.write("#" + bs + es + "[0;35m" + spcl(each) + allcd + " #" + bs + es + "[0m " + nl)
    cdsfile.write("#" + bs + es + "[0;0m" + 	each + es + "[0;30m " + nl)

def cdslft(dx, howmany): return dx[:howmany]
def cdsrt(dx, howmany): return dx[-howmany:]
top = """
import sys ; from sys import stdout
import os ; from os import system as cdssh
from os import name as cdsosname
from random import randint
from os import name as cdsosname

#### esc: clear the screen
def cdsesc():
    if cdsosname == "nt": cls = cdssh("cls") 
    else: stdout.write(chr(27) + "[2J" + chr(27) + "[1;1H") ; sys.stdout.flush()

#### display wot: put wot on the screen
def cdsdisplay(dx): print cdsdelpz(dx)

#### sleep: wait for cd seconds
def cdssleep(cd):
    from time import sleep ; sleep(cd)

def cdsdelpz(p):
    if type(p) in (int, float):
        if float(int(p)) == float(p): return int(p)
    return p

"""
bs = chr(8) 
nl = chr(10) 
es = chr(27) 
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
            if l == chr(34):
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
    while ('') in px: px.remove('')
    while (':') in px: px.remove(':')
    for p in range(len(px)):
        if px[p][0] != "#":
            if cdsrt(px[p], 1) == ":":
                lenpx = len(px[p]) - 1
                if lenpx > 0:
                    px[p] = left(px[p], lenpx)
    return px[:]

def getmore(p, s):
    try:
        for t in range(1, s + 1):
            if len(p) == 1: p = []
            p = cdsrt(p, len(p) - 1)
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
            p = cdsrt(p, len(p) - 1)
        while "" in p: p.remove("")
        return p
    except: return []

p = ""
try: p = cdsrt(sys.argv, 1)[0]
except: pass
if not ".cds" in p.lower():
    if 1 == 0:
        stdout.write(nl + "    type (any) part of the command you want help on." +
        nl * 2 + "    codeschl will show all matches." + nl * 2 +"    ")
    else:
        print "using built-in demo source, translating to demo.cds.py..." ; print
        p = "demo.cds"
        inputfile = demo.replace(chr(13), "").split(nl)
else:
    try:
        inputfile = open(p).read().replace(chr(13) + chr(10), 
        chr(10)).replace(chr(13), chr(10)).split(chr(10))
    except: print "couldn't open " + chr(34) + p + chr(34) + ", exiting." ; print ; quit()
try: cdsfile = open(p + ".py", "w")
except: print "couldn't write to " + chr(34) + p + ".py" "" + chr(34) + ", exiting." ; print ; quit()
outname = p + ".py"
cdsfile.write("""#!/usr/bin/env python""" + nl)
cdsfile.write("""# coding: utf-8""" + nl)
cdsfile.write("""# codeschl translator version: """ + proginf + nl)
cdsfile.write("#" + bs + es + "[0;32m " + nl + top + "#" + bs + es + "[0;30m " + nl)
def spcl(dx):
    return chr(32) * (len(dx) - len(dx.lstrip()))
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

            if allch.lower().strip() == "esc":
                cdsfile.write(chr(32) * atleast(0, indent) + """cdsesc()""" + nl)
                allch = ""
                cdsfile.write("#" + bs + es + "[0;35m" + spcl(each) + "clear the screen" + " #" + bs + es + "[0m " + nl)
                cdsfile.write("#" + bs + es + "[0;37m" + 	each + es + "[0;30m " + nl)
                break # stop parsing this line, go to next line

            elif allch.lower().strip() == "display":
                allcd = cdsdisplay_dc(cdsrt(each, len(each) - len(allch)).strip())
                allch = "cdsdisplay(" + chr(34) + cdsrt(each, len(each) - len(allch)).strip() + chr(34) + ")"
                outverb(each, allch, allcd)
                break

            elif allch.lower().strip() in fnclist:
                mkfncname = allch.lower().strip()
                mkfncwot = getlmore(fsplit(each.lstrip()), 1)[0]
                funcp = getlmore(fsplit(each.lstrip()), 2)
                try: funcps = ", ".join(funcp)
                except: funcps = ""
                allch = "cdsfnc = " + mkfncname + "(" + funcps + ")"
                cdsfile.write(chr(32) * atleast(0, indent) + allch + nl)
                allcd = ("call function " + mkfncname + ", setting variable " + 
                mkfncwot + ", with parameters " + "(" + funcps + ")")
                allch = "if cdsfnc != None: " + mkfncwot + " = cdsfnc"
                outverb(each, allch, allcd)
                break

            #### mkfnc name variable-to-set parameter parameter etc 
            elif allch.lower().strip() == "mkfnc" and len(getmore(fsplit(each.lstrip()), 1)) > 0:
                funcname = getlmore(fsplit(each.lstrip()), 1)[0]
                funcset = getlmore(fsplit(each.lstrip()), 2)[0]
                funcp = getlmore(fsplit(each.lstrip()), 3)
                try: funcps = ", ".join(funcp)
                except: funcps = ""
                allcd = cdsmkfnc_dc(funcname, funcset, "(" + funcps + ")")

                allch = funcname + " = 0" + nl + chr(32) * atleast(0, indent)
                allch += "def " + funcname + "(" + funcps + "):"
                outverb(each, allch, allcd)

                fnclist += [funcname]
                indent += 4
                break
 
            elif allch.lower().strip() == "sleep":
                gmro = gm(cdsrt(each, len(each) - len(allch)).strip())[0]
                allch = "cdssleep(" + cdsrt(each, len(each) - len(allch)).strip() + ")"
                allcd = "wait for " + gmro + " seconds" ; outverb(each, allch, allcd)
                break # stop parsing this line, go to next line

            else:
                if (allch + " ").lstrip()[0] == "#": allcd = "this line is just a comment:"
                else: allcd = "set " + allch.strip() + " to the value of " + cdsrt(each, len(each) - len(allch)).strip() 
                allch = allch.strip() + " = " + cdsrt(each, len(each) - len(allch)).strip()
                outverb(each, allch, allcd)
                break

cdsfile.write(" #" + bs + es + "[0m " + nl)
cdsfile.close() ; p = cdssh("chmod +x " + outname)
print nl + "your program is compiled to: " + outname
print "now running: " + outname + nl
prog = nl.join(open(outname).readlines())
exec(prog)
