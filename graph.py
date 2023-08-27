"""This file defines the graph data structure, nodes, edges, attributes, and relationships.
The structures of the Graph and Node superclasses in this file are largely drawn from the format promoted in the
University of Toronto's CSC111: Foundations of Computer Science II lectures.
I took this course in the Winter, 2023 Semester.
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

    def add_node(self, item: Any):
        """Add a vertex with the given item to this graph.

        The new vertex is not adjacent to any other vertices.

        Preconditions:
            - item not in self._vertices
        """
        self._nodes[item] = _Node(item, set())

    def add_connection(self, item1: Any, item2: Any) -> None:
        """Add a connection between the two nodes with the given items in this graph.

        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - item1 != item2
        """
        if item1 in self._nodes and item2 in self._nodes:
            n1 = self._nodes[item1]
            n2 = self._nodes[item2]

            # Add the new edge
            n1.neighbours.add(n2)
            n2.neighbours.add(n1)
        else:
            # We didn't find an existing vertex for both items.
            raise ValueError


class Character(_Node):
    """A character _Node in the TaleGraph.

    Instance Attributes:
        - name: The name of the character.
        - traits: List of character traits.
        - motive: Character's motive or goal.
        - relationships: Dictionary of character relationships.
        - attitudes:  Dictionary of character attitudes towards other characters.
    """
    name: str
    traits: list[str]
    motive: str
    relationships: dict[str, str]
    attitudes: dict[str, str]

    def __init__(self, name: str, traits: list[str], motive: str, relationships: dict[str, str], attitudes: dict[str, str]) -> None:
        """Initialize a character node with the given attributes."""
        super().__init__({'name': name, 'traits': traits, 'motive': motive, 'relationships': relationships, 'attitudes': attitudes}, set())

    def add_relationship(self, character: Character, relationship_type: str) -> None:
        """Add a relationship to another character."""
        self.item['relationships'][character.name] = relationship_type
        character.item['relationships'][self.name] = relationship_type


class Setting(_Node):
    """
    A setting _Node in the TaleGraph.

    Instance Attributes:
        - name: The name of the character.
        - descriptions: list of descriptions of the setting.
    """
    name: str
    descriptions: list[str]

    def __init__(self, name: str, descriptions: list[str]) -> None:
        """Initialize a setting node with the given attributes."""
        super().__init__({'name': name, 'description': descriptions}, set())


class Object(_Node):
    """
    A setting Object in the TaleGraph.

    Instance Attributes:
        - name: The name of the object.
        - descriptions: list of descriptions or properties of the setting.
    """
    name: str
    descriptions: list[str]

    def __init__(self, name: str, descriptions: list[str]) -> None:
        """Initialize an object node with the given attributes."""
        super().__init__({'name': name, 'description': descriptions}, set())


class TaleGraph(Graph):
    """
    This is a subclass of Graph that stores information on all characters, objects, and settings in a tale.
    >>> cinderella = TaleGraph()
    >>> cinderella.add_character('Cinderella', ['kind', 'caring', 'hardworking', 'beautiful'], 'attend the royal ball', {'lover': 'Prince Charming', 'step-mother': 'Lady Tremaine', 'step sister': 'Anastasia', 'step sister': 'Drizella'}, {'Prince Charming': 'love'})
    >>> cinderella.add_setting('the enchanted forest', ['magical', 'vast', 'beautiful'])
    >>> cinderella.add_object('the glass slipper', ['magical', 'elegant', 'delicate'])
    """

    def __init__(self):
        super().__init__()

    def add_character(self, name: str, traits: list[str], motive: str, relationships: dict[str, str], attitudes: dict[str, str]) -> None:
        """ Add a character as a _Node in the graph.
        """
        character = Character(name, traits, motive, relationships, attitudes)
        self._nodes[name] = character

    def add_setting(self, name: str, descriptions: list[str]) -> None:
        """ Add a setting as a _Node in the graph.
        """
        setting = Setting(name, descriptions)
        self._nodes[name] = setting

    def add_object(self, name: str, descriptions: list[str]) -> None:
        """ Add an object as a _Node in the graph.
        """
        setting = Setting(name, descriptions)
        self._nodes[name] = setting



