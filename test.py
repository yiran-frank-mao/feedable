import os
import exifread

def get_image_metadata(file_path):
    img = open(file_path, 'rb')
    tags = exifread.process_file(img, details=False)
    return tags
    return {key: tags[key] for key in ['Image Make', 'Image Model', 'EXIF LensModel', 'EXIF FocalLength', 'EXIF ApertureValue', 'EXIF ShutterSpeedValue'] if key in tags}

folder_path = "images/"
metadata_list = []
for file in os.listdir(folder_path):
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        image_info = get_image_metadata(os.path.join(folder_path, file))
        image_info['file_name'] = file
        metadata_list.append(image_info)


print(metadata_list)
