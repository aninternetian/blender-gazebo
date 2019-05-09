## What it does

It collects all models and their locations, convert it's coordinates into an SDF format.

Example you have a robot with 6 wheels.
This script will gather all the locations of the wheels and the robot.

## How to use

Open terminal in mesh folder

```
source ~/rmf/build/ros1_mainline/install/setup.bash
```

Type in the following line:  
`blender -b -P ~/blender2gazebo/blend2gz.py --  `

Along with:

* Blend file name, eg: `silly_robot.blend`
* Text file name, eg: `output_text.txt`

Your last line should look something like this:  
`blender -b -P ~/blender2gazebo/blend2gz.py -- silly_robot.blend output_text.txt`

## Disclaimer

* Do NOT `apply location` of objects
* SDF automation and exports are not done yet
* This was done to practice scripting, the Python syntax and to automate my work.
* Excuse the ugly-ness since I'm still new at this.
