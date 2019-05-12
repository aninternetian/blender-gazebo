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

model.set('name', 'robot_name')    # model.append()

tree = ET.ElementTree(sdf)
indent(sdf)
tree.write('model.sdf', xml_declaration=True, encoding='utf-8')