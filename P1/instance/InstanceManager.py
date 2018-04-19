from Config import LOGGER_NAME
from Instance import Instance

import logging


class InstanceManager:
    """
    InstanceManager class will contains all instance that is currently running

    Attributes:
        numInstances (int): number of instances in the stack
        instanceList (list): list of instances
        logger (Logger): global logger
    """

    def __init__(self):
        """
        constructor of ImageManager class
        """
        self.numInstances = 0
        self.instanceDict = {}
        self.logger = logging.getLogger(LOGGER_NAME)

    def createInstance(self, name, image, flavor, server):
        """
        create a instance
        """
        if name not in self.instanceDict:
            self.instanceDict[name] = Instance(name=name, image=image, flavor=flavor, hostServer=server)
            self.numInstances += 1
            return self.instanceDict[name]
        else:
            print "Instance name already exist, please use another name."
            return None

    def show(self):
        """
        show host server for each instance
        """
        for instance in self.instanceDict:
            self.instanceDict[instance].showHostServer()
        return True

    def remove(self, instName):
        """
        remove a instance by name

        instName (str)

        """
        if instName not in self.instanceDict:
            print "No instance %s in instance Manager" % instName
            return False
        else:
            del self.instanceDict[instName]
            return True

    def showAllInstance(self):
        """
        show all instances in the manager
        """
        print "======================================== instance List ========================================"
        for instance in self.instanceDict:
            print "Instance %s" % instance
            self.instanceDict[instance].show()
        return True
