<p float="center">
    <img src="res/RetroMan_AI_logo.png" alt="RetroMan logo" width="300"/>
</p></br>

# RetroMan
This project is still under contruction, any help is appreciated, see below.

RetroMan is a ROMs manager project that helps you to manage your roms library and sync it with your devices.
This super hero software aims to be the only solution when comes to manage your roms.

## Planned features
- Multi device support: aims to support all the devices on the market, either they are devices or softwares like Miyoo devices, Anbernic Devices, RetroDECK, Batocera, RetroPie (custom device managements as yml templates with their own rules)
- Scraping support
- RetroAchievements support
- Decide which ROMs you want to syncronize on which device with various protocols (local copy, s/ftp, smb)
- Saves backup
- It knows which system are supported or available on the device (supported = surely working, available = emulator is available but may not be really playable)
- Duplicates management
- CLI support

## Nice to have:
- Saves sync between devices if supported, or enforced
- ARCADE romsets support
- Format conversions (chd for example)
- m3u generation
- folder as a file support
- cloud storage support
- webserver
- ROMtation

## ROMtation:
A ROM rortation system: when you got a limited memory on your device the ROMtation can be enabled, if enabled it removes the oldest/unused ROMs to make space to the new ones.

## How is written?
~~Here's the fun thing: I am writing this in python using OpenAI to see how far it can go.
Of course manual action is needed by my side as the AI is not yet enough matured to write its own full software.
</br>The logo? Ah yeah, that's AI generated too and it's temporary.~~
</br>OpenAI it's not skilled enough yet, neither am I, so I will continue this work whenever I find someone collaborator more skilled then me or when I will learn a good Python (SPOILER: maybe never).

**Note:** the main branch is actually a develop branch as the software is still unmatured enough to be called even a beta.

## How it (should) work?
In your main library you can choose which ROMs to sync in which devices, each device template can tell you if that system is supported or available in the selected device (supported = playable, available = avaliable but maybe not fully playable).
When the device is connected it start to sync the ROMs and their scraped metadata and backup the saves/states.
It will scan for the device searching which ROMs are not present in your library and it asks to be imported.
On your Library will show the ROMs scraped metadata, images, boxarts, videos, RetroAchievement data and such.

### From template to actual device
Mainly the software should match the template in `template/template-id.yaml` with the device data in `devices/frienly-name/friendly-name.yml`.
The template is instructing the software how to behave regarding a specific device type, the device folder contain the actual device info.
Let's say that I got two Miyoo Minis, then I will have a single template file but in the devices folder I will have `devices/My Miyoo Mini 1/My Miyoo Mini 1.yml` and `devices/My Miyoo Mini 2/My Miyoo Mini 2.yml` that are pointing to the same template under `templates/miyoominiv3-onion.yml`

### Library template/device
Similar to above but that's the main Library where all the ROMs are synced from (and in some cases to), usually an user got a main library + devices but it's done in this way because it's forseen to implement the multi library support.

### Library and devices folder Structure
Inside every device or library folder there are system subfolders with the gamelist.xml file, for example under `devices/My Miyoo Mini` I got `megadrive/gamelist.xml` and `mastersystem/gamelist.xml`, these gamelists are identical to the EmulationStation ones.
In the Library we got the same files but there is more data to each rom such as on which devices is synced and when it was the last sync.
Then we got the media folder under Library folder for the scraped data, in the screenscraper format.

### Described by AI (maybe wrong/updated):
The `generate_retro_gamelist` function is the main function that coordinates the process of generating the game list. It does this by calling several other functions:
- `get_device_data`: Given the name of a device, this function searches for a YAML file with the same name in the devices/<device_name>/<device_name>.yml path and returns its contents.
- `get_template_data`: Given a template ID, this function searches for a YAML file with the same name in the templates/<template_id>.yml path and returns its contents.
- `get_library_data`: This function loads the contents of the templates/library.yml file.
- `update_system_data`: This function updates the system data in the given template data with the values from the library data.
The `generate_gamelist` function appears to be another function that is used to generate the game list, but it is not clear how it is used in the script.