'''setting up this for sdf'''

import bpy

scene = bpy.context.scene

scene.unit_settings.system = 'METRIC'
scene.unit_settings.scale_length = 1.0

retrieveModelInfo = bpy.data.objects

def modelNames(blendInfo):
    for model in retrieveModelInfo:
        print(model.name)

modelNames(retrieveModelInfo)    # this will only return the model name

def modelLocation(blendInfo):

    for model in retrieveModelInfo:

        coords = model.location
        pos = []

        pos.append(coords[0])
        pos.append(coords[1])
        pos.append(coords[2])

        trans = ["%.3f" % p for p in pos]
        print(' '.join(trans) + " 0 0 0")

modelLocation(retrieveModelInfo)