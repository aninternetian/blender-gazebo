import xml.etree.ElementTree as ET

# write xml file - https://stackoverflow.com/questions/3605680/creating-a-simple-xml-file-using-python

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

sdf = ET.Element('sdf', {'version': '1.6'})
model = ET.SubElement(sdf, 'model')
model.set('name', 'robot_name')     # modelName()

static = ET.SubElement(model, 'static')
static.text = 'true'    # most models are static unless specified
link = ET.SubElement(model, 'link')
link.set('name', 'body')
pose = ET.SubElement(link, 'pose')
pose.text = '0 0 0 0 0 0'   # main pose

visual = ET.SubElement(link, 'visual')
visual.set('name', 'visual')

pose = ET.SubElement(visual, 'pose')
pose.text = '0 0 0 0 0 0'   # main pose
geometry = ET.SubElement(visual, 'geometry')
mesh = ET.SubElement(geometry, 'mesh')
uri = ET.SubElement(mesh, 'uri')
uri.text = 'model://robot_name/meshes/robot.obj' #  manually fill for now

collision = ET.SubElement(link, 'collision')
collision.set('name', 'collision')

pose = ET.SubElement(collision, 'pose')
pose.text = '0 0 0 0 0 0'   # main pose
geometry = ET.SubElement(collision, 'geometry')
mesh = ET.SubElement(geometry, 'mesh')
uri = ET.SubElement(mesh, 'uri')
uri.text = 'model://robot_name/meshes/robot.obj'

tree = ET.ElementTree(sdf)
indent(sdf)
tree.write('model.sdf', xml_declaration=True, encoding='utf-8')