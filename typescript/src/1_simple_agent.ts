import { Agent } from "@strands-agents/sdk";

const agent = new Agent();
const result = await agent.invoke("エージェンティックAIについて教えてください。");
console.log(result.lastMessage);
