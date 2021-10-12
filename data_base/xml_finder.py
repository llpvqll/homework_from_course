from xml.etree import ElementTree as ET

FILENAME = 'example.xml'

tree = ET.parse(FILENAME)
root = tree.getroot()

print(root.tag)
print('-'*20)
print(root.attrib)
print('-'*20)

for child in root:
    print(child.tag, child.attrib)

print('-'*20)

for description in root.iter('description'):
    print('-' * 20)
    print(description.text)

for price in root.iter('price'):
    print('-' * 20)
    print(price.text)





