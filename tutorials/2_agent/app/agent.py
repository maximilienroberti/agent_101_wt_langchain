"""Agent factory for the terminal agent tutorial."""

from __future__ import annotations

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
    )


def build_agent():
    """Build the stateful tutorial agent."""
    memory = InMemorySaver()
    return create_agent(
        model=build_model(),
        tools=TOOLS,
        system_prompt=SYSTEM_PROMPT,
        checkpointer=memory,
    )


def build_config(thread_id: str = "tutorial-thread") -> dict[str, dict[str, str]]:
    """Build the runtime config used for conversation memory."""
    return {"configurable": {"thread_id": thread_id}}
