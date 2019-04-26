import bpy

class BlenderButton(bpy.types.Panel):
    bl_label = "Blender to Gazebo"
    bl_idname = "OBJECT_PT_log"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        row = layout.row()
        row.prop(obj, "Export")

        row = layout.row()
        row.operator("")

def register():
    bpy.utils.register_class(BlenderButton)

def unregister():
    bpy.utils.unregister_class(BlenderButton)

if __name__ == "__main__":
    register()