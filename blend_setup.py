'''setting up this for sdf'''

import bpy

scene = bpy.context.scene

scene.unit_settings.system = 'METRIC'
scene.unit_settings.scale_length = 1.0

def check_models():

    models = bpy.data.objects

    for model in models:
        return model

def write_models_name(model):
    print(model.name)

def model_location(model):

    coords = model.location
    pos = []

    pos.append(coords[0])
    pos.append(coords[1])
    pos.append(coords[2])

    trans = ["%.3f" % p for p in pos]
    print(' '.join(trans) + " 0 0 0")


##########
# TO-DOS #
##########
# don't parse .dae as that doesn't have position/what i need
# wrap these things     # def model_name     # def model_location
# setup as module?
# argparse output xml into designated location
# use blender GUI instead of argparse (blender button, etc)
# add-on for blender
# import io_scene_obj.export_obj
