from utils.llm_client import call_llm

class BaseAgent:
    def __init__(self, name, provider):
        self.name = name
        self.provider = provider

    def think(self, prompt):
        print(f"\n{'='*60}")
        print(f"[{self.name} PROMPT → LLM]")
        print(f"{'-'*60}")
        print(prompt)
        print(f"{'='*60}")

        print(f"\n[{self.name} THINKING]")

        response = call_llm(prompt, self.provider)

        print(f"\n[{self.name} RESPONSE]")
        print(response)

        return response