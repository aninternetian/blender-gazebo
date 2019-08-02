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

    pos.append(coords[0] * -1)
    pos.append(coords[1] * -1)
    pos.append(coords[2])

    trans = ["%.2f" % p for p in pos]
    print(' '.join(trans) + " 0 0 0")