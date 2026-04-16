def detect_language(code):
    code_lower = code.lower()

    if "public class" in code or "system.out" in code_lower:
        return "java"
    elif "def " in code or "print(" in code:
        return "python"
    else:
        return "unknown"