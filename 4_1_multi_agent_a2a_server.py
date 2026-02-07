from strands_tools.calculator import calculator
from strands import Agent, tool
from strands.multiagent.a2a import A2AServer

@tool
def reserve_hotel(date: str, room_type: str, number_of_guests: int) -> str:
    """
    Reserve a hotel room for a given date, room type, and number of guests.
    """
    msg = f"ホテルの予約が完了しました。{date}に{room_type}の部屋が{number_of_guests}人で予約されました。"
    print(msg)
    return msg

agent = Agent(
    name="Reservation Agent",
    description="ホテルの予約エージェントです。ユーザーの予約を受け付けます。",
    tools=[reserve_hotel],
    callback_handler=None,
)

server = A2AServer(agent=agent)

server.serve()