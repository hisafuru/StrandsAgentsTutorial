from strands import Agent, tool
from strands_tools import calculator, current_time


@tool
def current_temperature(city: str) -> float:
    """
    Get the current temperature in a city.
    """
    # 今回はダミーで実装
    return 20.0

agent = Agent(tools=[calculator, current_time, current_temperature], callback_handler=None)

prompt = """
次のタスクを順に実行し、それぞれの結果を教えてください。
1. 東京の現在の気温を取得する
2. 現在の時刻を取得する
3. 3111696 / 74088を計算する
"""

response = agent(prompt)
print(response)