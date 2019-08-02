import xml.etree.ElementTree as ET

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

def get_pose(): 
    return '0 0 0 0 0 0'

def uri_location():
    # uri.text = 'model://'
    # model_name()/meshes/model_name().obj
    return 'model://robot_name/meshes/robot.obj' #  fill manually for now

def vis_col_container():
    mesh = ET.SubElement(geometry, 'mesh')
    uri = ET.SubElement(mesh, 'uri')
    uri.text = uri_location()

sdf = ET.Element('sdf', {'version': '1.6'})
model = ET.SubElement(sdf, 'model')
# model.set('name', model_name())     # retrieve from common_functions.py
model.set('name', 'file_name')

static = ET.SubElement(model, 'static')
static.text = 'true'    # modelled assets are static unless specified
link = ET.SubElement(model, 'link')
link.set('name', 'body')
pose = ET.SubElement(link, 'pose')
pose.text = '0 0 0 0 0 0'

# visual
visual = ET.SubElement(link, 'visual')
visual.set('name', 'visual')

pose = ET.SubElement(visual, 'pose')
pose.text = get_pose()
geometry = ET.SubElement(visual, 'geometry')
vis_col_container()

# collision
collision = ET.SubElement(link, 'collision')
collision.set('name', 'collision')

pose = ET.SubElement(collision, 'pose')
pose.text = get_pose()
geometry = ET.SubElement(collision, 'geometry')
vis_col_container()

tree = ET.ElementTree(sdf)
indent(sdf)
tree.write('model.sdf', xml_declaration=True, encoding='utf-8')