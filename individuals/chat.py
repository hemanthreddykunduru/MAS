import subprocess

def run_mistral(prompt):
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode(),
        capture_output=True,
        check=True
    )

    print("🧠 Mistral Response:\n")
    print(result.stdout.decode().strip())

if __name__ == "__main__":
    prompt = input("💬 Enter general prompt: ").strip()
    run_mistral(prompt)
