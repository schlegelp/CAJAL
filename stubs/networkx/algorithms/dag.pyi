from _typeshed import Incomplete
from collections.abc import Generator

def descendants(G, source): ...
def ancestors(G, source): ...
def is_directed_acyclic_graph(G): ...
def topological_generations(G) -> Generator[Incomplete, None, None]: ...
def topological_sort(G) -> None: ...
def lexicographical_topological_sort(G, key: Incomplete | None = ...) -> Generator[Incomplete, None, Incomplete]: ...
def all_topological_sorts(G) -> Generator[Incomplete, None, None]: ...
def is_aperiodic(G): ...
def transitive_closure(G, reflexive: bool = ...): ...
def transitive_closure_dag(G, topo_order: Incomplete | None = ...): ...
def transitive_reduction(G): ...
def antichains(G, topo_order: Incomplete | None = ...) -> Generator[Incomplete, None, None]: ...
def dag_longest_path(G, weight: str = ..., default_weight: int = ..., topo_order: Incomplete | None = ...): ...
def dag_longest_path_length(G, weight: str = ..., default_weight: int = ...): ...
def dag_to_branching(G): ...
