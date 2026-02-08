import { Agent, SlidingWindowConversationManager } from "@strands-agents/sdk";

const conversationManager = new SlidingWindowConversationManager({
  windowSize: 3,
});

const agent = new Agent({ conversationManager });

console.log("===== 自分の名前を教える =====");
await agent.invoke("私の名前はhisafuruです。よろしくお願いします。");
console.log("\n");

console.log("===== 天気を聞く (会話を進める) ====");
await agent.invoke("よい天気ですね！");
console.log("\n");

console.log(
  "===== 名前を覚えているか確認 (windowSize=3なので覚えているはず) ===="
);
await agent.invoke("私の名前は何ですか？");
console.log("\n");

console.log(
  "===== 3回天気を聞く (会話を進めて名前を会話マネージャーから追い出す) ===="
);
await agent.invoke("よい天気ですね！");
await agent.invoke("よい天気ですね！");
await agent.invoke("よい天気ですね！");
console.log("\n");

console.log(
  "===== 名前を聞く (会話マネージャーから名前についての会話が無くなったので覚えていないはず) ===="
);
await agent.invoke("私の名前は何ですか？");
console.log("\n");
