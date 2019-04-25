'''Translates all objects location in your scene into the gazebo SDF'''

import bpy
import os 

# <pep8 compliant>

dir_path = os.path.dirname(os.path.realpath("/meters.py"))
bpy.ops.script.python_file_run(filepath=dir_path)

f = open('log.txt', 'w')

models = bpy.data.objects

for model in models:
    f.write(model.name + "\n")

    gz_x = (model.location[1] * -1) + 0
    gz_y = (model.location[0] * -1) + 0
    gz_z = (model.location[2]) + 0

    conv = [gz_x, gz_y, gz_z]

    rnd = ["%.3f" % c for c in conv] 
    output = "{0} {1} {2}".format(rnd[0], rnd[1], rnd[2])
    
    f.write(output + "\n")

# TO-DOS
###
# button in blender
