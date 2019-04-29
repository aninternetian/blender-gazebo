'''Translates all objects location in your scene into the gazebo SDF'''

import bpy
import argparse

def transform(num):
    return "%.2f" % num if num else '0'

def print_coords(model, f):
    f.write("\n" + model.name + "\n")

    coords = model.location
    position = []

    position.append(coords[1] * -1 + 0)
    position.append(coords[0] * -1 + 0)
    position.append(coords[2] + 0)
    f.write(' '.join(map(transform, position)))

def check_models():

    models = bpy.data.objects

    f = open(args.output, 'w')

    for model in models:
        print_coords(model, f)

    f.close()

def unit_meter():
    # this section changes unit
    scene = bpy.context.scene

    scene.unit_settings.system = 'METRIC'
    scene.unit_settings.scale_length = 1.0

    check_models()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    _, all_arguments = parser.parse_known_args()
    double_dash_index = all_arguments.index('--')
    script_args = all_arguments[double_dash_index + 1:]

    parser.add_argument('input', help='Input .blend file')
    parser.add_argument('output', help='Output .txt file for the coordinates')
    args, _ = parser.parse_known_args(script_args)

    bpy.ops.wm.open_mainfile(filepath=args.input)

    unit_meter()

##########
# TO-DOS #
##########
# read argparse
# import sdformatpy
# import io_scene_obj.export_obj

# io_scene_obj.export_obj.save(bpy.context, output_filename, global_matrix=Matrix.Identity(4), use_normals=True)
# output_obj_extension = output_filename.find('.obj')
# output_mtl_file = output_filename[:output_obj_extension] + '.mtl'
