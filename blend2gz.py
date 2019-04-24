'''Writes all your blender models into the gazebo SDF'''

import bpy
import os 

dir_path = os.path.dirname(os.path.realpath("/meters.py"))
bpy.ops.script.python_file_run(filepath=dir_path)

models = bpy.data.objects
print("~~~~~~~~~~")

for model in models:
    print(model)

    gz_x = (model.location[1] * -1) + 0
    gz_y = (model.location[0] * -1) + 0
    gz_z = (model.location[2]) + 0

    conv = [gz_x, gz_y, gz_z]
    
    for c in conv:
        print(round(c, 3))

print("~~~~~~~~~~")

# TO-DOS
###
# button in blender
# format results in one line
# print only object name