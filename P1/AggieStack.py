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
               print "server %s do not have enough capacity to host the flavor %s" % (machineName, flavor)

        except Exception as e:
            print "Exception raised, please check the log"
            self.logFailure(e)
            return False

        return True

    def createInstance(self, name, image, flavor):
        """
        create a instance if a existing server can host it
        """
        if image not in self.imageManager.imageDict or flavor not in self.flavorManager.flavorDict:
            print "image or flavor not being added."
            return False

        hardware = self.hardwareManager.hardwareDict
        for machine in hardware:
            if self.hardwareManager.hardwareDict[machine].canHost(self.flavorManager.flavorDict[flavor]):
                print "Machine %s can host %s with flavor %s" % (machine, name, flavor)
                newInstance = self.InstanceManager.createInstance(name=name,
                                                                  image=self.imageManager.imageDict[image],
                                                                  flavor=self.flavorManager.flavorDict[flavor],
                                                                  server=machine)
                if newInstance is not None:
                    hardware[machine].host(newInstance)
                    return True
                else:
                    return False
        return False

    def deleteInstance(self, name):
        """
        remove a instance
        """
        if name in self.InstanceManager.instanceDict \
            and self.hardwareManager.removeInstance(name, self.InstanceManager.instanceDict[name].hostServer) \
            and self.InstanceManager.remove(name):
            return True
        return False

