# Mathematical Derivations

Complete mathematical proofs for container optimization using Lagrange multipliers.

## Table of Contents
- [Closed Cylinder](#closed-cylinder)
- [Open Cylinder](#open-cylinder)
- [Open Top Box](#open-top-box)
- [Closed Box (Cube)](#closed-box-cube)

---

## Closed Cylinder

### Problem Statement
Find the dimensions of a closed cylinder that minimize surface area for a given volume V.

### Variables
- r: radius of cylinder base
- h: height of cylinder
- V: fixed volume (constant)

### Objective Function
Minimize surface area:
```
S(r, h) = 2πr² + 2πrh
```
where:
- 2πr² represents the top and bottom circles
- 2πrh represents the lateral surface

### Constraint
Volume must equal V:
```
g(r, h) = πr²h - V = 0
```

### Lagrange Multiplier Method

#### Step 1: Form the Lagrangian
```
L(r, h, λ) = 2πr² + 2πrh - λ(πr²h - V)
```

#### Step 2: Compute Partial Derivatives

∂L/∂r:
```
∂L/∂r = 4πr + 2πh - 2λπrh = 0  ...(1)
```

∂L/∂h:
```
∂L/∂h = 2πr - λπr² = 0  ...(2)
```

∂L/∂λ:
```
∂L/∂λ = πr²h - V = 0  ...(3)
```

#### Step 3: Solve the System

From equation (2):
```
2πr - λπr² = 0
2πr = λπr²
λ = 2/r  ...(4)
```

Substitute (4) into equation (1):
```
4πr + 2πh - 2(2/r)πrh = 0
4πr + 2πh - 4πh = 0
4πr = 2πh
h = 2r
```

### Result
**Optimal relationship: h = 2r**

The height equals the diameter! This means the optimal cylinder is neither too tall and thin, nor too short and wide.

### Finding Specific Dimensions

Substitute h = 2r into the volume constraint:
```
V = πr²h = πr²(2r) = 2πr³

r³ = V/(2π)
r = (V/(2π))^(1/3)

h = 2r = 2(V/(2π))^(1/3)
```

### Verification (Second Derivative Test)

To confirm this is a minimum, we can check the bordered Hessian or simply note that:
- As r → 0, h → ∞ and S → ∞
- As r → ∞, h → 0 and S → ∞
- There exists a unique critical point, which must be a minimum

---

## Open Cylinder

### Problem Statement
Find the dimensions of an open cylinder (no top) that minimize surface area for a given volume V.

### Objective Function
Minimize surface area:
```
S(r, h) = πr² + 2πrh
```
where:
- πr² represents the bottom circle only
- 2πrh represents the lateral surface

### Constraint
```
g(r, h) = πr²h - V = 0
```

### Lagrange Multiplier Method

#### Step 1: Form the Lagrangian
```
L(r, h, λ) = πr² + 2πrh - λ(πr²h - V)
```

#### Step 2: Compute Partial Derivatives

∂L/∂r:
```
∂L/∂r = 2πr + 2πh - 2λπrh = 0  ...(1)
```

∂L/∂h:
```
∂L/∂h = 2πr - λπr² = 0  ...(2)
```

∂L/∂λ:
```
∂L/∂λ = πr²h - V = 0  ...(3)
```

#### Step 3: Solve the System

From equation (2):
```
2πr = λπr²
λ = 2/r  ...(4)
```

Substitute (4) into equation (1):
```
2πr + 2πh - 2(2/r)πrh = 0
2πr + 2πh - 4πh = 0
2πr = 2πh
h = r
```

### Result
**Optimal relationship: h = r**

For an open cylinder, the height equals the radius!

### Finding Specific Dimensions

Substitute h = r into the volume constraint:
```
V = πr²h = πr²(r) = πr³

r³ = V/π
r = (V/π)^(1/3)

h = r = (V/π)^(1/3)
```

---

## Open Top Box

### Problem Statement
Find the dimensions of an open-top rectangular box that minimize surface area for a given volume V.

### Variables
- l: length
- w: width  
- h: height
- V: fixed volume (constant)

### Objective Function
Minimize surface area:
```
S(l, w, h) = lw + 2lh + 2wh
```
where:
- lw is the base
- 2lh and 2wh are the four sides

### Constraint
```
g(l, w, h) = lwh - V = 0
```

### Lagrange Multiplier Method

#### Step 1: Form the Lagrangian
```
L(l, w, h, λ) = lw + 2lh + 2wh - λ(lwh - V)
```

#### Step 2: Compute Partial Derivatives

∂L/∂l:
```
∂L/∂l = w + 2h - λwh = 0  ...(1)
```

∂L/∂w:
```
∂L/∂w = l + 2h - λlh = 0  ...(2)
```

∂L/∂h:
```
∂L/∂h = 2l + 2w - λlw = 0  ...(3)
```

∂L/∂λ:
```
∂L/∂λ = lwh - V = 0  ...(4)
```

#### Step 3: Solve the System

From equation (1): w + 2h = λwh  ...(5)
From equation (2): l + 2h = λlh  ...(6)

Dividing (5) by w: 1 + 2h/w = λh  ...(7)
Dividing (6) by l: 1 + 2h/l = λh  ...(8)

From (7) and (8):
```
1 + 2h/w = 1 + 2h/l
2h/w = 2h/l
l = w
```

So the base is square!

From equation (3):
```
2l + 2w - λlw = 0
```

Since l = w:
```
2l + 2l - λl² = 0
4l = λl²
λ = 4/l  ...(9)
```

Substitute (9) into equation (1) with w = l:
```
l + 2h - (4/l)lh = 0
l + 2h - 4h = 0
l = 2h
```

### Result
**Optimal relationships: l = w = 2h**

The base is square, and each side is twice the height!

### Finding Specific Dimensions

Substitute l = w = 2h into the volume constraint:
```
V = lwh = (2h)(2h)(h) = 4h³

h³ = V/4
h = (V/4)^(1/3)

l = w = 2h = 2(V/4)^(1/3)
```

---

## Closed Box (Cube)

### Problem Statement
Find the dimensions of a closed rectangular box that minimize surface area for a given volume V.

### Objective Function
Minimize surface area:
```
S(l, w, h) = 2lw + 2lh + 2wh
```

### Constraint
```
g(l, w, h) = lwh - V = 0
```

### Lagrange Multiplier Method

#### Step 1: Form the Lagrangian
```
L(l, w, h, λ) = 2lw + 2lh + 2wh - λ(lwh - V)
```

#### Step 2: Compute Partial Derivatives

∂L/∂l:
```
∂L/∂l = 2w + 2h - λwh = 0  ...(1)
```

∂L/∂w:
```
∂L/∂w = 2l + 2h - λlh = 0  ...(2)
```

∂L/∂h:
```
∂L/∂h = 2l + 2w - λlw = 0  ...(3)
```

∂L/∂λ:
```
∂L/∂λ = lwh - V = 0  ...(4)
```

#### Step 3: Solve the System

From equation (1): 2w + 2h = λwh  ...(5)
From equation (2): 2l + 2h = λlh  ...(6)
From equation (3): 2l + 2w = λlw  ...(7)

Dividing (5) by 2h: w/h + 1 = λw/2  ...(8)
Dividing (6) by 2h: l/h + 1 = λl/2  ...(9)

From (8) and (9), we can show that l = w.

Similarly, from (7) and comparing with (5) and (6), we can show that l = h and w = h.

Therefore: **l = w = h**

### Result
**Optimal shape: CUBE (l = w = h)**

The optimal closed box is a cube!

### Finding Specific Dimensions

Substitute l = w = h into the volume constraint:
```
V = lwh = h³

h = V^(1/3)
l = w = h = V^(1/3)
```

---

## Summary of Results

| Container Type | Optimal Relationship | Physical Meaning |
|---------------|---------------------|------------------|
| Closed Cylinder | h = 2r | Height equals diameter |
| Open Cylinder | h = r | Height equals radius |
| Open Top Box | l = w = 2h | Square base, sides twice height |
| Closed Box | l = w = h | Perfect cube |

## Key Insights

1. **Symmetry is Optimal**: In all cases, the optimal shapes exhibit symmetry
2. **Closed vs Open**: Removing a surface (top) changes the optimal proportions
3. **Mathematical Elegance**: The ratios (2:1, 1:1) are simple and elegant
4. **Practical Applications**: These results guide real-world packaging design

## Further Explorations

- What if we have different material costs for different surfaces?
- What about containers with minimum volume but fixed surface area?
- How do these results extend to other shapes (spheres, cones, etc.)?
- What if we add additional constraints (maximum height, minimum base area, etc.)?