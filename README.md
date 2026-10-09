# Numerical-Root-finding-and-Nonlinear-Eigenvalue-Problems

**Course:** DA7067 – Computational Mathematics  
**University:** Stockholm University  
**Date:** October 2026

## Project Overview

This project investigates numerical methods for finding roots of complex-valued functions and solving nonlinear eigenvalue problems.

## Task 1: Numerical Root-Finding

The Delves–Lyness/Beyn–Hankel (DL/BH) method is used to compute the roots.

### Methodology

- Apply the Cauchy Argument Principle to count the roots.
- Evaluate contour integrals using the periodic trapezoidal rule.
- Compute moments of the roots.
- Construct Hankel matrices.
- Solve a generalized eigenvalue problem to approximate the roots.
- Refine the roots using Newton's method.
- Validate the results using residuals.

### Results

Four roots were identified inside the unit disk. Increasing the number of quadrature points demonstrated convergence of the numerical root count to four.

## Task 2: Nonlinear Eigenvalue Problems


The AAA algorithm constructs a rational approximation of \(g(z)\), whose poles are considered candidate eigenvalues.

### Methodology

- Load the supplied sample data.
- Construct a rational approximation using the AAA algorithm.
- Extract the poles of the rational approximation.
- Identify poles inside the prescribed region \(K\).
- Validate candidate eigenvalues using residuals.
- Compare AAA and DL/BH in terms of computational cost, accuracy, and theoretical advantages.

### Results

- **Samples provided:** 1,111
- **AAA support points:** 41
- **Total poles found:** 40
- **Poles inside \(K\):** 19
- **Validation:** Residuals were used to assess the candidate eigenvalues.

## Methods and Technologies

- Python
- NumPy
- SciPy
- Jupyter Notebook
- Complex contour integration
- Periodic trapezoidal quadrature
- Hankel matrices and generalized eigenvalue problems
- Newton's method
- AAA rational approximation
- Sparse matrix computations
- Residual-based validation

## Repository Structure

```text
.
├── Numerical_Root_finding.ipynb
├── Main_ONE.pdf
├── g_eval.csv
├── g_nlevp.py
└── gun.mat

```






