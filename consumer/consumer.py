import time
import json
import stomp

from quixstreams import Application

"""
Receives messages from Artemis broker and creates Producer for Kafka, 
sending a valid messages to a Kafka Consumer 

"""

def send_data_from_artemis_message_to_kafka(payload):

    """    app = Application(
        broker_address="localhost:9092",
        loglevel="DEBUG",
        )
    """
    app = Application(broker_address="localhost:9092/bootstrap")

    with app.get_producer() as producer:


        producer.produce(
            topic="poc-cola",
            key="message",
            value=str(payload)
        )
        print("Message sent to Kafka topic +++")


# Artemis Consumer
class MyListener(stomp.ConnectionListener):
    def on_message(self, message):
        print(f"Received message: {message}")
        print(message.body)
        send_data_from_artemis_message_to_kafka(message.body)




    def on_error(self, message):
        print(f"Error: {message}")

    def on_disconnected(self):
        print("Disconnected from the broker")

# Connect to the broker
def connect_to_broker():
    conn = stomp.Connection([('localhost', 61613)])
    conn.set_listener('', MyListener())
    conn.connect('admin', 'admin', wait=True)
    return conn


def subscribe_to_queue(conn, queue_name):
    conn.subscribe(destination=queue_name, id=1, ack='auto')



if __name__ == "__main__":
    queue_name = 'poc-cola'
    while True:
        connection = connect_to_broker()
        subscribe_to_queue(connection, queue_name)



