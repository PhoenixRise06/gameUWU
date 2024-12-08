import xml.etree.ElementTree as ET, xmltodict, shutil

saveFilePath = 'save_the_world.xml'

def dupe():
    templateFilePath = 'core\\save_the_world.xml'
    shutil.copy(templateFilePath, saveFilePath)

def write(element, value):
    """this thing saves the thing to the thing :thumbs_up:"""
    tree = ET.parse(saveFilePath)
    file=open(saveFilePath,"r+")
    xml_string=file.read()
    save_dict=xmltodict.parse(xml_string)
    save_dict["savedata"][element]=value
    file.seek(0)
    file.truncate()
    xmltodict.unparse(save_dict,file)
    file.close()
    tree.write(saveFilePath)

def read(element):
    """this thing reads save value"""
    tree = ET.parse(saveFilePath)
    root = tree.getroot()
    value = root.find(element).text
    return value

