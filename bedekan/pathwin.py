#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import random
from appJar import gui
import numpy as np

app = gui()
app.setGeometry("fullscreen")
score = []
f = open("../datas.txt", "r")
datas = f.readlines()

def path_write():
    f = open("..\datas.txt", "w")
    f.write("samantha\n")
    f.write("evan\n")
    f.write("hutomo\n")
    f.close()

# def tampilan(data):
#     bun = data

def path_read():
    # a = datas[2].split()
    # print("total data : " + str(len(datas)))
    # rand_qlist = random.sample(datas, len(datas))
    # random.shuffle(rand_qlist);

    bun = loadandrand().split("-")

    # for i in rand_qlist:
    #     bun = i.split()
    #
    #     txtinput = raw_input("press enter to reveal %s, %s kanji : " % (str(bun[1]), str(bun[3]))).lower().strip()
    #     print(str(bun[0]))

    # bun = rand_qlist[0].split()

    # raw_input("press enter to reveal")
    # print(str(bun[0]))
    app.setFont(60)
    app.addLabel("romaji", str(bun[1]), row=0, column=0, rowspan=0, colspan=0)
    app.setLabelBg("romaji", "white")
    app.setLabelFg("romaji", "black")
    app.addLabel("meaning", str(bun[2]), row=1, column=0, rowspan=0, colspan=0)
    app.setLabelBg("meaning", "white")
    app.setLabelFg("meaning", "black")
    app.addLabel("kanji", str(bun[0]), row=0, column=1, rowspan=2, colspan=0)
    app.setLabelBg("kanji", "white")
    app.setLabelFg("kanji", "white")
    app.setLabelOverFunction("kanji", [showtext, hidetext])
    app.setLabelOverFunction("meaning", [showtext, hidetext])
    app.setLabelOverFunction("romaji", [showtext, hidetext])

    app.addLabel("RESET", "RESET", row=2, column=0, rowspan=0, colspan=2)
    app.setLabelBg("RESET", "grey")
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
    random.shuffle(rand_qlist);
    return rand_qlist[0]

def resetlabel(wdgt):
    bun = loadandrand().split("-")
    if len(bun) != 1:
        app.setLabel("romaji", str(bun[1]))
        app.setLabel("meaning", str(bun[2]))
        app.setLabel("kanji", str(bun[0]))
