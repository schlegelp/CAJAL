from . import exceptions as exceptions, grouping as grouping, util as util
from .constants import log as log, tol as tol
from .geometry import faces_to_edges as faces_to_edges
from _typeshed import Incomplete
from networkx.classes import graph

def face_adjacency(faces: Incomplete | None = ..., mesh: Incomplete | None = ..., return_edges: bool = ...): ...
def face_neighborhood(mesh): ...
def face_adjacency_unshared(mesh): ...
def face_adjacency_radius(mesh): ...
def vertex_adjacency_graph(mesh) -> graph.Graph : ...
def shared_edges(faces_a, faces_b): ...
def facets(mesh, engine: Incomplete | None = ...): ...
def split(mesh, only_watertight: bool = ..., adjacency: Incomplete | None = ..., engine: Incomplete | None = ..., **kwargs): ...
def connected_components(edges, min_len: int = ..., nodes: Incomplete | None = ..., engine: Incomplete | None = ...): ...
def connected_component_labels(edges, node_count: Incomplete | None = ...): ...
def split_traversal(traversal, edges, edges_hash: Incomplete | None = ...): ...
def fill_traversals(traversals, edges, edges_hash: Incomplete | None = ...): ...
def traversals(edges, mode: str = ...): ...
def edges_to_coo(edges, count: Incomplete | None = ..., data: Incomplete | None = ...): ...
def neighbors(edges, max_index: Incomplete | None = ..., directed: bool = ...): ...
def smoothed(mesh, angle: Incomplete | None = ..., facet_minarea: int = ...): ...
def is_watertight(edges, edges_sorted: Incomplete | None = ...): ...
def graph_to_svg(graph): ...
def multigraph_paths(G, source, cutoff: Incomplete | None = ...): ...
def multigraph_collect(G, traversal, attrib: Incomplete | None = ...): ...
