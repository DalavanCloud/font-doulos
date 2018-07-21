#!/usr/bin/python
# this is a smith configuration file

# set the default output folders
out="results"
DOCDIR="documentation"
OUTDIR="installers"
ZIPDIR="releases"
STANDARDS = 'standards'

# set the font name, version, licensing and description
APPNAME="DoulosSIL"
FILENAMEBASE="DoulosSIL"
VERSION="6.000"
TTF_VERSION="6.000"
COPYRIGHT="Copyright (c) 2007-2018, SIL International (http://www.sil.org)"
LICENSE='OFL.txt'

DESC_SHORT = "Unicode font for Roman- and Cyrillic-based writing systems"
DESC_LONG = """
DoulosSIL is a Unicode font for Roman- and Cyrillic-based writing systems
Font sources are published in the repository and a smith open workflow is
used for building, testing and releasing.
"""
DESC_NAME = "DoulosSIL"
DEBPKG = 'fonts-sil-Doulos'

# set the build and test parameters

for style in ['-Regular'] :
    fname = FILENAMEBASE + style
    source_fname = 'source/' + fname
    feabase = 'source/opentype/' + FILENAMEBASE
    font( target = process(fname + '.ttf', name(FILENAMEBASE, lang='en-US', subfamily=(style[1:])),
            cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', [source_fname + '.ufo'])),
        source = source_fname + '.ufo',
        version = VERSION,
        ap =  source_fname +'_ap' + '.xml',
        opentype = fea(source_fname + '.fea',
            master = feabase + style + '.fea',
            make_params="--omitaps 'C L11 L12 L13 L21 L22 L23 L31 L32 L33 C11 C12 C13 C21 C22 C23 C31 C32 C33 U11 U12 U13 U21 U22 U23 U31 U32 U33'",
            depends = (feabase + '_gsub.fea', feabase + style + '_gpos_lkups.fea', feabase + '_gpos_feats.fea', feabase + '_gdef.fea')
            ),
        graphite = gdl(source_fname + '.gdl',
            master = 'source/graphite/main.gdh', params = '-e gdlerr' + style + '.txt',
                      ),
        license = ofl('DoulosSIL','SIL'),
        woff = woff()
        )
