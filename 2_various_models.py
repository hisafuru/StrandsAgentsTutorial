from strands import Agent
from strands.models.anthropic import AnthropicModel
from strands.models.openai import OpenAIModel
from dotenv import load_dotenv
import os

load_dotenv()

model_openai = OpenAIModel(
    client_args={
        "api_key": os.getenv("OPENAI_API_KEY"),
    },
    model_id="gpt-4o",
    params={
        "max_tokens": 1000,
        "temperature": 0.7,
    }
)

model_anthropic = AnthropicModel(
    client_args={
        "api_key": os.getenv("ANTHROPIC_API_KEY"),
    },
    max_tokens=1028,
    model_id="claude-3-7-sonnet-20250219",
    params={
        "temperature": 0.7,
    }
)

agent_openai = Agent(model=model_openai, callback_handler=None)
agent_anthropic = Agent(model=model_anthropic, callback_handler=None)

response_openai = agent_openai("あなたのことについて教えてください。")
response_anthropic = agent_anthropic("あなたのことについて教えてください。")


print("Response from OpenAI:", response_openai)
print("Response from Anthropic:", response_anthropic)