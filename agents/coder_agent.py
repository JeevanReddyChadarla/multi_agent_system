from agents.base_agent import BaseAgent

class CoderAgent(BaseAgent):
    def __init__(self, provider):
        super().__init__("Coder", provider)

    def generate_code(self, task, plan, memory):
        prompt = f"""
You are a coding agent.

Your task is to generate correct, executable code based on the given problem.

CONTEXT:
- The code will be executed directly without modification.
- There is no human in the loop to fix errors.
- The solution must be complete and runnable.

INSTRUCTIONS:
1. Understand the problem clearly.
2. Identify inputs, outputs, and constraints.
3. Choose the correct approach and data structures.
4. Handle edge cases (nulls, empty input, limits, invalid cases).
5. Write clean, correct, and efficient code.

LANGUAGE RULES:
- Follow the programming language EXACTLY as specified in the task.
- Do NOT mix syntax from other languages.
- Use standard libraries only.

OUTPUT RULES (STRICT):
- Output ONLY code.
- NO explanations.
- NO comments.
- NO markdown.
- NO extra text.

FORMAT RULES:
- Ensure the code is complete and directly executable.
- Include all required imports.
- Include a main entry point if needed.

JAVA-SPECIFIC RULE:
- If the language is Java:
  - Class name MUST be Main
  - Include public static void main(String[] args)

QUALITY RULES:
- Avoid syntax errors.
- Avoid incomplete logic.
- Avoid placeholder code.
- Ensure correct indentation and formatting.

Task:
{task}

Plan:
{plan}

Previous context:
{memory}
"""
        return self.think(prompt)