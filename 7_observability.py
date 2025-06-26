from strands import Agent

agent = Agent(callback_handler=None)

result = agent("今後、AIはどのように進化すると思いますか？")

# メトリクス
print(f"使用トークン数: {result.metrics.accumulated_usage['totalTokens']}")
print(f"実行時間: {sum(result.metrics.cycle_durations):.2f} 秒")
print(f"イベントループサイクル数: {result.metrics.cycle_count} 回")
print(f"レイテンシ: {result.metrics.accumulated_metrics['latencyMs']:.2f} 秒")