# LangChain with Assistant UI

This project shows a simple setup for working with LangChain and an Assistant UI.

## Installation

Make sure you have Python 3.11 or newer installed.

You can check your Python version with:

```bash
python3 --version
```

For a faster clean setup from the repository root, you can run:

```bash
make clean_install
```

That will remove `.venv`, recreate it, upgrade `pip`, and install everything from `requirements.txt`.
It will use Python 3.11 or above if one is available on your machine.

If you prefer to run the setup manually:

Create a Python virtual environment named `.venv`:

```bash
python3.11 -m venv .venv
```

Activate the virtual environment:

On macOS and Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Upgrade `pip`:

```bash
python -m pip install --upgrade pip
```

Install the project dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## LangSmith Setup

To set up LangSmith, go to `https://smith.langchain.com/`.

Create an API key:

1. Go to `Settings`.
2. Open `API Keys`.
3. Create a new API key.
4. Save the key somewhere safe because you will need it in your `.env` file.

Create a `.env` file in the project root and add the following variables:

```env
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=<your_api_key>
LANGSMITH_PROJECT="the_name_of_your_project"
```

Replace:

- `<your_api_key>` with the API key you created in LangSmith.
- `"the_name_of_your_project"` with the project name you want to use in LangSmith.

## Google AI Studio Setup

You also need a Google AI Studio API key.

You can get a free key by going to `https://aistudio.google.com/`.

Once you have created the key, add it to your `.env` file:

```env
GOOGLE_API_KEY=<your_ai_google_studio_api_key>
```

Replace `<your_ai_google_studio_api_key>` with your Google AI Studio API key.

## Reference

LangChain docs:

`https://docs.langchain.com/oss/python/langchain/agents`
