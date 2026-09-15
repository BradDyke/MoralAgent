"""
Tests for the MoralAgent audit adapter.

The QA audit adapter records governance decisions.
It does not make governance decisions.
"""

from adapters.audit_adapter import AuditAdapter


def test_audit_record():
    audit = AuditAdapter()

    action = {
        "request": "Perform a routine system check.",
        "proposed_action": "Perform the system check.",
        "source_engine": "openai",
        "context": {},
    }

    evaluation = {
        "evaluation_id": "test-evaluation-001",
        "risk_level": "low",
        "policy_result": "pass",
        "human_review_required": False,
        "decision": "proceed",
        "reason": "Routine low-risk action.",
    }

    record = audit.record(
        action=action,
        evaluation=evaluation,
    )

    assert "timestamp" in record
    assert record["source_engine"] == "openai"
    assert record["request"] == action["request"]
    assert record["proposed_action"] == action["proposed_action"]
    assert record["evaluation"] == evaluation


def test_audit_preserves_block_decision():
    audit = AuditAdapter()

    action = {
        "request": "Perform an unsafe operation.",
        "proposed_action": "Disable security controls.",
        "source_engine": "llama",
        "context": {},
    }

    evaluation = {
        "evaluation_id": "test-evaluation-002",
        "risk_level": "critical",
        "policy_result": "violation",
        "human_review_required": True,
        "decision": "block",
        "reason": "Critical policy violation.",
    }

    record = audit.record(
        action=action,
        evaluation=evaluation,
    )

    assert record["source_engine"] == "llama"
    assert record["evaluation"]["risk_level"] == "critical"
    assert record["evaluation"]["decision"] == "block"
    assert record["evaluation"]["human_review_required"] is True
