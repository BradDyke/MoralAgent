"""
Base interface for AI engine integrations.

MoralAgent does not depend on a specific AI engine.
Engine adapters should implement this interface and submit
proposed actions to the MoralAgent governance layer.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict
from uuid import uuid4

class BaseEngine(ABC):
    """
    Common interface for AI engine integrations.
    """

    engine_name = "unknown"

    @abstractmethod
    def generate(self, request: str, context: Dict[str, Any] | None = None) -> str:
        """
        Generate a proposed action from an AI engine.

        The engine is responsible for generating the proposed action.
        MoralAgent is responsible for evaluating its governance risk.

        Args:
            request: User or system request.
            context: Optional contextual information.

        Returns:
            The AI engine's proposed action.
        """
        raise NotImplementedError

    def create_action(self, request: str, proposed_action: str) -> Dict[str, Any]:
        """
        Convert an engine response into the standardized
        MoralAgent action format.
        """

return {
    "action_id": f"ACT-{uuid4().hex}",
    "request": request,
    "proposed_action": proposed_action,
    "source_engine": self.engine_name,
    "context": {},
}
