'''Translates all objects location in the blender scene into the gazebo SDF'''

import argparse
import bpy

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    _, all_arguments = parser.parse_known_args()
    double_dash_index = all_arguments.index('--')
    script_args = all_arguments[double_dash_index + 1:]

    parser.add_argument('input', help='Input .blend file')
    parser.add_argument('output', help='Output .txt file for the coordinates')
    args, _ = parser.parse_known_args(script_args)

    bpy.ops.wm.open_mainfile(filepath=args.input)

    scene = bpy.context.scene

    scene.unit_settings.system = 'METRIC'
    scene.unit_settings.scale_length = 1.0

    models = bpy.data.objects

    f = open(args.output, 'w')

    for model in models:
        f.write(model.name + "\n")
        
        coords = model.location

        gz_x = (coords[0] * -1)        
        gz_y = (coords[1] * -1)
        gz_z = (coords[2])

        conv = [gz_x, gz_y, gz_z]

        trans = ["%.2f" % c for c in conv]
        f.write(' '.join(trans) + " 0 0 0\n")

    f.close()
