
# **Project Overview – OECD Leading Indicators Analysis**

**Author:** Jing Pan  
**Date:** November 2025  

---

## **Purpose**

This document provides a complete structural overview of the **_OECD Leading Indicators Analysis_** project.  
It summarizes the purpose and content of each Jupyter Notebook (00–06), ensuring a clear understanding of the project flow — from **_data preparation_** to **_analysis_** and **_discussion_**.

---
## **Research Questions → Notebook Mapping**

| RQ | Question | Notebook |
|---|---|---|
| RQ1 | How did the **<u>CLI</u>** change **before and after 2020**? | 03 _cli_trends_analysis_ |
| RQ2 | Which **<u>countries</u>** experienced the **largest variations** in **<u>CLI</u>** during this period? | 03 _cli_trends_analysis_ |
| RQ3 | Is there a significant **<u>correlation</u>** between **<u>CLI</u>** and **<u>GDP growth</u>** (or other **<u>macroeconomic indicators</u>**)? | 04 _correlation_study_ |

---
## **Notebook Summary**

| Notebook | Title | Purpose | Phase |
|-----------|--------|----------|--------|
| 00 _project_description_ | Project Description | Defines the **<u>motivation</u>**, **<u>research questions</u>**, **<u>objectives</u>**, **<u>methods</u>**, and **<u>dataset sources</u>**. | Project Setup |
| 01 _intro_and_dataset_ | Dataset Introduction and Cleaning | Loads and merges the two **<u>OECD CSV datasets</u>**, performs **<u>cleaning</u>**, and saves a unified dataset. | Data Preparation |
| 02 _data_dictionary_ | Data Dictionary | Documents **<u>field meanings</u>**, **<u>types</u>**, **<u>relationships</u>**, and naming consistency; clarifies dual naming (machine-friendly vs human-readable). | Data Understanding |
| 03 _cli_trends_analysis_ | CLI Trends Analysis | Explores **<u>CLI time-series patterns</u>**, compares **<u>pre/post-2020</u>** changes, and identifies countries with **<u>largest fluctuations</u>**. | Exploratory Analysis |
| 04 _correlation_study_ | Correlation Study | Quantifies relationships between **<u>CLI</u>** and **<u>GDP growth</u>** (and other indicators) via **<u>correlation</u>**/**<u>regression</u>** with aligned **<u>time</u>** and **<u>country</u>** dimensions. | Statistical Analysis |
| 05 _summary_and_discussion_ | Summary and Discussion | Synthesizes findings, discusses implications, and identifies limitations and future work. | Interpretation |
| 06 _appendix_and_references_ | Appendix and References *(optional)* | Provides supplementary figures, tables, and references. | Supplementary |

---

## **Detailed Notebook Frameworks**

### **00 – Project Description**
| Step | Section | Description |
|------|----------|-------------|
| 1 | Introduction and Motivation | Introduce the concept of **_OECD CLI_** and project motivation. |
| 2 | Research Questions | Present the three key questions. |
| 3 | Objectives | Outline project goals and scope. |
| 4 | Methodology Overview | Explain workflow structure (**_IMRAD_**, **_CRISP-DM_**). |
| 5 | Expected Outcomes | Define expected patterns and results. |
| 6 | Project Structure | Display organized file and folder layout. |
| 7 | References | List main data and conceptual sources. |

---

### **01 – Intro and Dataset**
| Step | Section | Description |
|------|----------|-------------|
| 1 | Overview | Introduce notebook purpose. |
| 2 | Load and Preview Dataset | Load both raw CSVs. |
| 3 | Basic Info and Data Types | Inspect structure and column types. |
| 4 | Missing Value Check | Identify and summarize missing fields. |
| 5 | Combine and Clean Dataset | Merge both datasets and deduplicate. |
| 6 | Initial Observations | Analyze **_country distribution_** and **_time range_**. |
| 7 | Basic Visualization | Display **_bar chart_** of record counts per country. |
| 8 | Save Cleaned Dataset | Save as `cleaned_oecd_cli.csv`. |
| 9 | Summary and Transition | Conclude and direct to the next step. |

---

### **02 – Data Dictionary**
| Step | Section | Description |
|------|----------|-------------|
| 1 | Purpose | Define notebook goal. |
| 2 | Load Cleaned Dataset | Import the unified dataset. |
| 3 | Column Overview | Display all column names. |
| 4 | Core Field Descriptions | Build a field dictionary table (**_name_**, **_type_**, **_meaning_**). |
| 5 | Extended Field Notes | Provide detailed notes for key fields (**_SUBJECT_**, **_MEASURE_**, **_VALUE_**). |
| 6 | Field Relationships | Explain inter-variable dependencies. |
| 7 | Data Consistency Check | Verify missing values and duplicates. |
| 8 | Summary and Next Step | Summarize and transition to trends analysis. |

---

### **03 – CLI Trends Analysis**
| Step | Section                             | Description                                                                                                                                |
| ---- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | **Purpose**                         | State goal: exploring **CLI time-series patterns**.                                                                                        |
| 2    | **Load Cleaned Dataset**            | Load the unified dataset produced in the previous notebook.                                                                                |
| 3    | **Data Quality & Filtering Check**  | Verify data integrity and ensure only **CLI (Index-based)** indicators are retained. *(New section — critical for preventing mixed data.)* |
| 4    | **Time Range Overview**             | Identify earliest and latest observation dates.                                                                                            |
| 5    | **Country Distribution**            | Count available records per country to confirm balanced coverage.                                                                          |
| 6    | **Time Series Visualization**       | Plot **country-level CLI** trends over time (clean, filtered data).                                                                        |
| 7    | **Before vs After 2020 Comparison** | Quantitatively compare pre- and post-pandemic CLI levels.                                                                                  |
| 8    | **Identify Extreme Movements**      | Find countries with largest increases/decreases in CLI.                                                                                    |
| 9    | **Observations and Insights**       | Summarize temporal and cross-country trends, discuss implications.                                                                         |
| 10   | **Summary and Next Step**           | Wrap up and transition to the **correlation analysis** notebook.                                                                           |

---

### **04 – Correlation Study**
| Step | Section | Description |
|------|----------|-------------|
| 1 | Purpose | Define correlation goals (**_CLI vs GDP_**, etc.). |
| 2 | Load CLI and GDP Data | Import **_CLI dataset_** and external **_GDP indicators_**. |
| 3 | Data Alignment | Synchronize **_time_** and **_country dimensions_**. |
| 4 | Correlation Computation | Calculate correlation coefficients (**_Pearson_**, **_Spearman_**). |
| 5 | Correlation Visualization | Plot **_heatmaps_** and **_scatterplots_**. |
| 6 | Country-Level Comparison | Compare correlation differences among nations. |
| 7 | Interpretation | Interpret findings from **_economic perspective_**. |
| 8 | Summary and Next Step | Summarize and move to discussion. |

---

### **05 – Summary and Discussion**
| Step | Section | Description |
|------|----------|-------------|
| 1 | Purpose | Define notebook purpose: reflection and synthesis. |
| 2 | Key Findings Recap | Summarize previous notebooks’ main insights. |
| 3 | Interpretation | Discuss **_economic and data-driven implications_**. |
| 4 | Limitations | Acknowledge **_data/methodological constraints_**. |
| 5 | Recommendations | Suggest **_practical takeaways_** or improvements. |
| 6 | Future Work | Describe **_extensions and next research steps_**. |
| 7 | Final Summary | Provide brief overall wrap-up. |

---

### **06 – Appendix and References (Optional)**
| Step | Section | Description |
|------|----------|-------------|
| 1 | Appendix Overview | Introduce appendix purpose. |
| 2 | Supplementary Figures | Include detailed **_plots_** or **_country-level visualizations_**. |
| 3 | Extended Tables | Provide **_supporting data tables_**. |
| 4 | Additional Code Snippets | Add **_reusable_** or secondary code blocks. |
| 5 | References | List all **_sources_** and **_citations_**. |

---

## **Project Flow Summary**
| Phase | Notebooks | Focus |
|--------|------------|--------|
| **_Setup and Understanding_** | 00–02 | **_Project design_**, **_data acquisition_**, **_cleaning_**, and **_field comprehension_**. |
| **_Exploration and Analysis_** | 03–04 | **_Trend analysis_** and **_correlation modeling_**. |
| **_Interpretation and Reporting_** | 05–06 | **_Conclusions_**, **_reflections_**, and **_documentation_**. |

---

## **Navigation**
- [README.md](README.md) — Project introduction and dataset overview  
- [Project Overview](project_overview.md) — Detailed notebook structure (this file)  
- `notebooks/` — Implementation and analysis notebooks  
- `data/` — Raw and cleaned datasets  
- `src/` — Utility scripts  

