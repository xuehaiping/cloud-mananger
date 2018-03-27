from flavor.FlavorManager import FlavorManager
from hardware.HardwareManager import HardwareManager
from image.ImageManager import ImageManager


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

    def showAll(self):
        """
        show images, hardware and flavors
        """
        self.hardwareManager.show()
        self.imageManager.show()
        self.flavorManager.show()
        return True
