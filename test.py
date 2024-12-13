import os
import exifread
import xml.etree.ElementTree as ET


def get_image_metadata(file_path):
    img = open(file_path, 'rb')
    tags = exifread.process_file(img, details=False)
    # return tags
    return {key: tags[key] for key in ['Image Make', 'Image Model', 'EXIF LensModel', 'EXIF FocalLength', 'EXIF ApertureValue', 'EXIF ShutterSpeedValue', 'EXIF ImageDescription'] if key in tags}

metadata_list = []

for file in os.listdir("images"):
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        image_info = get_image_metadata(os.path.join("images", file))
        image_info['file_name'] = file
        metadata_list.append(image_info)

print(metadata_list)
