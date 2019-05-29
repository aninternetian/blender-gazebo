'''This works in headless mode'''

import argparse
import bpy

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    _, all_arguments = parser.parse_known_args()
    double_dash_index = all_arguments.index('--')
    script_args = all_arguments[double_dash_index + 1:]

    parser.add_argument('input', help='Input .blend file')
    parser.add_argument('output', help='Output .sdf file')
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
        pos = []

        pos.append(coords[0])
        pos.append(coords[1])      
        pos.append(coords[2])

        trans = ["%.3f" % p for p in pos]
        f.write(' '.join(trans) + " 0 0 0\n")

    f.close()
