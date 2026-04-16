import subprocess
import tempfile

def run_python_code(code):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w") as f:
        f.write(code)
        file_name = f.name

    try:
        result = subprocess.run(
            ["python", file_name],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout, result.stderr
    except Exception as e:
        return "", str(e)