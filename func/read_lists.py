# This function is used to read and parse the gamelists.wml starting grom the given folder

import os
import glob
import xml.etree.ElementTree as ET

def read_lists(folder):
    # Creiamo una lista vuota per memorizzare le entries che troveremo
    entries = []

    # Usiamo il metodo os.walk per esplorare ricorsivamente la cartella e le sotto-cartelle
    for root, dirs, files in os.walk(folder):
        # Per ogni file nella cartella corrente, usiamo il modulo glob per cercare i file che soddisfano il criterio
        for file in glob.glob(os.path.join(root, 'gamelist.xml')):
            # Se il file esiste, leggiamolo e estraiamo le informazioni che ci interessano
            tree = ET.parse(file)
            root = tree.getroot()

            # Estraggo il nome del sistema e le relative rom
            system_name = root.attrib['name']
            rom_list = [rom.attrib['name'] for rom in root.findall('game')]

            # Aggiungiamo l'entry alla lista
            entries.append({
                'system_name': system_name,
                'rom_list': rom_list
            })

    # Dopo aver esplorato tutte le cartelle, restituiamo la lista delle entries
    return entries