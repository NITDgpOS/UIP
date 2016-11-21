import os
import json, argparse

HOME_DIR = os.path.join(os.path.expanduser("~"), '.uip')
NUMBER_OF_IMAGES_TO_PARSE = 24
DEFAULT_PICS_FOLDER = os.path.join(os.path.expanduser("~"), 'pics')

settings_file_path = os.path.join(HOME_DIR, "settings.json")

class ParseSettings:

    def __init__(self):
        self.settings = self.get_settings_from_file()
        self.settings.update(self.get_settings_from_cli())

    def get_settings_from_file(self):
        with open(settings_file_path, "r") as settings_file:
            settings = json.loads(settings_file.read())

        return settings

    def get_settings_from_cli(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--offline", action="store_true",
                        help="Runs UIP in offline mode.")
        parser.add_argument("--flush", action="store_true",
                        help="Delete all downloaded wallpapers"
                             " and downloads new ones. "
                             "When combined with --offline,"
                             " deletes the wallpapers and exits.")
        args = parser.parse_args()
        settings = {'offline' : args.offline, 'flush' : args.flush}
        return settings
