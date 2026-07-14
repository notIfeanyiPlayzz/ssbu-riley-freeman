import os
import subprocess

print("Converting Mixamo FBX Mesh to Smash Ultimate format...")

# Use subprocess to handle paths safely without quote glitches
blender_cmd = [
    "blender", 
    "--background", 
    "--python-expr", 
    'import bpy; bpy.ops.import_scene.fbx(filepath="raw_assets/Riley_Main_Rig_T-Pose.fbx")'
]

subprocess.run(blender_cmd)
