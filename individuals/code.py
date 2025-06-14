import subprocess

def run_qwen2_coder(prompt):
    result = subprocess.run(
        ["ollama", "run", "qwen2.5-coder"],
        input=prompt.encode(),
        capture_output=True,
        check=True
    )

    print("🧠 Qwen2.5-Coder Response:\n")
    print(result.stdout.decode().strip())

if __name__ == "__main__":
    prompt = input("💻 Enter coding prompt: ").strip()
    run_qwen2_coder(prompt)
