import redis
import sys
import getopt


# start redis client with a port number
def startRedisClient(hostServer, portNumber):

    print "Start connecting Redis server %s via port %d.................................." % (hostServer, portNumber)

    try:
        client = redis.Redis(host=hostServer, port=portNumber, db=0)
        return client

    except Exception as e:
        print "Got exception from connecting redis server: \n%s" % e
        sys.exit(2)


# start application
def startApplication(redisServer):

    print "Start application ............................................................"

    subscribing = False
    selectedBoard = ""
    channel = None

    while True:
        try:
            if subscribing:
                print "Start listening to "
                for message in channel.listen():
                    print message

            cmd = raw_input('Enter your command: ')
            args = str.strip(cmd).split(" ")
            print args

            if args[0] == "select":
                if len(args) < 2:
                    print "Please enter a board name to read using: select <board_name>"
                else:
                    selectedBoard = args[1]

            elif args[0] == "quit":
                break

            elif selectedBoard == "":
                print "Please select a board to read using: select <board_name>"
                continue

            elif args[0] == "read":
                print "Read a board: %s" % selectedBoard
                print redisServer.lrange(selectedBoard, 0, -1)

            elif args[0] == "write":
                if len(args) < 2:
                    print "please write some message"
                else:
                    pushMessage = ' '.join(args[1:])
                    redisServer.lpush(selectedBoard, pushMessage)
                    redisServer.publish(selectedBoard, pushMessage)
                    print "write message: \"%s\" to board %s" % (pushMessage, selectedBoard)
                
            elif args[0] == "listen":
                print "Listen a board: %s" % selectedBoard
                subscribing = True
                channel = redisServer.pubsub()
                channel.subscribe(selectedBoard)

            # elif args[0] == "stop":
            #     subscribing = False
            #     print "Stop listen to board %s" % selectedBoard

            else:
                print "Input format wrong"

        except KeyboardInterrupt:
            print "Stop listen to board %s" % selectedBoard
            subscribing = False

        # catch all other exception
        except Exception as e:
            print "Got an unexpected exception: \n%s" % str(e)


# main function
def main(argv):
    # default port number for redis server
    portNumber = 6379
    try:
        opts, args = getopt.getopt(argv, "p:", ["portNumber="])

        for opt, arg in opts:
            if opt in ("-p", "--portNumber"):
                portNumber = int(arg)

        print 'Port number for redis server is %d' % portNumber

    # catch format error
    except getopt.GetoptError:
        print 'test.py -p <portNumber>'
        sys.exit(2)
    # catch port number exception
    except ValueError as valExc:
        print "invalid port number exception: \n%s" % valExc
        sys.exit(2)
    # catch all other exception
    except Exception as e:
        print "Got an unexpected exception: \n%s" % str(e)

    # connect redis server
    client = startRedisClient('localhost', portNumber)

    # start application
    startApplication(client)


if __name__ == "__main__":
    main(sys.argv[1:])
