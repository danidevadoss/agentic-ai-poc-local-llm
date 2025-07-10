# Agentic AI POC - LangGraph with Local LLM

This project demonstrates an agentic AI system using LangGraph with a local LLM (Ollama) that can perform multiplication operations using function calling/tool usage.

## Prerequisites

- Python 3.8 or higher
- macOS, Linux, or Windows
- At least 8GB of RAM (for running Llama 3.1 8B model)

## Installation Steps

### 1. Install Ollama

#### On macOS:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### On Linux:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### On Windows:
Download and install from: https://ollama.com/download

### 2. Start Ollama Service

```bash
# Start Ollama server (default port 11434)
ollama serve
```

### 3. Pull Llama 3.1 8B Model

```bash
# Pull the Llama 3.1 8B model (this will take some time)
ollama pull llama3.1:8b
```

### 4. Verify Ollama Installation

```bash
# Test the model
ollama run llama3.1:8b "Hello, how are you?"
```

## Python Environment Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd agentic-ai-poc
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows
```

### 3. Install Python Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

### 4. Create requirements.txt

```txt
langgraph
langchain
langchain-ollama
langchain-openai
langchain-core
httpx
```

## Project Structure

```
agentic-ai-poc/
├── README.md
├── requirements.txt
├── app.py              # Main application entry point
├── agent.py            # Agent configuration
├── llm_model.py        # LLM model setup
├── tools.py            # Function/tool definitions
├── prompt.py           # Prompt templates
└── venv/               # Virtual environment
```

## Code Flow

### 1. LLM Model Setup (`llm_model.py`)
- Configures the Ollama ChatLLM instance
- Connects to local Ollama server on port 11434
- Uses Llama 3.1 8B model for function calling

### 2. Tools Definition (`tools.py`)
- Defines the `multiply` function that takes two integers
- Includes proper docstrings for function calling
- Provides debugging output to track function calls

### 3. Prompt Configuration (`prompt.py`)
- Sets up the system prompt for the multiplication assistant
- Instructs the LLM to extract numbers from user input
- Configures the agent to use the multiply tool

### 4. Agent Creation (`agent.py`)
- Creates a ReAct agent using LangGraph
- Combines the LLM, tools, and prompts
- Configures the agent for function calling

### 5. Main Application (`app.py`)
- Handles user input and agent interaction
- Processes the response and extracts the final answer
- Provides a simple interface for testing

## Running the Application

### 1. Start Ollama Server

```bash
# In a separate terminal
ollama serve
```

### 2. Run the Application

```bash
# Activate virtual environment
source venv/bin/activate

# Run the application
python app.py
```

### 3. Expected Output

```
******STARTING APP******

User input: what's of 2 * 4 ??
***calling function for a=2, b=4 ***
Response: The result of 2 * 4 is 8.

******End of Agent Response******
```

## Configuration Options

### Using Different Ollama Port

If you need to run Ollama on a different port:

```bash
# Set custom port
export OLLAMA_HOST=0.0.0.0:4892
ollama serve
```

Update `llm_model.py`:
```python
llm_instance = ChatOllama(
    model="llama3.1:8b",
    base_url="http://localhost:4892",
    temperature=0
)
```

### Alternative: Using Azure OpenAI

To use Azure OpenAI instead of local Ollama, uncomment the Azure configuration in `llm_model.py` and update your API credentials.

## Troubleshooting

### 1. Ollama Connection Issues
- Ensure Ollama is running: `ollama serve`
- Check if the model is pulled: `ollama list`
- Verify the port is correct (default: 11434)

### 2. Function Calling Issues
- Some local models have limited function calling support
- Try using Azure OpenAI for better tool calling capabilities
- Ensure your prompt is clear and specific

### 3. Memory Issues
- Llama 3.1 8B requires significant RAM
- Consider using a smaller model if needed: `ollama pull llama3.1:7b`

### 4. Python Environment Issues
- Ensure virtual environment is activated
- Check Python version: `python --version`
- Reinstall dependencies if needed

## Performance Notes

- First run may be slow as the model loads into memory
- Subsequent runs should be faster
- Model stays in memory for better performance
- Use `ollama stop <model>` to free memory when done

## Development

To add new tools or modify the agent:

1. Define new functions in `tools.py`
2. Add them to the tools list in `agent.py`
3. Update prompts in `prompt.py` if needed
4. Test with different inputs in `app.py`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.
