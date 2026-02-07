from strands import Agent
from strands.models.openai import OpenAIModel
from strands.models.anthropic import AnthropicModel
from strands.models.gemini import GeminiModel
from dotenv import load_dotenv
import os

load_dotenv()

model_openai = OpenAIModel(
    client_args={
        "api_key": os.getenv("OPENAI_API_KEY"),
    },
    model_id="gpt-4.1",
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
    model_id="claude-sonnet-4-20250514",
    params={
        "temperature": 0.7,
    }
)

model_gemini = GeminiModel(
    client_args={
        "api_key": os.getenv("GEMINI_API_KEY"),
    },
    model_id="gemini-2.5-flash",
    params={
        "temperature": 0.7,
        "max_output_tokens": 2048,
    }
)

agent_openai = Agent(model=model_openai, callback_handler=None)
agent_anthropic = Agent(model=model_anthropic, callback_handler=None)
agent_gemini = Agent(model=model_gemini, callback_handler=None)

response_openai = agent_openai("あなたのことについて教えてください。")
response_anthropic = agent_anthropic("あなたのことについて教えてください。")
response_gemini = agent_gemini("あなたのことについて教えてください。")

print("Response from OpenAI:", response_openai)
print("Response from Anthropic:", response_anthropic)
print("Response from Gemini:", response_gemini)