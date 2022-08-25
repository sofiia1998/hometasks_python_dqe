# import xml.etree.ElementTree as ET
#
#
# xml_file = ET.parse('xml_text.xml')
#
# root = xml_file.getroot()

from all_the_modules import FileParsing


x = FileParsing()
x.if_clause_xml_parsing()



# elem = root[0]
# strike = ET.tostring(elem, encoding='unicode')
# print(strike)


# with open('xml_text.xml', "a") as f:
#     f.write(strike)
# for i in range(len(root)):
#     print(i)

# l = root[0][0].text
# print(l)
# for type in root:
#     print(type.tag)


# for type in root.iter('NEWS'):
#     for j in type:
#         if j.tag == 'news_text':
#             print(j.text)

# for typer in root.findall('.//news_text'):
#     t = typer
#     print(t)
#
#     #print(stri)
#     #print(type(typer))
