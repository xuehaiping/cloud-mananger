class Image:
    """
    This is the class that used to represent one Image for AggieStack

    Attributes:
            name (str): name of the image
            capacity (int): capacity of the image
            path (str): path of the image
    """

    def __init__(self, name, capacity, path):
        """
        constructor of flavor class

        Args:
            name (str): name of the image
            capacity (int): capacity of the image
            path (str): path of the image
        """
        self.name = name
        self.capacity = capacity
        self.path = path

    def show(self):
        """
        Display information about the image
        """
        print " image name: %s;\n capacity: %s\n path; %s" \
              % (self.name, self.capacity, self.path)
