

from asyncio.log import logger
import logging
import argparse
import os

class P_app():
    def __init__(self, debug=False, log_file=True) -> None:
        """_summary_

        :param debug: _description_, defaults to False
        :type debug: bool, optional
        :param log_file: _description_, defaults to True
        :type log_file: bool, optional
        """
        self.debug = debug
        self.argsparser = self.__param_parser()
        self.logger = self.__param_logger()

    def __param_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-d", "--debug", action='store_true', help="Debug mode.")
        parser.add_argument("-cf", "--config-file", help="Set config file")

        return parser

    def __param_logger(self):
        logger = logging.getLogger("logger_app")
        if self.debug == True:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)
        # console loggin
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        # file loggin
        fh = logging.FileHandler("app.log")
        fh.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)

        logger.addHandler(sh)
        logger.addHandler(fh)

        return logger
