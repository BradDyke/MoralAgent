"""
Action adapter for connecting AI engines to MoralAgent.

The adapter creates a controlled boundary between an AI engine
and the MoralAgent governance layer.
"""

from typing import Any, Dict

from moralagent import MoralAgent
from engines.base_engine import BaseEngine


class ActionAdapter:
    """
    Connects an AI engine to the MoralAgent governance engine.

    The AI engine generates the proposed action.
    MoralAgent evaluates the proposed action.
    """

    def __init__(self, engine: BaseEngine):
        self.engine = engine
        self.moral_agent = MoralAgent()

    def evaluate_request(
        self,
        request: str,
        context: Dict[str, Any] | None = None,
        risk_factors: list[str] | None = None,
        uncertainty: bool = False,
    ) -> Dict[str, Any]:
        """
        Generate an AI proposed action and submit it to MoralAgent.
        """

        proposed_action = self.engine.generate(
            request=request,
            context=context
        )

        action = self.engine.create_action(
            request=request,
            proposed_action=proposed_action
        )

        evaluation = self.moral_agent.evaluate(
            action_id=action["action_id"],
            action=action["proposed_action"],
            risk_factors=risk_factors,
            uncertainty=uncertainty,
        )

        return {
            "action": action,
            "evaluation": self.moral_agent.result_to_dict(evaluation),
        }
