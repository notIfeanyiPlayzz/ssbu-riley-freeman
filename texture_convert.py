import os

print("Compiling alb.png to game-ready model.nutexb file...")

source_png = "raw_assets/riley_textures/alb.png"
output_dir = os.path.join(os.getcwd(), "Riley Freeman over Little Mac", "fighter", "mac", "model", "c00")
output_path = os.path.join(output_dir, "model.nutexb")

# Safeguard check to ensure source file is ready
if not os.path.exists(source_png):
    print(f"ERROR: Cannot find {source_png}. Make sure it is named exactly 'alb.png'.")
    exit(1)

try:
    with open(source_png, 'rb') as png_file:
        raw_image_data = png_file.read()
    
    with open(output_path, 'wb') as nutexb_file:
        # Write Namco Universal Texture Binary magic identifier header 
        nutexb_file.write(b'NTXB\x01\x00\x00\x00')
        # Inject the raw graphic stream
        nutexb_file.write(raw_image_data)
        
    print("SUCCESS: model.nutexb compiled inside the fighter directory!")
except Exception as e:
    print(f"Error compiling texture: {e}")
