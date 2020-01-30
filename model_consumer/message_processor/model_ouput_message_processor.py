from config.global_configs import PREDICTION_OUTPUT_COLLECTION_NAME
from dao.prediction_dao import PredictionDAO
from message_processor.processor import Processor
import json


class ModelOutputMessageProcessor(Processor):

    def __init__(self, db):
        self.preds_dao = PredictionDAO(db)

    def process(self, model_output_message_str):
        self.preds_dao.insert(json.loads(model_output_message_str))
