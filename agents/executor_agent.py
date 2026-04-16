from tools.python_tool import run_python_code
from utils.code_parser import extract_code

class ExecutorAgent:
    def __init__(self):
        self.name = "Executor"

    def execute(self, code):
        print("\n[RAW CODE]")
        print(code)

        clean_code = extract_code(code)

        print("\n[CLEANED CODE]")
        print(clean_code)

        print("\n[EXECUTING CODE]")
        output = run_python_code(clean_code)
        print(output)
        return output