import subprocess

def run_mathstral(prompt):
    result = subprocess.run(
        ["ollama", "run", "mathstral"],
        input=prompt.encode(),
        capture_output=True,
        check=True
    )

    print("🧮 Mathstral Response:\n")
    print(result.stdout.decode().strip())

if __name__ == "__main__":
    prompt = input("🔢 Enter math query: ").strip()
    run_mathstral(prompt)
