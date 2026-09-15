"""
MoralAgent
Human-Centered AI Governance Engine

Prototype v0.1

Purpose:
    Evaluate AI-proposed actions against governance policies
    and return a structured PROCEED / REVIEW / BLOCK decision.

Core principle:
    AI may identify an ethical concern.
    AI should not become the final authority over human values.
"""

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import List, Dict, Any


@dataclass
class EvaluationResult:
    evaluation_id: str
    timestamp: str
    action_id: str
    policy_id: str

    risk_level: str
    risk_factors: List[str]

    policy_result: str
    uncertainty: bool
    human_review_required: bool

    decision: str
    reason: str


class MoralAgent:

def __init__(self, policy: Dict[str, Any] | None = None):
    self.policy = policy or {
        "policy_id": "MORALAGENT-DEFAULT-v0.1"
    }

    def evaluate(
        self,
        action_id: str,
        action: str,
        risk_factors: List[str] | None = None,
        uncertainty: bool = False,
    ) -> EvaluationResult:

        risk_factors = risk_factors or []

        risk_level = self._determine_risk(
            risk_factors,
            uncertainty
        )

        policy_result = self._evaluate_policy(
            action,
            risk_level
        )

        decision = self._determine_decision(
            risk_level,
            policy_result,
            uncertainty
        )

        human_review_required = decision in {
            "review",
            "block"
        }

        reason = self._build_reason(
            risk_level,
            policy_result,
            uncertainty,
            decision
        )

        return EvaluationResult(
            evaluation_id=self._generate_id(),
            timestamp=datetime.now(
                timezone.utc
            ).isoformat(),

            action_id=action_id,
            policy_id=self.policy.get(
                "policy_id",
                "unknown"
            ),

            risk_level=risk_level,
            risk_factors=risk_factors,

            policy_result=policy_result,
            uncertainty=uncertainty,

            human_review_required=human_review_required,

            decision=decision,
            reason=reason
        )

    def _determine_risk(
        self,
        risk_factors: List[str],
        uncertainty: bool
    ) -> str:

        count = len(risk_factors)

        if count >= 4:
            return "critical"

        if count >= 2:
            return "high"

        if count == 1:
            return "moderate"

        if uncertainty:
            return "moderate"

        return "low"

    def _evaluate_policy(
        self,
        action: str,
        risk_level: str
    ) -> str:

        blocked_terms = [
            "bypass safety",
            "disable security",
            "unauthorized access",
            "destroy evidence",
            "harm a person"
        ]

        action_lower = action.lower()

        for term in blocked_terms:
            if term in action_lower:
                return "violation"

        if risk_level in {
            "high",
            "critical"
        }:
            return "review_required"

        return "pass"

    def _determine_decision(
        self,
        risk_level: str,
        policy_result: str,
        uncertainty: bool
    ) -> str:

        if policy_result == "violation":
            return "block"

        if risk_level == "critical":
            return "block"

        if risk_level == "high":
            return "review"

        if uncertainty:
            return "review"

        if policy_result == "review_required":
            return "review"

        return "proceed"

    def _build_reason(
        self,
        risk_level: str,
        policy_result: str,
        uncertainty: bool,
        decision: str
    ) -> str:

        reasons = []

        reasons.append(
            f"Risk level assessed as {risk_level}."
        )

        reasons.append(
            f"Policy evaluation result: {policy_result}."
        )

        if uncertainty:
            reasons.append(
                "Significant uncertainty remains."
            )

        if decision == "proceed":
            reasons.append(
                "No governance condition currently "
                "requires human intervention."
            )

        elif decision == "review":
            reasons.append(
                "Authorized human review is required "
                "before consequential execution."
            )

        elif decision == "block":
            reasons.append(
                "The proposed action must not proceed "
                "without an authorized governance decision."
            )

        return " ".join(reasons)

    def _generate_id(self) -> str:

        timestamp = datetime.now(
            timezone.utc
        ).strftime("%Y%m%d%H%M%S%f")

        return f"eval-{timestamp}"


@staticmethod
def result_to_dict(
    result: EvaluationResult
) -> Dict[str, Any]:

    return asdict(result)


if __name__ == "__main__":

    policy = {
        "policy_id": "MORALAGENT-HIGH-IMPACT-v0.1"
    }

    agent = MoralAgent(policy)

    result = agent.evaluate(
        action_id="ACTION-001",
        action="Recommend a routine infrastructure change.",
        risk_factors=[],
        uncertainty=False
    )

    print("MoralAgent Evaluation")
    print("=====================")

    for key, value in result_to_dict(result).items():
        print(f"{key}: {value}")
