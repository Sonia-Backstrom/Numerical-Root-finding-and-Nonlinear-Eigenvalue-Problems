import numpy as np
import scipy.sparse.linalg as spla
from scipy.io import loadmat
from scipy.sparse import csc_matrix


class g_nlevp:
    """
    Evaluates the scalarized NLEVP response function g(z) = v^T F(z)^{-1} w
    for the Gun problem loaded from disk.
    """

    def __init__(self):
        # Load matrices from disk
        data = loadmat('gun.mat')
        self.data_mat = {key: csc_matrix(data[key]) for key in ["K", "M", "W1", "W2"]}
        self.alpha2s = [0.0, 11854.2882308]

        n = self.data_mat["K"].shape[0]

        # Generate reproducible random complex sketching vectors
        rng = np.random.default_rng(42)
        self.v = rng.standard_normal(n) + 1j * rng.standard_normal(n)
        self.w = rng.standard_normal(n) + 1j * rng.standard_normal(n)

    def F(self, z):
        """Builds the matrix operator F(z)."""
        return (
            self.data_mat["K"] 
            - z * self.data_mat["M"]
            + 1j * (
                (z - self.alpha2s[0])**0.5 * self.data_mat["W1"]
              + (z - self.alpha2s[1])**0.5 * self.data_mat["W2"]
            )
        )

    def __call__(self, z):
        """Evaluates g(z) = v^T F(z)^{-1} w."""
        F_z = self.F(z)
        # Solve F(z) x = w, then evaluate v^T x
        sol = spla.spsolve(F_z, self.w)
        return np.dot(self.v, sol)
