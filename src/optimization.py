""" Container Optimization using Lagrange Multipliers

This module implements optimization algorithms to find container dimensions
that minimize surface area for a given volume using multivariable calculus.
"""

import numpy as np
from scipy.optimize import fsolve, minimize
from typing import Tuple, Dict


class CylinderOptimizer:
    """Optimize cylinder dimensions to minimize surface area for given volume."""
    
    def __init__(self, volume: float, closed: bool = True):
        """
        Initialize cylinder optimizer.
        
        Args:
            volume: Required volume (must be positive)
            closed: True for closed cylinder, False for open top
        """
        if volume <= 0:
            raise ValueError("Volume must be positive")
        self.volume = volume
        self.closed = closed
    
    def analytical_solution(self) -> Tuple[float, float, float]:
        """
        Find optimal dimensions using analytical solution from Lagrange multipliers.
        
        For a closed cylinder:
        - Surface area: S = 2πr² + 2πrh
        - Volume constraint: V = πr²h
        - Result: h = 2r (height equals diameter)
        
        For an open cylinder:
        - Surface area: S = πr² + 2πrh
        - Volume constraint: V = πr²h
        - Result: h = r
        
        Returns:
            Tuple of (radius, height, surface_area)
        """
        if self.closed:
            # Closed cylinder: h = 2r
            # From V = πr²h and h = 2r: V = 2πr³
            # So r = (V / (2π))^(1/3)
            r = (self.volume / (2 * np.pi)) ** (1/3)
            h = 2 * r
            surface_area = 2 * np.pi * r**2 + 2 * np.pi * r * h
        else:
            # Open cylinder: h = r
            # From V = πr²h and h = r: V = πr³
            # So r = (V / π)^(1/3)
            r = (self.volume / np.pi) ** (1/3)
            h = r
            surface_area = np.pi * r**2 + 2 * np.pi * r * h
        
        return r, h, surface_area
    
    def numerical_solution(self) -> Tuple[float, float, float]:
        """
        Find optimal dimensions using numerical optimization.
        
        Returns:
            Tuple of (radius, height, surface_area)
        """
        def surface_area(r):
            """Calculate surface area given radius."""
            if r <= 0:
                return np.inf
            h = self.volume / (np.pi * r**2)
            if self.closed:
                return 2 * np.pi * r**2 + 2 * np.pi * r * h
            else:
                return np.pi * r**2 + 2 * np.pi * r * h
        
        # Initial guess
        r0 = (self.volume / np.pi) ** (1/3)
        
        # Minimize surface area
        result = minimize(surface_area, r0, method='Nelder-Mead')
        
        if result.success:
            r = result.x[0]
            h = self.volume / (np.pi * r**2)
            return r, h, result.fun
        else:
            raise RuntimeError("Numerical optimization failed")
    
    def surface_area_for_dimensions(self, r: float, h: float) -> float:
        """
        Calculate surface area for given dimensions.
        
        Args:
            r: Radius
            h: Height
            
        Returns:
            Surface area
        """
        if self.closed:
            return 2 * np.pi * r**2 + 2 * np.pi * r * h
        else:
            return np.pi * r**2 + 2 * np.pi * r * h
    
    def verify_volume(self, r: float, h: float) -> bool:
        """
        Verify that given dimensions satisfy volume constraint.
        
        Args:
            r: Radius
            h: Height
            
        Returns:
            True if volume constraint is satisfied (within tolerance)
        """
        calculated_volume = np.pi * r**2 * h
        return np.isclose(calculated_volume, self.volume, rtol=1e-6)


