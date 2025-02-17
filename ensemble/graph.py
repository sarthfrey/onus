import inspect
import numpy as np

from collections import defaultdict
from .node import Node
from typing import Dict, List, Optional


class Graph:
  """
  Background object that maintains ensemble tree hierarchies for a session

  | **nodes**: `node_name -> Node()`
  | **arg_names**: `model_name -> arg_names`
  | **ensemble_groups**: `model_name -> ensemble_names`
  | **weight_map**: `ensemble_name -> model_name -> weight`
  """
  nodes = {}                          # node_name     -> Node()
  arg_names = defaultdict(set)        # model_name    -> arg_names
  ensemble_groups = defaultdict(set)  # model_name    -> ensemble_names
  weight_map = defaultdict(dict)      # ensemble_name -> model_name -> weight

  def __init__(self, *args, **kwargs):
    raise NotImplementedError('You may not instantiate the Graph class')

  @classmethod
  def add_node(cls, ensemble_name: str, node: Node, weight: Optional[np.float] = None):
    cls.nodes[node.get_name()] = node
    cls.ensemble_groups[node.get_name()] |= set([ensemble_name])
    if weight is not None:
      cls.weight_map[ensemble_name][node.get_name()] = weight

  @classmethod
  def _get_children(cls, ensemble_name: str) -> Dict[str, Node]:
    return {
      node_name: node for node_name, node in cls.nodes.items() if ensemble_name in cls.ensemble_groups[node_name]
    }

  @classmethod
  def _get_weights(cls, ensemble_name: str) -> Optional[List[np.float]]:
    return list(cls.weight_map[ensemble_name].values()) if cls.weight_map[ensemble_name] else None
