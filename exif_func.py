import exiftool
import os
import json


def extract_exif(output_txt,image_files,image_dir):

    with open(output_txt, 'w') as output_file:
        with exiftool.ExifTool() as et:
            for image in image_files:
                image_path = os.path.join(image_dir, image)

                # Extract metadata
                metadata_str = et.execute("-j", image_path)

                 # Ensure valid JSON response
                try:
                    metadata_list = json.loads(metadata_str)  # Parse JSON
                except json.JSONDecodeError:
                    print(f"Error: Unable to parse metadata for {image}")
                    continue

                if metadata_list:
                    metadata = metadata_list[0]
                    output_file.write(f"Metadata for {image}:\n")
                
                    # Writing metadata to file
                    for key, value in metadata.items():
                        output_file.write(f"{key}: {value}\n")

                    output_file.write("\n" + "-"*50 + "\n\n")
                
                else:
                    print(f"No metadata found for {image}")

