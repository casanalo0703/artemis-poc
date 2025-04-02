import random
import time

import stomp
from lorem_text import lorem

# Configuración del servidor Artemis en Docker
ARTEMIS_HOST = 'localhost'
ARTEMIS_PORT = 61613 
QUEUE_NAME = 'poc-cola'

class ArtemisListener(stomp.ConnectionListener):
    """
    Artemis Base class to handle connection and message reception.
    """
    def on_error(self, headers, message):
        """
        Callback method to handle errors."""
        print(f'Error: {message}')

    def on_message(self, headers, message):
        """
        Callback method to handle received messages.
        """
        print(f'Received message: {message}, With headers: {headers}')

conn = stomp.Connection([(ARTEMIS_HOST, ARTEMIS_PORT)])
conn.set_listener('', ArtemisListener())
conn.connect('admin', 'admin', wait=True)
while True:
    try:
        conn.send(
            body=f'Test message!! {random.randint(1,4)}',
            destination=f'{QUEUE_NAME}',
            headers={'persistent': 'true'},
        )

        print(f'Message sent {QUEUE_NAME}')
        time.sleep(2)
    except KeyboardInterrupt:
        print("\nDisconnecting...")
        break

conn.disconnect()