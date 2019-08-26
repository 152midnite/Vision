import sys
import re
from xml.etree.ElementTree import Element, SubElement as subelement, Comment, tostring, ElementTree
from xml.etree import ElementTree
from xml.dom import minidom

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ")


def toxml(coords,path,shape=[0,0,3],object_name='licence plate'):
    fname = path.split('/')[-1]
    directory = path.split('/')[-2]
    root = Element('annotation')
    folder = subelement(root, 'folder')
    folder.text = directory
    filename = subelement(root,'filename')
    filename.text = fname
    xmlpath = subelement(root,'path')
    xmlpath.text = path
    source = subelement(root,'source')
    database = subelement(source,'database')
    database.text = 'na'
    size = subelement(root,'size')
    width = subelement(size,'width')
    width.text = str(shape[1])
    height = subelement(size,'height')
    height.text = str(shape[0])
    depth = subelement(size, 'depth')
    try:
        depth.text = str(shape[2])
    except IndexError:
        depth.text = 0
    segmented = subelement(root,'segmented')
    segmented.text = '0'
    objct = subelement(root,'object')
    name = subelement(objct,'name')
    name.text = 'license plate'
    pose = subelement(objct,'pose')
    pose.text = 'Frontal'
    truncated = subelement(objct,'truncated')
    truncated.text = '0'
    difficult = subelement(objct,'difficult')
    difficult.text = '0'
    occluded = subelement(objct,'occulded')
    occluded.text = '0'
    bndbox = subelement(objct,'bndbox')
    xmin = subelement(bndbox, 'xmin')
    xmin.text = str(coords[0])
    xmax = subelement(bndbox, 'xmax')
    xmax.text = str(coords[2])
    ymin = subelement(bndbox, 'ymin')
    ymin.text = str(coords[1])
    ymax = subelement(bndbox, 'ymax')
    ymax.text = str(coords[3])
    return root

def writexml(xml,name,path):
    xml = prettify(xml)
    with open('{}{}.xml'.format(path,name),'wt') as out:
        out.write(xml)



    


