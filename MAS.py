import os
import sys
import sqlite3
import subprocess
import time
from datetime import datetime

class MCPServer:
    def __init__(self):
        self.db_path = "history.db"
        self.history = []  # To keep track of messages during the session
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                query TEXT,
                response TEXT,
                agent_name TEXT,
                response_time REAL,
                timestamp TEXT
            )
        """)
        conn.commit()
        conn.close()

    def save_chat(self, query, response, agent_name, response_time):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO chat_history (query, response, agent_name, response_time, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, (query, response, agent_name, response_time, datetime.now().isoformat()))
        conn.commit()
        conn.close()

    def detect_model(self, prompt):
        lower = prompt.lower()
        has_image = any(ext in lower for ext in [".png", ".jpg", ".jpeg", ".bmp", ".gif"])
        has_code = any(kw in lower for kw in ["code", "python", "java", "c++", "script", "program", "function", "compile"])
        has_math = any(kw in lower for kw in [
            "solve", "equation", "math", "integral", "derivative", "matrix",
            "algebra", "calculus", "limit", "factorial", "expression", "geometry",
            "polynomial", "logarithm", "simplify", "evaluate", "probability",
            "trigonometry", "theorem", "statistics", "vector", "function", "roots",
            "quadratic", "mean", "median", "mode", "variance", "standard deviation"
        ])

        if has_image and has_code:
            return "llama3.2-vision", True
        elif has_image:
            return "llama3.2-vision", True
        elif has_code:
            return "qwen2.5-coder", False
        elif has_math:
            return "mathstral", False
        else:
            return "mistral", False

    def extract_image_path(self, prompt):
        parts = prompt.strip().split()
        for part in parts:
            if os.path.isfile(part) and part.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
                return part
        return None

    def format_context(self):
        context = ""
        for i, (q, r) in enumerate(self.history[-10:]):  # Use last 10 messages
            context += f"User: {q}\nAssistant: {r}\n"
        return context

    def run_ollama_model(self, model_name, prompt, use_image):
        try:
            context = self.format_context()

            if use_image:
                image_path = self.extract_image_path(prompt)
                if image_path:
                    prompt_text = prompt.replace(image_path, "").strip()
                    prompt = f"<image>{image_path}</image>\n{prompt_text}"
            else:
                prompt = context + "User: " + prompt

            start = time.time()
            result = subprocess.run(
                ["ollama", "run", model_name],
                input=prompt.encode(),
                capture_output=True,
                check=True
            )
            end = time.time()
            response = result.stdout.decode().strip()
            return response, model_name, round(end - start, 3)
        except subprocess.CalledProcessError as e:
            return f"Error running {model_name}: {e}", model_name, 0.0

    def run(self):
        print("\nMCP Server started. Type 'exit' to quit.\n")
        while True:
            query = input(">> ")
            if query.lower() in ["exit", "/exit"]:
                print("Goodbye!")
                break

            model, use_image = self.detect_model(query)
            response, model_used, response_time = self.run_ollama_model(model, query, use_image)
            self.history.append((query, response))
            self.save_chat(query, response, model_used, response_time)
            print(response)

if __name__ == "__main__":
    sys.path.append(".")
    server = MCPServer()
    server.run()
