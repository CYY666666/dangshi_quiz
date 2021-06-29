import json
import asyncio

import aiohttp

from utils.jsonify import load_json
from utils.socket_utils import get_message

socket_url = 'wss://djgamelink.migufun.com/socket.io/?EIO=3&transport=websocket'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI MiniGame WindowsWechat',
    'Origin': 'https://game.servicewechat.com',
    'Upgrade': 'websocket',
    'Host': 'djgamelink.migufun.com',
    'Connection': 'Upgrade'
}


def get_user_info():
    user_info = load_json('user_info.json')
    return user_info
print(get_user_info())

async def main():
    timeout = aiohttp.ClientTimeout(total=20)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.ws_connect(socket_url, headers=headers) as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    data = get_message(msg.data)
                    json_data = json.loads(data)
                    print(json_data)
                    if json_data and json_data[0] == 'session':
                        pass
                    # if msg.data == '40':
                    #     await ws.send_str(msg.data + '/answer')
                    # else:
                    #     await ws.send_str(msg.data + '/answer')
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    break

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
