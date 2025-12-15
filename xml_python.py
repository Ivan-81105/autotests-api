import xml.etree.ElementTree as ET

xml_data = """
<user>
    <id>1</id>
    <first_name>John</first_name>
    <last_name>Doe</last_name>
    <email>John.Doe@example.com</email>
</user>
"""
root = ET.fromstring(xml_data)
print(root.find('email').text)

<person>
    <name>value1</name>
    <age>value2</age>
</person>