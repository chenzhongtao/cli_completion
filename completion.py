#!/usr/bin/env python
# coding=utf-8


import os
import sys
import json
import logging


jsonpath = "/etc/mycompletion"


logger=logging.getLogger()
handler=logging.FileHandler("/var/log/messages")
logger.addHandler(handler)
logger.setLevel(logging.NOTSET)

def main():
    logger.info("sys.argv: %s",sys.argv)
    if len(sys.argv)<2:
        return
    filename = sys.argv[1]+".json"
        
    jsonfile = os.path.join(jsonpath,filename)
        
    fd = open(jsonfile,"r")
    s1 = fd.read()
    json1 = json.loads(s1)
    fd.close()
    
    subcmd = json1
    for i in range(2, len(sys.argv)-1):
        if isinstance(subcmd,dict):
            if subcmd.has_key(sys.argv[i]):
                if sys.argv[i].startswith("--"):
                    subcmd.pop(sys.argv[i])
                else:
                    subcmd = subcmd[sys.argv[i]]
            else:
                continue
        elif isinstance(subcmd,list):
            if sys.argv[i] in subcmd:
                subcmd.remove(sys.argv[i])
            if sys.argv[i]+"=" in subcmd:
                subcmd.remove(sys.argv[i]+"=")
            else:
                continue
        else:
            return
    if isinstance(subcmd,dict):
        options = subcmd.keys()
    elif isinstance(subcmd,list):
        options = subcmd
    else:
        return
    for key in options:
        if key.startswith(sys.argv[-1]) or sys.argv[-1] == "*":
            print key


if __name__ == "__main__":
    sys.exit(main())


