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

curvesUp = ['''
c 35.7581,-0.68267 63.72637,6.39695 54.72625,-16.57489 -15.72317,-40.13164 35.25937,-52.78228 22.91384,0.16167 -6.41467,27.50944 42.91196,16.62166 44.76546,16.04597"
id="h-path-3"
inkscape:connector-curvature="0"
sodipodi:nodetypes="cssc" />''',

'''
c 20.09073,-2.58723 76.2504,-1.51451 50.42293,-21.25338 -17.63388,-13.47686 33.52009,-47.1489 20.05825,-5.06398 -11.44108,35.76753 49.79557,26.29418 49.93846,26.22837"
id="h-path-4"
inkscape:connector-curvature="0"
sodipodi:nodetypes="cssc" />'''   ,

'''
c 13.12253,-1.7362 63.95988,7.46198 55.4026,-15.19551 -10.40114,-27.53946 34.99949,-25.51452 14.06173,-4.83315 -19.23617,19.00062 48.65193,19.96716 52.15725,19.96325"
id="h-path-5"
inkscape:connector-curvature="0"
sodipodi:nodetypes="cssc" />''',

'''
c 23.17049,-0.56907 64.79681,4.92371 58.521,-18.4949 -23.38396,-52.90541 26.73447,-5.20324 18.63611,2.88633 -18.88235,18.86186 39.10093,15.22492 42.81962,15.6325"
id="h-path-6"
inkscape:connector-curvature="0"
sodipodi:nodetypes="ccsc" />''',
'''
c 18.19946,0.91231 45.48344,-2.99776 50.52869,-19.92224 9.77893,-39.74546 49.13351,-24.86452 18.89912,-5.06411 -32.99346,21.60731 42.39691,24.95945 50.85923,25.01678"
id="h-path-2-6"
inkscape:connector-curvature="0"
sodipodi:nodetypes="ccsc" />
''']

curvesRight = ['''
c 0.27496,-27.03449 5.83815,-48.2699 19.42526,-51.6031 39.74556,-9.75042 24.8646,-48.98992 5.06414,-18.84388 -21.60738,32.89704 -27.00862,-43.09661 -25.03631,-51.16624"
id="h-path-2-1"
inkscape:connector-curvature="0"
sodipodi:nodetypes="cssc" />''',
'''
c 0.68267,-35.7581 -6.90631,-65.73258 16.06553,-56.73246 40.13164,15.72317 52.78228,-35.25937 -0.16167,-22.91384 -27.50944,6.41467 -16.92544,-41.13994 -16.34975,-42.99344"
id="h-path-3-9"
inkscape:connector-curvature="0"
sodipodi:nodetypes="cssc" />
''',
'''
c 2.58723,-20.09073 1.58611,-76.7516 21.32498,-50.92413 13.47686,17.63388 47.1489,-33.52009 5.06398,-20.05825 -35.76753,11.44108 -26.29418,-49.79557 -26.22837,-49.93846"
id="h-path-4-4"
inkscape:connector-curvature="0"
sodipodi:nodetypes="cssc" />
''',
'''
c 1.7362,-13.12253 -7.53792,-63.04855 15.11957,-54.49127 27.53946,10.40114 25.51452,-34.99949 4.83315,-14.06173 -19.00062,19.23617 -21.09366,-48.96836 -21.08975,-52.47368"
id="h-path-5-2"
inkscape:connector-curvature="0"
sodipodi:nodetypes="cssc" />
''',
'''
c 0.56907,-23.17049 -4.92371,-64.79681 18.4949,-58.521 52.90541,23.38396 5.20324,-26.73447 -2.88633,-18.63611 -18.86186,18.88235 -15.43972,-40.67614 -15.8473,-44.39483"
id="h-path-6-3"
inkscape:connector-curvature="0"
sodipodi:nodetypes="ccsc" />''' ]

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
    for i in range(1, rows):
        for j in range(1, columns):
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
