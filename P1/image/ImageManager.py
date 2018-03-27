from Config import LOGGER_NAME
from Image import Image

import logging

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
        self.imageDict = {}
        self.numImage = 0
        self.logger = logging.getLogger(LOGGER_NAME)

    def addImages(self, fname):
        """
        Added image types from a configuration file

        Args:
            fname (str): name of the file to read the configuration
        """
        try:
            with open(fname, 'r') as f:
                lines = f.readlines()
                self.numImage += int(lines[0])
                images = lines[1:]
                for image in images:
                    tokens = image.split(" ")
                    self.imageDict[tokens[0]] = Image(name=tokens[0], path=tokens[1])
            f.close()

        except Exception:
            self.logger.debug(str(Exception))
            return False

        return True

    def show(self):
        """
        Display information about the image available
        """
        print "======================================== Image List ========================================"
        for key in self.imageDict:
            print "Image name: %s" % key
            self.imageDict[key].show()
        return True
