import os
import logging

def generate_gamelist(data, debug=False):

    """
    This function generates a gamelist.xml file for the given device, using the given data.
    """

    # Set up logging
    if debug:
        logging.basicConfig(filename='retroman.log', level=logging.DEBUG)
        logging.debug(f'Called generate_gamelist.')
        logging.debug(f'System names: {system_names}')
    
    # Extract the device ID from the template data
    device_id = list(data['template_data'].keys())[0]

    # Extract the roms_path value from the template data
    roms_path = data['template_data'][device_id]['roms_path']

    # Loop over the system names
    for system_name in system_names:
        # Convert the system name to lowercase
        system_name = system_name.lower()

        if debug:
            logging.debug(f'Doing "{system_name}" system.')

        # Create the gamelist file path
        gamelist_path = os.path.join(f'devices/library/{system_name}/gamelist.xml')
        if debug:
            logging.debug(f'Created devices/library/{system_name}/gamelist.xml')

        # Loop through the system folder names in the roms folder
        for system_folder in library[system_name]["system_folders"]:
            
            # Convert the system folder name to lowercase
            system_folder = system_folder.lower()

            system_path = os.path.join(roms_path, system_folder)
            if os.path.exists(system_path):
                # Loop through the files in the system folder
                for filename in os.listdir(system_path):
                    # Check if the file has a supported extension
                    name, ext = os.path.splitext(filename)

                    # Convert the file extension to lowercase
                    ext = ext.lower()

                    if ext in library[system_name]["extensions"]:
                        # Add the file to the gamelist for this system
                        gamelist.append({"path": os.path.join(system_folder, filename)})

                        # Print a debug message
                        print(f'Found {filename} in {system_folder}')

        # Save the gamelist for the system
        with open(gamelist_path, 'w') as f:
          
          # Write the XML header to the file
          f.write('<?xml version="1.0"?>\n')
          # Write the gameList tag to the file
          f.write('<gameList>\n')
          # Loop through the gamelist items and write them to the file
          for game in gamelist:
            f.write(f'  <game>\n')
            f.write(f'    <path>{game["path"]}</path>\n')
            f.write(f'  </game>\n')
          # Write the closing gameList tag to the file
          f.write('</gameList>\n')
          # Write debug message to the log
          if debug:
            logging.debug(f'Created gamelist.xml file for "{system_name}" system in devices/library/{system_name}')


# # Test the function
# # Set the system name
# system = 'megadrive'

# # Create a list to store the gamelist for the system
# gamelist = []

# # Set the path to the ROMs directory
# roms_path = 'roms'

# # Load the library file
# with open(f'templates/library.yml') as f:
#   library = yaml.safe_load(f)

# # Generate the gamelist for the system
# generate_gamelist(system, gamelist, roms_path, library, debug=True)
