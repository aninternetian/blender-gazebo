import xml.etree.ElementTree as ET

tree = ET.parse('HCR-5.sdf')
root = tree.getroot()

vis_name = root.find("./model/link/visual[@name='j1']")
vis_name.attrib["name"] = "Hospi"
print(vis_name.attrib)
# print(test)