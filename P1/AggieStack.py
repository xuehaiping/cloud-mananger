from Config import LOGGER_NAME
from flavor.FlavorManager import FlavorManager
from hardware.HardwareManager import HardwareManager
from image.ImageManager import ImageManager

import logging

class AggieStack:
    """
    A singleton Aggie Stack class
    """
    __instance = None

    @staticmethod
    def getStack():
        """
        static method to create a stack
        """
        if AggieStack.__instance is None:
            AggieStack.__instance = AggieStack()
        return AggieStack.__instance

    def __init__(self):
        """
        constructor of stackLogger class
        """
        if AggieStack.__instance is not None:
            raise Exception("Only one Logger in this program!")
        else:
            self.flavorManager = FlavorManager()
            self.hardwareManager = HardwareManager()
            self.imageManager = ImageManager()
            self.logger = logging.getLogger(LOGGER_NAME)

    def logFailure(self, exception):
        print "Can not find machine or flavor name"
        self.logger.exception(exception)

    def showAll(self):
        """
        show images, hardware and flavors
        """
        self.hardwareManager.show()
        self.imageManager.show()
        self.flavorManager.show()
        return True

    def canHost(self, machineName, flavor):
        """
        check if the stack can host a new instance with spec
        """
        try:
            if self.hardwareManager \
                    .hardwareDict[machineName] \
                    .canHost(self.flavorManager.flavorDict[flavor]):
                print "Aggie Stack can host flavor: %s on Server: %s" % (machineName, flavor)

            else:
                self.logFailure("server % do not have enough capacity to host the flavor %s" % (machineName, flavor))

        except Exception as e:
            self.logFailure(e)
            return False

        return True
