import { Agent } from "@strands-agents/sdk";

const agent = new Agent({ printer: false });

for await (const event of agent.stream("AWSの概要について教えてください")) {
  if (
    event.type === "modelContentBlockDeltaEvent" &&
    event.delta.type === "textDelta"
  ) {
    process.stdout.write(event.delta.text);
  }
}