from kafka import KafkaProducer, KafkaConsumer
import json

from message_processor.processor import Processor


class Producer:

    def __init__(self, hosts, value_serializer):
        self.producer = KafkaProducer(bootstrap_servers=hosts, value_serializer=value_serializer)

    def get_producer(self):
        return self.producer

    def send_message(self, topic, message):
        self.get_producer().send(topic, value=message)
        self.get_producer().flush()


class Consumer:

    def __init__(self, hosts, group_id, topic, value_deserializer, message_processor: Processor):
        self.consumer = KafkaConsumer(bootstrap_servers=hosts,
                                      value_deserializer=value_deserializer,
                                      group_id=group_id,
                                      # auto_offset_reset='earliest',
                                      enable_auto_commit=False)
        self.consumer.subscribe([topic])
        self.message_processor = message_processor

    def consume_messages(self):
        for message in self.consumer:
            try:
                self.message_processor.process(message.value)
            except Exception as e:
                raise e
            self.consumer.commit()


def send_message_to_kafka(producer: Producer, topic: str, message: dict):
    message_json_str = json.dumps(message)
    producer.send_message(topic, message_json_str)


def string_serializer(message):
    return message.encode('utf-8')


def string_deserializer(json_str):
    return json_str.decode('utf-8')
