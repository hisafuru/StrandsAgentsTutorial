import { Agent, tool } from "@strands-agents/sdk";
import { z } from "zod";

// カスタムツール: 気温を取得する（ダミー実装）
// ※ TypeScript版ではcalculator, current_timeツールが無いので自前で実装
const currentTemperature = tool({
  name: "current_temperature",
  description: "指定された都市の現在の気温を取得する。",
  inputSchema: z.object({
    city: z.string().describe("都市名"),
  }),
  callback: (input) => {
    // 今回はダミーで実装
    return `${input.city}の現在の気温は20.0度です。`;
  },
});

// カスタムツール: 現在時刻を取得する
const currentTime = tool({
  name: "current_time",
  description: "現在の日時を取得する。",
  inputSchema: z.object({}),
  callback: () => {
    return new Date().toLocaleString("ja-JP", { timeZone: "Asia/Tokyo" });
  },
});

// カスタムツール: 計算機
const calculator = tool({
  name: "calculator",
  description: "数式を計算する。",
  inputSchema: z.object({
    expression: z.string().describe("計算する数式"),
  }),
  callback: (input) => {
    const result = Function(`"use strict"; return (${input.expression})`)();
    return String(result);
  },
});

const agent = new Agent({
  tools: [calculator, currentTime, currentTemperature],
  printer: false,
});

const prompt = `
次のタスクを順に実行し、それぞれの結果を教えてください。
1. 東京の現在の気温を取得する
2. 現在の時刻を取得する
3. 3111696 / 74088を計算する
`;

const response = await agent.invoke(prompt);
console.log(response.toString());
