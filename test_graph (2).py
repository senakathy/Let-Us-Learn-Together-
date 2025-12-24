import pytest
from graph import Graph

# ---------------------------------------------------------
# Fixtures
# ---------------------------------------------------------
@pytest.fixture
def small_graph():
    """Graph with three vertices but no edges."""
    return Graph(["a", "b", "c"])


@pytest.fixture
def graph_with_edges():
    """Graph preloaded with a->b and b->c."""
    g = Graph(["a", "b", "c"])
    g.add_edge("a", "b")
    g.add_edge("b", "c")
    return g


# ---------------------------------------------------------
# Test add_edge and get_edges
# ---------------------------------------------------------
def test_add_edge_valid(small_graph):
    g = small_graph
    g.add_edge("a", "b")

    edges = g.get_edges()
    assert ("a", "b") in edges
    assert edges.count(("a", "b")) == 1   # no duplicates


def test_add_edge_ignores_invalid_vertices(small_graph):
    g = small_graph
    # Behavior depends on your implementation:
    # Either raise ValueError or ignore silently.
    with pytest.raises(ValueError):
        g.add_edge("x", "a")

# TODO add unit tests for the is_ methods
"""
Unit tests typically follow the Arrange–Act–Assert pattern:

1. Arrange:
   Set up everything the test needs.
   This includes creating objects, adding data, or preparing inputs.

2. Act:
   Perform the action you want to test.
   Usually this means calling a method or function.

3. Assert:
   Check that the result is what you expect.
   Assertions confirm whether the test passes or fails.
"""

# ---------------------------------------------------------
# Reflexive tests
# ---------------------------------------------------------
def test_is_reflexive_true():
    # Arrange the data for the test
    vertices = ["a", "b", "c"]
    g = Graph(vertices)
    for v in vertices:
        g.add_edge(v, v)

    # Act
    result = g.is_reflexive()

    # Assert
    assert result is True

def test_is_reflexive_false():
    # Arrange
    g = Graph(["a", "b", "c"])
    g.add_edge("a", "a")
    g.add_edge("b", "b")
    # Missing edge (c,c)

    # Act
    result = g.is_reflexive()

    # Assert
    assert result is False
#===========================================================
def test_is_symmetric_true():
    # Arrange the data for the test
    vertices = ["a", "b", "c", "d"]
    g = Graph(vertices)
    g.add_edge(vertices[0], vertices[1])
    g.add_edge(vertices[1], vertices[0])

    # Act
    result = g.is_symmetric()

    # Assert
    assert result is True

def test_is_symmetric_false():
    # Arrange the data for the test
    vertices = ["a", "b", "c", "d"]
    g = Graph(vertices)
    g.add_edge(vertices[0], vertices[1])
    g.add_edge(vertices[1], vertices[2])

    # Act
    result = g.is_symmetric()

    # Assert
    assert result is False

def test_is_transitive_true():
    # Arrange the data for the test
    vertices = ["1", "2", "3", "4"]
    g = Graph(vertices)
    g.add_edge(vertices[0], vertices[1])
    g.add_edge(vertices[1], vertices[2])
    g.add_edge(vertices[0], vertices[2])

    # Act
    result = g.is_transitive()

    # Assert
    assert result is True

def test_is_transitive_false():
    # Arrange the data for the test
    vertices = ["1", "2", "3", "4"]
    g = Graph(vertices)
    g.add_edge(vertices[0], vertices[1])
    g.add_edge(vertices[1], vertices[2])
    g.add_edge(vertices[2], vertices[2])
    # Act
    result = g.is_transitive()

    # Assert
    assert result is False

def test_is_antisymmetric_true(): 
    # Arrange the data for the test
    vertices = ["1", "2", "3", "4"]
    g = Graph(vertices)
    g.add_edge(vertices[1],vertices[1])
    g.add_edge(vertices[2],vertices[2])
    g.add_edge(vertices[3],vertices[3])

    # Act
    result = g.is_antisymmetric()

    # Assert
    assert result is True

def test_is_antisymmetric_false(): 
    # Arrange the data for the test
    vertices = ["1", "2", "3", "4"]
    g = Graph(vertices)
    g.add_edge(vertices[1], vertices[2])
    g.add_edge(vertices[2], vertices[1])

    # Act
    result = g.is_antisymmetric()

    # Assert
    assert result is False

def test_is_equivalence_relation_true(): 
    # Arrange the data for the test
    vertices = ["1", "2", "3", "4"]
    g = Graph(vertices)
    for v in vertices:
        for v1 in vertices: 
            g.add_edge(v, v1)

    # Act
    result = g.is_equivalence_relation()

    # Assert
    assert result is True

def test_is_equivalence_relation_false(): 
    # Arrange the data for the test
    vertices = ["1", "2", "3", "4"]
    g = Graph(vertices)
    for v in vertices:
        for v1 in vertices[1:]: 
            g.add_edge(v, v1)

    # Act
    result = g.is_equivalence_relation()

    # Assert
    assert result is False

def test_is_partial_order_true(): 
    # Arrange the data for the test
    vertices = ["1", "2", "3", "4"]
    g = Graph(vertices)
    g.add_edge(vertices[0], vertices[0])
    g.add_edge(vertices[1], vertices[1])
    g.add_edge(vertices[2], vertices[2])
    g.add_edge(vertices[3], vertices[3])


    # Act
    result = g.is_partial_order()

    # Assert
    assert result is True

def test_is_partial_order_false(): 
    # Arrange the data for the test
    vertices = ["1", "2", "3", "4"]
    g = Graph(vertices)
    g.add_edge(vertices[0], vertices[0])
    g.add_edge(vertices[1], vertices[1])
    g.add_edge(vertices[2], vertices[2])

    # Act
    result = g.is_partial_order()

    # Assert
    assert result is False

    