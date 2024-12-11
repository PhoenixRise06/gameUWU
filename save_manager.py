import xml.etree.ElementTree as ET, xmltodict

save_file_path = 'save_the_world.xml'

def create_save():
    """this thing creates a new save file if it doesnt already exist"""
    save_data = {'save_data': {
        'worldinfo' : {
            'newplayer' : '1',
            'tuitorialstarted' : '0',
            'tuitorialcheckpoint' : '0'
            },
        'playerstate' : {
            'playername' : 'Player'
            },
        'guidedata' : {
            'guidename' : '???'
            }
        }
    }
    file=open(save_file_path, 'w')
    xml_string=xmltodict.unparse(save_data)
    file.write(xml_string)
    file.close()

def write(section, element, value):
    """this thing saves the thing to the thing :thumbs_up:"""
    tree = ET.parse(save_file_path)
    root = tree.getroot()
    el = root.find(f'{section}/{element}')
    if el is not None:
        el.text = value
        tree.write(save_file_path)

def read(section, element):
    """this thing reads save value"""
    tree = ET.parse(save_file_path)
    root = tree.getroot()
    value = root.find(section + "/" + element).text
    return value