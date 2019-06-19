'''This works with blender gui'''

import bpy

retrieveModelInfo = bpy.data.objects    #this is a list of x things

def modelInfo(blendInfo):
    for modelNames in retrieveModelInfo:
        names = modelNames.name

modelInfo(retrieveModelInfo)