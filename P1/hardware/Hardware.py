class Hardware:
    """
    This is the class that used to represent one physical machines

    Attributes:
        name (str): name of the server
        ip (str): IP address of the server
        memSize (int): amount of RAM in GB
        numDisk (int): number of virtual disks the machine can accommodate locally
        numVcpu (int): number of virtual CPUs cores that the hardware can accommodate
    """

    def __init__(self, name, ip, memSize, numDisk, numVcpu):
        """
        constructor of Hardware class

        Args:
            name (str): name of the server
            ip (str): IP address of the server
            memSize (int): amount of RAM in GB
            numDisk (int): number of virtual disks the machine can accommodate locally
            numVcpu (int): number of virtual CPUs cores that the hardware can accommodate
        """
        self.name = name
        self.ip = ip
        self.memSize = memSize
        self.numDisk = numDisk
        self.numVcpu = numVcpu

    def show(self):
        print " name: %s\n ip: %s\n mem: %d\n num-disks: %d\n num-vcpus: %d\n" \
              % (self.name, self.ip, self.memSize, self.numDisk, self.numVcpu)
