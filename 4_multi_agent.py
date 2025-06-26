from strands import Agent
from strands_tools import swarm

agent = Agent(tools=[swarm])

result = agent.tool.swarm(
    task="OpenAI、Gemini、Claudeの違いやそれぞれの特徴を分析して教えてください。回答は日本語でお願いします。",
    swarm_size=3,
    coordination_pattern="collaborative"
)

result = agent.tool.swarm(
    task="生成AIを使ったユニークなアプリのアイデアを考えてください",
    swarm_size=3,
    coordination_pattern="competitive"
)