class Instance:
    """
    This is the class that used to represent one instance(virtual server)

    Attributes:
        name (str): name of the instance
        image (Image): image this instance used
        flavor (Flavor): flavor this instance used
        hostServer (str): the server that hosts the instance
    """

    def __init__(self, name, image, flavor, hostServer):
        """
        constructor of Instance class
        """
        self.name = name
        self.image = image
        self.flavor = flavor
        self.hostServer = hostServer

    def showHostServer(self):
        """
        show host server of the instance
        """
        print "Host server of instance %s: %s" % (self.name, self.hostServer)