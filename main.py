import configparser
import requests
import logging
import os, sys

remote_config_url = "https://raw.githubusercontent.com/Bftech/AudacityConfigUpdater/dev/remote_configs/ANA.cfg"

platform = sys.platform
if platform == 'win32' or platform == 'cygwin':
    local_config_path = os.getenv('APPDATA') + "\\audacity\\audacity.cfg"  # TODO : A verifier
elif platform == 'linux':
    local_config_path = "~/.audacity-data/audacity.cfg"


def writeConfig():
    try:
        config = configparser.ConfigParser()
        logging.log(logging.INFO, "Fetching remote cfg...")
        remote_config = requests.get(remote_config_url).text
        
        config.read_string(remote_config)

        with open(local_config_path, 'w') as configfile:
            config.write(configfile)
            logging.log(logging.info, "Local cfg updated")

    except requests.exceptions.RequestException as e:
        # NO INTERNET !
        logging.log(logging.ERROR, "No remote cfg")