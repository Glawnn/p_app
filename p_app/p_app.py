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

        :param debug: If you want debug your project, defaults to False
        :type debug: bool, optional
        :param log_file: If you want output log file, defaults to True
        :type log_file: bool, optional
        """
        self.log_file = log_file
        self.argsparser = self.__param_parser()
        self.args = self.argsparser.parse_args()
        self.logger = self.__param_logger()

    def __param_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-d", "--debug", action="store_true", help="Debug mode.")
        parser.add_argument("-cf", "--config-file", help="Set config file")

        return parser

    def load_config_file(self):
        if self.args['config_file'] != None:
            if os.path.isfile(self.args['config_file']):
                with open(self.args['config_file']) as json_file:
                    return json.load(json_file)
            else:
                self.logger.info("Not found")
        return None

    def load_args(self):
        return vars(self.argsparser.parse_args())

    def __param_logger(self):
        logger = logging.getLogger("logger_app")
        if self.args.debug == True:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)
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

        logger.addHandler(sh)
        if self.log_file:
            logger.addHandler(fh)

        return logger
