# Value-at-Risk Analyse eines Krypto-Portfolios

**Portfoliozusammensetzung:**  
50 % Bitcoin (BTC), 40 % Ethereum (ETH), 10 % Solana (SOL)

---

## 1. Ziel der Arbeit

Ziel dieses Projekts ist es, das Risiko eines Krypto-Portfolios mithilfe des
Value-at-Risk-Ansatzes (VaR) zu quantifizieren.  
Da Kryptowährungen für ihre hohe Volatilität bekannt sind, eignet sich der
VaR als Kennzahl, um potenzielle Verluste unter normalen Marktbedingungen
abzuschätzen.

Die Analyse basiert auf historischen Marktdaten und verwendet eine
Monte-Carlo-Simulation, um mögliche Verlustszenarien zu simulieren.

---

## 2. Datengrundlage

- **Datenquelle:** Yahoo Finance (`yfinance`)
- **Assets:** Bitcoin (BTC), Ethereum (ETH), Solana (SOL)
- **Zeitraum:** Letzte 12 Monate
- **Preisdaten:** Schlusskurse (Close)

Aus den Kursdaten werden logarithmische Tagesrenditen berechnet, da diese
in der Finanzanalyse üblich sind und eine bessere mathematische
Handhabung ermöglichen.

---

## 3. Methodik

### 3.1 Portfolio-Renditen
Die einzelnen Asset-Renditen werden entsprechend der vorgegebenen
Portfolio-Gewichtung kombiniert:

- 50 % BTC  
- 40 % ETH  
- 10 % SOL  

Dadurch entsteht eine Zeitreihe der täglichen Portfolio-Renditen.

---

### 3.2 Monte-Carlo-Simulation

Zur Risikoschätzung wird eine **historische Monte-Carlo-Simulation**
(Bootstrap-Verfahren) verwendet:

- Zufälliges Ziehen aus den historischen Portfolio-Renditen
- Anzahl der Simulationen: **100.000**
- Investitionssumme: **10.000 €**
- Betrachtungshorizont: **1 Tag**
- Konfidenzniveau: **99 %**

Aus den simulierten Renditen werden mögliche Tagesverluste berechnet.
Der Value-at-Risk ergibt sich als das entsprechende Quantil der
Verlustverteilung.

---

### 3.3 Unsicherheitsabschätzung

Zusätzlich wird ein Bootstrap-Verfahren mit 500 Wiederholungen eingesetzt,
um den Standardfehler sowie ein 95 %-Konfidenzintervall des VaR zu schätzen.
Aufgrund der hohen Anzahl an Simulationen ist die VaR-Schätzung sehr stabil.

---

## 4. Ergebnisse

Die Monte-Carlo-Simulation liefert eine Verteilung möglicher Tagesverluste
des Portfolios.  
Der geschätzte **1-Tages-Value-at-Risk (99 %)** liegt im negativen Bereich
und beschreibt den maximal erwarteten Verlust unter normalen Marktbedingungen.

Die hohe Anzahl an Simulationen führt zu einem sehr engen
Konfidenzintervall, was auf eine geringe numerische Unsicherheit der
Schätzung hinweist.

Ein Histogramm der simulierten Verluste mit markiertem VaR ist in der
folgenden Abbildung dargestellt:

![Histogramm der simulierten Verluste](reports/simulated_var_histogram.png)

---

## 5. Interpretation

Der 99 %-VaR kann wie folgt interpretiert werden:
Mit einer Wahrscheinlichkeit von 99 % wird der Tagesverlust des Portfolios
den geschätzten VaR-Wert nicht überschreiten.

Dabei ist zu beachten:
- Der VaR basiert ausschließlich auf historischen Daten
- Extremereignisse außerhalb der Beobachtungsperiode werden nicht explizit
  berücksichtigt
- Der VaR macht keine Aussage über die Höhe möglicher Verluste jenseits
  der VaR-Schwelle

---

## 6. Fazit

Die Analyse zeigt, dass sich der Value-at-Risk-Ansatz gut eignet, um das
Risiko eines Krypto-Portfolios quantitativ zu erfassen.
Trotz der Einfachheit des Modells liefert die Monte-Carlo-Simulation
eine anschauliche Einschätzung möglicher Verluste.

Mögliche Erweiterungen des Modells wären:
- Mehrtägige VaR-Berechnung
- Berücksichtigung von Korrelationen und Volatilitätsmodellen
- Ergänzung durch Stress-Tests oder Expected Shortfall

---

## 7. Projektstruktur

- `notebooks/finale_analyse.ipynb` – Hauptanalyse
- `src/simulate_var.py` – Monte-Carlo- und Bootstrap-Funktionen
- `reports/simulated_var_histogram.png` – Visualisierung der Ergebnisse
- `requirements.txt` – verwendete Python-Pakete