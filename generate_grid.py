#import svgwrite
#from svgwrite import inch
import xml.etree.ElementTree as ET
import random
from random import shuffle

imgWidth = "2.2"
imgHeight = "2.2"
canvasWidth = "15"
canvasHeight = "15"

unit = "in"

columns = int(int(canvasWidth)//(float(imgWidth)))
rows = int(int(canvasHeight)//(float(imgHeight)))
colsXrows = str(columns)+"x"+str(rows)
canvasWidth2 = str(float(canvasWidth)-float(imgWidth)/2)
canvasHeight2 = str(float(canvasHeight)-float(imgHeight)/2)

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
    gridPaths = "<g inkscape:label=\"Layer 1\"\n" + \
                " inkscape:groupmode=\"layer\"\n" + \
                " id=\"layer1\"\n" + \
                " transform=\"translate(0,0)\">\n"
    tracker = 0
    for i in range(0, rows+1):
        for j in range(1, columns+2):
            if tracker%2 == 0:
                pathH = '''
                    c 7.61591,1.56165 31.15693,3.54295 42.14933,3.54746 13.46822,0.005 21.80173,-1.08379 26.93813,-3.52117 7.16802,-3.40145 9.22223,-13.60951 6.06204,-30.12437 -0.8249,-4.31088 -1.4999,-10.61594 -1.5,-14.01124 -1.4e-4,-5.20488 0.41174,-6.6628 2.62562,-9.29385 5.05723,-6.01018 16.19596,-9.55525 24.90861,-7.92755 5.54779,1.03644 7.1891,1.90658 10.84701,5.7505 4.37874,4.6014 5.62754,10.98658 4.55689,23.29947 -2.05093,23.58643 3.82366,33.65435 21.5617,36.95267 8.66209,1.61068 33.51739,0.52118 48.31367,-2.11778 6.77252,-1.20789 12.49535,-2.0145 12.71739,-1.79246"
                     id="UP"
                     inkscape:connector-curvature="0"
                     sodipodi:nodetypes="ccsssssssssc"
                     inkscape:label="#path4161" />'''
                pathV = '''
                    c -1.5617,7.61591 -3.543,31.15693 -3.5475,42.14933 0,13.46822 1.0838,21.80173 3.5212,26.93813 3.4014,7.16802 13.60949,9.22223 30.12435,6.06204 4.31088,-0.8249 10.61594,-1.4999 14.01124,-1.5 5.20488,-1.4e-4 6.6628,0.41174 9.29385,2.62562 6.01018,5.05723 9.55525,16.19596 7.92755,24.90862 -1.03644,5.54779 -1.90658,7.1891 -5.7505,10.84701 -4.6014,4.37874 -10.98658,5.62754 -23.29947,4.55689 -23.58642,-2.05093 -33.65432,3.82361 -36.95262,21.56171 -1.6107,8.6621         -0.5212,33.5174 2.1177,48.3137 1.2079,6.7725 2.0145,12.4953 1.7925,12.7173"
                     id="RIGHT"
                     inkscape:connector-curvature="0"
                     sodipodi:nodetypes="ccsssssssssc"
                     inkscape:label="#path4161" />'''
            else:
                pathH = '''
                    c 7.61591,-1.56165 31.15693,-3.54295 42.14933,-3.54746 13.46822,-0.005 21.80173,1.08379 26.93813,3.52117 7.16802,3.40145 9.22223,13.60951 6.06204,30.12437 -0.8249,4.31088 -1.4999,10.61594 -1.5,14.01124 -1.4e-4,5.20488 0.41174,6.6628 2.62562,9.29385 5.05723,6.01018 16.19596,9.55525 24.90862,7.92755 5.54779,-1.03644 7.1891,-1.90658 10.84701,-5.7505 4.37874,-4.6014 5.62754,-10.98658 4.55689,-23.29947 -2.05093,-23.58643 3.82366,-33.65435 21.5617,-36.95267 8.66209,-1.61068 33.51739,-0.52118 48.31367,2.11778 6.77252,1.20789 12.49535,2.0145 12.71739,1.79246"
                     id="DOWN"
                     inkscape:connector-curvature="0"
                     sodipodi:nodetypes="ccsssssssssc"
                     inkscape:label="#path4161" />'''
                pathV = '''
                    c 1.5617,7.61591 3.543,31.15693 3.5475,42.14933 0,13.46822 -1.0838,21.80173 -3.5212,26.93813 -3.4014,7.16802 -13.60949,9.22223 -30.12435,6.06204 -4.31088,-0.8249 -10.61594,-1.4999 -14.01124,-1.5 -5.20488,-1.4e-4 -6.6628,0.41174 -9.29385,2.62562 -6.01018,5.05723 -9.55525,16.19596 -7.92755,24.90862 1.03644,5.54779 1.90658,7.1891 5.7505,10.84701 4.6014,4.37874 10.98658,5.62754 23.29947,4.55689 23.58642,-2.05093 33.65432,3.82361 36.95262,21.56171 1.6107,8.6621 0.5212,33.5174 -2.1177,48.3137 -1.2079,6.7725 -2.0145,12.4953 -1.7925,12.7173"
                     id="LEFT"
                     inkscape:connector-curvature="0"
                     sodipodi:nodetypes="ccsssssssssc"
                     inkscape:label="#path4161" />'''
            if(i==0 and j==1):
                pathLeft = "<path style=\"fill:none; fill-rule:evenodd; stroke:#000000;" + \
                       " stroke-width:0.001in; stroke-linecap:butt; stroke-linejoin:miter;" + \
                       " stroke-opacity:1; stroke-miterlimit:4; stroke-dasharray:none\"\n" + \
                       " d = \"M 0 0 v " + str(float(canvasHeight)*90) + " \"\n" + \
                       " id = \"v-path" + "-left" + "\"\n" + \
                       " inkscape:connector-curvature=\"0\"\n" + "/>\n"
                gridPaths += pathLeft
                pathBottom = "<path style=\"fill:none; fill-rule:evenodd; stroke:#000000;" + \
                       " stroke-width:0.001in; stroke-linecap:butt; stroke-linejoin:miter;" + \
                       " stroke-opacity:1; stroke-miterlimit:4; stroke-dasharray:none\"\n" + \
                       " d = \"M 0 0 h " + str(float(canvasHeight)*90) + " \"\n" + \
                       " id = \"h-path" + "-bottom" + "\"\n" + \
                       " inkscape:connector-curvature=\"0\"\n" + "/>\n"
                gridPaths += pathBottom
                pathTop = "<path style=\"fill:none; fill-rule:evenodd; stroke:#000000;" + \
                       " stroke-width:0.001in; stroke-linecap:butt; stroke-linejoin:miter;" + \
                       " stroke-opacity:1; stroke-miterlimit:4; stroke-dasharray:none\"\n" + \
                       " d = \"M 0 " + str(float(canvasHeight)*90) + \
                            "  h " + str(float(canvasHeight)*90) + " \"\n" + \
                       " id = \"h-path" + "-top" + "\"\n" + \
                       " inkscape:connector-curvature=\"0\"\n" + "/>\n"
                gridPaths += pathTop
                pathRight = "<path style=\"fill:none; fill-rule:evenodd; stroke:#000000;" + \
                       " stroke-width:0.001in; stroke-linecap:butt; stroke-linejoin:miter;" + \
                       " stroke-opacity:1; stroke-miterlimit:4; stroke-dasharray:none\"\n" + \
                       " d = \"M " + str(float(canvasHeight)*90) + \
                            " 0 v " + str(float(canvasHeight)*90) + " \"\n" + \
                       " id = \"v-path" + "-right" + "\"\n" + \
                       " inkscape:connector-curvature=\"0\"\n" + "/>\n"
                gridPaths += pathRight

            xy = str(90*float(imgWidth)*i) + "," + str(90*float(canvasHeight)-j*90*float(imgHeight))
            pathHorizontal = '''
                        <path
                           style="fill:none;fill-rule:evenodd;
                           stroke:#000000;stroke-width:0.00096099in;
                           stroke-linecap:butt;stroke-linejoin:miter;
                           stroke-miterlimit:4;stroke-dasharray:none;
                           stroke-opacity:1"
                        ''' + \
                        " d = \"m " + xy + pathH
            gridPaths += pathHorizontal

            xy = str(90*float(imgWidth)*i) + "," + str(90*float(canvasHeight)-j*90*float(imgHeight))
            pathVertical = '''
                        <path
                           style="fill:none;fill-rule:evenodd;
                           stroke:#000000;stroke-width:0.00096099in;
                           stroke-linecap:butt;stroke-linejoin:miter;
                           stroke-miterlimit:4;stroke-dasharray:none;
                           stroke-opacity:1"
                        ''' + \
                        " d = \"m " + xy + pathV
            gridPaths += pathVertical
            tracker += 1
    return gridPaths + "\n</g>\n"+ "</svg>"


f = open('' + "grid_" + colsXrows +'.svg', "w+")
f.write(generateHeader()+generatePaths())
f.close()
