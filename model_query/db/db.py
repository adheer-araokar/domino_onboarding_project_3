from pymongo import MongoClient


import os

from config.global_configs import DB_NAME

client = MongoClient(os.environ['MONGO_HOST'], int(os.environ['MONGO_PORT']))


def setup_schema(db_name):
    global db
    db = client[db_name]
    return db


db = setup_schema(DB_NAME)


def create_collection(collection_name):
    if db is None:
        raise Exception("Schema not setup!")
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)


def get_collection(collection_name):
    if db is None:
        raise Exception("Schema not setup!")
    if collection_name not in db.list_collection_names():
        raise Exception("Collection does not exist!")
    return db[collection_name]


def get_db():
    return db


def get_mongo_client():
    return client


# def add_car_location(message: Message, host_name: str):
#     rec = car_collection.find_one({"key": host_name})
#     if rec is None:
#         print("new"+message.key)
#         car_collection.insert_one({"key": host_name, "locations": {message.key: [message.value]}})
#     else:
#         all_cars = rec["locations"]
#         if message.key in all_cars.keys():
#             locations = rec["locations"][message.key]
#             locations.append(message.value)
#         else:
#             locations = [message.value]
#         car_collection.update_one({"key": host_name}, {"$set": {"locations."+message.key: locations}})
#
#
# def get_car_data_for_key(key: str):
#     recs = car_collection.find({"locations."+key: {"$exists": True}})
#     resp = {"locations": []}
#     locations = resp["locations"]
#     for rec in recs:
#         if rec["locations"][key] is not None:
#             locations.extend(rec["locations"][key])
#     return json_util.dumps(resp)
