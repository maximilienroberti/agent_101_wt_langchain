"""Terminal entrypoint for the tutorial agent."""

from __future__ import annotations

from dotenv import load_dotenv

from agent import build_agent, build_config
from utils import render_agent_stream


def main() -> None:
    """Run a simple terminal chat loop."""
    load_dotenv()

    agent = build_agent()
    config = build_config()

    print("Terminal agent ready. Type your question and press Enter.")
    print("Type 'quit' or 'exit' to stop.\n")

    while True:
        try:
            prompt = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break

        if not prompt:
            continue

        if prompt.lower() in {"quit", "exit"}:
            print("Goodbye.")
            break

        try:
            render_agent_stream(agent, prompt, config)
        except KeyboardInterrupt:
            print("\nRequest interrupted.\n")
            continue
        except Exception as exc:
            print(f"Agent error: {exc}")
            print("Check your network access and GOOGLE_API_KEY, then try again.\n")
            continue
        print()


if __name__ == "__main__":
    main()
