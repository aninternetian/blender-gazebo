## What it does

It collects all models and their locations, convert it's coordinates into an SDF format.

## How to use

Open terminal in mesh folder

```
source ~/rmf/build/ros1_mainline/install/setup.bash
```

Type in the following line:  
`blender -b -P ~/blender2gazebo/blend2gz.py -- `

Along with:

* Blend file name, eg: `silly_robot.blend`
* Text file name, eg: `output_text.txt`

Your last line should look something like this:  
`blender -b -P ~/blender2gazebo/blend2gz.py -- silly_robot.blend output_text.txt`

## Disclaimer

* SDF automation is not done yet, so you'll still need to fill in your sdf file with teh coordinates and the model info.
* One of my first few scripting projects.
* Written to practice scripting, the Python syntax and to automate my work.

## To-do's

* Simplify and make the code look pretty.
* Get this script up and running into Blender with a UI button.
* Automate it further so that it auto-fills in Gazebo's SDF.
