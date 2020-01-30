#!/usr/bin/env python3
import os
from config.global_configs import DB_NAME
from config.kafka_global_config import GROUP_ID, TOPIC
from db.db import setup_schema
from kafka_utls.kafka_utils import Consumer, string_deserializer
from message_processor.model_ouput_message_processor import ModelOutputMessageProcessor


def main():
    db = setup_schema(DB_NAME)
    message_processor = ModelOutputMessageProcessor(db)
    consumer = Consumer(os.environ['KAFKA_HOST'], GROUP_ID, TOPIC, string_deserializer, message_processor)
    consumer.consume_messages()


if __name__ == '__main__':
    main()
