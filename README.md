# Multi-Agent System (MAS) 🤖

A sophisticated Multi-Agent System that intelligently combines specialized AI agents to collaboratively solve complex, cross-domain tasks. Each agent excels in a particular domain—natural language understanding, code generation, image analysis, and mathematical reasoning—working together to achieve superior performance than any single agent could alone.

## 🌟 Overview

Modern AI applications require handling diverse tasks across multiple domains. Rather than relying on a single model that may not excel in all areas, this Multi-Agent System orchestrates specialized agents to leverage their individual strengths:

- **Mistral**: Advanced natural language understanding and general reasoning
- **Qwen2.5-Coder**: Specialized code generation and programming tasks
- **LLaMA3.2-Vision**: Image analysis and visual understanding
- **Mathstral**: Complex mathematical reasoning and computations

## 🚀 Key Features

- **Intelligent Task Routing**: Automatically determines which agent(s) are best suited for specific tasks
- **Collaborative Problem Solving**: Agents work together on multi-faceted problems
- **Cross-Domain Integration**: Seamlessly combines outputs from different specialized domains
- **Scalable Architecture**: Easy to add new agents or modify existing ones
- **Performance Optimization**: Leverages each agent's strengths while mitigating weaknesses
- **Real-time Coordination**: Efficient communication and coordination between agents

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Task Input Layer                         │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                Task Analyzer & Router                       │
│            (Determines agent selection)                     │
└─────────────────────┬───────────────────────────────────────┘
                      │
      ┌───────────────┼───────────────┐
      │               │               │
┌─────▼────┐  ┌──────▼──────┐  ┌─────▼────┐  ┌──────▼──────┐
│ Mistral  │  │Qwen2.5-Coder│  │LLaMA3.2  │  │  Mathstral  │
│   (NLU)  │  │   (Code)    │  │ (Vision) │  │   (Math)    │
└─────┬────┘  └──────┬──────┘  └─────┬────┘  └──────┬──────┘
      │               │               │               │
      └───────────────┼───────────────┘               │
                      │                               │
┌─────────────────────▼───────────────────────────────┼─────┐
│              Response Aggregator                    │     │
│           (Combines agent outputs)                  │     │
└─────────────────────┬───────────────────────────────┼─────┘
                      │                               │
┌─────────────────────▼───────────────────────────────▼─────┐
│                   Final Output                            │
└───────────────────────────────────────────────────────────┘
```

## 📋 Prerequisites

- Python 3.8 or higher
- CUDA-compatible GPU (recommended for optimal performance)
- Sufficient RAM (minimum 16GB recommended)
- Internet connection for model downloads

## 🔧 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/hemanthreddykunduru/MAS.git
cd MAS
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Download required models:**
```bash
python setup_models.py
```

5. **Configure environment variables:**
```bash
cp .env.example .env
# Edit .env with your configurations
```

## 🚀 Quick Start

### Basic Usage

```python
from mas import MultiAgentSystem

# Initialize the system
mas = MultiAgentSystem()

# Simple text analysis
result = mas.process("Analyze the sentiment of this text and explain the reasoning")

# Code generation task
result = mas.process("Write a Python function to calculate fibonacci numbers")

# Image analysis
result = mas.process("Analyze this image and describe what you see", image_path="image.jpg")

# Mathematical problem
result = mas.process("Solve this differential equation: dy/dx = 2x + 3")
```

### Advanced Usage

```python
# Multi-domain task
complex_task = """
I have a dataset of customer reviews. I need to:
1. Analyze sentiment patterns
2. Generate a Python script to process the data
3. Create visualizations of the results
4. Calculate statistical significance of sentiment changes
"""

result = mas.process(complex_task, collaboration_mode=True)
```

## 📊 Usage Examples

### Example 1: Code Analysis and Optimization

```python
code_task = """
Review this Python code for bugs and optimization opportunities:

def calculate_average(numbers):
    total = 0
    count = 0
    for i in range(len(numbers)):
        total += numbers[i]
        count += 1
    return total / count
"""

result = mas.process(code_task)
```

### Example 2: Image Analysis with Code Generation

```python
vision_code_task = """
Analyze this flowchart image and generate Python code 
that implements the algorithm shown in the diagram.
"""

result = mas.process(vision_code_task, image_path="flowchart.png")
```

### Example 3: Mathematical Problem with Visualization

```python
math_viz_task = """
Solve this optimization problem and create a Python script 
to visualize the solution:
Minimize f(x,y) = x² + y² subject to x + y = 10
"""

