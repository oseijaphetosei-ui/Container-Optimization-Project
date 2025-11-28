"""Streamlit web application for container optimization.

This app provides an interactive interface to explore container optimization
using Lagrange multipliers and multivariable calculus.
"""

import streamlit as st
import numpy as np
from src.optimization import (
    CylinderOptimizer,
    RectangularBoxOptimizer,
    compare_shapes
)
from src.visualization import (
    plot_cylinder_3d,
    plot_box_3d,
    plot_optimization_landscape_cylinder,
    plot_optimization_landscape_box,
    plot_shape_comparison
)

# Page configuration
st.set_page_config(
    page_title="Container Optimization",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and introduction
st.title("📦 Container Design Optimization")
st.markdown("""
    ### Using Multivariable Calculus to Minimize Surface Area
    
    This interactive tool demonstrates how **Lagrange multipliers** can be used to find
    optimal container dimensions that minimize material usage (surface area) for a given volume.
""")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose a page:",
    ["🏠 Home", "🔵 Cylinder Optimizer", "📦 Box Optimizer", "📊 Shape Comparison", "📚 Math Background"]
)

if page == "🏠 Home":
    st.header("Welcome to Container Optimization!")
    
    st.markdown("""
    ## What This Tool Does
    
    This application explores a classic optimization problem:
    
    **Given a fixed volume, what container shape uses the least material?**
    
    ### Key Features:
    - ✅ **Cylinder Optimization** - Find optimal radius and height
    - ✅ **Rectangular Box Optimization** - Find optimal dimensions
    - ✅ **Shape Comparison** - Compare different container types
    - ✅ **Interactive 3D Visualizations** - Rotate and explore the results
    - ✅ **Mathematical Derivations** - Learn the theory behind the optimization
    
    ### Mathematical Approach
    
    We use **Lagrange multipliers** to solve constrained optimization problems:
    
    1. **Objective Function**: Minimize surface area S(r, h)
    2. **Constraint**: Volume V = constant
    3. **Lagrangian**: L = S(r, h) - λ(V - constant)
    4. **Solution**: Find critical points where ∇L = 0
    
    ### Real-World Applications
    
    - 📦 **Packaging Design** - Minimize material costs
    - 🏭 **Manufacturing** - Optimize production efficiency
    - ♻️ **Sustainability** - Reduce waste
    - 💰 **Cost Reduction** - Lower material expenses
    """)

