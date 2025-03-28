import stomp
import time

class MyListener(stomp.ConnectionListener):
    def on_message(self, message):
        print(f"Received message: {message}")
  

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
    conn.subscribe(destination=f'{queue_name}', id=1, ack='auto')  
    print(f"Subscribed to queue: {queue_name}")


if __name__ == "__main__":
    try:
       
        connection = connect_to_broker()

        
        queue_name = 'poc-cola'
        subscribe_to_queue(connection, queue_name)

       
        while True:
            time.sleep(1)  
    except KeyboardInterrupt:
        print("Consumer interrupted by user")
    finally:
       
        connection.disconnect()
        print("Disconnected from the broker")
