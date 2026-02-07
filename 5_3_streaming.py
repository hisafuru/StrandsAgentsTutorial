import asyncio
from strands import Agent

agent = Agent(callback_handler=None)

async def process_streaming_response():
    agent_stream = agent.stream_async("AWSの概要について教えてください")
    async for event in agent_stream:
        text = event.get("event", {}).get("contentBlockDelta", {}).get("delta", {}).get("text")
        if text:
            print(text, end="", flush=True)

asyncio.run(process_streaming_response())