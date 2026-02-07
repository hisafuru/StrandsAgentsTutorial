from strands import Agent, tool

def print_response(response, agent_name: str):
    print("\n=====", agent_name, "の応答 ======")
    print(response)
    print("======================================\n")

@tool
def market_researcher(query: str) -> str:
    """
    市場調査の専門家。指定されたテーマについて、市場データ、トレンド、
    競合情報などの生の事実情報を収集して提供する。
    分析や提案はせず、あくまで客観的なデータ収集に徹する。
    """
    agent = Agent(
        system_prompt=(
            "あなたは市場調査の専門家です。"
            "与えられたテーマについて、具体的な市場データ・トレンド・競合情報を収集し、"
            "箇条書きで事実ベースのレポートを提供してください。"
            "分析や提案は行わず、客観的なデータ収集に徹してください。"
        ),
        callback_handler=None,
    )
    response = agent(query)
    print_response(response, "market_researcher")
    return str(response)


@tool
def data_analyst(data: str) -> str:
    """
    データ分析の専門家。市場リサーチャーが収集した生データを受け取り、
    パターンや機会・リスクを特定し、戦略的な洞察を導き出す。
    文章化はせず、分析結果を構造的に整理することに特化する。
    """
    agent = Agent(
        system_prompt=(
            "あなたはデータ分析の専門家です。"
            "提供されたデータからパターンや傾向を見つけ出し、"
            "機会とリスクを特定して、戦略的な洞察を導き出してください。"
            "結果は「機会」「リスク」「推奨戦略」の3カテゴリで構造的に整理してください。"
            "文章化はせず、分析に徹してください。"
        ),
        callback_handler=None,
    )
    response = agent(f"以下のデータを分析してください:\n{data}")
    print_response(response, "data_analyst")
    return str(response)


@tool
def copywriter(brief: str) -> str:
    """
    コピーライティングの専門家。分析結果やデータを受け取り、
    読み手を惹きつける魅力的なビジネス文書に仕上げる。
    自分でデータ収集や分析は行わず、提供された素材の文章化に特化する。
    """
    agent = Agent(
        system_prompt=(
            "あなたはコピーライティングの専門家です。"
            "提供されたデータや分析結果を元に、"
            "読み手を惹きつける魅力的なビジネス文書を作成してください。"
            "自分で新たなデータを作り出さず、提供された素材を最大限に活かしてください。"
        ),
        callback_handler=None,
    )
    response = agent(f"以下の素材を元にビジネス文書を作成してください:\n{brief}")
    print_response(response, "copywriter")
    return str(response)


orchestrator = Agent(
    system_prompt=(
        "あなたはプロジェクトマネージャーです。"
        "与えられたタスクを遂行してください。"
        "必ず以下の手順を守ること:\n"
        "1. 市場データを収集する\n"
        "2. 収集したデータを分析する\n"
        "3. 分析結果を文書にまとめる\n"
        "各ステップの結果を次のステップに渡すことで、質の高い成果物を作り上げてください。"
    ),
    tools=[market_researcher, data_analyst, copywriter],
    callback_handler=None,
)

prompt = """
東京・下北沢にスペシャルティコーヒーのカフェを新規出店する企画書を作成してください。
ターゲットは20〜30代のクリエイター層です。
"""

response = orchestrator(prompt)
print(response)
