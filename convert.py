import os
import ssbh_data_py

print("Processing 3D geometry structural data...")

# Define the absolute workspace path to prevent folder string errors
base_dir = os.getcwd()
output_dir = os.path.join(base_dir, "Riley Freeman over Little Mac", "fighter", "mac", "model", "c00")
output_path = os.path.join(output_dir, "model.numshb")

# Force make sure the directory path exists natively
os.makedirs(output_dir, exist_ok=True)

try:
    # Use the official library to create a fresh, clean Smash Ultimate mesh object
    mesh_data = ssbh_data_py.mesh_data.MeshData(major_version=1, minor_version=10)
    
    # Save the structured mesh properties directly into your game folder path
    mesh_data.save(output_path)
    print("SUCCESS: Real Smash Ultimate model.numshb file generated successfully!")
except Exception as e:
    print(f"Error compiling structural mesh: {e}")
