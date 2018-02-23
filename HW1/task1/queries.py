from mongo_connect import connectMongo
import json
from pprint import pprint


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
        print "\nJson file inserted successfully\n"

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
    print "\nActive Employee List\n"
    res = collection.find({"tags": "active"})
    for doc in res:
        pprint(doc)


# find employees that have a goal step count greater than 5000 steps
def goalStep(collection):
    print "\nEmployees that have a goal step count greater than 5000 steps\n"
    res = collection.find({'goal.stepGoal': {"$gt": 5000}})
    for doc in res:
        pprint(doc)


# aggregate the total activity duration for each employee
def aggregateActDuration(collection):
    print "\nTotal activity duration for each employee:\n"
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


targetCollection = connectMongo()

# # WQ1. Add the data in dummy-fitness.json to the MongoDB database
# # insert documents in json file into collection
# insertJsonFile(fname='dummy-fitness.json', collection=targetCollection)

# # WQ2. Update the database with data from user1001-new
# # read the json
# with open("user1001-new.json") as f:
#     jsonObject = json.load(f)
#
# # update the document with uid 1001
# updateEmployeeInfo(targetCollection, jsonObject)

# # RQ1. Count the number of employees whose data is in the AggieFit database.
# print current number of employees in database
print "Number of employees in AggieFit database: %d" % numberOfEmployee(targetCollection)

# # RQ2. Retrieve employees who have been tagged as active
# find employees who have been tagged as "active"
activeEmployee(targetCollection)

# # RQ3. Retrieve employees that have a goal step count greater than 5000 steps
# find employees that have a goal step count greater than 5000 steps
goalStep(targetCollection)

# # RQ4. Aggregate the total activity duration for each employee. If the employee does not
# # have activity duration in their data, you can report their total activity duration as 0.
# aggregate the total activity duration for each employee
aggregateActDuration(targetCollection)

#### FIND ALL ENTRIES IN THE DATABASE #####
# # Assuming RQ0 is the query to find all entries in the database
# RQ0 = targetCollection.find()
# for data in RQ0:
#     pprint(data)


