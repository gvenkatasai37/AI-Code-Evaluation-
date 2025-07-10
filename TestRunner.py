import subprocess
import sys
from pathlib import Path

class TestRunner:
    def __init__(self, code, test_cases):
        self.code = code
        self.test_cases = test_cases
        #Added
        
    def run_tests(self):
        """Execute code against test cases"""
        # Save code to temp file
        temp_file = Path("temp_code.py")
        temp_file.write_text(self.code)
        
        # Run pytest programmatically
        result = subprocess.run(
            [sys.executable, "-m", "pytest", str(temp_file)],
            capture_output=True,
            text=True
        )
        
        return {
            "passed": result.returncode == 0,
            "output": result.stdout,
            "errors": result.stderr
        }