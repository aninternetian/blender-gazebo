'''Translates all objects location in your scene into the gazebo SDF'''

import bpy
import argparse

def transform(num):
    scene = bpy.context.scene

    scene.unit_settings.system = 'METRIC'
    scene.unit_settings.scale_length = 1.0

    models = bpy.data.objects

    f = open(args.output, 'w')

    return "%.2f" % num if num else '0'

    for model in models:
        f.write(model.name)

        coords = model.location
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

####################
# argparse
# sdformatpy
