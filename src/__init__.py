"""Container Optimization Package.

This package provides tools for optimizing container dimensions
using multivariable calculus and Lagrange multipliers.
"""

from .optimization import (
    CylinderOptimizer,
    RectangularBoxOptimizer,
    compare_shapes
)

from .visualization import (
    plot_cylinder_3d,
    plot_box_3d,
    plot_optimization_landscape_cylinder,
    plot_optimization_landscape_box,
    plot_shape_comparison,
    plot_dimensions_comparison
)

__version__ = '1.0.0'

__all__ = [
    'CylinderOptimizer',
    'RectangularBoxOptimizer',
    'compare_shapes',
    'plot_cylinder_3d',
    'plot_box_3d',
    'plot_optimization_landscape_cylinder',
    'plot_optimization_landscape_box',
    'plot_shape_comparison',
    'plot_dimensions_comparison'
]