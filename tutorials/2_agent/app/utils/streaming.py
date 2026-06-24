"""Streaming helpers for terminal-based agent interactions."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any


def _message_text(message: Any) -> str:
    text = getattr(message, "text", None)
    if isinstance(text, str):
        return text
    if callable(text):
        value = text()
        if isinstance(value, str):
            return value

    content = getattr(message, "content", "")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                parts.append(str(item.get("text", "")))
        return "".join(parts)
    return ""


def _message_type(message: Any) -> str:
    explicit_type = getattr(message, "type", None)
    if isinstance(explicit_type, str):
        return explicit_type
    return message.__class__.__name__.lower()


def _tool_call_key(tool_call: Any) -> str:
    if isinstance(tool_call, dict):
        return str(tool_call.get("id") or tool_call.get("name") or tool_call)
    return str(getattr(tool_call, "id", None) or getattr(tool_call, "name", None))


def _tool_call_name(tool_call: Any) -> str:
    if isinstance(tool_call, dict):
        return str(tool_call.get("name", "unknown_tool"))
    return str(getattr(tool_call, "name", "unknown_tool"))


def _tool_call_args(tool_call: Any) -> Any:
    if isinstance(tool_call, dict):
        return tool_call.get("args", {})
    return getattr(tool_call, "args", {})


def render_agent_stream(agent: Any, prompt: str, config: dict[str, Any]) -> None:
    """Render a LangChain/LangGraph agent stream in the terminal."""
    seen_tool_calls: set[str] = set()
    seen_tool_messages: set[str] = set()
    last_assistant_text = ""
    assistant_started = False

    stream_input = {"messages": [{"role": "user", "content": prompt}]}
    chunks: Iterable[dict[str, Any]] = agent.stream(
        stream_input, config=config, stream_mode="values"
    )

    for chunk in chunks:
        messages = chunk.get("messages", [])
        if not messages:
            continue

        message = messages[-1]

        for tool_call in getattr(message, "tool_calls", []) or []:
            call_key = _tool_call_key(tool_call)
            if call_key in seen_tool_calls:
                continue
            seen_tool_calls.add(call_key)
            print(
                f"[tool] {_tool_call_name(tool_call)} args={_tool_call_args(tool_call)}"
            )

        message_type = _message_type(message)
        if "tool" in message_type:
            tool_message_id = str(getattr(message, "id", None) or id(message))
            if tool_message_id not in seen_tool_messages:
                seen_tool_messages.add(tool_message_id)
                tool_name = getattr(message, "name", "tool")
                tool_text = _message_text(message)
                print(f"[tool-result] {tool_name}: {tool_text}")
            continue

        if "ai" not in message_type and "assistant" not in message_type:
            continue

        text = _message_text(message)
        if not text:
            continue

        if not assistant_started:
            print("Assistant: ", end="", flush=True)
            assistant_started = True

        if text.startswith(last_assistant_text):
            delta = text[len(last_assistant_text) :]
        else:
            delta = text

        if delta:
            print(delta, end="", flush=True)
            last_assistant_text = text

    if assistant_started:
        print()
