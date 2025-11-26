Container Design Optimization

> A multivariable calculus project exploring optimal container dimensions using Lagrange multipliers

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Project Overview

This project uses **multivariable calculus** to solve real-world optimization problems: finding container dimensions that minimize surface area for a given volume. 

**Key Question:** What's the most efficient way to package a product?

### Mathematical Approach
- **Lagrange Multipliers** for constrained optimization
- **Partial Derivatives** to find critical points


## 🚀 Features

- [ ] Optimize rectangular boxes (open top)
- [ ] Optimize cylinders (closed and open)
- [ ] Interactive web interface with Streamlit
- [ ] 3D visualizations (rotate and zoom)
- [ ] Shape comparison analysis


## 📚 Calculus Concepts

This project demonstrates:

1. **Lagrange Multipliers** - Constrained optimization technique
2. **Partial Derivatives** - Finding critical points of multivariable functions
3. **3D Surface Visualization** - Graphing and analyzing optimization landscapes
4. **Real-World Applications** - Packaging design, manufacturing, cost minimization

## 🛠️ Tech Stack

- **Python 3.8+** - 
- **NumPy and SciPy** - Numerical computations and optimizations
- **Matplotlib** - 2D plotting
- **Plotly** - Interactive 3D graphics
- **Streamlit** - Web interface


## 📐 Mathematical Background

### Problem: Minimize Surface Area

**For a Cylinder (closed):**

- **Objective:** Minimize S = 2πr² + 2πrh
- **Constraint:** V = πr²h = constant

**Using Lagrange Multipliers:**

Set up the Lagrangian:
```
L(r, h, λ) = 2πr² + 2πrh - λ(πr²h - V)
```

Take partial derivatives and solve:
```
∂L/∂r = 4πr + 2πh - 2λπrh = 0
∂L/∂h = 2πr - λπr² = 0
∂L/∂λ = πr²h - V = 0
```

**Result:** Optimal cylinder has h = 2r (height equals diameter)

[See full derivations in `/docs/derivations.md`]



##  Contributing

Contributions are welcome! This is a learning project, so feel free to:

- Fix bugs
- Add new container shapes (cone, sphere, etc.)
- Improve visualizations
- Add features
- Improve documentation

### How to Contribute

1. **Fork** this repository
2. **Create a branch** for your feature
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```
4. **Push to your fork**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**



## 📋 Development Roadmap

### Phase 1: Core Math ✏️
- [ ] Derive formulas using Lagrange multipliers
- [ ] Document all mathematical proofs
- [ ] Create test cases

### Phase 2: Implementation 💻
- [ ] Implement cylinder optimization
- [ ] Implement rectangular box optimization
- [ ] Add numerical verification
- [ ] Write unit tests

### Phase 3: Visualization 📊
- [ ] Basic 2D plots (matplotlib)
- [ ] 3D container models (Plotly)
- [ ] Optimization landscape plots
- [ ] Shape comparison charts

### Phase 4: Web Interface 🌐
- [ ] Set up Streamlit app
- [ ] Add interactive sliders
- [ ] Display results and visualizations
- [ ] Add mathematical derivation display

### Phase 5: Advanced Features(coming soon) 🚀
- [ ] Add more shapes (cone, sphere)
- [ ] Material cost optimization
- [ ] Gradient descent animation
- [ ] Export results feature


## 📖 Documentation

- [Mathematical Derivations](docs/derivations.md) - Full calculus proofs
- [API Reference](docs/api.md) - Function documentation
- [Examples](docs/examples.md) - Usage examples

## 💡 Use Cases

- **Packaging Design** - Minimize material costs
- **Manufacturing** - Optimize production efficiency
- **Education** - Learn multivariable calculus concepts
- **Sustainability** - Reduce material waste


## 🎓 Educational Value

This project is ideal for:
- Calculus 3 / Multivariable Calculus students
- Learning about optimization techniques
- Understanding real-world applications of calculus
- Practicing Python and data visualization

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **OSEI JAPHET ACQUAH** - Initial work and mathematical derivations


## 📬 Contact

- GitHub: oseijaphetosei-ui(https://github.com/oseijaphetosei-ui)
- Email:jotk2024@mymail.pomona.edu

## ⭐ Show Your Support

Give a ⭐️ if this project helped you learn about optimization!

---

### Quick Links
- [Issues](../../issues) - Report bugs or suggest features
- [Projects](../../projects) - Track development progress
- [Wiki](../../wiki) - Additional documentation
