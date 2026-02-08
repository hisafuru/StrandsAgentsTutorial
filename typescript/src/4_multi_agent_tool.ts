import { Agent, AgentResult, tool } from "@strands-agents/sdk";
import { z } from "zod";

// ツールとしてのマルチエージェント（オーケストレーターパターン）
// Python版と同様に、各専門エージェントをツールとして定義し、
// オーケストレーターが順番に呼び出す構成です。

function printResponse(response: AgentResult, agentName: string): void {
  console.log(`\n===== ${agentName} の応答 ======`);
  console.log(response.toString());
  console.log("======================================\n");
}

// 市場調査エージェント
const marketResearcher = tool({
  name: "market_researcher",
  description:
    "市場調査の専門家。指定されたテーマについて、市場データ、トレンド、競合情報などの生の事実情報を収集して提供する。分析や提案はせず、あくまで客観的なデータ収集に徹する。",
  inputSchema: z.object({
    query: z.string().describe("調査テーマ"),
  }),
  callback: async (input) => {
    const agent = new Agent({
      systemPrompt:
        "あなたは市場調査の専門家です。" +
        "与えられたテーマについて、具体的な市場データ・トレンド・競合情報を収集し、" +
        "箇条書きで事実ベースのレポートを提供してください。" +
        "分析や提案は行わず、客観的なデータ収集に徹してください。",
      printer: false,
    });
    const response = await agent.invoke(input.query);
    printResponse(response, "market_researcher");
    return response.toString();
  },
});

// データ分析エージェント
const dataAnalyst = tool({
  name: "data_analyst",
  description:
    "データ分析の専門家。市場リサーチャーが収集した生データを受け取り、パターンや機会・リスクを特定し、戦略的な洞察を導き出す。文章化はせず、分析結果を構造的に整理することに特化する。",
  inputSchema: z.object({
    data: z.string().describe("分析対象のデータ"),
  }),
  callback: async (input) => {
    const agent = new Agent({
      systemPrompt:
        "あなたはデータ分析の専門家です。" +
        "提供されたデータからパターンや傾向を見つけ出し、" +
        "機会とリスクを特定して、戦略的な洞察を導き出してください。" +
        '結果は「機会」「リスク」「推奨戦略」の3カテゴリで構造的に整理してください。' +
        "文章化はせず、分析に徹してください。",
      printer: false,
    });
    const response = await agent.invoke(
      `以下のデータを分析してください:\n${input.data}`
    );
    printResponse(response, "data_analyst");
    return response.toString();
  },
});

// コピーライターエージェント
const copywriter = tool({
  name: "copywriter",
  description:
    "コピーライティングの専門家。分析結果やデータを受け取り、読み手を惹きつける魅力的なビジネス文書に仕上げる。自分でデータ収集や分析は行わず、提供された素材の文章化に特化する。",
  inputSchema: z.object({
    brief: z.string().describe("文書作成の素材"),
  }),
  callback: async (input) => {
    const agent = new Agent({
      systemPrompt:
        "あなたはコピーライティングの専門家です。" +
        "提供されたデータや分析結果を元に、" +
        "読み手を惹きつける魅力的なビジネス文書を作成してください。" +
        "自分で新たなデータを作り出さず、提供された素材を最大限に活かしてください。",
      printer: false,
    });
    const response = await agent.invoke(
      `以下の素材を元にビジネス文書を作成してください:\n${input.brief}`
    );
    printResponse(response, "copywriter");
    return response.toString();
  },
});

// オーケストレーターエージェント
const orchestrator = new Agent({
  systemPrompt:
    "あなたはプロジェクトマネージャーです。" +
    "与えられたタスクを遂行してください。" +
    "必ず以下の手順を守ること:\n" +
    "1. 市場データを収集する\n" +
    "2. 収集したデータを分析する\n" +
    "3. 分析結果を文書にまとめる\n" +
    "各ステップの結果を次のステップに渡すことで、質の高い成果物を作り上げてください。",
  tools: [marketResearcher, dataAnalyst, copywriter],
  printer: false,
});

const prompt = `
東京・下北沢にスペシャルティコーヒーのカフェを新規出店する企画書を作成してください。
ターゲットは20〜30代のクリエイター層です。
`;

const response = await orchestrator.invoke(prompt);
console.log(response.toString());
