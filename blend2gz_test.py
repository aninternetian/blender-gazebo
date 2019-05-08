'''This works with blender gui'''

import bpy

scene = bpy.context.scene

scene.unit_settings.system = 'METRIC'
scene.unit_settings.scale_length = 1.0

models = bpy.data.objects

for model in models:
    print(model.name)
    
    coords = model.location
    pos = []

    pos.append(coords[1] * -1)
    pos.append(coords[0] * -1)
    pos.append(coords[2])

    out = ""
    for p in pos:
        out += ("0" if p == 0.0 else "%.2f" % p)
        out += " "
    print(out + "0 0 0")

##########
# TO-DOS #
##########
# xml.etree.ElementTree
# don't parse .dae as that doesn't have position/what i need
# wrap these things     # def model_name     # def model_location
# argparse output xml into designated location
# use blender GUI instead of argparse (blender button, etc)
# add-on for blender
# import io_scene_obj.export_obj
