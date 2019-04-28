def transform(num):
    return f'{num:.2f}' if num else '0'

floats = [3.141, 0.0, 2.71828, 1.61, 0.12345678, 0.0]

print(' '.join(map(transform, floats)))

'''Translates all objects location in your scene into the gazebo SDF'''

import bpy
import argparse

# def blend_sdf(output_filename):

    f = open(args.output, 'w')

    models = bpy.data.objects
    coords = model.location

    for model in models:
        f.write(model.name + "\n")

        gz_x = (coords[1] * -1) + 0
        gz_y = (coords[0] * -1) + 0
        gz_z = (coords[2]) + 0

        conv = [gz_x, gz_y, gz_z]

        out = ""
        length = len(conv)

        for x in range(0, length):
            c = conv[x]
            out += ("0" if c == 0.0 else "%.2f" % c)
            if x != length - 1: 
                out += " "
        f.write(out)

    f.close()

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