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
        self.hardwareList = []
        self.numHardware = 0

    def addHardware(self, fname):
        """
        Added a list of hardware from a configuration file

        Args:
            fname (str): name of the file to read the configuration
        """

    def show(self):
        """
        Display information about the hardware hosting the cloud
        """
        pass
