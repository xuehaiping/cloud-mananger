class ImageManager:
    """
    ImageManager class will contains all available image information and status for AggieStack

    Attributes:
        images (list): list for all images
        numImage (int): numbers of images in current AggieStack
    """

    def __init__(self):
        """
        constructor of ImageManager class
        """
        self.images = []
        self.numImage = 0

    def addImages(self, fname):
        """
        Added image types from a configuration file

        Args:
            fname (str): name of the file to read the configuration
        """

    def show(self):
        """
        Display information about the image available
        """
        pass
