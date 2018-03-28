from Flavor import Flavor
from Config import LOGGER_NAME

import logging


class FlavorManager:
    """
    FlavorManager class will contains all available instance type information and status for AggieStack

    Attributes:
        flavors (list): list for all images
        numType (int): numbers of instance type in current AggieStack
    """

    def __init__(self):
        """
        constructor of FlavorManager class
        """
        self.flavorDict = {}
        self.numType = 0
        self.logger = logging.getLogger(LOGGER_NAME)

    def addFlavor(self, fname):
        """
        Added flavor types from a configuration file

        Args:
            fname (str): name of the file to read the configuration
        """
        try:
            with open(fname, 'r') as f:
                lines = f.readlines()
                self.numType += int(lines[0])
                flavors = lines[1:]
                for flavor in flavors:
                    tokens = flavor.split(" ")
                    self.flavorDict[tokens[0]] = Flavor(instanceType=tokens[0],
                                                        memSize=int(tokens[1]),
                                                        numDisk=int(tokens[2]),
                                                        numVcpu=int(tokens[3]))
            f.close()

        except Exception as e:
            self.logger.exception(e)
            return False

        return True

    def show(self):
        """
        Display information about the instance type available
        """
        print "======================================== Flavor List ========================================"
        for key in self.flavorDict:
            print "Instance type: %s" % key
            self.flavorDict[key].show()
        return True