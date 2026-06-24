"""Agent factory for the terminal agent tutorial."""

from __future__ import annotations

from deepagents import create_deep_agent
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver

from tools import TOOLS

SYSTEM_PROMPT = "You are a helpful assistant. Use the available tools when they help."


def build_model() -> ChatGoogleGenerativeAI:
    """Build the Gemini chat model used in this tutorial."""
    return ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite",
        temperature=0,
        thinking_level="minimal",
    )


def build_agent(use_deepagent: bool = True):
    """Build the stateful tutorial agent."""
    memory = InMemorySaver()
    model = build_model()

    if use_deepagent:
        deep_agent_kwargs = {
            "model": model,
            "tools": TOOLS,
            "system_prompt": SYSTEM_PROMPT,
        }
        try:
            return create_deep_agent(
                checkpointer=memory,
                **deep_agent_kwargs,
            )
        except TypeError:
            return create_deep_agent(**deep_agent_kwargs)

    return create_agent(
        model=model,
        tools=TOOLS,
        system_prompt=SYSTEM_PROMPT,
        checkpointer=memory,
    )


def build_config(thread_id: str = "tutorial-thread") -> dict[str, dict[str, str]]:
    """Build the runtime config used for conversation memory."""
    return {"configurable": {"thread_id": thread_id}}
