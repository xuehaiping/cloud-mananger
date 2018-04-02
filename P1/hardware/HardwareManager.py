from Config import LOGGER_NAME
from hardware.Hardware import Hardware

import logging


class HardwareManager:
    """
    HardwareManager class will contains all hardware information and status for AggieStack

    Attributes:
        hardwareList (list): list for all Hardware
        numHardware (int): numbers of hardware in current AggieStack
    """

    def __init__(self):
        """
        constructor of HardwareManager class
        """
        self.hardwareDict = {}
        self.rackDict = {}
        self.numHardware = 0
        self.logger = logging.getLogger(LOGGER_NAME)

    def addHardware(self, fname):
        """
        Added a list of hardware from a configuration file

        Args:
            fname (str): name of the file to read the configuration
        """
        try:
            with open(fname, 'r') as f:
                lines = f.readlines()
                self.numHardware += int(lines[0])
                hardwares = lines[1:]
                for hardware in hardwares:
                    tokens = hardware.split(" ")
                    self.hardwareDict[tokens[0]] = Hardware(name=tokens[0],
                                                            ip=tokens[1],
                                                            memSize=int(tokens[2]),
                                                            numDisk=int(tokens[3]),
                                                            numVcpu=int(tokens[4]))
            f.close()

        except Exception as e:
            self.logger.exception(e)
            return False

        return True

    def show(self):
        """
        Display information about the hardware hosting the cloud
        """
        print "======================================== Hardware List ========================================"
        for key in self.hardwareDict:
            print "Hardware name: %s" % key
            self.hardwareDict[key].show()
        return True

    def showRemainCapacity(self):
        """
        show remainCapacity for all hardware
        """
        print "============================== Remaining Hardware Capacity List =============================="
        for key in self.hardwareDict:
            print "Hardware name: %s" % key
            self.hardwareDict[key].showRemainCapacity()
        return True

    def removeInstance(self, instName, serverName):
        """
        remove instance from a specific hardware
        """
        if serverName in self.hardwareDict:
            return self.hardwareDict[serverName].remove(instName)
        else:
            print "No hardware %s in hardware manager" % serverName
            return False
