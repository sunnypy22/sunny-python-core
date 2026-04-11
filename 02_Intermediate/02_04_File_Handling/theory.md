# File Handling in Python: CSV, JSON, XML
**Definition**: Python provides excellent built-in support for reading and writing different file formats. Understanding these formats is essential for data processing, configuration, APIs, and data exchange.
## 1. CSV (Comma-Separated Values)
- Simple tabular data format
- Human-readable and widely supported
- Best for spreadsheets and datasets
**Key Module**: `csv`
```python
import csv
# Writing CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Sunny", 25, "Pune"])
# Reading CSV
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```
### Using DictReader / DictWriter (Recommended):
```python
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["Age"])
```
## 2. JSON (JavaScript Object Notation)
Most popular data interchange format
Used in APIs, configuration files, web development
Native support in Python via json module
**Key Module: json**
```python
import json
data = {
    "name": "Sunny",
    "age": 25,
    "skills": ["Python", "Data Science"],
    "active": True
}
# Writing JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
# Reading JSON
with open("data.json", "r") as f:
    loaded = json.load(f)
```
## 3. XML (eXtensible Markup Language)
Hierarchical data format
Used in configuration, web services (SOAP), Android, etc.
More verbose than JSON
**Key Module**: xml.etree.ElementTree
```python
import xml.etree.ElementTree as ET
# Writing XML
root = ET.Element("student")
ET.SubElement(root, "name").text = "Sunny"
ET.SubElement(root, "age").text = "25"
tree = ET.ElementTree(root)
tree.write("student.xml", encoding="utf-8", xml_declaration=True)
```