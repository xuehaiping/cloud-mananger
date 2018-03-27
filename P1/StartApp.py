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
    # start parser
    myParser = Parser(myStack)
    myParser.parse()
