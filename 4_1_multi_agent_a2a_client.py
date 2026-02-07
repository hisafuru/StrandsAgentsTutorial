import asyncio
from uuid import uuid4

import httpx
from a2a.client import A2ACardResolver, ClientConfig, ClientFactory
from a2a.types import Message, Part, Role, TextPart

def print_response(response):
    for artifact in getattr(response, "artifacts", []) or []:
        for part in artifact.parts:
            print(part.root.text)

async def send_message(text: str):
    async with httpx.AsyncClient(timeout=300) as httpx_client:
        resolver = A2ACardResolver(httpx_client=httpx_client, base_url="http://127.0.0.1:9000")
        agent_card = await resolver.get_agent_card()

        print("\n===== 相手のエージェントカードの情報 ======")
        print("名前: ", agent_card.name)
        print("説明: ", agent_card.description)
        print("======================================\n")

        client = ClientFactory(
            ClientConfig(httpx_client=httpx_client, streaming=False)
        ).create(agent_card)

        msg = Message(
            kind="message",
            role=Role.user,
            parts=[Part(TextPart(kind="text", text=text))],
            message_id=uuid4().hex,
        )

        async for event in client.send_message(msg):
            task = event[0] if isinstance(event, tuple) else event
            print_response(task)
            return

asyncio.run(send_message("2026年3月1日にホテルを予約したいです。部屋は1人部屋です。"))
