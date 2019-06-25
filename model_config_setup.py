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

tree = ET.ElementTree(model)
indent(model)
tree.write('model.config', xml_declaration=True, encoding='utf-8')