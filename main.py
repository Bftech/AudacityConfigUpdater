import configparser
import requests
import logging
import os, sys

config = configparser.ConfigParser()

config['Spectrum'] = {'MinFreq' : '200',
                      'MaxFreq' : '15000',
                      'Range' : '75',
                      'Gain' : '15',
                      'FrequencyGain' : '15',
                      'FFTSize' : '1024',
                      'ZeroPaddingFactor' : '1',
                      'WindowType' : '3',
                      'Grayscale' : '1',
                      'ScaleType' : '0',
                      'EnableSpectralSelection' : '0',
                      'Algorithm' : '0'}

config['GUI'] = {'DefaultViewModeNew' : '2',
                 'Theme' : 'dark'}

# [Spectrum]
# MinFreq = 200
# MaxFreq = 15000
# Range = 75
# Gain = -12
# FrequencyGain = 15
# FFTSize = 1024
# ZeroPaddingFactor = 1
# WindowType = 3
# Grayscale = 1
# ScaleType = 0
# EnableSpectralSelection = 0
# Algorithm = 0

# [GUI]
# DefaultViewModeNew = 2
# Theme=dark

remote_config_url = "https://raw.githubusercontent.com/Bftech/AudacityConfigUpdater/dev/remote_configs/ANA.cfg"

platform = sys.platform
if platform == 'win32' or platform == 'cygwin':
    local_config_path = os.getenv('APPDATA') + "\audacity\audacity.cfg"  # TODO : A verifier
elif platform == 'linux':
    local_config_path = ""


try:
    logging.log(logging.INFO, "Fetching remote cfg...")
    remote_config = requests.get(remote_config_url).text
    
    config.read_string(remote_config)

    with open(local_config_path, 'w') as configfile:
        config.write(configfile)

except requests.exceptions.RequestException as e:
    # NO INTERNET !
    logging.log(logging.ERROR, "No remote cfg")
    pass 

