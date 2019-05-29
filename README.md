## What it does

To import a robot from Blender into Gazebo, it should be modelled into separate parts (wheels, joints, etc).
This script converts each part into an SDF friendly format.

1. Change Blender units into meters
2. Collect each part name and location coordinates (X, Y, Z)
3. Print out a txt.log into an SDF format.

## How to use

In Blender, export each robo part as an .obj:
* `Forward: Y Forward`
* `Up: Z Up`

Clone this repo into your home folder and open the terminal from the folder where the final blender model is in.

```
source ~/rmf/build/ros1_mainline/install/setup.bash
```

Type in the following line:

```
blender -b -P ~/blender-gazebo/blend_sdf_headless.py -- 
```

Along with:

* Blend file name, eg: `silly_robot.blend`
* Text file name, eg: `output_text.txt`

Your last line should look something like this:  
`blender -b -P ~/blender-gazebo/blend_sdf_headless.py -- silly_robot.blend output_text.txt`

## Final notes

* There is another version of the script which runs in the Blender GUI. This is mostly used for testing.
* Click on `Apply: Location` ONLY for the main body/part.
* Click on `Apply: Rotation & Scale` for each part.
* SDF automation and exports are in the process
* This was done to practice scripting and to automate my work.
* Feedback on code improvement greatly welcome!
* Code is messy at the moment and cleaning up will happen when possible.

