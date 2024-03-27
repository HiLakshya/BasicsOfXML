import xml.etree.ElementTree as ET
mytree = ET.parse('combined.svg')

myroot = mytree.getroot()

print(myroot.tag)
print("\n \n")
print(myroot.attrib)
print("\n \n")
print(myroot[0].tag)
print("\n \n")
print(myroot[1].tag)

print("*****************************************\n")

# Printing tags and attributes recursively
def print_tags_and_attributes(element):
    print("\n")
    print("Tag:", element.tag)
    print("Attributes:", element.attrib)
    for child in element:
        print_tags_and_attributes(child)

#it should be noted that the first element is the root element ie svg
       
        

# Print tags and attributes
print_tags_and_attributes(myroot)

print("*****************************************\n")

def display_tag_attributes(index, tree):
    root = tree.getroot()
    if index < len(root):
        element = root[index]
        print("Tag:", element.tag)
        print("Attributes:", element.attrib)
    else:
        print("Index out of range")

# Display tag and attributes
display_tag_attributes(0, mytree)
display_tag_attributes(1, mytree)

#If you will give -1 as index it will print display_tag_attributes(1, mytree)
#If you will give -2 as index it will print display_tag_attributes(0, mytree)


print("*****************************************\n")

for x in myroot.findall('{http://www.w3.org/2000/svg}path'):
    print(x.tag, x.attrib)

print("*****************************************\n")
# Now we are displating only the path and its d attribute
for x in myroot.findall('{http://www.w3.org/2000/svg}path'):
    print(x.tag,"===>", x.attrib['d'])

# we are iterating over the tag path and changing the attribute of the path tag
for x in myroot.iter('{http://www.w3.org/2000/svg}path'):
    x.set('updated', 'yes') #adding updated attribute to the path tag

mytree.write('updated.svg')

print("*****************************************\n")

ET.SubElement(myroot[1], 'LakshyaTag2') #adding new tag to the inside fist child of the root element
ET.SubElement(myroot[0], 'LakshyaTag1') #adding new tag to the inside fist child of the root element


# adding text to the new tag LaskhyaTag1

for x in myroot.iter('LakshyaTag1'):
    x.text = 'This is the new tag added by Lakshya'

mytree.write('updated1.svg')


print("*****************************************\n")
#removing the tag from the updated attribute from roote tag

for x in myroot.iter('{http://www.w3.org/2000/svg}path'):
    x.attrib.pop('updated')


mytree.write('updated2.svg')

print("*****************************************\n")

#removing the firts child of the root element
myroot.remove(myroot[0])

mytree.write('updated3.svg')