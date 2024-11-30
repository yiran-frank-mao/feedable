# import xml.etree.ElementTree as ET

# # 创建根元素
# feed = ET.Element("feed", xmlns="http://www.w3.org/2005/Atom")

# # 添加基本信息
# title = ET.SubElement(feed, "title")
# title.text = "My Image Feed"
# link = ET.SubElement(feed, "link", href="http://example.com")
# updated = ET.SubElement(feed, "updated")
# updated.text = "2024-11-30T12:00:00Z"  # 使用 ISO 8601 格式
# author = ET.SubElement(feed, "author")
# name = ET.SubElement(author, "name")
# name.text = "Yiran"

# # 添加一个图片条目
# entry = ET.SubElement(feed, "entry")
# entry_title = ET.SubElement(entry, "title")
# entry_title.text = "Beautiful Sunset"
# entry_link = ET.SubElement(entry, "link", href="http://example.com/sunset.jpg", rel="enclosure", type="image/jpeg")
# entry_id = ET.SubElement(entry, "id")
# entry_id.text = "http://example.com/sunset.jpg"
# entry_updated = ET.SubElement(entry, "updated")
# entry_updated.text = "2024-11-30T12:00:00Z"
# entry_summary = ET.SubElement(entry, "summary")
# entry_summary.text = "A stunning sunset over the ocean."

# # 生成 XML
# tree = ET.ElementTree(feed)
# tree.write("image_atom_feed.xml", encoding="utf-8", xml_declaration=True)

# print("Image Atom feed generated: image_atom_feed.xml")

import os

print(os.path.join('https://raw.githubusercontent.com/yiran-frank-mao/photography/master', 'image', '1.jpg'))
