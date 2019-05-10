## What it does

To import a robot from Blender into Gazebo, it should be modelled into separate parts (wheels, joints, etc).
This script converts each part into an SDF friendly format.

1. Change Blender units into meters
2. Collect each part name and location coordinates (X, Y, Z)
3. Print out a txt.log into an SDF format.

## How to use

Open terminal in the working mesh folder

```
source ~/rmf/build/ros1_mainline/install/setup.bash
```

Type in the following line:

```
blender -b -P ~/blender2gazebo/blend2gz.py -- 
```

Along with:

* Blend file name, eg: `silly_robot.blend`
* Text file name, eg: `output_text.txt`

Your last line should look something like this:  
`blender -b -P ~/blender2gazebo/blend2gz.py -- silly_robot.blend output_text.txt`

## Final notes

* Do NOT `apply location` of objects
* SDF automation and exports are in the process
* This was done to practice scripting and to automate my work.
* Still working on un-messy-fying the code
* Feedback on code improvement greatly welcome!
