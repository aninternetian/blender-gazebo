'''Translates all objects location in your scene into the gazebo SDF'''

import bpy

scene = bpy.context.scene

scene.unit_settings.system = 'METRIC'
scene.unit_settings.scale_length = 1.0

models = bpy.data.objects

def transform(num):
    return "%.2f" % num if num else '0'

for model in models:
    print(model.name)

    vector = []
    vector.append(model.location[1] * -1 + 0)
    vector.append(model.location[0] * -1 + 0)
    vector.append(model.location[2] + 0)
    print(' '.join(map(transform, vector)))

##########
# TO-DOS #
##########
# 0.0
# wrap this into a function
# read argparse
#####
# import sdformatpy
# import io_scene_obj.export_obj

# io_scene_obj.export_obj.save(bpy.context, output_filename, global_matrix=Matrix.Identity(4), use_normals=True)

# output_obj_extension = output_filename.find('.obj')
# output_mtl_file = output_filename[:output_obj_extension] + '.mtl'