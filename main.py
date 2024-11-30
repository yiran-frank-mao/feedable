import os
import exifread
from datetime import datetime
import xml.etree.ElementTree as ET

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

    import xml.etree.ElementTree as ET

    feed = ET.Element("feed", xmlns="http://www.w3.org/2005/Atom")

    title = ET.SubElement(feed, "title")
    title.text = os.environ["INPUT_TITLE"]
    link = ET.SubElement(feed, "link", href=os.environ["INPUT_BASEURL"])
    updated = ET.SubElement(feed, "updated")
    updated.text = datetime.utcnow().isoformat() + "Z"  # current time in ISO 8601 format
    author = ET.SubElement(feed, "author")
    name = ET.SubElement(author, "name")
    name.text = os.environ["INPUT_AUTHOR"]

    # Add an entry for each image
    for image_info in metadata_list:
        entry = ET.SubElement(feed, "entry")
        entry_title = ET.SubElement(entry, "title")
        entry_title.text = "Beautiful Sunset"
        entry_link = ET.SubElement(entry, "link", href="http://example.com/sunset.jpg", rel="enclosure", type="image/jpeg")
        entry_id = ET.SubElement(entry, "id")
        entry_id.text = "http://example.com/sunset.jpg"
        entry_updated = ET.SubElement(entry, "updated")
        entry_updated.text = "2024-11-30T12:00:00Z"
        entry_summary = ET.SubElement(entry, "summary")
        entry_summary.text = "A stunning sunset over the ocean."

    # Create XML
    tree = ET.ElementTree(feed)
    tree.write(output_path, encoding="utf-8", xml_declaration=True)

    set_github_action_output('output', output_path)


if __name__ == "__main__":
    main()
