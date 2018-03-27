class FlavorManager:
    """
    FlavorManager class will contains all available instance type information and status for AggieStack

    Attributes:
        flavors (list): list for all images
        numType (int): numbers of instance type in current AggieStack
    """

    def __init__(self):
        """
        constructor of FlavorManager class
        """
        self.flavors = []
        self.numType = 0

    def addImages(self, fname):
        """
        Added image types from a configuration file

        Args:
            fname (str): name of the file to read the configuration
        """

    def show(self):
        """
        Display information about the instance type available
        """
        pass
