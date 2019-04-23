# blender to gazebo cordinates converter
# paste blender coordinates here

import bpy

selected = bpy.data.objects[0]

blend_x = selected.location[0]
blend_y = selected.location[1]
blend_z = selected.location[2]

gz_x = (blend_y * -1) / 100
gz_y = (blend_x * -1) / 100
gz_z = blend_z / 100

conv = [gz_x, gz_y, gz_z]

output = ["%.3f" % c for c in conv]

print(output)