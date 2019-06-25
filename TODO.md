## Script intention
Blender export
* Export coordinate (y up, etc)
* Export everything in that folder
* Check if .mtl file is in the right link
* Make it an add on

XML export
* Export sdf files:
* model.sdf
* model.config

System export
* Export to folder (ability to name folder)
* Create subfolder "meshes"

## Note to self

* Not parse .dae (doesn't have position/what i need)
* Wrap these things (# def model_name , # def model_location)
* Setup as module?
* Argparse output xml into designated location
* Import io_scene_obj.export_obj