#!/usr/bin/python
# encoding: utf-8
# this is a smith configuration file

APPNAME = "PayapLanna"

# set some default output folders (most are already set by default)
DOCDIR = ["documentation", "web"]
STANDARDS = 'tests/reference'

# set the font name and description
DESC_SHORT = "A font for the Lanna script."
TEXTSIZE = 20

getufoinfo("source/masters/PayapLanna-Regular.ufo")
BUILDLABEL = "alpha"
fontfamily=APPNAME


for weight in ('-Regular','-Bold') :
    font(target = fontfamily + weight + ".ttf",
         source = "source/masters/" + fontfamily + weight + ".ufo",
         graphite = gdl('generated/' + fontfamily + '.gdl',
                        master='source/' + fontfamily + '.gdl',
                        make_params="-l lastcomp --autodefines",
                        params='-v2 -d -q -e gdlerr' + weight + '.txt' ),
         ap = 'source/' + fontfamily + '.xml',
         #ap_params = '-e "L=LD;U=UD;UR=URD"',       # LR != LRD
         #opentype = fea(create("srcs/{}.fea".format(f), cmd("psfmakefea -i ${SRC[2]} -c ${SRC[1]} -o ${TGT} ${SRC[0]}",
         #                                                   ['source/{}.xml'.format(f), 'source/khun_classes.xml', 'source/khun.feap'])),
         #               no_make=1),
         #        woff = woff(),
         fret = fret(),
         version = VERSION,
         script = 'lana',
         classes = 'source/lanna_classes.xml')
