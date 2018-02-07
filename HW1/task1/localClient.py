import pymongo
import json
from pprint import pprint


# create local database
def createDb():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.hw

    with open('initial.json') as f:
        json_data = json.load(f)

    result = db.fitness_122006286.insert_many(json_data)

    pprint(result.inserted_ids)


# insert json file with multiple json to database
def insertJsonFile(fname, collection):
    with open(fname) as f:
        json_data = json.load(f)

    result = collection.insert_many(json_data)

    pprint(result.inserted_ids)


# insert one json into collection
def insertJson(jsonObject, collection):
    try:
        collection.insert_one(jsonObject)
        print "\nRecords updated successfully\n"

    except Exception, e:
        print str(e)


# update one employee in collection
def updateEmployeeInfo(collection, jsonObject):
    try:
        collection.update_one(
            {'uid': jsonObject["uid"]},
            {"$set": jsonObject}
        )
        print "\nRecords updated successfully\n"

    except Exception, e:
        print str(e)


# find number of employees in the collection
def numberOfEmployee(collection):
    return collection.count()


# find active employees in the collection
def activeEmployee(collection):
    res = collection.find({"tags": "active"})
    for doc in res:
        pprint(doc)


# find employees that have a goal step count greater than 5000 steps
def goalStep(collection):
    res = collection.find({'goal.stepGoal': {"$gt": 5000}})
    for doc in res:
        pprint(doc)


# aggregate the total activity duration for each employee
def aggregateActDuration(collection):
    pipeline = [
        {'$project':
            {
                'uid': 1,
                'total_activity_duration':
                    {
                        '$reduce':
                            {
                                'input': '$activityDuration',
                                'initialValue': 0,
                                'in': {
                                    '$add': ['$$value', '$$this']
                                }
                            }
                    }
            }
        },

        {'$project':
            {
                'uid': 1,
                'total_activity_duration': {'$ifNull': ['$total_activity_duration', 0]}
            }
        }
    ]

    res = collection.aggregate(pipeline)
    for doc in res:
        pprint(doc)


# get target collection
targetCollection = pymongo.MongoClient('localhost', 27017).hw.fitness_122006286
#
# # insert documents in json file into collection
# insertJsonFile(fname='dummy-fitness.json', collection=targetCollection)

# read the json
# with open("user1001-new.json") as f:
#     jsonObject = json.load(f)
#
# # update the document with uid 1001
# updateEmployeeInfo(targetCollection, jsonObject)
#
# # print current number of employees in database
# print "Number of employees in AggieFit database: %d" % numberOfEmployee(targetCollection)

# # find employees who have been tagged as "active"
# activeEmployee(targetCollection)

# # find employees that have a goal step count greater than 5000 steps
# goalStep(targetCollection)

# # aggregate the total activity duration for each employee
# aggregateActDuration(targetCollection)

# resCollection = pymongo.MongoClient('localhost', 27017).hw.fitness_122006286
#
# RQ0 = resCollection.find()
# for data in RQ0:
#     pprint(data)



