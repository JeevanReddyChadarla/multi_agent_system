import re

def extract_code(text):
    code_blocks = re.findall(r"```(?:\w+)?(.*?)```", text, re.DOTALL)
    if code_blocks:
        return code_blocks[0].strip()
    return text.strip()