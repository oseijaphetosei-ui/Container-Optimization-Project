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

### Solution Using Gradient Method

#### Step 1: Find Gradients

∇S (gradient of surface area):
```
∇S = (∂S/∂r, ∂S/∂h) = (4πr + 2πh, 2πr)
```

∇g (gradient of constraint):
```
∇g = (∂g/∂r, ∂g/∂h) = (2πrh, πr²)
```

#### Step 2: Set ∇S = λ∇g

For r-component:
```
4πr + 2πh = λ(2πrh)  ...(1)
```

For h-component:
```
2πr = λ(πr²)  ...(2)
```

#### Step 3: Solve

From equation (2):
```
2πr = λπr²
λ = 2/r
```

Substitute into equation (1):
```
4πr + 2πh = (2/r)(2πrh)
4πr + 2πh = 4πh
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

### Solution Using Gradient Method

#### Step 1: Find Gradients

∇S (gradient of surface area):
```
∇S = (∂S/∂r, ∂S/∂h) = (2πr + 2πh, 2πr)
```

∇g (gradient of constraint):
```
∇g = (∂g/∂r, ∂g/∂h) = (2πrh, πr²)
```

#### Step 2: Set ∇S = λ∇g

For r-component:
```
2πr + 2πh = λ(2πrh)  ...(1)
```

For h-component:
```
2πr = λ(πr²)  ...(2)
```

#### Step 3: Solve

From equation (2):
```
2πr = λπr²
λ = 2/r
```

Substitute into equation (1):
```
2πr + 2πh = (2/r)(2πrh)
2πr + 2πh = 4πh
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

### Solution Using Gradient Method

#### Step 1: Find Gradients

∇S (gradient of surface area):
```
∇S = (∂S/∂l, ∂S/∂w, ∂S/∂h) = (w + 2h, l + 2h, 2l + 2w)
```

∇g (gradient of constraint):
```
∇g = (∂g/∂l, ∂g/∂w, ∂g/∂h) = (wh, lh, lw)
```

#### Step 2: Set ∇S = λ∇g

For l-component:
```
w + 2h = λ(wh)  ...(1)
```

For w-component:
```
l + 2h = λ(lh)  ...(2)
```

For h-component:
```
2l + 2w = λ(lw)  ...(3)
```

#### Step 3: Solve

Divide equation (1) by w:
```
1 + 2h/w = λh  ...(4)
```

Divide equation (2) by l:
```
1 + 2h/l = λh  ...(5)
```

From (4) and (5):
```
1 + 2h/w = 1 + 2h/l
2h/w = 2h/l
l = w
```

So the base is square!

Substitute l = w into equation (3):
```
2l + 2l = λl²
4l = λl²
λ = 4/l
```

Substitute λ = 4/l into equation (1) with w = l:
```
l + 2h = (4/l)(lh)
l + 2h = 4h
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

### Solution Using Gradient Method

#### Step 1: Find Gradients

∇S (gradient of surface area):
```
∇S = (∂S/∂l, ∂S/∂w, ∂S/∂h) = (2w + 2h, 2l + 2h, 2l + 2w)
```

∇g (gradient of constraint):
```
∇g = (∂g/∂l, ∂g/∂w, ∂g/∂h) = (wh, lh, lw)
```

#### Step 2: Set ∇S = λ∇g

For l-component:
```
2w + 2h = λ(wh)  ...(1)
```

For w-component:
```
2l + 2h = λ(lh)  ...(2)
```

For h-component:
```
2l + 2w = λ(lw)  ...(3)
```

#### Step 3: Solve

Divide equation (1) by wh:
```
2/h + 2/w = λ  ...(4)
```

Divide equation (2) by lh:
```
2/h + 2/l = λ  ...(5)
```

Divide equation (3) by lw:
```
2/w + 2/l = λ  ...(6)
```

From (4) and (5):
```
2/h + 2/w = 2/h + 2/l
2/w = 2/l
l = w
```

From (4) and (6) with l = w:
```
2/h + 2/w = 2/w + 2/w
2/h = 2/w
h = w
```

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


