'''
Using this as a sample of how SDF is generate from svg.py.
Extracting stuff which I might use.
My code will be very diff since i'm using stuff from blender
'''

# import numpy as np
# from collections import namedtuple
# import StringIO
# import warnings
# import yaml
from xml.etree.ElementTree import ElementTree, Element, SubElement

# blender has no xml parsing? - https://blenderartists.org/t/xml-parsing/383339


# visual or collision tag
def generate_geometric_sdf(vis_or_col, name, material):
    container = Element(vis_or_col)
    container.set('name', name)
    geometry = SubElement(container, 'geometry')

    if vis_or_col == 'visual':
        if material is not None:
            container.append(material)

    return container, geometry

# model tag
def generate_model_sdf(name, static=True):
    model = Element('model')
    model.set('name', name)

    if static:
        static_elem = SubElement(model, 'static')
        static_elem.text = 'true'

    return model

# retrieve location of models, etc
def generate_include_uri_sdf(uri):
    include = Element('include')
    uri_elem = SubElement(include, 'uri')
    uri_elem.text = uri
    return include

def generate_imported_model_sdf(name, uri, pose_arrow,
                                offset_x=0.0, offset_y=0.0, offset_z=0.0,
                                roll=0.0, pitch=0.0, yaw=0.0,
                                scale=1.0, static=True, random_bounds=None):
    include = Element('include')
    name_elem = SubElement(include, 'name')
    name_elem.text = name

    if static:
        static_elem = SubElement(include, 'static')
        static_elem.text = 'true'

    uri_elem = SubElement(include, 'uri')
    uri_elem.text = uri

    pose = SubElement(include, 'pose')
    x, y, yaw = arrow_to_pose(pose_arrow, yaw, scale)
    z = offset_z

    x += offset_x*np.cos(yaw) + offset_y*np.sin(yaw)
    y += -offset_x*np.sin(yaw) + offset_y*np.cos(yaw)

# don't think i need to use rand bounds as mine is not from SVG

    if random_bounds is not None:

        def get_rand(i):
            return np.random.random(1).item(0) * (random_bounds[1][i] - random_bounds[0][i]) + random_bounds[0][i]

        x += get_rand(0)
        y += get_rand(1)
        z += get_rand(2)
        roll += get_rand(3)
        pitch += get_rand(4)
        yaw += get_rand(5)

    pose.text = '{0} {1} {2} {3} {4} {5}'.format(x, y, z, roll, pitch, yaw)

    return include

def element_to_text(elem):
    output = StringIO.StringIO()
    tree = ElementTree(elem)
    tree.write(output)
    output.seek(0)
    output_str = ''
    for text_line in output.readlines():
        output_str += '\n' + text_line
    return output_str

def add_imported_models(world, doc, group_filter_substr, uri,
                        offset_x=0.0, offset_y=0.0, offset_z=0.0,
                        roll=0.0, pitch=0.0, yaw=0.0,
                        scale=1.0, static=True, random_bounds=None):
    result = paths_from_group_substr(doc, group_filter_substr, svgpathtools.CONVERT_ONLY_PATHS)
    counter = 0
    for tup in result:
        world.append(generate_imported_model_sdf(group_filter_substr+'_'+str(counter), uri, tup.path,
                                                 offset_x=offset_x, offset_y=offset_y, offset_z=offset_z,
                                                 roll=roll, pitch=pitch, yaw=yaw,
                                                 scale=scale, static=static, random_bounds=random_bounds))
        counter += 1

def add_imported_models_from_group_title(world, svg_doc, layer_group,
                                         offset_x=0.0, offset_y=0.0, offset_z=0.0,
                                         roll=0.0, pitch=0.0, yaw=0.0,
                                         scale=1.0, static=True, random_bounds=None):
    for group in layer_group.iterfind(svgpathtools.SVG_GROUP_TAG, svgpathtools.SVG_NAMESPACE):
        title_elem = group.find('svg:title', svgpathtools.SVG_NAMESPACE)
        model_name = group.get('id')
        if title_elem is None:
            print("OH NO no title defined for object group ID [{}]. Ignoring it...".format(model_name))
            continue
        model_type = title_elem.text
        result = svg_doc.flatten_group(
            group, path_conversions=svgpathtools.CONVERT_ONLY_PATHS)
        pose_path = None
        for tup in result:
            title_elem = tup.element.find(
                'svg:title', svgpathtools.SVG_NAMESPACE)
            if title_elem is not None and title_elem.text == "pose":
                pose_path = tup.path
                break

        if pose_path is None:
            print("OH NO no pose path for model_type={} model_name={}. Ignoring...".format(
                model_type, model_name))
            continue

        desc_elem = group.find('svg:desc', svgpathtools.SVG_NAMESPACE)
        model_offset_z = 0.0
        if desc_elem is not None:
            params = yaml.safe_load(desc_elem.text)
            if 'z' in params:
                model_offset_z = offset_z + float(params['z'])

        print("adding model of type {}".format(model_type))

        world.append(generate_imported_model_sdf(model_name, 'model://'+model_type, pose_path,
                                                 offset_x=offset_x, offset_y=offset_y,
                                                 offset_z=model_offset_z,
                                                 roll=roll, pitch=pitch, yaw=yaw,
                                                 scale=scale, static=static, random_bounds=random_bounds))
