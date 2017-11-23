#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import random
from appJar import gui

app = gui()
app.setGeometry("fullscreen")
hadread = []
f = open("../datas2.txt", "r")
datas = f.readlines()


def path_read():
    bun = loadandrand().split("-")

    app.setFont(60)
    app.addLabel("romaji", str(bun[2]), row=0, column=0, rowspan=0, colspan=0)
    app.setLabelBg("romaji", "white")
    app.setLabelFg("romaji", "black")
    app.addLabel("meaning", str(bun[3]), row=1, column=0, rowspan=0, colspan=0)
    app.setLabelBg("meaning", "white")
    app.setLabelFg("meaning", "black")
    app.addLabel("kanji", str(bun[1]), row=0, column=1, rowspan=2, colspan=0)
    app.setLabelBg("kanji", "white")
    app.setLabelFg("kanji", "white")
    app.setLabelOverFunction("kanji", [showtext, hidetext])
    app.setLabelOverFunction("meaning", [showtext, hidetext])
    app.setLabelOverFunction("romaji", [showtext, hidetext])

    app.addLabel("RESET", "RESET", row=2, column=0, rowspan=0, colspan=2)
    app.setLabelBg("RESET", "grey")
    hadread.append(bun[0]+"-"+bun[1]+"-"+bun[2]+"-"+bun[3])
    app.setLabelSubmitFunction("RESET", resetlabel)
    app.go()

def hidetext(wdgt):
    app.setLabelBg("kanji", "white")
    app.setLabelFg("kanji", "white")

def showtext(wdgt):
    app.setLabelBg("kanji", "white")
    app.setLabelFg("kanji", "black")

def loadandrand():
    rand_qlist = random.sample(datas, len(datas))
    new_qlist = [val for val in rand_qlist if val not in hadread]
    if len(new_qlist) == 0:
        app.stop()
    else:
        random.shuffle(new_qlist);
        return new_qlist[0]

def resetlabel(wdgt):
    if len(hadread) == len(datas):
        app.stop()
    else:
        bun = loadandrand().split("-")
        if len(bun) != 1:
            app.setLabel("romaji", str(bun[2]))
            app.setLabel("meaning", str(bun[3]))
            app.setLabel("kanji", str(bun[1]))
            hadread.append(bun[0] + "-" + bun[1] + "-" + bun[2] + "-" + bun[3])
