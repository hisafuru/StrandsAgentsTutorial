import contextlib
import os

from strands import Agent
from strands.agent.conversation_manager import SummarizingConversationManager

agent = Agent(
    conversation_manager=SummarizingConversationManager(
        preserve_recent_messages=2, # 通常使用時は更に大きくするか、設定自体を削除
    )
)

# 複数のメッセージを送って会話履歴を蓄積する
# with open...の部分は出力を抑制するためのコードなので、本来は不要です
with open(os.devnull, "w") as devnull, contextlib.redirect_stdout(devnull):
    agent("私の名前はhisafuruです。よろしくお願いします。")
    agent("私の趣味はプログラミングです。特にPythonが好きです。")
    agent("最近、AIエージェントの開発に興味を持っています。")

# 手動でreduce_contextを呼び出して要約を発動させる
print(">>> reduce_context() を呼び出して要約を実行...")
agent.conversation_manager.reduce_context(agent)
