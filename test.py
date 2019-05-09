import bpy

C = bpy.context

test = C.object.location.z
print(test)