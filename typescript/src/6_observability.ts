import { Agent } from "@strands-agents/sdk";

const agent = new Agent({ printer: false });

let totalInputTokens = 0;
let totalOutputTokens = 0;
let totalLatency = 0;

for await (const event of agent.stream(
  "今後、AIはどのように進化すると思いますか？"
)) {
  if (event.type === "modelMetadataEvent") {
    if (event.usage) {
      totalInputTokens += event.usage.inputTokens;
      totalOutputTokens += event.usage.outputTokens;
    }
    if (event.metrics) {
      totalLatency += event.metrics.latencyMs;
    }
  }
}

console.log("\n");
console.log(`入力トークン数: ${totalInputTokens}`);
console.log(`出力トークン数: ${totalOutputTokens}`);
console.log(`合計トークン数: ${totalInputTokens + totalOutputTokens}`);
console.log(`レイテンシ: ${totalLatency}ms`);
