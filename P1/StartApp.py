from AggieStack import AggieStack
import StackLogger
from parser.CommandParser import Parser

def runStack():
    """
    start the Aggie Stack
    """
    print "======================================== Aggie Stack start running ========================================"
    return AggieStack.getStack()


if __name__ == "__main__":
    # global logger
    logger = StackLogger.createLogger()
    logger.info("start running aggie stack")
    # start aggie stack
    myStack = runStack()
    # myStack.hardwareManager.addHardware("p1/hdwr-config.txt")
    # myStack.imageManager.addImages("p1/image-config.txt")
    # myStack.flavorManager.addFlavor("p1/flavor-config.txt")
    #
    # myStack.createInstance("sm1", "linux-ubuntu-16", "small")
    # myStack.createInstance("lg1", "linux-ubuntu-96", "large")
    # myStack.createInstance("xlg1", "linux-ubuntu-64", "xlarge")

    # start parser
    myParser = Parser(myStack)
    myParser.parse()
