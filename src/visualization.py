"""Visualization utilities for container optimization.

This module provides functions to create 3D visualizations of containers
and optimization landscapes using matplotlib and plotly.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go
from typing import Tuple, Optional


def plot_cylinder_3d(radius: float, height: float, closed: bool = True, 
                     title: str = "Optimized Cylinder") -> go.Figure:
    """
    Create an interactive 3D visualization of a cylinder.
    
    Args:
        radius: Cylinder radius
        height: Cylinder height
        closed: Whether cylinder has top and bottom caps
        title: Plot title
        
    Returns:
        Plotly figure object
    """
    # Generate cylinder surface
    theta = np.linspace(0, 2*np.pi, 100)
    z = np.linspace(0, height, 50)
    theta_grid, z_grid = np.meshgrid(theta, z)
    
    x_grid = radius * np.cos(theta_grid)
    y_grid = radius * np.sin(theta_grid)
    
    # Create figure
    fig = go.Figure()
    
    # Add cylinder surface
    fig.add_trace(go.Surface(
        x=x_grid, y=y_grid, z=z_grid,
        colorscale='Blues',
        showscale=False,
        name='Cylinder Surface',
        opacity=0.8
    ))
    
    # Add top and bottom caps if closed
    if closed:
        r = np.linspace(0, radius, 20)
        theta_cap = np.linspace(0, 2*np.pi, 100)
        r_grid, theta_cap_grid = np.meshgrid(r, theta_cap)
        
        x_cap = r_grid * np.cos(theta_cap_grid)
        y_cap = r_grid * np.sin(theta_cap_grid)
        
        # Bottom cap
        fig.add_trace(go.Surface(
            x=x_cap, y=y_cap, z=np.zeros_like(x_cap),
            colorscale='Blues',
            showscale=False,
            name='Bottom',
            opacity=0.8
        ))
        
        # Top cap
        fig.add_trace(go.Surface(
            x=x_cap, y=y_cap, z=np.ones_like(x_cap) * height,
            colorscale='Blues',
            showscale=False,
            name='Top',
            opacity=0.8
        ))
    
    # Update layout
    fig.update_layout(
        title=title,
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z (Height)',
            aspectmode='data',
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=1.5)
            )
        ),
        width=700,
        height=700
    )
    
    # Hide mode bar to remove all buttons
    config = {
        'displayModeBar': False
    }
    
    return fig, config


def plot_box_3d(length: float, width: float, height: float, 
                open_top: bool = True, title: str = "Optimized Box") -> go.Figure:
    """
    Create an interactive 3D visualization of a rectangular box.
    
    Args:
        length: Box length (x-direction)
        width: Box width (y-direction)
        height: Box height (z-direction)
        open_top: Whether box has open top
        title: Plot title
        
    Returns:
        Plotly figure object
    """
    # Define vertices
    vertices = np.array([
        [0, 0, 0], [length, 0, 0], [length, width, 0], [0, width, 0],  # bottom
        [0, 0, height], [length, 0, height], [length, width, height], [0, width, height]  # top
    ])
    
    # Define faces
    faces = [
        [0, 1, 2, 3],  # bottom
        [0, 1, 5, 4],  # front
        [1, 2, 6, 5],  # right
        [2, 3, 7, 6],  # back
        [3, 0, 4, 7],  # left
    ]
    
    if not open_top:
        faces.append([4, 5, 6, 7])  # top
    
    fig = go.Figure()
    
    # Add each face
    for i, face in enumerate(faces):
        face_vertices = vertices[face]
        x = list(face_vertices[:, 0]) + [face_vertices[0, 0]]
        y = list(face_vertices[:, 1]) + [face_vertices[0, 1]]
        z = list(face_vertices[:, 2]) + [face_vertices[0, 2]]
        
        fig.add_trace(go.Mesh3d(
            x=face_vertices[:, 0],
            y=face_vertices[:, 1],
            z=face_vertices[:, 2],
            opacity=0.7,
            color='lightblue',
            flatshading=True
        ))
        
        # Add edges
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='lines',
            line=dict(color='darkblue', width=4),
            showlegend=False
        ))
    
    # Update layout
    fig.update_layout(
        title=title,
        scene=dict(
            xaxis_title='Length',
            yaxis_title='Width',
            zaxis_title='Height',
            aspectmode='data',
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=1.5)
            )
        ),
        width=700,
        height=700
    )
    
    # Hide mode bar to remove all buttons
    config = {
        'displayModeBar': False
    }
    
    return fig, config


def plot_optimization_landscape_cylinder(volume: float, closed: bool = True,
                                         optimal_r: Optional[float] = None,
                                         optimal_h: Optional[float] = None) -> go.Figure:
    """
    Plot the optimization landscape showing how surface area varies with dimensions.
    
    Args:
        volume: Fixed volume constraint
        closed: Whether cylinder is closed
        optimal_r: Optimal radius to mark on plot
        optimal_h: Optimal height to mark on plot
        
    Returns:
        Plotly figure object
    """
    # Create grid of radius values
    r_range = np.linspace(0.1, 3 * (volume / np.pi) ** (1/3), 100)
    h_values = volume / (np.pi * r_range**2)
    
    # Calculate surface areas
    if closed:
        surface_areas = 2 * np.pi * r_range**2 + 2 * np.pi * r_range * h_values
    else:
        surface_areas = np.pi * r_range**2 + 2 * np.pi * r_range * h_values
    
    # Create figure
    fig = go.Figure()
    
    # Add surface area curve
    fig.add_trace(go.Scatter(
        x=r_range,
        y=surface_areas,
        mode='lines',
        name='Surface Area',
        line=dict(color='blue', width=2)
    ))
    
    # Mark optimal point
    if optimal_r is not None:
        if closed:
            optimal_sa = 2 * np.pi * optimal_r**2 + 2 * np.pi * optimal_r * optimal_h
        else:
            optimal_sa = np.pi * optimal_r**2 + 2 * np.pi * optimal_r * optimal_h
        
        fig.add_trace(go.Scatter(
            x=[optimal_r],
            y=[optimal_sa],
            mode='markers',
            name='Optimal Point',
            marker=dict(color='red', size=12, symbol='star')
        ))
    
    # Update layout
    fig.update_layout(
        title='Optimization Landscape: Surface Area vs Radius',
        xaxis_title='Radius (r)',
        yaxis_title='Surface Area',
        hovermode='closest',
        showlegend=True
    )
    
    return fig


def plot_optimization_landscape_box(volume: float, open_top: bool = True,
                                   optimal_l: Optional[float] = None,
                                   optimal_h: Optional[float] = None) -> go.Figure:
    """
    Plot the optimization landscape for a square-base box.
    
    Args:
        volume: Fixed volume constraint
        open_top: Whether box has open top
        optimal_l: Optimal base side length to mark on plot
        optimal_h: Optimal height to mark on plot
        
    Returns:
        Plotly figure object
    """
    # Create grid of base side length values (assuming square base l = w)
    l_range = np.linspace(0.1, 3 * volume ** (1/3), 100)
    h_values = volume / (l_range**2)
    
    # Calculate surface areas
    if open_top:
        surface_areas = l_range**2 + 4 * l_range * h_values
    else:
        surface_areas = 2 * l_range**2 + 4 * l_range * h_values
    
    # Create figure
    fig = go.Figure()
    
    # Add surface area curve
    fig.add_trace(go.Scatter(
        x=l_range,
        y=surface_areas,
        mode='lines',
        name='Surface Area',
        line=dict(color='green', width=2)
    ))
    
    # Mark optimal point
    if optimal_l is not None:
        if open_top:
            optimal_sa = optimal_l**2 + 4 * optimal_l * optimal_h
        else:
            optimal_sa = 2 * optimal_l**2 + 4 * optimal_l * optimal_h
        
        fig.add_trace(go.Scatter(
            x=[optimal_l],
            y=[optimal_sa],
            mode='markers',
            name='Optimal Point',
            marker=dict(color='red', size=12, symbol='star')
        ))
    
    # Update layout
    fig.update_layout(
        title='Optimization Landscape: Surface Area vs Base Side Length',
        xaxis_title='Base Side Length (l = w)',
        yaxis_title='Surface Area',
        hovermode='closest',
        showlegend=True
    )
    
    return fig


def plot_shape_comparison(results: dict, volume: float) -> go.Figure:
    """
    Create a bar chart comparing surface areas of different container shapes.
    
    Args:
        results: Dictionary from compare_shapes function
        volume: Volume constraint
        
    Returns:
        Plotly figure object
    """
    shapes = list(results.keys())
    surface_areas = [results[shape]['surface_area'] for shape in shapes]
    
    # Format shape names for display
    shape_labels = [shape.replace('_', ' ').title() for shape in shapes]
    
    fig = go.Figure(data=[
        go.Bar(
            x=shape_labels,
            y=surface_areas,
            marker_color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],
            text=[f'{sa:.2f}' for sa in surface_areas],
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title=f'Surface Area Comparison (Volume = {volume:.2f})',
        xaxis_title='Container Shape',
        yaxis_title='Surface Area',
        showlegend=False,
        height=500
    )
    
    return fig


def plot_dimensions_comparison(results: dict) -> go.Figure:
    """
    Create a grouped bar chart comparing dimensions of different shapes.
    
    Args:
        results: Dictionary from compare_shapes function
        
    Returns:
        Plotly figure object
    """
    shapes = list(results.keys())
    shape_labels = [shape.replace('_', ' ').title() for shape in shapes]
    
    fig = go.Figure()
    
    # Add bars for each dimension type
    for i, shape in enumerate(shapes):
        data = results[shape]
        dims = []
        labels = []
        
        if 'radius' in data:
            dims.extend([data['radius'], data['height']])
            labels.extend(['Radius', 'Height'])
        else:
            dims.extend([data['length'], data['width'], data['height']])
            labels.extend(['Length', 'Width', 'Height'])
        
        fig.add_trace(go.Bar(
            name=shape_labels[i],
            x=labels,
            y=dims,
        ))
    
    fig.update_layout(
        title='Dimensions Comparison',
        xaxis_title='Dimension',
        yaxis_title='Value',
        barmode='group',
        height=500
    )
    
    return fig