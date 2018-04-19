class Rack:
    """
    This is the class that used to represent one rack

    Attributes:
        name (str): name of the rack
        capacity (int): capacity of rack
    """

    def __init__(self, name, capacity):
        """
        constructor of Hardware class

        Args:
            name (str): name of the rack
            capacity (int): capacity of rack
            imageList (list): list of image the current rack is caching
        """
        # hardware information
        self.name = name
        self.capacity = capacity

        # remain capacity
        self.remainCap = capacity
        self.imageDict = {}

    def show(self):
        """
        show rack specs
        """
        print " name: %s\n remain capacity: %d\n" \
              % (self.name, self.remainCap)


    def canHost(self, image):
        """
        check if the rack cache can host the image with spec
        """
        if self.remainCap >= image.capacity:
            return True

        return False

    def host(self, image):
        """
        host a instance
        """
        self.remainCap -= image.capacity
        self.imageDict[image.name] = image
        return True

    def remove(self, imgName):
        """
        remove a image
        """
        if imgName in self.imageDict:
            self.remainCap += self.imageDict[imgName].capacity
            del self.imageDict[imgName]
            return True
        print "No image %s found in rack %s" % (imgName, self.name)
        return False

