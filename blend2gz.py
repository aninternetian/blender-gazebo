# blender to gazebo cordinates converter
# paste blender coordinates here

blend_x = float(input("Blender X = "))
blend_y = float(input("Blender Y = "))
blend_z = float(input("Blender Z = "))

gz_x = (blend_y * -1) /100
gz_y = (blend_x * -1) /100
gz_z = blend_z /100

print("Gazebo X = " + str(gz_x))
print("Gazebo Y = " + str(gz_y))
print("Gazebo Z = " + str(gz_z))