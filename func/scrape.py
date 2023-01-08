# This function takes in the list of system directories, and for each system, it reads the gamelist.xml file to get the list of roms,
# and then scrapes the data for each rom and saves it in the corresponding system's media folder.
# You will need to replace the devid and apikey values in the URL with your own values from screenscraper.fr.

# You can call this function after calling the scan function to scrape the missing data for each system's roms.

import os
import requests
from yaml import load
from bs4 import BeautifulSoup
from xml.etree import ElementTree

def scrape(friendly_name: str):
  # Load the device file using the friendly name
  with open(f'devices/{friendly_name}/{friendly_name}.yml') as f:
    device = load(f)
  
  # Load the template file using the ID of the device
  with open(f'templates/{device["id"]}.yml') as f:
    template = load(f)
  
  # loop through the supported systems of the device
  for system in template["supported_systems"]:
    # read the gamelist.xml file for this system
    gamelist_path = os.path.join('devices', friendly_name, system, 'gamelist.xml')
    gamelist_xml = ElementTree.parse(gamelist_path)
    # loop through each game in the gamelist.xml file
    for game in gamelist_xml.findall('game'):
      # get the rom's filename
      rom = game.find('path').text
      # scrape the data for this rom from the website
      url = "http://www.screenscraper.fr/api2/jeuInfos.php?devid=xxxx&apikey=xxxx&rom=" + rom
      response = requests.get(url)
      soup = BeautifulSoup(response.text, 'html.parser')
      # extract the relevant data from the scraped page
      name = soup.find('nomjeu').text
      desc = soup.find('description').text
      image = soup.find('image').text

      # create the media folder for this system if it doesn't exist
      media_dir = os.path.join('devices', friendly_name, system, 'media')
      if not os.path.exists(media_dir):
        os.makedirs(media_dir)

      # save the scraped data in the media folder
      with open(os.path.join(media_dir, rom + '.txt'), 'w') as f:
        f.write(name + '\n')
        f.write(desc + '\n')
        f.write(image + '\n')



# To use this function, you would call it like this:
# scrape('My Miyoo Mini')
# This will load the device file and the template file for the device with the friendly name "My Miyoo Mini",
# and then scrape the data for all the roms in the device's supported systems and save it in the media folder.
