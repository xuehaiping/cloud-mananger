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
            self.instanceManager = InstanceManager()
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

        Args:
            name (str)
            image (str)
            flavor (str)
        """
        if image not in self.imageManager.imageDict or flavor not in self.flavorManager.flavorDict:
            print "image or flavor not being added."
            return False

        iMage = self.imageManager.imageDict[image]
        fLavor = self.flavorManager.flavorDict[flavor]

        hardware = self.hardwareManager.priorHost(iMage, fLavor)
        if hardware:
            newInstance = self.instanceManager.createInstance(name=name,
                                                              image=iMage,
                                                              flavor=fLavor,
                                                              server=hardware)
            self.hardwareManager.hardwareDict[hardware].host(newInstance)
            return True
        return False

    def deleteInstance(self, name):
        """
        remove a instance
        """
        if name in self.instanceManager.instanceDict \
                and self.hardwareManager.removeInstance(name, self.instanceManager.instanceDict[name].hostServer) \
                and self.instanceManager.remove(name):
            return True
        return False

    def removeHardware(self, name, rack):
        """
        remove all virtual machines(instance) from that hardware to other available hardware,
        then delete that hardware
        """
        hardware = self.hardwareManager.hardwareDict
        if name in hardware:
            # instance object
            instanceList = self.hardwareManager.hardwareDict[name].instanceList
            for instance in instanceList:
                for machine in hardware:
                    if machine != name and \
                            hardware[machine].rackName != rack and \
                            hardware[machine].canHost(instance.flavor):
                        print "Machine %s can host %s with flavor %s" % (machine, instance.name, instance.flavor)
                        instance.hostServer = machine
                        hardware[machine].host(instance)
                        break
                if instance.hostServer == name:
                    print "No machine can host %s with flavor %s" % (instance.name, instance.flavor)
                    return False

            self.hardwareManager.remove(name)
            print "Hardware %s is removed" % name
            return True
        return False

    def evacuate(self, name):
        """
        migrate all virtual machines(instance) from servers on that rack to other available server,
        then clean that rack
        """
        hardwares = self.hardwareManager.hardwareDict
        racks = self.hardwareManager.rackDict
        if name in racks:
            for hardware in hardwares.keys():
                if hardwares[hardware].rackName == name:
                    self.removeHardware(hardware, name)
            return True
        return False


