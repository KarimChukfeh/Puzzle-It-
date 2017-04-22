#import svgwrite
#from svgwrite import inch
import xml.etree.ElementTree as ET
import random

#sourceDir = 'scaled_svgs/'

#picTree = ET.parse(sourceDir + '1.svg')
#picRoot = picTree.getroot()

#imgWidth = picRoot.attrib['width'][:-2]
#imgHeight = picRoot.attrib['height'][:-2]
#imgMargin = 0.002


imgMargin = "0.002"

'''
PLAY W/THESE 4 PARAMETERS
'''
imgWidth = "3.7"
imgHeight = "3.7"
canvasWidth = "25"
canvasHeight = "25"

#canvasWidth = "22"
#canvasHeight = "11"

#unit = picRoot.attrib['height'][-2:] #inches

unit = "in"

columns = int(int(canvasWidth)//(float(imgWidth)+float(imgMargin)))
rows = int(int(canvasHeight)//(float(imgHeight)+float(imgMargin)))
colsXrows = str(columns)+"x"+str(rows)

curvesUP = [''' \nc 35.013,-0.0629 61.99073,-2.28755 46.25437,-31.19439 -30.40911,-55.85986 67.13537,-50.55814 57.79004,-11.58819 -12.81648,53.44464 37.07772,40.02245 44.57986,41.40599 ''',
        ''' \nc 35.01301,-0.0629 71.03413,-9.53331 46.25438,-31.19439 -97.828676,-85.51639 78.1699,-71.51873 57.79004,-11.58819 -17.69445,52.03363 37.07772,40.02245 45.82879,40.71422 ''',
        ''' \nc 35.013,-0.0629 59.91289,-1.24972 46.25437,-31.19439 -26.46642,-58.02447 126.89756,-83.36875 57.79004,-11.58819 -38.11833,39.59273 37.07772,40.02245 44.57986,41.40599 ''' ,
        ''' \nc 35.013,-0.0629 71.78687,-10.42591 46.25437,-31.19439 -35.15126,-28.59252 66.87605,-49.06706 57.79004,-11.58819 -12.94886,53.41272 37.07772,40.02245 45.82879,40.71422 ''',
        ''' \nc 35.013,-0.0629 57.00994,5.8207 50.48222,-26.43806 -13.80724,-68.23282 100.25915,-67.84318 41.9356,-11.0597 -39.37897,38.33913 48.70428,34.73763 56.20648,36.12117 ''',
        ''' \nc 38.219,-0.73081 81.8561,-6.65234 46.2543,-31.19439 -51.8606,-35.74999 109.7698,-58.12639 66.7587,0.36998 -32.5572,44.27886 28.1091,28.06428 36.8602,28.75605 ''',
        ''' \nc 35.016,-0.0643 100.5326,-9.37668 46.2543,-31.19439 -53.4717,-21.49348 101.9674,-55.48201 57.7901,-11.58819 -38.9874,38.73724 37.0777,40.02245 44.5798,41.40599 ''']

'''  <path
           style="fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:0.00096099in;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           d="M 0.03569412,285.90326 C 37.912144,287.54979 155.11002,270.06953 142.49678,240.12384 118.0558,182.09738 259.8183,156.89358 195.86421,228.53525 c -35.39911,39.65426 123.55364,65.19187 143.59314,57.28368"
           id="h-path-2"
           inkscape:connector-curvature="0"
           sodipodi:nodetypes="cssc" />'''

curves2UP = ['''
 c 98.3169,-21.95184 178.24682,14.93883 152.76781,-37.6291 -44.51166,-91.8358 99.81787,-120.78511 64.86817,0.36998 -18.15969,62.95161 116.57142,39.28789 121.81862,37.97054"
id="h-path-003"
inkscape:connector-curvature="0"
sodipodi:nodetypes="cssc" />''',

'''
 c 48.6553,0.79401 215.6431,-3.50535 142.305,-48.675 -50.0721,-30.83996 95.1816,-107.89372 56.9562,-11.58823 -32.4874,81.84907 141.49301,61.4489 140.61321,60.26997"
id="h-path-004"
inkscape:connector-curvature="0"
sodipodi:nodetypes="cssc" />'''   ,

'''
 c 33.216,-0.063 177.2317,16.71459 153.0215,-35.13401 -29.4268,-63.02033 99.0201,-58.38662 39.7833,-11.06001 -54.4227,43.48032 139.055,44.11883 146.1872,45.50237"
id="h-path-005"
inkscape:connector-curvature="0"
sodipodi:nodetypes="cssc" />''',

'''
 c 37.1864,-0.033 187.8483,4.40932 165.771,-45.45327 -27.3125,-61.6864 88.3127,-63.10268 61.3904,-12.31013 -42.2357,79.6831 103.8432,57.05312 111.8323,58.10935"
id="h-path-006"
inkscape:connector-curvature="0"
sodipodi:nodetypes="cssc" />'''
]

def generateHeader():
    gridHeader = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\n<svg\n" \
    + " width=\"" + canvasWidth+unit + "\"\n" \
    + " height=\""+ canvasHeight+unit + "\"\n" \
    +  " viewBox=\"0 0 " + canvasWidth+unit + " " + canvasHeight+unit +"\"\n" \
    +   " id=\"svgGrid" + colsXrows + "\"\n" \
    +  " version=\"1.1\" inkscape:version=\"0.91 r13725\"\n" \
    +  " sodipodi:docname=\"grid_" + colsXrows + ".svg\"" + "\n>\n"

    return gridHeader

def generatePaths():
    verticalPats = ""
    horizontalPaths = ""

    gridPaths = "<g inkscape:label=\"Layer 1\"\n" + \
                " inkscape:groupmode=\"layer\"\n" + \
                " id=\"layer1\"\n" + \
                " transform=\"translate(0,0)\">\n"

    for i in range(rows):
        for j in range(columns):
            xy = str(90*float(imgWidth)*i) + "," + str(j*90*float(imgHeight))
            path = '''
                        <path
                           style="fill:none;fill-rule:evenodd;
                           stroke:#000000;stroke-width:0.00096099in;
                           stroke-linecap:butt;stroke-linejoin:miter;
                           stroke-miterlimit:4;stroke-dasharray:none;
                           stroke-opacity:1"
                        ''' + \
                        " d = \"m " + xy + " " + random.choice(curves2UP)

            gridPaths += path

    return gridPaths + "\n</g>\n"+ "</svg>"


f = open('' + "grid_" + colsXrows +'.svg', "w+")
f.write(generateHeader()+generatePaths())
f.close()
