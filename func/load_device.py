import os
import yaml
import logging

from generate_gamelist import generate_gamelist


def get_device_data(device_name):
    """
    Given the name of a device, this function searches for a YAML file with the same name
    in the devices/<device_name>/<device_name>.yml path, and returns its contents.
    """

    # Set up logging
    logging.basicConfig(filename='retroman.log', level=logging.DEBUG, format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.debug(f'Called get_device_data for: {device_name}')

    # Compute the path of the device file
    device_path = f'devices/{device_name}/{device_name}.yml'

    # Check if the file exists
    if not os.path.isfile(device_path):
        logging.error(f"Device file not found: {device_path}")
        raise ValueError(f"Device file not found: {device_path}")

    # Load the data from the YAML file
    with open(device_path) as f:
        data = yaml.full_load(f)

    logging.debug(f"Device data: {data}")

    # Return the data as a dictionary
    return data


def get_template_data(template_id):
    """
    Given a template ID, this function searches for a YAML file with the same name
    in the templates/<template_id>.yml path, and returns its contents.
    """

    logging.debug(f"Calling get_template_data for template ID: {template_id}")

    # Compute the path of the template file
    template_path = f'templates/{template_id}.yml'
    logging.debug(f"Template path: {template_path}")

    # Check if the file exists
    if not os.path.isfile(template_path):
        logging.debug(f"Template file not found: {template_path}")
        raise ValueError(f"Template file not found: {template_path}")

    # Load the YAML file
    with open(template_path, 'r') as f:
        # Parse the YAML file using yaml.safe_load
        template_data = yaml.safe_load(f)

    # Print the template data for debugging purposes
    logging.debug(f"Template data: {template_data}")
    logging.debug('Returning it')

    return template_data[template_id]


def get_library_data():
    """
    This function loads the contents of the templates/library.yml file.
    """

    # Set up logging
    logging.basicConfig(filename='retroman.log', level=logging.DEBUG, format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.debug('Called get_library_data')

    # Compute the path of the library file
    library_path = 'templates/library.yml'

    # Check if the file exists
    if not os.path.isfile(library_path):
        logging.error(f"Library file not found: {library_path}")
        raise ValueError(f"Library file not found: {library_path}")

    # Load the YAML file
    with open(library_path, 'r') as f:
        library_data = yaml.safe_load(f)

    logging.debug(f'Returing library data: {library_data}')

    return library_data


def update_system_data(data, library_data):
    """
    This function updates the system data in the given data with the values from the library data.
    """

    # Check if the data dictionary has a 'systems' key
    if 'systems' not in data:
        raise KeyError("The data dictionary does not have a 'systems' key")

    # Get the list of systems from the data
    systems = data['systems']
    library_systems = library_data['library']['systems']

    # TODO: parse the supported systems
    # TODO: parse the available systems

    # Return the updated data
    return library_systems


def generate_retro_gamelist(device_name, debug=False):
    """
    This is the main function that generates the retro game list for the given device.
    """

    # Set up logging
    logging.basicConfig(filename='retroman.log', level=logging.DEBUG if debug else logging.INFO,
                        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.debug(f'Called generate_retro_gamelist for device name: {device_name}')

    # Get the device data from the YAML file
    device_data = get_device_data(device_name)

    # Get the template data
    template_id = device_data['id']
    template_data = get_template_data(template_id)

    # Get the library data
    library_data = get_library_data()

    # Update the system data in the template data
    systems = update_system_data(template_data, library_data)

    # Initialize the game list
    gamelist = []

    # Iterate through the supported systems
    for system in systems:
        # Get the system name and the ROMs path from the system data
        system_id = list(system.keys())[0]
        system_name = system[system_id]['name']
        roms_path = template_data['roms_path']

        # Generate the game list for the current system
        # FIXME match the parameters with the definition of this function
        gamelist = generate_gamelist(system, gamelist, roms_path, library_data, debug)

    return gamelist


# # Test the get_device_data function
# device_name = 'My Miyoo Mini'
# device_data = get_device_data(device_name)
# print(f'Device data for {device_name}: {device_data}')

# # Test the get_template_data function
# template_id = device_data['id']
# template_data = get_template_data(template_id)
# print(f'Template data for {template_id}: {template_data}')

# # Test the get_library_data function
# library_data = get_library_data()
# print(f'Library data: {library_data}')

# # Test the update_system_data function
# systems = update_system_data(template_data, library_data)
# print(f'Supported systems: {systems}')

# # Test the generate_retro_gamelist function
# gamelist = generate_retro_gamelist(device_name)
# print(f'Game list for {device_name}: {gamelist}')

generate_retro_gamelist("My Miyoo Mini", debug=True)
