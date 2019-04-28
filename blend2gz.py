'''Translates all objects location in your scene into the gazebo SDF'''

import bpy
import argparse

scene = bpy.context.scene

scene.unit_settings.system = 'METRIC'
scene.unit_settings.scale_length = 1.0

f = open(args.output, 'w')

def transform(num):
    return "%.2f" % num if num else '0'

    models = bpy.data.objects
    coords = model.location

    for model in models:
        f.write(model.name)

        position = []
        position.append(coords[1] * -1 + 0)
        position.append(coords[0] * -1 + 0)
        position.append(coords[2] + 0)
        f.write(' '.join(map(transform, position)))

f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    _, all_arguments = parser.parse_known_args()
    double_dash_index = all_arguments.index('--')
    script_args = all_arguments[double_dash_index + 1:]

    parser.add_argument('input', help='Input .blend file')
    parser.add_argument('output', help='Output .txt file for the coordinates')
    args, _ = parser.parse_known_args(script_args)

    bpy.ops.wm.open_mainfile(filepath=args.input)

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
