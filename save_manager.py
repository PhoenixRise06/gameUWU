import xml.etree.ElementTree as ET, xmltodict, os

saveFilePath = 'save_the_world.xml'

def createSave():
    savedata = {'savedata': {
        'worldinfo' : {
            'newplayer' : '1'
            },
        'playerstate' : {
            'playername' : 'Player'
            },
        'guidedata' : {
            'guidename' : '???'
            }
        }
    }
    file=open(saveFilePath, 'w')
    xml_string=xmltodict.unparse(savedata)
    file.write(xml_string)
    file.close()


def write(section, element, value):
    """this thing saves the thing to the thing :thumbs_up:"""
    tree = ET.parse(saveFilePath)
    file = open(saveFilePath,"r+")
    xml_string=file.read()
    dict=xmltodict.parse(xml_string)
    dict["savedata"][section][element]=value
    file.seek(0)
    file.truncate()
    xmltodict.unparse(dict,file)
    file.close()
    tree.write(saveFilePath)

def read(section, element):
    """this thing reads save value"""
    tree = ET.parse(saveFilePath)
    root = tree.getroot()
    value = root.find(section + "/" + element).text
    return value