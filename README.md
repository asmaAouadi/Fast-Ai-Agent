# ⚡ Fast AI-Agent

Fast AI-Agent is a dual-model intelligent assistant system built with Python. It integrates two language models:

* **Fast Model** (for immediate, concise replies)
* **Slow Model** (for deeper, more thoughtful analysis in the background)

This architecture allows quick user interaction while preparing more comprehensive results behind the scenes.

---

## 🚀 Features

* 🧠 Dual-Layer Intelligence: Fast agent gives instant answers; slow agent works in parallel for deeper context.
* 🔀 Async Execution: Models run concurrently using Python threads.
* 🔄 Flexible Backend: Supports **Ollama** (locally hosted LLMs) and **OpenAI API**.
* 📦 Simple Setup: Just install dependencies and choose your preferred agent runtime.

---

## 🧰 Tech Stack

* Python 3.10+
* [Langchain](https://www.langchain.com/)
* [Ollama](https://ollama.com/) (for local model execution)
* [OpenAI](https://openai.com/) (optional)

---

## 📂 Project Structure

```bash
.
├── main.py                 # Entry point: runs fast & slow agents
├── agents.py               # Fast and slow agent setup
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/fast-ai-agent.git
cd fast-ai-agent
```

### 2. Install requirements

```bash
pip install -r requirements.txt
```

### 3. Choose your backend

#### Option A: Use with Ollama (local models)

Ensure [Ollama](https://ollama.com/) is installed and the models (e.g., `llama3`, `phi3`) are available:

```bash
ollama run llama3
ollama run phi3
```

#### Option B: Use OpenAI API

Add your API key:

```bash
export OPENAI_API_KEY=your_key_here
```

Replace the agent loader logic accordingly.

---

## 🧪 Usage Example

```python
from agents import run_fast_agent, run_slow_agent

question = "How does a black hole work?"

# Fast reply immediately
fast_reply = run_fast_agent(question)

# Background process for slow agent
threading.Thread(target=run_slow_agent, args=(question,)).start()
```

---

## ✅ Sample Output

```
User: What is quantum computing?

Fast Agent: It's a type of computing that uses qubits instead of bits to process data in parallel.

(Slow Agent, after a few seconds): Quantum computing leverages quantum phenomena such as superposition and entanglement to perform computations more efficiently on certain problems...
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests and issues are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---

