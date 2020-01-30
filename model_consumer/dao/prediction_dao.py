from config.global_configs import PREDICTION_OUTPUT_COLLECTION_NAME
from db.db import db


class PredictionDAO:

    def __init__(self,  db):
        self.db = db
        self.collection = self.db.get_collection(PREDICTION_OUTPUT_COLLECTION_NAME)

    def insert(self, obj):
        self.collection.insert_one(obj)

    def find(self, prediction_id: str):
        return self.collection.find({"prediction_id": prediction_id})

    def find_query(self, query):
        return self.collection.find(query)


instance = PredictionDAO(db)


def find_prediction(prediction_id: str):
    return instance.find(prediction_id)


def execute_find_query(query):
    return instance.find_query(query)