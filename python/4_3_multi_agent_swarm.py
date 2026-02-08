from strands import Agent
from strands.multiagent import Swarm

creator = Agent(name="creator", system_prompt="創造的で独創的な出力をしてください。")
reviewer = Agent(name="reviewer", system_prompt="客観的・批判的な出力をしてください。")

swarm = Swarm([creator, reviewer], entry_point=creator)

result = swarm("生成AIを使った独創的なアプリのアイデアを考えてください。また、それに対する客観的な批判をしてください。")