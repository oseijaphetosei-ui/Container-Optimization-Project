"""Unit tests for optimization module."""

import pytest
import numpy as np
from src.optimization import (
    CylinderOptimizer, 
    RectangularBoxOptimizer, 
    compare_shapes
)


class TestCylinderOptimizer:
    """Test cases for CylinderOptimizer class."""
    
    def test_closed_cylinder_analytical(self):
        """Test analytical solution for closed cylinder."""
        volume = 1000.0
        optimizer = CylinderOptimizer(volume, closed=True)
        r, h, sa = optimizer.analytical_solution()
        
        # Verify optimal relationship: h = 2r
        assert np.isclose(h, 2 * r, rtol=1e-6)
        
        # Verify volume constraint
        assert optimizer.verify_volume(r, h)
        
        # Verify surface area calculation
        expected_sa = 2 * np.pi * r**2 + 2 * np.pi * r * h
        assert np.isclose(sa, expected_sa, rtol=1e-6)
    
    def test_open_cylinder_analytical(self):
        """Test analytical solution for open cylinder."""
        volume = 500.0
        optimizer = CylinderOptimizer(volume, closed=False)
        r, h, sa = optimizer.analytical_solution()
        
        # Verify optimal relationship: h = r
        assert np.isclose(h, r, rtol=1e-6)
        
        # Verify volume constraint
        assert optimizer.verify_volume(r, h)
        
        # Verify surface area calculation
        expected_sa = np.pi * r**2 + 2 * np.pi * r * h
        assert np.isclose(sa, expected_sa, rtol=1e-6)
    
    def test_numerical_matches_analytical_closed(self):
        """Test that numerical solution matches analytical for closed cylinder."""
        volume = 1000.0
        optimizer = CylinderOptimizer(volume, closed=True)
        
        r_analytical, h_analytical, sa_analytical = optimizer.analytical_solution()
        r_numerical, h_numerical, sa_numerical = optimizer.numerical_solution()
        
        # Solutions should be very close
        assert np.isclose(r_analytical, r_numerical, rtol=1e-3)
        assert np.isclose(h_analytical, h_numerical, rtol=1e-3)
        assert np.isclose(sa_analytical, sa_numerical, rtol=1e-3)
    
    def test_numerical_matches_analytical_open(self):
        """Test that numerical solution matches analytical for open cylinder."""
        volume = 500.0
        optimizer = CylinderOptimizer(volume, closed=False)
        
        r_analytical, h_analytical, sa_analytical = optimizer.analytical_solution()
        r_numerical, h_numerical, sa_numerical = optimizer.numerical_solution()
        
        # Solutions should be very close
        assert np.isclose(r_analytical, r_numerical, rtol=1e-3)
        assert np.isclose(h_analytical, h_numerical, rtol=1e-3)
        assert np.isclose(sa_analytical, sa_numerical, rtol=1e-3)
    
    def test_invalid_volume(self):
        """Test that invalid volume raises ValueError."""
        with pytest.raises(ValueError):
            CylinderOptimizer(0)
        
        with pytest.raises(ValueError):
            CylinderOptimizer(-100)
    
    def test_surface_area_calculation(self):
        """Test surface area calculation for given dimensions."""
        volume = 1000.0
        optimizer = CylinderOptimizer(volume, closed=True)
        
        r, h = 5.0, 10.0
        sa = optimizer.surface_area_for_dimensions(r, h)
        expected = 2 * np.pi * r**2 + 2 * np.pi * r * h
        
        assert np.isclose(sa, expected, rtol=1e-6)


