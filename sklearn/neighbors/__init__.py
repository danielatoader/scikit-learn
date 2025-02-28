"""
The :mod:`sklearn.neighbors` module implements the k-nearest neighbors
algorithm.
"""

from ._ball_tree import BallTree
from ._kd_tree import KDTree
from ._graph import kneighbors_graph, radius_neighbors_graph
from ._graph import KNeighborsTransformer, RadiusNeighborsTransformer
from ._unsupervised import NearestNeighbors
from ._classification import KNeighborsClassifier, RadiusNeighborsClassifier
from ._regression import KNeighborsRegressor, RadiusNeighborsRegressor
from ._nearest_centroid import NearestCentroid
from ._kde import KernelDensity
from ._lof import LocalOutlierFactor
from ._nca import NeighborhoodComponentsAnalysis
from ._base import sort_graph_by_row_values
from ._base import VALID_METRICS, VALID_METRICS_SPARSE

__all__ = [
    "BallTree",
    "KDTree",
    "KNeighborsClassifier",
    "KNeighborsRegressor",
    "KNeighborsTransformer",
    "NearestCentroid",
    "NearestNeighbors",
    "RadiusNeighborsClassifier",
    "RadiusNeighborsRegressor",
    "RadiusNeighborsTransformer",
    "kneighbors_graph",
    "radius_neighbors_graph",
    "KernelDensity",
    "LocalOutlierFactor",
    "NeighborhoodComponentsAnalysis",
    "sort_graph_by_row_values",
    "VALID_METRICS",
    "VALID_METRICS_SPARSE",
]
