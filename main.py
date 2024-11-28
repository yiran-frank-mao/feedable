import os
import exifread
from feedgen.feed import FeedGenerator

def get_image_metadata(file_path):
    img = open(file_path, 'rb')
    tags = exifread.process_file(img, details=False)
    return {key: tags[key] for key in ['EXIF LensModel', 'EXIF FocalLength', 'EXIF ApertureValue', 'EXIF ShutterSpeedValue'] if key in tags}

# Set the output value by writing to the outputs in the Environment File, mimicking the behavior defined here:
#  https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter
def set_github_action_output(output_name, output_value):
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
    f.write(f'{output_name}={output_value}')
    f.close()

def main():
    folder_path = os.environ["INPUT_FOLDERPATH"]
    output_path = os.environ["INPUT_OUTPUTPATH"]

    metadata_list = []
    for file in os.listdir(folder_path):
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
            image_info = get_image_metadata(os.path.join(folder_path, file))
            image_info['file_name'] = file
            metadata_list.append(image_info)

    fg = FeedGenerator()
    fg.title(os.environ["INPUT_TITLE"])
    fg.link(href=os.environ["INPUT_BASEURL"], rel='self')
    fg.description(os.environ["INPUT_DESCRIPTION"])

    for image_info in metadata_list:
        fe = fg.add_entry()
        fe.title(image_info.get('ImageDescription', 'No Title'))
        fe.link(href=os.path.join(os.environ["INPUT_DIRECTLINK"]+folder_path, image_info['file_name']))
        # fe.description(str(image_info))

    fg.rss_file(output_path)

    set_github_action_output('Generated: ', output_path)


if __name__ == "__main__":
    main()
