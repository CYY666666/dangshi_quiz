import asyncio

import aiohttp

from configs import OPEN_ID, USER_ID

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI MiniGame WindowsWechat',
    'Content-Type': 'application/json',
    'Host': 'djgame.migufun.com',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Dest': 'empty'
}


async def login(client, headers, data):
    # 登录
    url = 'https://djgame.migufun.com/partyhistory-api/publicapi/user/login'
    async with client.post(url, headers=headers, json=data) as resp:
        assert resp.status == 200
        return await resp.json()


async def battle_invite_room(client, headers, data):
    # 查询房间
    url = 'https://djgame.migufun.com/partyhistory-api/publicapi/battle/invite/vs2/room'
    async with client.post(url, headers=headers, json=data) as resp:
        assert resp.status == 200
        return await resp.json()


async def query(client, data):
    # 主页查询
    url = 'https://djgame.migufun.com/partyhistory-api/publicapi/home/query'
    async with client.post(url, headers=headers, json=data) as resp:
        assert resp.status == 200
        return await resp.json()


async def announcement_query(client, headers, data):
    # 查看公告
    url = 'https://djgame.migufun.com/partyhistory-api/publicapi/announcement/query'
    async with client.post(url, headers=headers, json=data) as resp:
        assert resp.status == 200
        return await resp.json()


async def share_query(client, headers, data):
    # 查询分享
    url = 'https://djgame.migufun.com/partyhistory-api/publicapi/share/query'
    async with client.post(url, headers=headers, json=data) as resp:
        assert resp.status == 200
        return await resp.json()


async def task_info(client, headers, data):
    # 获取任务
    url = 'https://djgame.migufun.com/partyhistory-api/publicapi/task/daily/info'
    async with client.post(url, headers=headers, json=data) as resp:
        assert resp.status == 200
        return await resp.json()


async def golds_tree_receive(client, headers, data):
    # 领取体力
    url = 'https://djgame.migufun.com/partyhistory-api/publicapi/goldsTree/receive'
    async with client.post(url, headers=headers, json=data) as resp:
        assert resp.status == 200
        return await resp.json()


async def take_reward(client, headers, data):
    # 完成任务
    url = 'https://djgame.migufun.com/partyhistory-api/publicapi/task/daily/takereward'
    async with client.post(url, headers=headers, json=data) as resp:
        assert resp.status == 200
        return await resp.json()


async def task_share(client, headers, data):
    # 分享
    url = 'https://djgame.migufun.com/partyhistory-api/publicapi/task/daily/shareTask'
    async with client.post(url, headers=headers, json=data) as resp:
        assert resp.status == 200
        return await resp.json()


async def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
