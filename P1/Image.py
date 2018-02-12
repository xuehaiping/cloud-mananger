class Image:
    """
    This is the class that used to represent one Image for AggieStack

    Attributes:
            name (str): name of the image
            path (str): path of the image
    """

    def __init__(self, name, path):
        """
        constructor of flavor class

        Args:
            name (str): name of the image
            path (str): path of the image
        """
        self.name = name
        self.path = path