class TestRectangularBoxOptimizer:
    """Test cases for RectangularBoxOptimizer class."""
    
    def test_open_box_analytical(self):
        """Test analytical solution for open top box."""
        volume = 1000.0
        optimizer = RectangularBoxOptimizer(volume, open_top=True)
        l, w, h, sa = optimizer.analytical_solution()
        
        # Verify optimal relationship: l = w = 2h
        assert np.isclose(l, w, rtol=1e-6)
        assert np.isclose(l, 2 * h, rtol=1e-6)
        
        # Verify volume constraint
        assert optimizer.verify_volume(l, w, h)
        
        # Verify surface area calculation
        expected_sa = l * w + 2 * l * h + 2 * w * h
        assert np.isclose(sa, expected_sa, rtol=1e-6)
    
    def test_closed_box_analytical(self):
        """Test analytical solution for closed box (cube)."""
        volume = 1000.0
        optimizer = RectangularBoxOptimizer(volume, open_top=False)
        l, w, h, sa = optimizer.analytical_solution()
        
        # Verify optimal relationship: l = w = h (cube)
        assert np.isclose(l, w, rtol=1e-6)
        assert np.isclose(l, h, rtol=1e-6)
        
        # Verify volume constraint
        assert optimizer.verify_volume(l, w, h)
        
        # Verify surface area calculation
        expected_sa = 2 * l * w + 2 * l * h + 2 * w * h
        assert np.isclose(sa, expected_sa, rtol=1e-6)
    
    def test_numerical_matches_analytical_open(self):
        """Test that numerical solution matches analytical for open box."""
        volume = 1000.0
        optimizer = RectangularBoxOptimizer(volume, open_top=True)
        
        l_analytical, w_analytical, h_analytical, sa_analytical = optimizer.analytical_solution()
        l_numerical, w_numerical, h_numerical, sa_numerical = optimizer.numerical_solution()
        
        # Solutions should be very close
        assert np.isclose(l_analytical, l_numerical, rtol=1e-2)
        assert np.isclose(w_analytical, w_numerical, rtol=1e-2)
        assert np.isclose(h_analytical, h_numerical, rtol=1e-2)
        assert np.isclose(sa_analytical, sa_numerical, rtol=1e-2)
    
    def test_numerical_matches_analytical_closed(self):
        """Test that numerical solution matches analytical for closed box."""
        volume = 1000.0
        optimizer = RectangularBoxOptimizer(volume, open_top=False)
        
        l_analytical, w_analytical, h_analytical, sa_analytical = optimizer.analytical_solution()
        l_numerical, w_numerical, h_numerical, sa_numerical = optimizer.numerical_solution()
        
        # Solutions should be very close
        assert np.isclose(l_analytical, l_numerical, rtol=1e-2)
        assert np.isclose(w_analytical, w_numerical, rtol=1e-2)
        assert np.isclose(h_analytical, h_numerical, rtol=1e-2)
        assert np.isclose(sa_analytical, sa_numerical, rtol=1e-2)
    
    def test_invalid_volume(self):
        """Test that invalid volume raises ValueError."""
        with pytest.raises(ValueError):
            RectangularBoxOptimizer(0)
        
        with pytest.raises(ValueError):
            RectangularBoxOptimizer(-100)
    
    def test_surface_area_calculation(self):
        """Test surface area calculation for given dimensions."""
        volume = 1000.0
        optimizer = RectangularBoxOptimizer(volume, open_top=True)
        
        l, w, h = 10.0, 10.0, 5.0
        sa = optimizer.surface_area_for_dimensions(l, w, h)
        expected = l * w + 2 * l * h + 2 * w * h
        
        assert np.isclose(sa, expected, rtol=1e-6)


class TestCompareShapes:
    """Test cases for shape comparison function."""
    
    def test_compare_shapes(self):
        """Test shape comparison function."""
        volume = 1000.0
        results = compare_shapes(volume)
        
        # Check that all expected shapes are present
        expected_shapes = ['cylinder_closed', 'cylinder_open', 'box_open', 'box_closed']
        assert all(shape in results for shape in expected_shapes)
        
        # Check that each shape has required keys
        for shape in expected_shapes:
            assert 'surface_area' in results[shape]
            assert 'dimensions_ratio' in results[shape]
        
        # Verify that all volumes are correct
        cyl_closed = results['cylinder_closed']
        calc_volume = np.pi * cyl_closed['radius']**2 * cyl_closed['height']
        assert np.isclose(calc_volume, volume, rtol=1e-5)
        
        box_open = results['box_open']
        calc_volume = box_open['length'] * box_open['width'] * box_open['height']
        assert np.isclose(calc_volume, volume, rtol=1e-5)
    
    def test_dimension_ratios(self):
        """Test that dimension ratios match theoretical values."""
        volume = 1000.0
        results = compare_shapes(volume)
        
        # Closed cylinder: h/r = 2
        assert np.isclose(results['cylinder_closed']['dimensions_ratio'], 2.0, rtol=1e-6)
        
        # Open cylinder: h/r = 1
        assert np.isclose(results['cylinder_open']['dimensions_ratio'], 1.0, rtol=1e-6)
        
        # Open box: l/h = 2 (since l = w = 2h)
        assert np.isclose(results['box_open']['dimensions_ratio'], 2.0, rtol=1e-6)
        
        # Closed box: l/h = 1 (cube)
        assert np.isclose(results['box_closed']['dimensions_ratio'], 1.0, rtol=1e-6)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])