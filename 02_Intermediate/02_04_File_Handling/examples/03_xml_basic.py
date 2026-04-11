
import xml.etree.ElementTree as ET
root = ET.Element("school")
student = ET.SubElement(root, "student")
ET.SubElement(student, "name").text = "Sunny"
ET.SubElement(student, "age").text = "25"
ET.SubElement(student, "grade").text = "A"
tree = ET.ElementTree(root)
tree.write("school.xml", encoding="utf-8", xml_declaration=True)
print("XML file created!")
