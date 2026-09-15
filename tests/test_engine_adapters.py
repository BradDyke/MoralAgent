"""
Tests for MoralAgent AI engine adapters.

These tests verify that different AI engines conform to the
same interface and produce standardized proposed actions.
"""

from engines.openai.adapter import OpenAIAdapter
from engines.ollama.adapter import OllamaAdapter
from engines.llama.adapter import LlamaAdapter


def test_openai_adapter():
    engine = OpenAIAdapter()

    request = "Perform a routine system check."
    proposed_action = engine.generate(request)

    action = engine.create_action(
        request=request,
        proposed_action=proposed_action
    )

    assert action["source_engine"] == "openai"
    assert action["request"] == request
    assert "proposed_action" in action


def test_ollama_adapter():
    engine = OllamaAdapter()

    request = "Perform a routine system check."
    proposed_action = engine.generate(request)

    action = engine.create_action(
        request=request,
        proposed_action=proposed_action
    )

    assert action["source_engine"] == "ollama"
    assert action["request"] == request
    assert "proposed_action" in action


def test_llama_adapter():
    engine = LlamaAdapter()

    request = "Perform a routine system check."
    proposed_action = engine.generate(request)

    action = engine.create_action(
        request=request,
        proposed_action=proposed_action
    )

    assert action["source_engine"] == "llama"
    assert action["request"] == request
    assert "proposed_action" in action
