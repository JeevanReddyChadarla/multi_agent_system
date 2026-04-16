from agents.base_agent import BaseAgent

class DebuggerAgent(BaseAgent):
    def __init__(self, provider):
        super().__init__("Debugger", provider)

    def fix_code(self, code, error):
        prompt = f"""
You are a debugging agent.

Fix the code.

STRICT RULES:
- Output ONLY corrected code
- NO explanation
- NO markdown
- DO NOT change programming language

Code:
{code}

Error:
{error}
"""
        return self.think(prompt)