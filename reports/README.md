# Value-at-Risk Analyse eines Krypto-Portfolios

*(Depot: 50 % Bitcoin (BTC), 40 % Ethereum (ETH), 10 % Solana (SOL))*

## 1. Einleitung
Kryptowährungen wie Bitcoin, Ethereum und Solana sind bekannt für ihre starke Volatilität. Diese Analyse untersucht das Risiko eines gemischten Krypto-Portfolios mithilfe des Value-at-Risk (VaR) Ansatzes.

## 2. Daten und Methodik
- **Datenquelle**: Yahoo Finance (`yfinance`)
- **Zeitraum**: Letzte 12 Monate
- **Log-Renditen**: `log(P_t / P_t-1)`
- **Gewichtung**:
  - 50 % BTC
  - 40 % ETH
  - 10 % SOL
- **Simulation**:
  - 100.000 Ziehungen
  - Bootstrap mit 500 Iterationen
  - 1-Tages-VaR bei 99 %

## 3. Ergebnisse

- 1-Tages-VaR (99 %): z. B. **–120.43 €**
- Standardfehler: ±2.15 €
- Konfidenzintervall (95 %): [–123.8 €, –117.0 €]

![Histogramm](simulated_var_histogram.png)

## 4. Interpretation
- Das 99 %-VaR bedeutet: Mit 99 %-Wahrscheinlichkeit wird der Tagesverlust des Portfolios **120 € nicht überschreiten**.
- Modell basiert auf historischen Renditen → keine Garantie für zukünftige Verluste.
- Kein Schutz gegen Extremereignisse.

## 5. Fazit
- VaR ist nützlich zur quantitativen Risikobewertung.
- Dieses einfache Modell zeigt bereits grundlegende Risikoeinschätzung.
- Erweiterungsideen:
  - Mehrtägige Betrachtung
  - Berücksichtigung von Korrelationen
  - Stressszenarien

## 6. Quellen / Anhänge
- Code: `notebooks/finale_analyse.ipynb`
- Simulation: `src/simulate_var.py`
- Plot: `reports/simulated_var_histogram.png`
- Packages: `requirements.txt`