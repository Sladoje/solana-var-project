# Monte-Carlo Value-at-Risk Analyse eines Krypto-Portfolios

Dieses Projekt implementiert eine Monte-Carlo-Simulation zur Berechnung
des **Value-at-Risk (VaR)** eines Krypto-Portfolios.
Das README dient dazu, den **Code, die Projektstruktur und die
Funktionsweise der Simulation** zu erklären.

---

## Projektidee und Fragestellung

Ziel des Projekts ist die Beantwortung folgender Frage:

**Welcher maximale Tagesverlust ist für ein Krypto-Portfolio mit einer
gegebenen Wahrscheinlichkeit zu erwarten?**

Der Fokus liegt auf der praktischen Umsetzung einer Monte-Carlo-Simulation
in Python und nicht auf einer theoretischen Abhandlung.

---

## Portfolio und Annahmen

### Portfoliozusammensetzung
- Bitcoin (BTC): 50 %
- Ethereum (ETH): 40 %
- Solana (SOL): 10 %

### Annahmen
- Betrachtung eines einzelnen Handelstags
- **Investitionssumme: 10.000 €**
- Risikoquantil: **99 % (alpha = 0.01)**
- Verwendung historischer Tagesrenditen

---

## Projektstruktur

solana-var-project/
├── figures/
│   └── simulated_var_histogram.png
├── notebooks/
│   └── finale_analyse.ipynb
├── src/
│   ├── __init__.py
│   └── simulate_var.py
├── .gitignore
├── README.md
└── requirements.txt

## Ablauf der Analyse

1. Datenimport und Vorbereitung

Im Notebook finale_analyse.ipynb werden historische Kursdaten für
Bitcoin, Ethereum und Solana über die Bibliothek yfinance geladen.
Verwendet werden tägliche Schlusskurse der letzten 12 Monate.

Aus den Kursdaten werden logarithmische Renditen berechnet:
log_returns = np.log(df / df.shift(1)).dropna()

2. Berechnung der Portfolio-Renditen

Die einzelnen Asset-Renditen werden entsprechend der Portfolio-Gewichtung
kombiniert:
weights = np.array([0.5, 0.4, 0.1])
portfolio_returns = log_returns @ weights

Das Ergebnis ist eine Zeitreihe täglicher Portfolio-Renditen, die als
Eingabe für die Monte-Carlo-Simulation dient.


Die Funktion simulate_var()

Die eigentliche Risikoberechnung erfolgt in der Funktion
simulate_var() in src/simulate_var.py.

Funktionsaufruf
simulate_var(
    returns,
    investment=10000,
    alpha=0.01,
    N=100_000,
    B=500,
    save_plot=False,
    plot_path="../figures/simulated_var_histogram.png"
)
Bedeutung der Parameter

returns
Zeitreihe der Portfolio-Log-Renditen.

investment = 10000
Investitionssumme in Euro, auf die sich alle simulierten Verluste beziehen.

alpha = 0.01
Risikolevel für den VaR.
Ein Wert von 0.01 entspricht einem 99 %-Value-at-Risk.

N = 100_000
Anzahl der Monte-Carlo-Ziehungen zur Simulation möglicher Tagesverluste.

B = 500
Anzahl der Bootstrap-Wiederholungen zur Schätzung des Standardfehlers
und eines 95 %-Konfidenzintervalls.

save_plot
Steuert, ob eine Grafik der simulierten Verluste gespeichert wird.

plot_path
Relativer Pfad zum Speicherort der erzeugten Grafik.

⸻

Monte-Carlo-Simulation

Die Monte-Carlo-Simulation basiert auf einem Bootstrap-Ansatz:
	•	Zufälliges Ziehen aus den historischen Portfolio-Renditen
	•	Umrechnung der Renditen in Verluste:
  sim_losses = -investment * sim_returns
  Berechnung des Value-at-Risk als entsprechendes Quantil der
  Verlustverteilung:
  VaR = np.percentile(sim_losses, alpha * 100)

  Bootstrap und Unsicherheit

Zusätzlich wird ein Bootstrap-Verfahren eingesetzt, um die Unsicherheit
der VaR-Schätzung zu beurteilen.
Dabei wird der VaR mehrfach aus neu gezogenen Stichproben berechnet.

Das Ergebnis sind:
	•	ein Standardfehler des VaR
	•	ein 95 %-Konfidenzintervall

Aufgrund der hohen Anzahl an Monte-Carlo-Ziehungen ist die
VaR-Schätzung numerisch sehr stabil.

⸻

Visualisierung

Optional wird ein Histogramm der simulierten Verluste erzeugt.
Der berechnete VaR wird als vertikale Linie im Plot dargestellt und
im Ordner figures/ gespeichert.

⸻

Hinweis zur Interpretation

Der berechnete Value-at-Risk gibt den maximal erwarteten Tagesverlust
unter normalen Marktbedingungen an.
Extremereignisse außerhalb der historischen Datenbasis werden nicht
explizit berücksichtigt.

⸻

Abhängigkeiten

Alle verwendeten Python-Pakete sind in der Datei requirements.txt
aufgeführt.