elif page == "🔵 Cylinder Optimizer":
    st.header("Cylinder Optimization")
    
    # Input parameters
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Input Parameters")
        volume = st.number_input(
            "Volume (cubic units)",
            min_value=1.0,
            max_value=10000.0,
            value=1000.0,
            step=100.0
        )
        
        cylinder_type = st.radio(
            "Cylinder Type",
            ["Closed (with top and bottom)", "Open (no top)"]
        )
        closed = cylinder_type.startswith("Closed")
    
    with col2:
        st.subheader("Mathematical Formulation")
        if closed:
            st.latex(r"\text{Minimize: } S = 2\pi r^2 + 2\pi rh")
            st.latex(r"\text{Subject to: } V = \pi r^2 h = " + f"{volume}")
            st.markdown("**Optimal Solution:** h = 2r")
        else:
            st.latex(r"\text{Minimize: } S = \pi r^2 + 2\pi rh")
            st.latex(r"\text{Subject to: } V = \pi r^2 h = " + f"{volume}")
            st.markdown("**Optimal Solution:** h = r")
    
    # Compute optimization
    optimizer = CylinderOptimizer(volume, closed=closed)
    r_analytical, h_analytical, sa_analytical = optimizer.analytical_solution()
    r_numerical, h_numerical, sa_numerical = optimizer.numerical_solution()
    
    # Display results
    st.subheader("Optimization Results")
    
    tab1, tab2 = st.tabs(["📊 Results", "🎨 3D Visualization"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Analytical Solution")
            st.metric("Optimal Radius", f"{r_analytical:.4f}")
            st.metric("Optimal Height", f"{h_analytical:.4f}")
            st.metric("Minimum Surface Area", f"{sa_analytical:.4f}")
            st.metric("Height/Radius Ratio", f"{h_analytical/r_analytical:.4f}")
        
        with col2:
            st.markdown("#### Numerical Verification")
            st.metric("Optimal Radius", f"{r_numerical:.4f}")
            st.metric("Optimal Height", f"{h_numerical:.4f}")
            st.metric("Minimum Surface Area", f"{sa_numerical:.4f}")
            st.metric("Height/Radius Ratio", f"{h_numerical/r_numerical:.4f}")
    
    with tab2:
        st.markdown("#### Interactive 3D Model")
        fig_3d, config_3d = plot_cylinder_3d(r_analytical, h_analytical, closed=closed)
        st.plotly_chart(fig_3d, use_container_width=True, config=config_3d)

elif page == "📦 Box Optimizer":
    st.header("Rectangular Box Optimization")
    
    # Input parameters
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Input Parameters")
        volume = st.number_input(
            "Volume (cubic units)",
            min_value=1.0,
            max_value=10000.0,
            value=1000.0,
            step=100.0,
            key="box_volume"
        )
        
        box_type = st.radio(
            "Box Type",
            ["Open Top", "Closed (all sides)"]
        )
        open_top = box_type == "Open Top"
    
    with col2:
        st.subheader("Mathematical Formulation")
        if open_top:
            st.latex(r"\text{Minimize: } S = lw + 2lh + 2wh")
            st.latex(r"\text{Subject to: } V = lwh = " + f"{volume}")
            st.markdown("**Optimal Solution:** l = w = 2h (square base)")
        else:
            st.latex(r"\text{Minimize: } S = 2lw + 2lh + 2wh")
            st.latex(r"\text{Subject to: } V = lwh = " + f"{volume}")
            st.markdown("**Optimal Solution:** l = w = h (cube)")
    
    # Compute optimization
    optimizer = RectangularBoxOptimizer(volume, open_top=open_top)
    l_analytical, w_analytical, h_analytical, sa_analytical = optimizer.analytical_solution()
    l_numerical, w_numerical, h_numerical, sa_numerical = optimizer.numerical_solution()
    
    # Display results
    st.subheader("Optimization Results")
    
    tab1, tab2 = st.tabs(["📊 Results", "🎨 3D Visualization"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Analytical Solution")
            st.metric("Optimal Length", f"{l_analytical:.4f}")
            st.metric("Optimal Width", f"{w_analytical:.4f}")
            st.metric("Optimal Height", f"{h_analytical:.4f}")
            st.metric("Minimum Surface Area", f"{sa_analytical:.4f}")
        
        with col2:
            st.markdown("#### Numerical Verification")
            st.metric("Optimal Length", f"{l_numerical:.4f}")
            st.metric("Optimal Width", f"{w_numerical:.4f}")
            st.metric("Optimal Height", f"{h_numerical:.4f}")
            st.metric("Minimum Surface Area", f"{sa_numerical:.4f}")
    
    with tab2:
        st.markdown("#### Interactive 3D Model")
        fig_3d, config_3d = plot_box_3d(l_analytical, w_analytical, h_analytical, open_top=open_top)
        st.plotly_chart(fig_3d, use_container_width=True, config=config_3d)

elif page == "📊 Shape Comparison":
    st.header("Container Shape Comparison")
    
    st.markdown("""
    Compare the optimal dimensions and surface areas of different container shapes
    with the same volume constraint.
    """)
    
    # Input
    volume = st.number_input(
        "Volume (cubic units)",
        min_value=1.0,
        max_value=10000.0,
        value=1000.0,
        step=100.0,
        key="comparison_volume"
    )
    
    # Compute comparisons
    results = compare_shapes(volume)
    
    # Display results in a table
    st.subheader("Comparison Table")
    
    import pandas as pd
    
    # Prepare data for table
    data = []
    for shape_name, shape_data in results.items():
        row = {'Shape': shape_name.replace('_', ' ').title()}
        row['Surface Area'] = f"{shape_data['surface_area']:.4f}"
        
        if 'radius' in shape_data:
            row['Dimension 1'] = f"r = {shape_data['radius']:.4f}"
            row['Dimension 2'] = f"h = {shape_data['height']:.4f}"
            row['Dimension 3'] = '-'
        else:
            row['Dimension 1'] = f"l = {shape_data['length']:.4f}"
            row['Dimension 2'] = f"w = {shape_data['width']:.4f}"
            row['Dimension 3'] = f"h = {shape_data['height']:.4f}"
        
        data.append(row)
    
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    
    # Visualizations
    st.subheader("Surface Area Comparison")
    fig_comparison = plot_shape_comparison(results, volume)
    st.plotly_chart(fig_comparison, use_container_width=True)
    
    # Find best shape
    best_shape = min(results.items(), key=lambda x: x[1]['surface_area'])
    st.success(f"🏆 Most efficient shape: **{best_shape[0].replace('_', ' ').title()}** "
               f"with surface area = {best_shape[1]['surface_area']:.4f}")
    
    # Key insights
    st.subheader("Key Insights")
    st.markdown("""
    - **Cylinders** generally use less material than rectangular boxes
    - **Closed containers** require more material than open-top versions
    - The **dimension ratios** follow predictable mathematical patterns
    - A **closed cylinder** with h = 2r is more efficient than a cube
    """)

elif page == "📚 Math Background":
    st.header("Mathematical Background")
    
    st.markdown("""
    ## Lagrange Multipliers Method
    
    The method of **Lagrange multipliers** is a strategy for finding the local maxima
    and minima of a function subject to equality constraints.
    
    ### General Formulation
    
    To optimize f(x, y) subject to constraint g(x, y) = c:
    
    1. Form the Lagrangian: L(x, y, λ) = f(x, y) - λ(g(x, y) - c)
    2. Take partial derivatives: ∇L = 0
    3. Solve the system of equations
    
    ### Example: Closed Cylinder
    
    **Objective:** Minimize surface area S = 2πr² + 2πrh
    
    **Constraint:** Volume V = πr²h = constant
    
    **Lagrangian:**
    """)
    
    st.latex(r"L(r, h, \lambda) = 2\pi r^2 + 2\pi rh - \lambda(\pi r^2 h - V)")
    
    st.markdown("**Partial Derivatives:**")
    
    st.latex(r"\frac{\partial L}{\partial r} = 4\pi r + 2\pi h - 2\lambda\pi rh = 0")
    st.latex(r"\frac{\partial L}{\partial h} = 2\pi r - \lambda\pi r^2 = 0")
    st.latex(r"\frac{\partial L}{\partial \lambda} = \pi r^2 h - V = 0")
    
    st.markdown("""
    **Solution:**
    
    From the second equation: λ = 2/r
    
    Substituting into the first equation and simplifying:
    """)
    
    st.latex(r"4\pi r + 2\pi h - 4\pi h = 0")
    st.latex(r"4\pi r = 2\pi h")
    st.latex(r"h = 2r")
    
    st.success("✅ Optimal cylinder has height equal to diameter!")
    
    st.markdown("""
    ### Why This Matters
    
    This result shows that for minimal material usage:
    - The optimal cylinder is not too tall and thin
    - It's not too short and wide
    - It has a specific geometric relationship: h = 2r
    
    ### Real-World Impact
    
    - **Soup cans** often approximate this ratio
    - **Industrial tanks** use these principles
    - **Packaging companies** save millions by optimizing dimensions
    - **Environmental benefit** from reduced material waste
    
    ### Further Reading
    
    - Multivariable Calculus textbooks
    - Optimization theory
    - Calculus of variations
    - Operations research
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("""
    ### About
    
    This project demonstrates the application of multivariable calculus
    to real-world optimization problems.
    
    **Technologies:**
    - Python
    - NumPy & SciPy
    - Plotly
    - Streamlit
    
    **Created by:**
    - JAPHET ACQUAH, OSEI
   
""")
