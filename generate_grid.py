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
imgWidth = "3.0"
imgHeight = "3.0"
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

    for i in range(columns+1):
        if i == 0:
            pathStart = "0 0 "
            pathEnd = canvasHeight
            path1 = "<path style=\"fill:none; fill-rule:evenodd; stroke:#000000;" + \
                   " stroke-width:0.001in; stroke-linecap:butt; stroke-linejoin:miter;" + \
                   " stroke-opacity:1; stroke-miterlimit:4; stroke-dasharray:none\"\n" + \
                   " d = \"M" + pathStart + "v " + str(int(pathEnd)*90) + "\"\n" + \
                   " id = \"v-path" + "-left" + "\"\n" + \
                   " inkscape:connector-curvature=\"0\"\n" + "/>\n"

            pathStart = str(int(canvasWidth)*90) + " 0 "
            pathEnd = canvasHeight
            path2 = "<path style=\"fill:none; fill-rule:evenodd; stroke:#000000;" + \
                   " stroke-width:0.001in; stroke-linecap:butt; stroke-linejoin:miter;" + \
                   " stroke-opacity:1; stroke-miterlimit:4; stroke-dasharray:none\"\n" + \
                   " d = \"M" + pathStart + " v " + str(int(pathEnd)*90-1) + "\"\n" + \
                   " id = \"v-path" + "-right" + "\"\n" + \
                   " inkscape:connector-curvature=\"0\"\n" + "/>\n"
            gridPaths += path1 + path2
        else:
            pathStart = str(i*float(imgWidth)*90) + " 0"
            pathEnd = canvasHeight
            path = "<path style=\"fill:none; fill-rule:evenodd; stroke:#000000;" + \
                   " stroke-width:0.001in; stroke-linecap:butt; stroke-linejoin:miter;" + \
                   " stroke-opacity:1; stroke-miterlimit:4; stroke-dasharray:none\"\n" + \
                   " d = \"M" + pathStart + " v " + str(int(pathEnd)*90-1) + "\"\n" + \
                   " id = \"v-path-" + str(i) + "\"\n" + \
                   " inkscape:connector-curvature=\"0\"\n" + "/>\n"
            gridPaths += path

    for i in range(rows+1):
        if i == 0:
            pathStart = "0 0 "
            pathEnd = canvasWidth
            path1 = "<path style=\"fill:none; fill-rule:evenodd; stroke:#000000;" + \
                   " stroke-width:0.001in; stroke-linecap:butt; stroke-linejoin:miter;" + \
                   " stroke-opacity:1; stroke-miterlimit:4; stroke-dasharray:none\"\n" + \
                   " d = \"M" + pathStart + "h " + str(int(pathEnd)*90) + "\"\n" + \
                   " id = \"h-path" + "-top" + "\"\n" + \
                   " inkscape:connector-curvature=\"0\"\n" + "/>\n"

            pathStart =  "0 " + str(int(canvasHeight)*90)
            pathEnd = canvasWidth
            path2 = "<path style=\"fill:none; fill-rule:evenodd; stroke:#000000;" + \
                   " stroke-width:0.001in; stroke-linecap:butt; stroke-linejoin:miter;" + \
                   " stroke-opacity:1; stroke-miterlimit:4; stroke-dasharray:none\"\n" + \
                   " d = \"M" + pathStart + " h " + str(int(pathEnd)*90-1) + "\"\n" + \
                   " id = \"h-path" + "-bot" + "\"\n" + \
                   " inkscape:connector-curvature=\"0\"\n" + "/>\n"
            gridPaths += path1 + path2
        else:
            pathStart = "M " + "0," str(i*float(width)*90)
            halfInterval = 90*float(imgWidth)/5
            mString = pathStart + str(halfInterval)+"," +  str(i*float(imgHeight)*90)
            curve = random.choice(curvesUP)
            print pathStart
            print str(halfInterval)
            print str(i*float(imgHeight)*90)
            path = "<path style=\"fill:none; fill-rule:evenodd; stroke:#000000;" + \
                   " stroke-width:0.001in; stroke-linecap:butt; stroke-linejoin:miter;" + \
                   " stroke-opacity:1; stroke-miterlimit:4; stroke-dasharray:none\"\n" + \
                   " d =  \"" + mString + curve + "\nl " + str(halfInterval*2) + \
                                curve + "\nl " + str(halfInterval*2) + ",0\"\n" + \
                   " id = \"h-path-" + str(i) + "\"\n" + \
                   " inkscape:connector-curvature=\"0\"\n" + "/>\n"
            gridPaths += path


    return gridPaths + "\n</g>\n"+ "</svg>"


f = open('' + "grid_" + colsXrows +'.svg', "w+")
f.write(generateHeader()+generatePaths())
f.close()
