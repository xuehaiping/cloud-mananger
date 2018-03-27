from AggieStack import AggieStack
import StackLogger


def runStack():
    """
    start the Aggie Stack
    """
    print "======================================== Aggie Stack start running ========================================"
    return AggieStack.getStack()


if __name__ == "__main__":
    # global logger
    logger = StackLogger.createLogger()
    # start aggie stack
    myStack = runStack()
    logger.info("Start run aggie stack")
