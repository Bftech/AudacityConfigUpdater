import configparser
import requests
import logging
import os, sys
import PySimpleGUI as sg

APP_NAME = "Adacity Config Updater"
REMOTE_CONFIG_URL = "https://raw.githubusercontent.com/Bftech/AudacityConfigUpdater/dev/remote_configs/ANA.cfg"


def getOSConfigPath(platform):
    if platform == 'win32' or platform == 'cygwin':
        local_config_path = os.getenv('APPDATA') + "\\audacity\\audacity.cfg"  # TODO : A verifier
    elif platform == 'linux':
        local_config_path = os.getenv('HOME') + "/.audacity-data/audacity.cfg"

    return local_config_path

def UpdateConfig(path, remote_cfg):
    try:
        config = configparser.ConfigParser()
        config.read_string(requests.get(remote_cfg).text)
        logging.info("Fetching remote cfg...")
        
        with open(path, 'w') as configfile:
            config.write(configfile)
            logging.info("Local cfg updated")
            sg.Popup(APP_NAME, 'La configuration d\'Audacity a été mise à jour avec succès.') 

    except requests.exceptions.RequestException as e:
        # NO INTERNET !
        logging.error("No remote cfg")
        sg.Popup(APP_NAME, 'Impossible de mettre à jour la configuration, serveur injoignable.')  

UpdateConfig(getOSConfigPath(sys.platform), REMOTE_CONFIG_URL)