from agents.planner_agent import PlannerAgent
from agents.coder_agent import CoderAgent
from agents.debugger_agent import DebuggerAgent

from tools.python_tool import run_python_code
from tools.java_tool import run_java_code

from utils.code_parser import extract_code
from utils.language_detector import detect_language

from memory.memory import Memory
from config import MAX_DEBUG_ATTEMPTS


# 🔥 Runtime LLM selection
def select_provider():
    print("\nSelect LLM Provider:")
    print("1. OpenAI")
    print("2. Ollama")

    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        return "openai"
    elif choice == "2":
        return "ollama"
    else:
        print("Invalid choice, defaulting to Ollama")
        return "ollama"


def main():
    # Step 0: Choose LLM
    provider = select_provider()

    # Step 1: User input
    task = input("\nEnter your task: ")

    # Step 2: Initialize agents
    planner = PlannerAgent(provider)
    coder = CoderAgent(provider)
    debugger = DebuggerAgent(provider)

    memory = Memory()

    print(f"\n🚀 Starting execution using: {provider.upper()}")

    # Step 3: Planning
    plan = planner.create_plan(task)

    attempt = 0

    while attempt < MAX_DEBUG_ATTEMPTS:
        print(f"\n🔁 Attempt: {attempt + 1}")

        # Step 4: Code generation
        raw_code = coder.generate_code(task, plan, memory.get_context())
        code = extract_code(raw_code)

        print("\n[CODE]")
        print(code)

        # Step 5: Detect language
        language = detect_language(code)
        print(f"\n[DETECTED LANGUAGE]: {language}")

        # Step 6: Execute
        if language == "python":
            stdout, stderr = run_python_code(code)

        elif language == "java":
            stdout, stderr = run_java_code(code)

        else:
            print("❌ Unsupported language")
            break

        # Step 7: Output
        print("\n[OUTPUT]")
        print(stdout)

        # Step 8: Success check
        if not stderr:
            print("\n✅ SUCCESS")
            break

        # Step 9: Error handling
        print("\n[ERROR]")
        print(stderr)

        # Save to memory
        memory.add(f"Error: {stderr}")
        memory.add(f"Code: {code}")

        # Step 10: Debug
        fixed_code = debugger.fix_code(code, stderr)
        code = extract_code(fixed_code)

        memory.add(f"Fix attempt: {code}")

        attempt += 1

    # Step 11: Final status
    if attempt == MAX_DEBUG_ATTEMPTS:
        print("\n❌ FAILED AFTER MULTIPLE ATTEMPTS")


if __name__ == "__main__":
    main()