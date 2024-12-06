import os
import exifread
import xml.etree.ElementTree as ET


figure = ET.Element("figure")
ET.SubElement(figure, "img", {
    "alt": "hh",
    "src": "https://",
    "referrerpolicy": "no-referrer"
})
content_str = ET.tostring(figure, encoding='unicode') + " by Yiran"

print(content_str)
