#!/usr/bin/python3
import json
import os, sys, re
import requests

HISTFILE = sys.argv[1]
URL      = "https://ss.luoruiyao.cn/api/upload_cmd_stat.php"
REG = r"^[\s]*([^\s]*).*$"
SEL = r"^.*CmdStat(.py)?\s[\S]*$"

f = open(HISTFILE, 'r')
lines = f.readlines()
f.close()

CMDS  = {}
for i in range(len(lines)-1, -1, -1):
    line = lines[i]
    if re.search(SEL,line):
        break
    elif len(line):
        cmds  = re.findall(REG, line)
        for cmd in cmds:
            try:
                CMDS[cmd] += 1
            except KeyError:
                CMDS[cmd] = 1
    else: continue

r = requests.post(URL, json={"content": CMDS})

f = open(HISTFILE, 'a+')
f.write('%s %s'%(sys.argv[0], sys.argv[1]))
f.close()