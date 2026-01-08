# src/simulate_var.py

import numpy as np
import matplotlib.pyplot as plt


def bootstrap_var_estimate(sim_losses, alpha=0.01, B=500, rng=None):
    """
    Führt Bootstrapping durch, um SE und CI des VaR zu schätzen.
    """
    if rng is None:
        rng = np.random.default_rng()
    var_boot = np.empty(B)
    for b in range(B):
        resample = rng.choice(sim_losses, size=len(sim_losses), replace=True)
        var_boot[b] = np.percentile(resample, alpha * 100)
    return var_boot


def simulate_var(returns, investment=1000, alpha=0.01, N=100_000, B=500, save_plot=False, plot_path="../figures/simulated_var_histogram.png"):
    """
    Schätzt Value-at-Risk (VaR) per Monte Carlo mit Bootstrap-CI.

    Parameter
    ---------
    returns : np.ndarray
        Log-Renditen des Portfolios.
    investment : float
        Investitionssumme in Euro.
    alpha : float
        VaR-Konfidenzniveau (z. B. 0.01 für 99%).
    N : int
        Anzahl der Monte-Carlo-Stichproben.
    B : int
        Bootstrap-Replikationen.
    save_plot : bool
        Falls True, speichert Plot als PNG.
    plot_path : str
        Pfad für das zu speichernde Histogramm.

    Returns
    -------
    VaR : float
        Geschätzter Value-at-Risk.
    se : float
        Standardfehler des VaR.
    ci : Tuple[float, float]
        95%-Konfidenzintervall für den VaR.
    """
    rng = np.random.default_rng(42)

    # Monte Carlo: Verluste simulieren
    sim_returns = rng.choice(returns, size=N, replace=True)
    sim_losses = -investment * sim_returns
    VaR = np.percentile(sim_losses, alpha * 100)

    # Bootstrap für SE & CI
    var_boot = bootstrap_var_estimate(sim_losses, alpha, B, rng)

    se = var_boot.std(ddof=1)
    ci_lower = np.percentile(var_boot, 2.5)
    ci_upper = np.percentile(var_boot, 97.5)

    # Plot speichern
    if save_plot:
        plt.hist(sim_losses, bins=60, color="orange", edgecolor="k")
        plt.axvline(VaR, color="red", linestyle="--", label=f"{int((1-alpha)*100)}%-VaR ≈ {VaR:.2f} €")
        plt.title("Simulierte Verluste (Monte Carlo)")
        plt.xlabel("Verlust in €")
        plt.ylabel("Häufigkeit")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(plot_path)

    return VaR, se, (ci_lower, ci_upper)