from model_generator.model_implementor import ModelPredictor
from kafka_utls.kafka_utils import Producer, send_message_to_kafka, string_serializer
from config import kafka_global_config
import uuid
import time
import os

from swagger_server.models import PredctionGetBody, PredictionResponse

kafka_producer = Producer(os.environ['KAFKA_HOST'], string_serializer)
predictor = ModelPredictor()


def predict(body: PredctionGetBody):
    prediction = predictor.predict(body.input_data.x, body.input_data.y)
    prediction_id = str(uuid.uuid4())
    message = {"input": {"x": body.input_data.x, "y": body.input_data.y},
               "prediction": prediction,
               "timestamp": int(time.time()),
               "prediction_id": prediction_id}
    send_message_to_kafka(kafka_producer, kafka_global_config.TOPIC, message)
    response = PredictionResponse()
    response.prediction = prediction
    response.prediction_id = prediction_id
    return response
