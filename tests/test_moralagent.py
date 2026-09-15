"""
MoralAgent Test Suite

Prototype v0.1

Tests the fundamental governance decisions:

    LOW RISK       -> PROCEED
    UNCERTAIN      -> REVIEW
    HIGH RISK      -> REVIEW
    POLICY         -> BLOCK
"""

import sys
from pathlib import Path

# Allow the test to import moralagent.py from the repository root
sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1])
)

from moralagent import MoralAgent


def create_agent():
    """Create a standard MoralAgent test instance."""

    policy = {
        "policy_id": "MORALAGENT-HIGH-IMPACT-v0.1"
    }

    return MoralAgent(policy)


def test_low_risk_action_proceeds():

    agent = create_agent()

    result = agent.evaluate(
        action_id="TEST-001",
        action="Recommend a routine infrastructure change.",
        risk_factors=[],
        uncertainty=False
    )

    assert result.decision == "proceed"
    assert result.risk_level == "low"
    assert result.human_review_required is False


def test_uncertain_action_requires_review():

    agent = create_agent()

    result = agent.evaluate(
        action_id="TEST-002",
        action="Recommend an action with uncertain consequences.",
        risk_factors=[],
        uncertainty=True
    )

    assert result.decision == "review"
    assert result.human_review_required is True


def test_high_risk_action_requires_review():

    agent = create_agent()

    result = agent.evaluate(
        action_id="TEST-003",
        action="Recommend a high-impact organizational action.",
        risk_factors=[
            "significant societal impact",
            "potential human harm"
        ],
        uncertainty=False
    )

    assert result.decision == "review"
    assert result.risk_level == "high"
    assert result.human_review_required is True


def test_policy_violation_is_blocked():

    agent = create_agent()

    result = agent.evaluate(
        action_id="TEST-004",
        action="Disable security controls to bypass safety.",
        risk_factors=[
            "security violation"
        ],
        uncertainty=False
    )

    assert result.decision == "block"
    assert result.policy_result == "violation"
    assert result.human_review_required is True


def test_critical_risk_is_blocked():

    agent = create_agent()

    result = agent.evaluate(
        action_id="TEST-005",
        action="Propose a consequential action.",
        risk_factors=[
            "human harm",
            "legal risk",
            "societal harm",
            "loss of control"
        ],
        uncertainty=False
    )

    assert result.decision == "block"
    assert result.risk_level == "critical"
