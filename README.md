# OECD Leading Indicators Analysis

## Overview
This project analyzes the OECD Composite Leading Indicators (CLI) dataset to examine how economic confidence and early warning signals evolved across countries from 2016 to 2020.  
The goal is to identify __patterns__, __correlations__, and __predictive trends__ from OECD’s leading economic indicators before and after major global events.

---

## Research Questions
1. **How did the Composite Leading Indicator (CLI) change before and after 2020 across major economies?**  
   Identify visible economic slowdown and recovery trends.

2. **Which countries show the strongest correlation between CLI and GDP-related confidence indices?**  
   Explore possible predictive relationships between leading indicators and real economic activity.

3. **Can leading indicators serve as early warning signals of economic downturns?**  
   Examine volatility and trend reversals to test the reliability of CLI as an early signal.

*Detailed motivation and background are provided in [00_project_description.ipynb](notebooks/00_project_description.ipynb).*

---

## Dataset
**Source:** [OECD Leading Indicators Dataset (Kaggle)](https://www.kaggle.com/datasets/alenavorushilova/leading-indicators-oecd)

**Files Used:**
- `MEI_20022020103548670.csv`
- `MEI_26032020094401290.csv`

Each file contains the following key fields:

| Field | Description |
|--------|-------------|
| __LOCATION__ | Country or region code (e.g., USA, FRA, CHN) |
| __SUBJECT__ | Type of economic indicator (e.g., GDP, CLI, Confidence Index) |
| __MEASURE__ | Measurement unit or category (e.g., index value, percentage) |
| __FREQUENCY__ | Reporting frequency (e.g., monthly, quarterly) |
| __TIME__ | Date (month/year) |
| __Value__ | Numeric value of the indicator |
| __Flag Codes__ | Additional codes explaining missing or estimated data |

*Dataset exploration is available in [01_intro_and_dataset.ipynb](notebooks/01_intro_and_dataset.ipynb).*

---

## Methodology (Planned)
- __Data Cleaning__: Handle missing values and inconsistent indicator naming.  
- __Feature Engineering__: Derive year-over-year changes and normalized CLI indices.  
- __Visualization__: Compare trends across selected countries and indicators.  
- __Statistical Analysis__: Conduct correlation and regression modeling to quantify relationships.

---

## Project Structure
```text

oecd-leading-indicators/
│
├── data/
│ ├── MEI_20022020103548670.csv
│ └── MEI_26032020094401290.csv
│
├── notebooks/
│ ├── 00_project_description.ipynb
│ ├── 01_intro_and_dataset.ipynb
│ ├── 02_data_dictionary.ipynb (planned)
│ ├── 03_cli_trends_analysis.ipynb (planned)
│ ├── 04_correlation_study.ipynb (planned)
│ └── 05_summary_and_discussion.ipynb(planned)
│
├── src/
│ └── utils.py
│
├── reports/
│ └── .gitkeep
│
├── figs/
│ └── .gitkeep
│
├── README.md
└── .gitignore
```


---

## Notebook Navigation
| Notebook | Description |
|-----------|--------------|
| [00_project_description.ipynb](notebooks/00_project_description.ipynb) | Defines research motivation and objectives. |
| [01_intro_and_dataset.ipynb](notebooks/01_intro_and_dataset.ipynb) | Presents dataset structure and initial exploration. |
| [02_data_dictionary.ipynb](notebooks/02_data_dictionary.ipynb) | Documents field definitions and meanings. |
| [03_cli_trends_analysis.ipynb](notebooks/03_cli_trends_analysis.ipynb) | Analyzes CLI changes before and after 2020. |
| [04_correlation_study.ipynb](notebooks/04_correlation_study.ipynb) | Tests relationships between CLI and GDP indicators. |
| [05_summary_and_discussion.ipynb](notebooks/05_summary_and_discussion.ipynb) | Summarizes findings and discusses implications. |

---

## Tools and Libraries
- Python 3.9+  
- Pandas  
- NumPy  
- Matplotlib / Seaborn  
- Jupyter Notebook  

---

## Next Steps
1. Complete the __Data Dictionary__ for all OECD fields.  
2. Clean and preprocess the dataset for CLI trend analysis.  
3. Visualize cross-country comparisons and highlight anomalies.  
4. Conduct statistical tests and summarize key findings.

---

## Author
**Jing Pan**  
Data Science Student, Wentworth Institute of Technology  
Boston, MA, USA

---

## Acknowledgments
Dataset by __Alena Vorushilova__ via Kaggle  
OECD Open Data Portal: [https://data.oecd.org](https://data.oecd.org)
