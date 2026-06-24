# 2. agent terminal app

This folder contains a small terminal chat app built from the same agent setup as the notebook.

## Files

```text
app/
  agent.py
  main.py
  middlewares/
  tools/
  utils/
  README.md
```

## Setup

Make sure your virtual environment is activated.

On macOS and Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

The app expects a `GOOGLE_API_KEY` in the repository `.env` file:

```env
GOOGLE_API_KEY=<your_google_ai_studio_api_key>
```

## Run The App

From the repository root, run:

```bash
python tutorials/2_agent/app/main.py
```

You can then chat with the agent directly in the terminal.

Use:

- `exit`
- `quit`

to stop the app.

## Memory

The app uses `InMemorySaver`, just like the notebook example.

That means conversation memory works during the current terminal session, but it resets when the script stops.