class RectangularBoxOptimizer:
    """Optimize rectangular box dimensions to minimize surface area for given volume."""
    
    def __init__(self, volume: float, open_top: bool = True):
        """
        Initialize rectangular box optimizer.
        
        Args:
            volume: Required volume (must be positive)
            open_top: True for open top box, False for closed box
        """
        if volume <= 0:
            raise ValueError("Volume must be positive")
        self.volume = volume
        self.open_top = open_top
    
    def analytical_solution(self) -> Tuple[float, float, float, float]:
        """
        Find optimal dimensions using analytical solution from Lagrange multipliers.
        
        For an open top box:
        - Surface area: S = lw + 2lh + 2wh
        - Volume constraint: V = lwh
        - Result: l = w = 2h (base is square, sides are half the base)
        
        For a closed box:
        - Surface area: S = 2lw + 2lh + 2wh
        - Volume constraint: V = lwh
        - Result: l = w = h (cube)
        
        Returns:
            Tuple of (length, width, height, surface_area)
        """
        if self.open_top:
            # Open top box: l = w = 2h
            # From V = lwh and l = w = 2h: V = 4h³
            # So h = (V / 4)^(1/3)
            h = (self.volume / 4) ** (1/3)
            l = 2 * h
            w = 2 * h
            surface_area = l * w + 2 * l * h + 2 * w * h
        else:
            # Closed box: l = w = h (cube)
            # From V = lwh and l = w = h: V = h³
            # So h = V^(1/3)
            h = self.volume ** (1/3)
            l = h
            w = h
            surface_area = 2 * l * w + 2 * l * h + 2 * w * h
        
        return l, w, h, surface_area
    
    def numerical_solution(self) -> Tuple[float, float, float, float]:
        """
        Find optimal dimensions using numerical optimization.
        
        Returns:
            Tuple of (length, width, height, surface_area)
        """
        def surface_area(params):
            """Calculate surface area given length and width."""
            l, w = params
            if l <= 0 or w <= 0:
                return np.inf
            h = self.volume / (l * w)
            if h <= 0:
                return np.inf
            
            if self.open_top:
                return l * w + 2 * l * h + 2 * w * h
            else:
                return 2 * l * w + 2 * l * h + 2 * w * h
        
        # Initial guess
        if self.open_top:
            h0 = (self.volume / 4) ** (1/3)
            l0 = 2 * h0
            w0 = 2 * h0
        else:
            l0 = w0 = self.volume ** (1/3)
        
        # Minimize surface area
        result = minimize(surface_area, [l0, w0], method='Nelder-Mead')
        
        if result.success:
            l, w = result.x
            h = self.volume / (l * w)
            return l, w, h, result.fun
        else:
            raise RuntimeError("Numerical optimization failed")
    
    def surface_area_for_dimensions(self, l: float, w: float, h: float) -> float:
        """
        Calculate surface area for given dimensions.
        
        Args:
            l: Length
            w: Width
            h: Height
            
        Returns:
            Surface area
        """
        if self.open_top:
            return l * w + 2 * l * h + 2 * w * h
        else:
            return 2 * l * w + 2 * l * h + 2 * w * h
    
    def verify_volume(self, l: float, w: float, h: float) -> bool:
        """
        Verify that given dimensions satisfy volume constraint.
        
        Args:
            l: Length
            w: Width
            h: Height
            
        Returns:
            True if volume constraint is satisfied (within tolerance)
        """
        calculated_volume = l * w * h
        return np.isclose(calculated_volume, self.volume, rtol=1e-6)


def compare_shapes(volume: float) -> Dict[str, Dict[str, float]]:
    """
    Compare optimal dimensions and surface areas for different container shapes.
    
    Args:
        volume: Required volume for all containers
        
    Returns:
        Dictionary with results for each shape
    """
    results = {}
    
    # Closed cylinder
    cyl_closed = CylinderOptimizer(volume, closed=True)
    r, h, sa = cyl_closed.analytical_solution()
    results['cylinder_closed'] = {
        'radius': r,
        'height': h,
        'surface_area': sa,
        'dimensions_ratio': h / r
    }
    
    # Open cylinder
    cyl_open = CylinderOptimizer(volume, closed=False)
    r, h, sa = cyl_open.analytical_solution()
    results['cylinder_open'] = {
        'radius': r,
        'height': h,
        'surface_area': sa,
        'dimensions_ratio': h / r
    }
    
    # Open top box
    box_open = RectangularBoxOptimizer(volume, open_top=True)
    l, w, h, sa = box_open.analytical_solution()
    results['box_open'] = {
        'length': l,
        'width': w,
        'height': h,
        'surface_area': sa,
        'dimensions_ratio': l / h
    }
    
    # Closed box (cube)
    box_closed = RectangularBoxOptimizer(volume, open_top=False)
    l, w, h, sa = box_closed.analytical_solution()
    results['box_closed'] = {
        'length': l,
        'width': w,
        'height': h,
        'surface_area': sa,
        'dimensions_ratio': l / h
    }
    
    return results