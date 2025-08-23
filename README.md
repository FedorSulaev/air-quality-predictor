# Air Quality Forecasting for Iași

## Summary
This project focuses on **forecasting air quality levels** in Iași, Romania, using meteorological variables as predictors.  
The problem is important because poor air quality has direct impacts on public health, urban sustainability, and climate resilience.  
By developing reproducible data pipelines and models, this project supports better understanding of the relationship between weather conditions and pollution, and enables actionable insights for citizens and policymakers.

## Hypothesis
Meteorological conditions (temperature, wind speed/direction, precipitation, pressure, etc.) have a significant effect on pollutant concentrations (e.g., NO₂, PM₁₀).  
By combining these variables in regression models, we can forecast air quality levels with meaningful accuracy.

## Dataset Info
### 1. Air Quality Data
- **Dataset:** Hourly air pollutant measurements (e.g., NO₂, PM₁₀, PM₂.₅, O₃, CO, SO₂)  
- **Source:** [OpenAQ](https://openaq.org/) – a global open air quality data platform  
- **Format:** CSV (retrieved via OpenAQ API and Open Data S3 archive)  
- **Coverage:** Monitoring stations in Iași, 2020–2025  
- **Why chosen:** Openly licensed, standardized, and aligned with official monitoring stations; hourly granularity suitable for regression modeling.

### 2. Meteorological Data
- **Dataset:** Hourly weather observations (temperature, dew point, sea-level pressure, wind, sky cover, precipitation)  
- **Source:** [NOAA ISD-Lite](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database)  
- **Station:** Iași Airport (WMO/USAF ID: 150900)  
- **Format:** Fixed-width `.gz` archives processed into CSV  
- **Coverage:** 2020–2025  
- **Why chosen:** Long-term, quality-controlled, and includes key meteorological drivers that affect pollutant dispersion and concentration.

---

## Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
pip install -r requirements.txt
```

Example dependencies (expand as needed):
- `pandas`

---

## Usage
1. Ensure you have an **OpenAQ API key** saved under `config/openaq_api_key`.  
2. Run the notebook to download raw data:

```bash
jupyter notebook notebooks/download_data.ipynb
```

Outputs will be stored under `data/raw/`.  
Processed data, figures, and reports will be saved under the respective `data/processed/` and `outputs/` folders.  
Additional notebooks and scripts will be added later for preprocessing, modeling, and evaluation.

---

## Folder Structure
```
.
├── config/                # API keys and config files
│   └── openaq_api_key
├── data/
│   ├── processed/         # Cleaned and processed datasets
│   ├── raw/               # Raw downloaded datasets
│   └── README.md
├── notebooks/
│   └── download_data.ipynb  # Notebook to download raw OpenAQ & NOAA data
├── outputs/
│   ├── figures/           # Plots, charts, visualizations
│   └── reports/           # Generated reports, summaries
├── references/            # External references, docs
├── src/                   # Source code for processing and modeling
├── requirements.txt       # Project dependencies
└── README.md              # Project overview (this file)
```

---

## Ethical Notes
- **Data Source:** Air quality data from OpenAQ (official and community stations); meteorological data from NOAA ISD-Lite.  
- **License:** Both datasets are open access – OpenAQ (CC-BY 4.0) and NOAA (public domain).  
- **Known Biases:** Urban monitoring stations only – no rural context; may underrepresent variability in suburban/rural air quality.  
- **Consent/Privacy:** Environmental sensor data only – no personal or private data.  
- **Limitations:** Results may not generalize to cities with very different climates, topographies, or monitoring infrastructures.

---

## Contact
Maintainer: **Fedor Sulaev**  
📧 Email: <fedor.sulaev@outlook.com>
