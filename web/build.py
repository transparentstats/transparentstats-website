#!/usr/bin/env python
"""
Build CSS-only (no LESS) version of website -> index.html
"""
import os
from os import path
from subprocess import call

directory = path.dirname(__file__)

#build main.css
call(("lessc", "--yui-compress", "css/main.less", "css/main.css"))

#build index.html
# replace LESS stylesheet with CSS stylesheet
for basename in ["index","chi2016/index","chi2017/index","chi2018/index"]:
    with open(basename + "-less.html", "rU") as in_:
        print "Writing " + basename
        with open(basename + ".html", "wb") as out_:
            for l in in_:
                if l == '<link rel="stylesheet/less" type="text/css" href="/css/main.less">\n':
                    out_.write('<link rel="stylesheet" type="text/css" href="/css/main.css">\n')
                elif l == '<script type="text/javascript" src="/js/less.js"></script>\n':
                    pass
                else:
                    out_.write(l)


