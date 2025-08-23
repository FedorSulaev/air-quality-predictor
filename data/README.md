# Data Sources

This project uses two primary open datasets for building and evaluating air quality regression models in Iași, Romania (2020–2025).

---

## 1. Air Quality Data

**Dataset:** Hourly air pollutant measurements (e.g., NO₂, PM₁₀, PM₂.₅, O₃, CO, SO₂)  
**Source:** [OpenAQ](https://openaq.org/) – a global open air quality data platform  
**Format:** CSV (retrieved via the OpenAQ API and Open Data S3 archive)  
**Coverage:** Monitoring stations in Iași, 2020–2025  

**Why this dataset?**  
- Provides openly licensed, standardized access to official government and community monitoring station data.  
- Hourly pollutant values (µg/m³) aligned with health-relevant metrics.  
- Global scope, but with local granularity – includes Romanian ANPM stations exposed through OpenAQ.  
- Consistent API and archive access makes it reproducible and automatable.

---

## 2. Meteorological Data

**Dataset:** Hourly meteorological observations (temperature, dew point, sea-level pressure, wind direction, wind speed, sky cover, precipitation)  
**Source:** [NOAA Integrated Surface Database – ISD-Lite](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database)  
**Format:** Fixed-width `.gz` text files (processed into CSV)  
**Station:** Iași Airport (WMO/USAF ID: 150900)  
**Coverage:** 2020–2025  

**Why this dataset?**  
- Long-term, quality-controlled hourly weather data from a globally trusted source (NOAA).  
- ISD-Lite provides a simplified format (fewer variables, fixed-width columns) that is easier to parse and combine with other datasets.  
- Includes the key meteorological drivers that affect pollutant dispersion and concentration (wind, pressure, precipitation, temperature).

---

## 3. Why These Two Together?

- **Air quality + meteorology are strongly interdependent**: pollutant concentrations are influenced by weather conditions such as wind, precipitation, and pressure.  
- Both datasets are **open access, reliable, and cover the same period (2020–2025)**, making them ideal for building reproducible regression models.  
- The combination allows for robust analysis of how meteorological factors impact local air quality in Iași.

---