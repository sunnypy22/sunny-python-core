
import xml.etree.ElementTree as ET
tree = ET.parse("school.xml")
root = tree.getroot()
for student in root.findall("student"):
    name = student.find("name").text
    age = student.find("age").text
    print(f"Student: {name}, Age: {age}")
