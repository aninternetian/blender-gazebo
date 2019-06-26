'''model.config setup'''

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

model = ET.Element('model')
name = ET.SubElement(model, 'name')
# name.text = model_name())     # retrieve from common_functions.py
name.text = 'file_name'

version = ET.SubElement(model, 'version')
version.text = '1.0'

sdf = ET.SubElement(model, 'sdf')
sdf.set('version' , '1.6')
sdf.text = 'model.sdf'

# section for author

author = ET.SubElement(model, 'author')

name = ET.SubElement(author, 'name')
name.text = 'Name'  # retrieve name from local file (user need to create file for name)

email = ET.SubElement(author, 'email')
email.text = 'email@email.com'  # retrieve email from local file as well

description = ET.SubElement(model, 'description')
description.text = 'description about the model'    # retrieve from field in blender addon

tree = ET.ElementTree(model)
indent(model)
tree.write('model.config', xml_declaration=True, encoding='utf-8')