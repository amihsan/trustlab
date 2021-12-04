import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from pympler import asizeof
from trustlab.lab.config import WEBSOCKET_MAX


class ChunkAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    """
    A websocket consumer for async handling with only json messages and the capability of chunked transfer.
    """

    async def send_websocket_message(self, message):
        """
        Handles all out going websocket messages to not overflow the size of one message handable for the websocket
        connection. Thus, this function introduces chunked transfer of the given message if required. The maximum size
        of one message is set in config with parameter WEBSOCKET_MAX.py

        :param message: The message to be send as JSON object via the websocket connection.
        :type message: dict or list
        """
        message_size = asizeof.asizeof(message)
        if message_size < WEBSOCKET_MAX:
            await self.send_json(message)
        else:
            message_str = json.dumps(message)
            parts = [message_str[i:i + WEBSOCKET_MAX] for i in range(0, len(message_str), WEBSOCKET_MAX)]
            for number, part in enumerate(parts, 1):
                print(f'Transferring part {number}/{len(parts)} ...')
                await self.send_json({
                    'type': 'chunked_transfer',
                    'part_number': (number, len(parts)),
                    'part': part
                })
