from Config import LOGGER_NAME
from flavor.FlavorManager import FlavorManager
from hardware.HardwareManager import HardwareManager
from image.ImageManager import ImageManager
from instance.InstanceManager import InstanceManager

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
            self.InstanceManager = InstanceManager()
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
        check if the stack can host a new instance on a server with flavor
        """
        try:
            if self.hardwareManager \
                    .hardwareDict[machineName] \
                    .canHost(self.flavorManager.flavorDict[flavor]):
                print "Aggie Stack can host flavor: %s on Server: %s" % (machineName, flavor)

            else:
               print "server % do not have enough capacity to host the flavor %s" % (machineName, flavor)

        except Exception as e:
            self.logFailure(e)
            return False

        return True

    def createInstance(self, name, image, flavor, server):
        """
        create a instance if a existing server can host it
        """
        hardware = self.hardwareManager.hardwareDict
        for machine in hardware:
            if self.canHost(machine, flavor):
                return self.InstanceManager.createInstance(name=name,
                                                           image=self.imageManager.imageDict[image],
                                                           flavor=self.flavorManager.flavorDict[flavor],
                                                           server=server)
        return False
