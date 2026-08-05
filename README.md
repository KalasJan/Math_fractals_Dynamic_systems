# Chaos Theory & Fractal Geometry Frameworks (Python)

A collection of computational scripts simulating non-linear dynamical systems, chaotic attractors, deterministic chaos, and recursive fractal structures.

## Key Features
- **Chaotic Attractors & Systems:** Numerical simulations of continuous and discrete chaotic systems, mapping phase space trajectories for Lorenz, Rössler, Hénon, Lozi, and Ikeda attractors.
- **Complex Dynamic Planes:** Visualizing structural convergence in the complex plane, focusing on high-resolution renderings of the Mandelbrot Set.
- **Deterministic & Recursive Fractals:** Algorithm architectures for infinite recursive shapes, covering Cantor sets, Koch curves/snowflakes, and the Sierpinski Triangle.
- **Pathological Functions:** Computational implementation of complex mathematical anomalies, specifically the non-differentiable Weierstrass function.

## Tech Stack
- **NumPy** – For matrix slicing, complex number math, and iterative coordinate updates in discrete dynamical equations.
- **Matplotlib** – For high-precision 2D/3D line charting, vector scattering, and pixel-density colormap renderings.

*Note: File names and inline comments are in Czech for internal logic documentation and reference.*

# Linear and Nonlinear Dynamical Systems: Phase Portraits

This repository contains a complete collection of Python scripts for simulating and visualizing **Phase Portraits of Linear Autonomous Systems** (classification of critical points based on eigenvalues) and a classic **Nonlinear Dynamical System (Mathematical Pendulum)**.

The scripts utilize `numpy` for efficient matrix operations and vectorization, and `matplotlib`'s `streamplot` and `quiver` engines to automatically generate high-quality phase trajectories with directional arrows.

---

## Repository Structure & Classification (All files DS_name.py)

The scripts are organized in a structured format mapping the complete taxonomy of 2D linear systems and specific boundary cases (where the determinant equals zero), along with a classic nonlinear oscillator.

### 1. Linear Systems (Isolated Critical Points)
*   **`Source_node_Uzel_zridlo.py`**: Node source (\(\lambda_1 \neq \lambda_2 > 0\)). Trajectories move directly outwards from the origin.
*   **`Sink_node_Uzel_vylevka.py`**: Node sink (\(\lambda_1 \neq \lambda_2 < 0\)). All trajectories asymptotically flow into the origin.
*   **`Saddle_point_Sedlo.py`**: Saddle point (\(\lambda_1 > 0, \lambda_2 < 0\)). Real eigenvalues with opposite signs creating hyperbolic flows.
*   **`Center_Stred.py`**: Center (\(\lambda_{1,2} = \pm i\beta\)). Purely imaginary eigenvalues generating stable, continuous periodic orbits.
*   **`Unstable_focus_Ohnisko_zridlo.py`**: Spiral source (\(\lambda_{1,2} = \alpha \pm i\beta, \alpha > 0\)). Trajectories spiral outwards.
*   **`Stable_focus_Ohnisko_vylevka.py`**: Spiral sink (\(\lambda_{1,2} = \alpha \pm i\beta, \alpha < 0\)). Trajectories spiral inwards to the sink.

### 2. Degenerate & Non-Isolated Systems (\(\det(J) = 0\))
*   **`Line_of_critical_points_Primka_kritickych_bodu.py`**: One zero eigenvalue (\(\lambda_1 = 0, \lambda_2 \neq 0\)). Generates an entire line of equilibrium points (\(y=0\)). Vectorized visualization implemented using `plt.quiver`.
*   **`Shear_flow_Smykove_proudeni.py`**: Double zero eigenvalues in a Jordan block (\(\lambda_1 = \lambda_2 = 0\)). Simulates parallel shear fluid flows moving in opposite directions above and below the critical line.
*   **`Plane_of_critical_points_Rovina_kritickych_bodu.py`**: Zero matrix system. Every point in the phase space is an equilibrium point. Outputs a static grid of stationary dots via `quiver`.

### 3. Nonlinear Systems
*   **`Nonlinear_pendulum_Matematicke_kyvadlo.py`**: Simulation of the classical nonlinear pendulum governed by \(\ddot{\alpha} + \sin(\alpha) = 0\). Vibrate trajectories map both stable orbits (centers), unstable upright positions (saddles), and the **separatrix** bounding the oscillating and circulating regimes. It includes a programmatic calculation of non-zero critical points using `np.linalg.solve(J, -u)`.

---

## Core Technical Implementations

### 1. Vectorized Phase Field Mapping
Instead of iterative `for` loops, the vector field is computed across a coordinate grid simultaneously using `np.meshgrid` and matrix multiplication:
```python
state = np.vstack([X.ravel(), Y.ravel()])
product = J @ state + u.reshape(-1, 1)
```

### 2. Automated Non-Zero Critical Point Solver
For non-homogeneous systems (\(J\vec{x} + \vec{u} = \vec{0}\)), the shift of the equilibrium point is solved programmatically using linear algebra before plotting:
```python
x_critical, y_critical = np.linalg.solve(J, -u)
```

---

## Requirements & Installation

To run these simulations, clone the repository and install the standard scientific Python stack:

```bash
git clone https://github.com
cd phase-portraits-ode
pip install numpy matplotlib scipy
```

Run any script directly using Python:
```bash
python saddle_point_sedlo.py
```

## License
This project is open-source and available under the MIT License.

