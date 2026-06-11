"""
Base Component Module

Abstract base class for all dashboard components.
Provides common interface and methods for component creation and rendering.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class BaseComponent(ABC):
	"""Base class for single dashboard components.

	Subclasses must implement `build_component(entity_id, model)` and may
	implement `component_data(entity_id, model)` when SQL-backed data is needed.
	"""

	def __init__(
		self,
		component_id: str,
		title: str = "",
		css_class: str = "",
		attrs: Optional[Dict[str, Any]] = None,
	) -> None:
		self.component_id = component_id
		self.title = title
		self.css_class = css_class
		self.attrs = attrs or {}

	@abstractmethod
	def build_component(self, entity_id: Any, model: Any) -> Any:
		"""Build and return a single HTML/FastHTML component."""
		raise NotImplementedError

	def component_data(self, entity_id: Any, model: Any) -> Any:
		"""Fetch data needed by `build_component`.

		Override this method in subclasses that need SQL-backed data.
		"""
		raise NotImplementedError

	def __call__(self, entity_id: Any, model: Any) -> Any:
		"""Allow instances to be called like functions by CombinedComponent."""
		return self.build_component(entity_id, model)

	def get_id(self) -> str:
		return self.component_id

	def set_title(self, title: str) -> "BaseComponent":
		self.title = title
		return self

	def add_css_class(self, css_class: str) -> "BaseComponent":
		if not css_class:
			return self

		if not self.css_class:
			self.css_class = css_class
			return self

		current = set(self.css_class.split())
		for cls in css_class.split():
			if cls not in current:
				self.css_class += f" {cls}"
		return self

	def to_html(self, entity_id: Any, model: Any) -> str:
		return str(self.build_component(entity_id, model))
