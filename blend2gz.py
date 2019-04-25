'''Translates all objects location in your scene into the gazebo SDF'''

import bpy
import os 

dir_path = os.path.dirname(os.path.realpath("/meters.py"))
bpy.ops.script.python_file_run(filepath=dir_path)

models = bpy.data.objects

print("~~~~~~~~~~")

for model in models:
    print(model.name)

    gz_x = (model.location[1] * -1) + 0
    gz_y = (model.location[0] * -1) + 0
    gz_z = (model.location[2]) + 0

    conv = [gz_x, gz_y, gz_z]

    rnd = ["%.3f" % c for c in conv] 
    output = "{0} {1} {2}".format(rnd[0], rnd[1], rnd[2])
    
    print(output)

print("~~~~~~~~~~")

# TO-DOS
###
# print only object name
# button in blender
