# Deep Learning Projects

A collection of hands-on projects and notebooks covering neural networks, computer vision, generative models, natural language processing, retrieval-augmented generation (RAG), and AI-powered applications. The repository is organized by topic so each experiment can be explored independently.

## Contents

| Folder or file | Description |
| --- | --- |
| `neuron.ipynb` | A minimal neuron implemented with PyTorch |
| `FNN/` | Feed-forward neural network classification and regression notebooks, with their tabular datasets |
| `CNN/` | Convolutional neural network image classification with CIFAR-10 |
| `GAN/` | A generative adversarial network for image generation |
| `RNN/` | Recurrent neural network sentiment analysis using the IMDB dataset |
| `transformer/` | A text summarization project using the SAMSum dataset and Hugging Face Transformers |
| `RAG/` | A retrieval-augmented generation pipeline using local documents |
| `Agentic_AI/` | Agent examples for web research, finance, persistent memory, and multilingual teams |
| `ai_assistant/` | A Flask-based assistant and email summarization application |
| `flask/` | Flask examples covering routes, templates, forms, and JSON responses |

## Getting Started

### Requirements

- Python 3.10 or later
- Git
- Jupyter Notebook or JupyterLab for notebook projects
- A compatible machine for the selected project; some deep-learning workloads benefit from a CUDA-capable GPU

Individual projects use different libraries. Depending on the project, these include PyTorch, torchvision, pandas, scikit-learn, Hugging Face Transformers, Flask, Streamlit, and Agno. Install the dependencies required by the notebook or application you intend to run.

### Set up a Python environment

From the repository root, create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install jupyterlab
```

If PowerShell prevents environment activation, use the Python executable in `.venv\Scripts\python.exe` directly, or activate the environment using your preferred shell.

### Run a notebook

Install that notebook's dependencies, then start Jupyter:

```powershell
jupyter lab
```

Open the notebook for the project you want to explore. Some notebooks use relative paths to read data files; start Jupyter from the relevant project folder when necessary. Run the cells in order.

### Run an application

Install the application's dependencies before launching it. For the Flask assistant:

```powershell
cd ai_assistant
python -m pip install flask openai python-dotenv
python main.py
```

For the Streamlit YouTube analyzer:

```powershell
cd Agentic_AI
python -m pip install streamlit agno openai python-dotenv
streamlit run ui.py
```

The agent examples in `Agentic_AI/` may also require the provider and tool packages used by the selected example.

## API Keys

Some projects call hosted AI services and require API credentials. Set the relevant key in your environment before starting the application or notebook. For example, in PowerShell:

```powershell
$env:OPENAI_API_KEY = "your-openai-api-key"
$env:GROQ_API_KEY = "your-groq-api-key"
```

Use only the keys required by the project you are running. Never commit API keys, passwords, or other credentials to the repository. The `.gitignore` excludes `.env` files; keep local credentials in an ignored `.env` file when the application loads them with `python-dotenv`.

## Data and Model Files

Datasets and pretrained/generated model files can be large. Some sample datasets are included, while large datasets, model checkpoints, and generated outputs are excluded from Git. Download or prepare any excluded assets according to the instructions in the relevant notebook before running it. Model downloads may require additional disk space and time.

## Notes

- These projects are intended for learning and experimentation, not production deployment.
- AI-generated outputs may be inaccurate; independently verify important results.
- Respect the licenses and usage terms of datasets, models, and external services used by each project.
