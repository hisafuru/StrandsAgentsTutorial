# StrandsAgentsTutorial

## usage

1. copy .env.example to .env

```bash
cp .env.example .env
```

2. set environment variables

```bash
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
BEDROCK_GUARDRAIL_ID=your_bedrock_guardrail_id
```

3. install dependencies

```bash
pip install -r requirements.txt
```

4. run

```bash
python 1_simple_agent.py
```