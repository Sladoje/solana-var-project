# src/simulate_var.py

import numpy as np
import matplotlib.pyplot as plt

def simulate_var(returns, investment=1000, alpha=0.01, N=100_000, B=500, save_plot=False):
    rng = np.random.default_rng(42)

    # Monte Carlo: Verluste simulieren
    sim_returns = rng.choice(returns, size=N, replace=True)
    sim_losses = -investment * sim_returns
    VaR = np.percentile(sim_losses, alpha * 100)

    # Bootstrap für SE & CI
    var_boot = np.empty(B)
    for b in range(B):
        resample = rng.choice(sim_losses, size=N, replace=True)
        var_boot[b] = np.percentile(resample, alpha * 100)

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
        plt.savefig("reports/simulated_var_histogram.png")

    return VaR, se, (ci_lower, ci_upper)