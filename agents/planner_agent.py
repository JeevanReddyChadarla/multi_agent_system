from agents.base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    def __init__(self, provider):
        super().__init__("Planner", provider)

    def create_plan(self, task):
        prompt = f"""
You are a planning agent.

Your job is to break a given task into clear, logical, high-level steps that can be executed sequentially.

CONTEXT:
- The task may be complex, ambiguous, or multi-step.
- Assume the executor agent is not intelligent and relies entirely on your steps.

INSTRUCTIONS:
1. Understand the user's goal.
2. Identify the main phases required to complete the task.
3. Break the task into ordered, high-level steps.
4. Each step should represent a meaningful action or milestone.
5. Avoid low-level implementation details.

OUTPUT RULES (STRICT):
- Output ONLY a numbered list of steps.
- Each step must be concise and actionable.
- Do NOT include explanations, reasoning, or extra text.
- Do NOT include sub-steps.
- Do NOT repeat the task.

QUALITY GUIDELINES:
- Steps must be logically ordered.
- Steps should cover the entire task from start to finish.
- Avoid vague steps like "do the work" or "process data".
- Prefer clarity over brevity if ambiguity exists.


Task:
{task}
"""
        return self.think(prompt)