result = mas.process(math_viz_task)
```

## 🎯 Agent Specializations

### Mistral Agent
- **Strengths**: Natural language understanding, general reasoning, text analysis
- **Use Cases**: Sentiment analysis, summarization, question answering
- **Triggers**: Text analysis, reasoning tasks, general NLP

### Qwen2.5-Coder Agent
- **Strengths**: Code generation, debugging, code review
- **Use Cases**: Programming tasks, algorithm implementation, code optimization
- **Triggers**: Code-related keywords, programming requests

### LLaMA3.2-Vision Agent
- **Strengths**: Image analysis, visual understanding, OCR
- **Use Cases**: Image description, chart analysis, visual data extraction
- **Triggers**: Image inputs, visual analysis requests

### Mathstral Agent
- **Strengths**: Mathematical reasoning, equation solving, statistical analysis
- **Use Cases**: Complex calculations, mathematical proofs, statistical modeling
- **Triggers**: Mathematical expressions, numerical computations

## ⚙️ Configuration

### Environment Variables

```bash
# Model configurations
MISTRAL_MODEL_PATH=./models/mistral
QWEN_MODEL_PATH=./models/qwen2.5-coder
LLAMA_MODEL_PATH=./models/llama3.2-vision
MATHSTRAL_MODEL_PATH=./models/mathstral

# System settings
MAX_AGENTS_CONCURRENT=2
RESPONSE_TIMEOUT=300
LOG_LEVEL=INFO
```

### Custom Agent Configuration

```python
# config.py
AGENT_CONFIG = {
    'mistral': {
        'temperature': 0.7,
        'max_tokens': 2048,
        'top_p': 0.9
    },
    'qwen': {
        'temperature': 0.2,
        'max_tokens': 4096,
        'top_p': 0.8
    },
    'llama_vision': {
        'temperature': 0.5,
        'max_tokens': 1024,
        'image_resolution': 'high'
    },
    'mathstral': {
        'temperature': 0.1,
        'max_tokens': 2048,
        'precision': 'high'
    }
}
```

## 🔄 API Reference

### MultiAgentSystem Class

```python
class MultiAgentSystem:
    def __init__(self, config_path: str = None)
    def process(self, task: str, image_path: str = None, 
                collaboration_mode: bool = False) -> dict
    def add_agent(self, agent_name: str, agent_instance: BaseAgent)
    def remove_agent(self, agent_name: str)
    def get_agent_status(self) -> dict
```

### Response Format

```python
{
    'task': 'Original task description',
    'agents_used': ['mistral', 'qwen'],
    'primary_response': 'Main response content',
    'agent_responses': {
        'mistral': 'Mistral-specific response',
        'qwen': 'Qwen-specific response'
    },
    'confidence_scores': {
        'mistral': 0.95,
        'qwen': 0.88
    },
    'execution_time': 2.34,
    'collaboration_details': {...}
}
```

## 📈 Performance Metrics

The system includes built-in performance monitoring:

- **Response Time**: Average processing time per agent
- **Accuracy Scores**: Task-specific accuracy measurements
- **Resource Usage**: Memory and CPU utilization
- **Agent Utilization**: Frequency of agent usage
- **Collaboration Efficiency**: Success rate of multi-agent tasks


## 📝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run code formatting
black mas/
isort mas/

# Run linting
flake8 mas/
```

## 📚 Documentation

- [User Guide](docs/user_guide.md)
- [API Documentation](docs/api.md)
- [Agent Development Guide](docs/agent_development.md)
- [Performance Tuning](docs/performance.md)
- [Troubleshooting](docs/troubleshooting.md)

## 🐛 Troubleshooting

### Common Issues

**Issue**: Model loading fails
```bash
# Solution: Check model paths and permissions
python -c "from mas import MultiAgentSystem; mas = MultiAgentSystem(); print(mas.get_agent_status())"
```

**Issue**: Out of memory errors
```bash
# Solution: Adjust batch size or enable model quantization
export ENABLE_QUANTIZATION=true
export BATCH_SIZE=1
```

**Issue**: Slow response times
```bash
# Solution: Enable GPU acceleration
export CUDA_VISIBLE_DEVICES=0
export USE_GPU=true
```

## 🔗 Related Projects

- [Mistral AI](https://github.com/mistralai/mistral-src)
- [Qwen2.5-Coder](https://github.com/QwenLM/Qwen2.5-Coder)
- [LLaMA](https://github.com/facebookresearch/llama)
- [Mathstral](https://github.com/mistralai/mathstral)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/hemanthreddykunduru/MAS/issues)
- **Discussions**: [Community discussions](https://github.com/hemanthreddykunduru/MAS/discussions)
- **Email**: [your-email@example.com](mailto:your-email@example.com)

## 🏆 Acknowledgments

- Thanks to all the open-source AI projects that made this possible
- Special thanks to the contributors and community members
- Inspired by the growing field of multi-agent systems in AI

---

**Star ⭐ this repository if you find it helpful!**
