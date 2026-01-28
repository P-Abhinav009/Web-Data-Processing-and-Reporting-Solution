# 📈 A Multi-Sector Financial Intelligence Pipeline
### An End-to-End ETL Pipeline: Python ➔ Excel ➔ Power BI

![Python](https://img.shields.io/badge/python-v3.9+-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-data%20analysis-150458.svg)
![BeautifulSoup](https://img.shields.io/badge/bs4-web%20scraping-brightgreen.svg)
![PowerBI](https://img.shields.io/badge/PowerBI-Visualization-F2C811.svg)
![License](https://img.shields.io/badge/license-MIT-red.svg)

## 📋 Project Overview
**AlphaStream** is a robust Data Engineering project that automates the extraction of high-frequency financial metrics from 25 global market leaders across 5 distinct economic sectors. 

While most scrapers only track "Price," AlphaStream captures the **Fundamental DNA** of a stock (Volatility, Valuation, and Profitability). It implements a persistent storage logic that appends daily snapshots into a master dataset, enabling long-term historical trend analysis.

---

## 🏗 System Architecture (ETL)

### 1. Extraction (E)
- **Source:** Real-time parsing of Yahoo Finance using `BeautifulSoup4`.
- **Strategy:** Targeted extraction using HTML data-attributes (`data-field`) for high reliability.
- **Resilience:** Implemented custom `User-Agent` rotation and `time.sleep` intervals to mimic human browsing and prevent IP throttling.

### 2. Transformation (T)
- **Data Cleaning:** Use of `Pandas` to convert raw string data (e.g., "$182.41") into clean numerical floats.
- **Categorization:** Automated sector tagging to enable "Macro vs. Micro" analysis.
- **Validation:** `try-except` blocks ensure that a failure in one stock doesn't crash the entire pipeline.

### 3. Loading (L)
- **Storage:** Data is loaded into a master Excel file (`market_analysis_data.xlsx`).
- **Logic:** Smart-append logic ensures that the file grows over time rather than being overwritten, facilitating time-series forecasting.

---

## 📊 Monitored Portfolio & Sectors
The pipeline tracks a diversified "Mini-Index" to observe market rotations:

| Sector | Tickers | Strategic Reasoning |
| :--- | :--- | :--- |
| **Technology** | AAPL, MSFT, GOOGL, NVDA, ORCL | Growth drivers & AI innovation. |
| **Consumer** | KO, PEP, PG, WMT, COST | Defensive stability & inflation resistance. |
| **Finance** | JPM, BAC, V, MA, GS | Interest rate sensitivity & credit health. |
| **Energy/Auto** | TSLA, XOM, CVX, F, TM | Global supply chain & transition indicators. |
| **Healthcare** | JNJ, PFE, UNH, ABBV, LLY | Demographic-driven long-term stability. |

---

## 🧪 Financial Metrics (The Data Dictionary)
This pipeline captures more than just prices; it captures **intelligence**:
*   **PE Ratio (TTM):** Helps identify if a stock is overvalued (Tech) or undervalued (Banking).
*   **Beta (5Y Monthly):** Measures systemic risk. (Beta > 1 = Aggressive; Beta < 1 = Conservative).
*   **Forward Dividend Yield:** Tracks cash-flow potential for passive income investors.
*   **Volume:** Measures the "Conviction" of price movements.
*   **EPS (TTM):** Tracks the direct profitability of the underlying business.

---

## 🚀 Installation & Deployment

### Prerequisites
- Python 3.9+
- Pip (Python Package Manager)

### Step-by-Step Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/AlphaStream-Scraper.git
   cd AlphaStream-Scraper