from asyncio.log import logger
from genericpath import isfile
import json
import logging
import argparse
import os


class P_app:
    """You can add_argument("-i", "--input-file") and use p_app.parse for retrieve all args."""

    def __init__(self, log_file=True) -> None:
        """Prepare loggin method. You can select debug mod for print all logs or no debug for print just info logs.
        With log_file you can output all logs in a file.

        :param log_file: If you want output log file, defaults to True
        :type log_file: bool, optional
        """
        self.log_file = log_file
        self.argsparser = self.__param_parser()
        self.logger = None

    def __param_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-d", "--debug", action="store_true", help="Debug mode.")
        parser.add_argument("-cf", "--config-file", help="Set config file")

        return parser

    def _load_config_file(self):
        if self.args['config_file'] != None:
            if os.path.isfile(self.args['config_file']):
                with open(self.args['config_file']) as json_file:
                    return json.load(json_file)
            else:
                self.logger.info("Not found")
        return {}

    def load_args(self):
        self.args = vars(self.argsparser.parse_args())
        self.__init_logger()
        for key, elem in self._load_config_file().items():
            self.args[key] = elem
        self.__init_logger()

    def __init_logger(self):
        self.logger = logging.getLogger("logger_app")
        if self.args['debug'] == True:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)
        # console loggin
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        # file loggin
        if self.log_file:
            fh = logging.FileHandler("reports/app.log")
            fh.setLevel(logging.DEBUG)

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        sh.setFormatter(formatter)
        if self.log_file:
            fh.setFormatter(formatter)

        self.logger.addHandler(sh)
        if self.log_file:
            self.logger.addHandler(fh)

        
