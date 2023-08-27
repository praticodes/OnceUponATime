"""This file defines the graph data structure, nodes, edges, attributes, and relationships.
The structure of the graph data structure in this file is largely drawn from the format promoted in the University of Toronto's 
CSC111: Foundations of Computer Science II. I took this course in the Winter, 2023 Semester.
"""

from __future__ import annotations
from typing import Any

class _Node:
    """A node in a graph.

    Instance Attributes:
        - item: The data stored in this vertex.
        - neighbours: The nodes that are adjacent to this node.
    """
    item: Any
    neighbours: set[_Node]

    def __init__(self, item: Any, neighbours: set[_Node]) -> None:
        """Initialize a new node with the given item and neighbours."""
        self.item = item
        self.neighbours = neighbours

  class Graph:
    """A graph.

    Representation Invariants:
    - all(item == self.nodes[item].item for item in self._nodes)
    """
    # Private Instance Attributes:
    #     - _vertices: A collection of the nodes contained in this graph.
    #                  Maps item to _Node instance.
    _vertices: dict[Any, _Node]

    def __init__(self) -> None:
        """Initialize an empty graph (no vertices or edges)."""
        self._nodes = {}
