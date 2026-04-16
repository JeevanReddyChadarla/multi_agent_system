import subprocess
import tempfile
import os

def run_java_code(code):
    # Ensure class name is Main
    if "public class" in code and "public class Main" not in code:
        code = code.replace("public class", "public class Main", 1)

    with tempfile.TemporaryDirectory() as tmpdir:
        java_file = os.path.join(tmpdir, "Main.java")

        with open(java_file, "w") as f:
            f.write(code)

        try:
            # Compile
            compile_proc = subprocess.run(
                ["javac", java_file],
                capture_output=True,
                text=True
            )

            if compile_proc.returncode != 0:
                return "", compile_proc.stderr

            # Run
            run_proc = subprocess.run(
                ["java", "-cp", tmpdir, "Main"],
                capture_output=True,
                text=True
            )

            return run_proc.stdout, run_proc.stderr

        except Exception as e:
            return "", str(e)