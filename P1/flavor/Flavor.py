
class Flavor:
    """
    This is the class that used to represent one instance type for AggieStack

    Attributes:
    type (str): type of instance
    memSize (int): amount of RAM in GB
    numDisk (int): number of virtual disks the machine can accommodate locally
    numVcpu (int): number of virtual CPUs cores that the hardware can accommodate
    """

    def __init__(self, instanceType, memSize, numDisk, numVcpu):
        """
        constructor of flavor class

        Args:
            type (str): type of instance
            memSize (int): amount of RAM in GB
            numDisk (int): number of virtual disks the machine can accommodate locally
            numVcpu (int): number of virtual CPUs cores that the hardware can accommodate
        """
        self.instanceType = instanceType
        self.memSize = memSize
        self.numDisk = numDisk
        self.numVcpu = numVcpu
