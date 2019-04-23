'''blender to gazebo cordinates converter'''

import bpy

bpy.ops.script.python_file_run(filepath="/snap/blender/20/2.79/scripts/presets/units_length/meters.py")
# will be working for all systems eventually

models = bpy.data.objects
print("~~~~~~~~~~")

for model in models:
    print(model)

    blend_x = model.location[0]
    print("Original_X: " + str(blend_x))
    blend_y = model.location[1]
    print("Original_Y: " + str(blend_y))
    blend_z = model.location[2]
    print("Original_Z: " + str(blend_z))

    gz_x = blend_y * -1
    gz_y = blend_x * -1
    gz_z = blend_z

    conv = [gz_x, gz_y, gz_z]
    
    for c in conv:
        print(round(c, 3))
        # to print in a better format

print("~~~~~~~~~~")