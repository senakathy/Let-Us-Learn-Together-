#Student: Kathyllen de Alcantara Sena
# December 2nd, 2025

class Graph:
    """
    A simple directed graph implemented using an adjacency list.

    It uses two parallel lists to represent the graph structure:

    - ``_vertices`` is a tuple of all vertices in the graph.
    - ``_adj_list`` is a list of lists where each inner list holds
      the terminal vertices for the vertex at the same index in ``_verti
      ces``.

    For example:
        If _vertices[2] == "c", then _adj_list[2] contains the list of
        vertices that have edges starting from "c".
    """

    def __init__(self, vertices):
        """
        Constructor automatically called when creating a Graph instance.

        :param vertices: a list of all vertices in the graph
        """

        # Note: private variables start with an underscore so that
        # they can't be accessed outside the class definition
        self._vertices = tuple(vertices)  # make an immutable copy
        self._adj_list = []

        # initialize adjacency list with an empty list for each vertex
        for vertex in vertices:
            self._adj_list.append([])

    def add_edge(self, start, end):
        """Add a directed edge from start -> end if both vertices 
           exist."""

        # Verify both vertices are in the graph
        if start in self._vertices and end in self._vertices:
            i = self._vertices.index(start)
            # Verify the edge is not already in the graph
            if end not in self._adj_list[i]:
                self._adj_list[i].append(end)
        else:
            raise ValueError(f"Edge ({start}, {end}) has invalid vertices.)")

    def get_vertices(self):
        """ Return an immutable list of all vertices in the graph. """
        return self._vertices

    def get_edges(self):
        """
        Return an immutable list of all edges in the graph.

        Each edge is represented as a tuple (start, end),
        e.g., (('a', 'b'), ('b', 'c'))
        """
        edges = list()
        # TODO Implement this method - 2 points
        for i in range(len(self._vertices)):
            start = self._vertices[i]
            # (start, end)
            for j in range(len(self._adj_list[i])):
                edge = (start, self._adj_list[i][j])
                edges.append(edge)

        return tuple(edges)

    def is_reflexive(self):
        """Return True if the graph is reflexive."""
        # TODO Implement this method - 2 points
        for i in range(len(self._vertices)):
            found = False
            start = self._vertices[i]
            # (start, end)
            for j in range(len(self._adj_list[i])):
                if (self._adj_list[i][j] == self._vertices[i]):
                    found = True 
                    break
            if (not found):
                return False
        return True

    def is_symmetric(self):
        """Return True if the graph is symmetric."""
        # TODO Implement this method - 2 points

        edges = self.get_edges()
        for i in range(len(edges)):
            found = False
            start, end  = edges[i]
            for j in range (len(edges)):
                start1, end1 = edges[j]
                if (start == end1 and end == start1):
                    found = True
                    break
            if(not found):
                return False
        return True

    def is_transitive(self):
        """Return True if the graph is transitive."""
        # TODO Implement this method - 2 points

        edges = self.get_edges()
        for i in range(len(edges)):
            start, end  = edges[i]
    
            for j in range (len(edges)):
                start1, end1 = edges[j]
                if (start1 == end):
                    if ( (start, end1) not in edges):
                        return False
                       
        return True

    def is_antisymmetric(self):
        """Return True if the graph is antisymmetric."""
        # TODO Implement this method - 2 points 

        edges = self.get_edges()
        for i in range(len(edges)):
            start, end  = edges[i]
            for j in range (len(edges)):
                start1, end1 = edges[j]
                if (start == end1 and end == start1):
                    if (start != end):
                        return False
        return True

    def is_equivalence_relation(self):
        """Return True if the graph represents an equivalence relation."""
        # TODO Implement this method - 2 points
        if (self.is_reflexive() and self.is_symmetric() and 
            self.is_transitive()):
            return True
        else:
            return False

    def is_partial_order(self):
        """Return True if the graph represents a partial order relation."""
        # TODO Implement this method - 2 points
        if (self.is_reflexive() and self.is_antisymmetric() and 
            self.is_transitive()):
            return True
        else:
            return False

    def __all_edges_exist(self, start, vertices):
        """
        Return True if the graph contains an edge from ``start`` to
        every vertex in the list ``vertices``.

        This helper method checks whether all pairs (start, v) are edges
        in the graph, where v ranges over the given list of ``vertices``.

        It is useful when implementing properties such as transitivity,
        where we need to verify that certain required edges exist.

        :param start: the starting vertex of the edges being checked
        :param vertices: a list of vertices that should each be reachable
                         directly from ``start``
        :return: True if all edges start -> v exist, otherwise False
        """
        i = self._vertices.index(start)
        for v in vertices:
            if v not in self._adj_list[i]:
                return False
        return True

    def __str__(self):
        """ Return a string representation of the graph instance. """
        result = "Directed Graph:\n"
        for i in range(len(self._vertices)):
            result += f"{self._vertices[i]} -> {self._adj_list[i]}\n"
        return result.rstrip("\n")
