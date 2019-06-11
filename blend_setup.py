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
