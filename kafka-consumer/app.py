from kafka import KafkaConsumer
import time
import signal
import sys

# Kafka broker configuration
KAFKA_BROKER = 'localhost:9092'
TOPIC_NAME = 'poc-cola'

def consume_messages():
    """
    Listens to messages from the specified Kafka topic indefinitely.
    Reconnects in case of errors.
    """
    while True:
        try:
            consumer = KafkaConsumer(
                TOPIC_NAME,
                bootstrap_servers=[KAFKA_BROKER],
                auto_offset_reset='earliest',
                enable_auto_commit=True,  
                group_id='my-group',
                value_deserializer=lambda x: x.decode('utf-8')
            )

            print(f"Listening to messages on topic '{TOPIC_NAME}'...")

            # Consume messages
            for message in consumer:
                print(f"Received message: {message.value}")

        except Exception as e:
            print(f"Error while consuming messages: {e}")
            print("Retrying in 5 seconds...")
            time.sleep(5)  # Wait before retrying

def signal_handler(sig, frame):
    """
    Handles the SIGINT signal (Ctrl+C) to gracefully stop the consumer.
    """
    print("\nStopping consumer...")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    consume_messages()