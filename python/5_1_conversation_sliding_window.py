from strands import Agent
from strands.agent.conversation_manager import SlidingWindowConversationManager

conversation_manager = SlidingWindowConversationManager(
    window_size=3,  
)

agent = Agent(conversation_manager=conversation_manager)


print("===== 自分の名前を教える =====")
agent("私の名前はhisafuruです。よろしくお願いします。")
print("\n")

print("===== 天気を聞く (会話を進める) ====")
agent("よい天気ですね！")
print("\n")

print("===== 名前を覚えているか確認 (window_size=3なので覚えているはず) ====")
agent("私の名前は何ですか？")
print("\n")

print("===== 3回天気を聞く (会話を進めて名前を会話マネージャーから追い出す) ====")
agent("よい天気ですね！")
agent("よい天気ですね！")
agent("よい天気ですね！")
print("\n")

print("===== 名前を聞く (会話マネージャーから名前についての会話が無くなったので覚えていないはず) ====")
agent("私の名前は何ですか？")
print("\n")