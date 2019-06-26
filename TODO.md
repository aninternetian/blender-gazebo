### Script intention

##Blender add-on.
Export setup:
- [ ] Main folder to export
- [ ] Author name
- [ ] Author email
- [ ] save main config to file
Configure export - User input:
- [ ] model description
- [ ] model names
- [ ] folder name
Apply configuration:
- [x] set to meters
- [ ] remove hidden faces
- [ ] set main model to 0, the rest should follow
- [ ] apply location, rotation and scale to main model
- [ ] apply rotation and scale to all objects
- [ ] ask user to check model
Export:
- [ ] Create subfolder "meshes"
- [ ] save texture in meshes
- [ ] relink texture to that folder
- [ ] Export coordinate (y up, etc)
- [ ] Export everything in that folder

XML export
Export sdf files:
- [ ] model.sdf
- [ ] model.config

### Note to self

* Not parse .dae (doesn't have position/what i need)
* Wrap these things (# def model_name , # def model_location)
* Setup as module?
* Argparse output xml into designated location
* Import io_scene_obj.export_obj