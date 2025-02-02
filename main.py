import os
from exif_func import extract_exif
import sys
from map_photos import map_coordinates

if len(sys.argv) != 2:
    print("Usage: python main.py <image_directory>")
    sys.exit(1)


image_dir = sys.argv[1]

output_txt = 'metadata_output.txt'

image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('jpg', 'jpeg', 'png', 'tiff', 'bmp'))]

extract_exif(output_txt,image_files,image_dir)

print(f"Metadata extraction completed! Check the {output_txt} file.")

locations = []

map_coordinates(locations,output_txt)
