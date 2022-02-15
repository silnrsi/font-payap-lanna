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
familyname=APPNAME

generated = 'generated/'

for dspace in ('',):
    designspace('source/' + APPNAME + dspace + '.designspace',
         target = '${DS:FILENAME_BASE}.ttf',
         # source = create("source/" + n + ".ufo", cmd("../tools/lannaaps -g 50 ${SRC} ${TGT}", "source/masters/" + n + ".ufo")),
         graphite = gdl(generated + '${DS:FILENAME_BASE}.gdl',
                        master = 'source/lanna.gdl',
                        make_params = '-l lastcomp --autodefines', # -m _X',
                        params = '-v4 -d -q -e gdlerr${DS:FILENAME_BASE}.txt'),
         ap = generated + '${DS:FILENAME_BASE}.xml',
         opentype = fea(generated + '${DS:FILENAME_BASE}.fea',
                        mapfile = generated + '${DS:FILENAME_BASE}.map',
                        master = 'source/lanna.feax',
                        params = '',
                        make_params = '-L lastcomp'),
         #ap_params = '-e "L=LD;U=UD;UR=URD"',       # LR != LRD
         #opentype = fea(create("srcs/{}.fea".format(f), cmd("psfmakefea -i ${SRC[2]} -c ${SRC[1]} -o ${TGT} ${SRC[0]}",
         #                                                   ['source/{}.xml'.format(f), 'source/khun_classes.xml', 'source/khun.feap'])),
         #               no_make=1),
         #        woff = woff(),
        woff = woff('web/${DS:FILENAME_BASE}.woff',
            metadata=f'../source/{familyname}-WOFF-metadata.xml'),
         fret = fret(params='-r -a ' + generated + '${DS:FILENAME_BASE}.xml'),
         version = VERSION,
         script = 'lana',
         classes = 'source/lanna_classes.xml')
