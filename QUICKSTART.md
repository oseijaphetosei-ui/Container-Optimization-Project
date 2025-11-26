# Quick Start Guide

Get up and running with the Container Optimization project in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

### Step 1: Clone or Navigate to the Project
```bash
cd /Users/japhetacquahosei/Container-Optimization-Project
```

### Step 2: Install Dependencies
```bash
pip3 install -r requirements.txt
```

This will install:
- numpy (numerical computations)
- scipy (optimization)
- matplotlib (plotting)
- plotly (interactive 3D graphics)
- streamlit (web interface)
- pandas (data handling)
- pytest (testing)

## Running the Application

### Option 1: Web Interface (Recommended)
```bash
streamlit run app.py
```

Your browser will automatically open to `http://localhost:8501`

**What you can do:**
- 🏠 **Home**: Overview and introduction
- 🔵 **Cylinder Optimizer**: Find optimal cylinder dimensions
- 📦 **Box Optimizer**: Find optimal box dimensions
- 📊 **Shape Comparison**: Compare different container types
- 📚 **Math Background**: Learn about Lagrange multipliers

### Option 2: Python Code
```python
from src.optimization import CylinderOptimizer, RectangularBoxOptimizer, compare_shapes

# Example 1: Optimize a closed cylinder with volume 1000
optimizer = CylinderOptimizer(volume=1000, closed=True)
r, h, surface_area = optimizer.analytical_solution()

print(f"Optimal Cylinder:")
print(f"  Radius: {r:.2f}")
print(f"  Height: {h:.2f}")
print(f"  Surface Area: {surface_area:.2f}")
print(f"  Relationship: h/r = {h/r:.2f} (should be ~2)")

# Example 2: Compare all shapes
results = compare_shapes(volume=1000)
for shape, data in results.items():
    print(f"\n{shape}:")
    print(f"  Surface Area: {data['surface_area']:.2f}")
```

### Option 3: Run Tests
```bash
pytest tests/ -v
```

All 14 tests should pass!

## Quick Examples

### Example 1: Optimize an Open Cylinder
```python
from src.optimization import CylinderOptimizer

optimizer = CylinderOptimizer(volume=500, closed=False)
r, h, sa = optimizer.analytical_solution()
print(f"Open cylinder: r={r:.2f}, h={h:.2f}, h/r={h/r:.2f}")
# Output: h/r ≈ 1.0 (height equals radius)
```

### Example 2: Optimize an Open Box
```python
from src.optimization import RectangularBoxOptimizer

optimizer = RectangularBoxOptimizer(volume=1000, open_top=True)
l, w, h, sa = optimizer.analytical_solution()
print(f"Open box: l={l:.2f}, w={w:.2f}, h={h:.2f}")
print(f"Base is square: l=w? {abs(l-w) < 0.01}")
print(f"l/h ratio: {l/h:.2f} (should be ~2)")
```

### Example 3: Visualize Results
```python
from src.optimization import CylinderOptimizer
from src.visualization import plot_cylinder_3d, plot_optimization_landscape_cylinder

# Find optimal dimensions
optimizer = CylinderOptimizer(volume=1000, closed=True)
r, h, sa = optimizer.analytical_solution()

# Create 3D visualization
fig_3d = plot_cylinder_3d(r, h, closed=True)
fig_3d.show()

# Create optimization landscape
fig_landscape = plot_optimization_landscape_cylinder(
    volume=1000, closed=True, optimal_r=r, optimal_h=h
)
fig_landscape.show()
```

## Common Use Cases

### For Students
1. Run the web app: `streamlit run app.py`
2. Navigate to "Math Background" to see derivations
3. Try different volumes in "Cylinder Optimizer"
4. Compare shapes in "Shape Comparison"

### For Researchers/Engineers
1. Use the Python API for batch calculations
2. Modify optimization.py to add constraints
3. Add custom visualization functions
4. Integrate into your existing workflow

### For Teachers
1. Use the web interface for live demonstrations
2. Show students the mathematical derivations
3. Have students verify results by hand
4. Assign exercises: "What if we change the constraint?"

## Troubleshooting

### Issue: "Module not found"
**Solution:** Make sure you're in the project directory and have installed dependencies:
```bash
cd /Users/japhetacquahosei/Container-Optimization-Project
pip3 install -r requirements.txt
```

### Issue: "Port already in use" when running Streamlit
**Solution:** Use a different port:
```bash
streamlit run app.py --server.port 8502
```

### Issue: Tests fail
**Solution:** Make sure all dependencies are installed:
```bash
pip3 install pytest
pytest tests/ -v
```

## What to Try First

1. **Start here**: Run `streamlit run app.py` and explore the Home page
2. **Try the Cylinder Optimizer** with volume = 1000 (default)
3. **Check the Math Background** page to understand the theory
4. **Compare all shapes** to see which is most efficient
5. **Read the derivations** in `docs/derivations.md`

## Next Steps

- Read `PROJECT_STATUS.md` for implementation details
- Check `docs/derivations.md` for full mathematical proofs
- Explore the source code in `src/`
- Modify and extend the project for your needs
- Star the repo if you find it useful!

## Key Results to Remember

| Container | Optimal Relationship |
|-----------|---------------------|
| Closed Cylinder | h = 2r (height = diameter) |
| Open Cylinder | h = r (height = radius) |
| Open Box | l = w = 2h (square base) |
| Closed Box | l = w = h (perfect cube) |

## Support

- **Documentation**: README.md, PROJECT_STATUS.md, docs/derivations.md
- **Email**: jotk2024@mymail.pomona.edu
- **Issues**: Use GitHub issues for bug reports

---

**Ready to go?** Run `streamlit run app.py` and start exploring! 🚀
