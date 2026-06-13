import json
import itertools
from dataclasses import dataclass, asdict
from typing import List, Tuple, Dict, Any


@dataclass
class Component:
    """A UI component placed on the canvas."""
    id: int
    type: str
    position: Tuple[int, int]

    def to_dict(self) -> Dict[str, Any]:
        return {"id": self.id, "type": self.type, "position": list(self.position)}


class BuilderError(Exception):
    """Base exception for builder errors."""
    pass


class ComponentNotFoundError(BuilderError):
    """Raised when a component ID cannot be found."""
    pass


class Builder:
    """Core logic for a drag‑and‑drop MVP builder."""

    _id_counter = itertools.count(1)

    def __init__(self) -> None:
        self._components: List[Component] = []

    # Public API -------------------------------------------------------------

    def add_component(self, type_: str, position: Tuple[int, int]) -> Component:
        """Create a new component and place it on the canvas.

        Args:
            type_: The component type (e.g., "button").
            position: (x, y) coordinates.

        Returns:
            The created Component instance.
        """
        if not isinstance(position, tuple) or len(position) != 2:
            raise ValueError("position must be a tuple of two ints")
        comp_id = next(self._id_counter)
        component = Component(id=comp_id, type=type_, position=position)
        self._components.append(component)
        return component

    def move_component(self, component_id: int, new_position: Tuple[int, int]) -> None:
        """Move an existing component to a new position.

        Raises:
            ComponentNotFoundError: If the component does not exist.
        """
        comp = self._find_by_id(component_id)
        if not isinstance(new_position, tuple) or len(new_position) != 2:
            raise ValueError("new_position must be a tuple of two ints")
        comp.position = new_position

    def render(self) -> List[Dict[str, Any]]:
        """Return a serialisable preview of the current design."""
        # Sort by id for deterministic output
        return [c.to_dict() for c in sorted(self._components, key=lambda c: c.id)]

    def save(self, file_path: str) -> None:
        """Persist the current design to a JSON file."""
        data = self.render()
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    @classmethod
    def load(cls, file_path: str) -> "Builder":
        """Load a design from a JSON file and return a Builder instance."""
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        builder = cls()
        # Reset counter to avoid id collisions with loaded ids
        max_id = 0
        for item in data:
            comp = Component(
                id=item["id"],
                type=item["type"],
                position=tuple(item["position"]),
            )
            builder._components.append(comp)
            max_id = max(max_id, comp.id)

        # Ensure future ids start after the highest loaded id
        cls._id_counter = itertools.count(max_id + 1)
        return builder

    # Internal helpers -------------------------------------------------------

    def _find_by_id(self, component_id: int) -> Component:
        for comp in self._components:
            if comp.id == component_id:
                return comp
        raise ComponentNotFoundError(f"Component with id {component_id} not found")
