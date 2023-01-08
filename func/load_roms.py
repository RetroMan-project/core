# Ho bisogno della funzione load_roms.py.

# Questa funzione deve leggere ricorsivamente tutti i gamelist e generare una lista di tutte le roms presenti in un determinato device
# Inoltre deve avere la possibilità di sapere quale rom è marchiata come "sync" e su quale device,
# questa informazione viene presa dal gamelist della libreria attiva sotto il tag:

# <sync>
#     <nome_device_1>data-e-ora</nome_device_1>
# </sync>

# NOTA: una rom può essere "sync" su più di un device, in quel caso si avranno più righe di sync.

# La funzione deve essere scritta in inglese.

# This functions scan for the gamelists recursively and check the what is synced and where

import xml.etree.ElementTree as ET

def load_roms(root_path):
    roms = []
    sync_roms = []

    # Recursively search for gamelist files
    for path, _, filenames in os.walk(root_path):
        for filename in filenames:
            if filename == 'gamelist.xml':
                # Parse the gamelist file and extract the ROMs
                roms += parse_gamelist(os.path.join(path, filename))

                # Check if any of the ROMs are marked as "sync" in this gamelist
                sync_roms += get_sync_roms(os.path.join(path, filename))

    # Return the list of ROMs and the list of "sync" ROMs
    return roms, sync_roms


def parse_gamelist(gamelist_path):
    roms = []

    # Parse the gamelist XML file
    tree = ET.parse(gamelist_path)
    root = tree.getroot()

    # Extract the ROMs from the gamelist
    for game in root.findall('game'):
        rom = {}
        rom['name'] = game.find('name').text
        rom['path'] = game.find('path').text
        roms.append(rom)

    return roms


def get_sync_roms(gamelist_path):
    sync_roms = []

    # Parse the gamelist XML file
    tree = ET.parse(gamelist_path)
    root = tree.getroot()

    # Extract the "sync" tag
    sync_tag = root.find('sync')

    # Add any ROMs marked as "sync" to the list
    for device in sync_tag.findall('device'):
        sync_roms.append(device.text)

    return sync_roms