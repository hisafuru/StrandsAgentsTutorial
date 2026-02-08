import { Agent } from "@strands-agents/sdk";
import { OpenAIModel } from "@strands-agents/sdk/openai";
import dotenv from "dotenv";

dotenv.config();

// OpenAI
// TypeScript版では、AnthropicとGeminiは未対応
const modelOpenai = new OpenAIModel({
  apiKey: process.env.OPENAI_API_KEY!,
  modelId: "gpt-4.1",
  maxTokens: 1000,
  temperature: 0.7,
});

const agent = new Agent({ model: modelOpenai, printer: false });

const response = await agent.invoke("あなたのことについて教えてください。");

console.log("Response from OpenAI:", response.toString());
