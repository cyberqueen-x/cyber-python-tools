import subprocess
import shlex

command = input("Enter a command to run: ")
try:
    result = subprocess.run(shlex.split(command), capture_output=True, text=True)
    print(result.stdout)
except Exception as e:
    print(f"💀 cant write a command? {e}")

