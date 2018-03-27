from Config import LOGGER_NAME

import logging


class Parser:
    """
    parser class to take in commands
    """
    def __init__(self, stack):
        self.stack = stack
        self.logger = logging.getLogger(LOGGER_NAME)

    def failurePromot(self):
        print "Input format wrong or you have invalid file name or options"
        self.logger.info("FAILURE")

    def successPromot(self):
        print "Operation succeeded!"
        self.logger.info("SUCCESS")

    def parseConfig(self, command):
        """
        parse config option
        """
        success = False
        if len(command) == 2:
            if command[0] == "--hardware":
                success = self.stack.hardwareManager.addHardware(command[1])

            elif command[0] == "--images":
                success = self.stack.imageManager.addImages(command[1])

            elif command[0] == "--flavors":
                success = self.stack.flavorManager.addFlavor(command[1])

            if success:
                self.successPromot()
            else:
                self.failurePromot()

    def parseShow(self, command):
        """
        parse show option
        """
        success = False
        if len(command) == 1:
            if command[0] == "hardware":
                success = self.stack.hardwareManager.show()

            elif command[0] == "images":
                success = self.stack.imageManager.show()

            elif command[0] == "flavors":
                success = self.stack.flavorManager.show()

            elif command[0] == "all":
                success = self.stack.showAll()

        if success:
            self.successPromot()
        else:
            self.failurePromot()

    def parse(self):
        """
        Parser for commands
        """
        while True:
            cmd = raw_input('Enter your command: ')
            self.logger.info("command: " + cmd)
            args = filter(None, str.strip(cmd).split(" "))
            # command length less than 2 is never correct
            if len(args) <= 1:
                self.failurePromot()
                continue

            if args[0] == "config":
                self.parseConfig(args[1:])

            elif args[0] == "show":
                self.parseShow(args[1:])

            elif args[0] == "quit":
                break
            else:
                self.failurePromot()
