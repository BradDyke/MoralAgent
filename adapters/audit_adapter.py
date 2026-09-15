"""
Audit adapter for MoralAgent.

The QA audit adapter records governance evaluation results.
It does not make governance decisions.
"""

from datetime import datetime, timezone
from typing import Any, Dict


class AuditAdapter:
    """
    Creates standardized audit records from MoralAgent evaluations.
    """

    def record(
        self,
        action: Dict[str, Any],
        evaluation: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Create an audit record for a governance evaluation.
        """

        return {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "source_engine": action.get("source_engine"),
            "request": action.get("request"),
            "proposed_action": action.get("proposed_action"),
            "evaluation": evaluation,
        }
