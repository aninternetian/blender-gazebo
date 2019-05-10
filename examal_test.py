import xml.etree.cElementTree as ET
from ElementTree_pretty import prettify     # used for testing

# write xml file - https://stackoverflow.com/questions/3605680/creating-a-simple-xml-file-using-python

sdf = ET.Element('sdf', {'version': '1.6'})
model = ET.SubElement(sdf, 'model')

model.set('name', 'default')    # model.append(robot_name)

tree = ET.ElementTree(sdf)
prettify(tree).write('model.sdf')