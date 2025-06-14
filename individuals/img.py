import subprocess
import os

def run_llama3_vision(image_path, prompt_text):
    if not os.path.exists(image_path):
        print("❌ Image not found:", image_path)
        return

    full_prompt = f"<image>{image_path}</image>\n{prompt_text}"

    result = subprocess.run(
        ["ollama", "run", "llama3.2-vision"],
        input=full_prompt.encode(),
        capture_output=True,
        check=True
    )

    print("🧠 LLaMA3.2-Vision Response:\n")
    print(result.stdout.decode().strip())

if __name__ == "__main__":
    img = input("🖼️  Image path: ").strip()
    prompt = input("💬 Prompt text: ").strip()
    run_llama3_vision(img, prompt)


# import subprocess
# import os

# def run_llama3_vision(image_path, prompt_text):
#     if not os.path.exists(image_path):
#         print("❌ Image not found:", image_path)
#         return

#     full_prompt = f"<image>{image_path}</image>\n{prompt_text}"

#     # Run llama3.2-vision with optimized prompt
#     result = subprocess.run(
#         ["ollama", "run", "llama3.2-vision"],
#         input=full_prompt.encode(),
#         capture_output=True,
#         check=True
#     )

#     print("\n🧠 LLaMA3.2-Vision (GPU Accelerated) Response:\n")
#     print(result.stdout.decode().strip())

# if __name__ == "__main__":
#     image = input("🖼️ Image path: ").strip()
#     prompt = input("💬 Prompt related to image: ").strip()
#     run_llama3_vision(image, prompt)
