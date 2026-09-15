"""
Tests for the MoralAgent action adapter.

These tests verify that an AI engine can generate a proposed action
and that the action is passed through MoralAgent for evaluation.
"""

from adapters.action_adapter import ActionAdapter
from engines.openai.adapter import OpenAIAdapter
from engines.ollama.adapter import OllamaAdapter
from engines.llama.adapter import LlamaAdapter


def test_openai_action_adapter():
    engine = OpenAIAdapter()
    adapter = ActionAdapter(engine)

    result = adapter.evaluate_request(
        "Perform a routine system check."
    )

    assert result["action"]["source_engine"] == "openai"
    assert "proposed_action" in result["action"]
    assert "evaluation" in result
    assert result["evaluation"]["decision"] == "proceed"


def test_ollama_action_adapter():
    engine = OllamaAdapter()
    adapter = ActionAdapter(engine)

    result = adapter.evaluate_request(
        "Perform a routine system check."
    )

    assert result["action"]["source_engine"] == "ollama"
    assert "proposed_action" in result["action"]
    assert "evaluation" in result
    assert result["evaluation"]["decision"] == "proceed"


def test_llama_action_adapter():
    engine = LlamaAdapter()
    adapter = ActionAdapter(engine)

    result = adapter.evaluate_request(
        "Perform a routine system check."
    )

    assert result["action"]["source_engine"] == "llama"
    assert "proposed_action" in result["action"]
    assert "evaluation" in result
    assert result["evaluation"]["decision"] == "proceed"


def test_high_risk_action_requires_review():
    engine = OpenAIAdapter()
    adapter = ActionAdapter(engine)

    result = adapter.evaluate_request(
        "Perform a high impact operation.",
        risk_factors=["human_impact", "security"],
    )

    assert result["evaluation"]["risk_level"] == "high"
    assert result["evaluation"]["decision"] == "review"
    assert result["evaluation"]["human_review_required"] is True
