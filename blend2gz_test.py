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

    trans = ["%.2f" % p for p in pos]
    print(' '.join(trans))


##########
# TO-DOS #
##########
# read argparse
# import sdformatpy
# import io_scene_obj.export_obj

# io_scene_obj.export_obj.save(bpy.context, output_filename, global_matrix=Matrix.Identity(4), use_normals=True)
# output_obj_extension = output_filename.find('.obj')
# output_mtl_file = output_filename[:output_obj_extension] + '.mtl'
