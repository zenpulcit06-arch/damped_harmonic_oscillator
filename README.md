# Numerical Study of a Damped Harmonic Oscillator

## Abstract

This project presents a numerical and analytical study of a one-dimensional damped harmonic oscillator. The system is simulated using a custom C-based numerical integrator, and the resulting time-series data are analysed using Python. Physical parameters such as the damping constant and angular frequency are extracted directly from the simulated data and validated against theoretical predictions. Particular emphasis is placed on regime classification (underdamped, critically damped, overdamped) and on the robustness of analysis methods.

---

## Motivation

Damped oscillatory systems appear throughout physics, from mechanical systems to electrical circuits and detector instrumentation. While the equations of motion are analytically solvable, numerical simulations are essential for understanding real-world effects such as dissipation, numerical stability, and data-driven parameter extraction. The goal of this project is not only to simulate motion, but to build a physically consistent analysis pipeline that mirrors experimental workflows.

---

## Physical Model

The system considered is a mass–spring oscillator with linear damping, governed by

[ m\ddot{x} + b\dot{x} + kx = 0 ]

where:

* (m) is the mass
* (k) is the spring constant
* (b) is the damping coefficient

The total mechanical energy is

[ E(t) = \frac{1}{2}m v^2 + \frac{1}{2}k x^2 ]

For an underdamped system, the energy decays exponentially:

[ E(t) = E_0 e^{-2\gamma t} ]

with (\gamma = b / (2m)).

---

## Numerical Simulation (C)

The equations of motion are integrated numerically in C using a time-stepping scheme. The simulation:

* accepts physical parameters and initial conditions as input
* evolves position and velocity in time
* computes acceleration and total energy at each step
* writes all quantities to a CSV file for post-processing

The C code is designed to be modular and solver-agnostic, allowing future extensions such as alternative integration schemes or external data sources.

---

## Data Analysis (Python)

The generated data are analysed using Python (NumPy, Pandas, Matplotlib). The analysis pipeline includes:

### 1. Time-Domain Diagnostics

* Position vs time
* Velocity vs time
* Energy vs time

These plots provide immediate qualitative insight into oscillatory behaviour and damping.

### 2. Phase-Space Analysis

A phase-space plot (velocity vs position) is used to visualise the system dynamics. In the underdamped regime, this appears as an inward spiral, confirming dissipative oscillatory motion.

### 3. Damping Extraction via Energy Decay

Rather than relying on peak detection in position data, the damping constant is extracted from the slope of (\ln E(t)) versus time. This method:

* uses the full dataset
* is robust to numerical noise
* remains valid even when extrema are poorly resolved

### 4. Frequency Analysis and Validation

The angular frequency extracted from data is compared with the theoretical prediction

[ \omega = \sqrt{\frac{k}{m} - \left(\frac{b}{2m}\right)^2} ]

This provides a consistency check between simulation, analysis, and theory.

---

## Regime Classification

The dynamical regime of the oscillator is classified by comparing

[ \left(\frac{b}{2m}\right)^2 \quad \text{and} \quad \frac{k}{m} ]

* Underdamped: oscillatory motion with exponential decay
* Critically damped: fastest non-oscillatory return to equilibrium
* Overdamped: slow, non-oscillatory relaxation

This classification ensures that oscillation-based analyses are only applied when physically meaningful.

---

## Key Outcomes

* Successful numerical simulation of damped oscillatory motion
* Robust extraction of damping parameters from energy decay
* Quantitative agreement between analytical theory and numerical results
* Clear identification of the dynamical regime

---

## Extensions and Future Work

Possible extensions include:

* timestep convergence and numerical stability studies
* comparison of integration schemes (Euler vs Verlet)
* driven or forced oscillators
* analysis of experimental data using the same pipeline

---

## Tools and Technologies

* **C**: numerical simulation and data generation
* **Python**: data analysis and visualisation
* **Libraries**: NumPy, Pandas, Matplotlib

---

## Summary

This project demonstrates a complete physics-informed workflow: from equations of motion, through numerical simulation, to data-driven parameter extraction and theoretical validation. The emphasis on robustness, regime awareness, and physical interpretation reflects methodologies commonly used in experimental and computational physics research.

