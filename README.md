## Heart Rate Monitoring Data Processing Pipeline

This project simulates real‑world data engineering work for a Taiwan‑based wearable health‑tech company, Seng‑Links, where I served as a junior data engineer responsible for building a batch‑processing pipeline to clean and analyze raw heart‑rate data. The company discovered that prototype devices were exporting inconsistent heart‑rate files containing malformed records, impossible values, and missing entries. Before the machine learning team could study sleep and exercise patterns, the data engineering team needed a reliable preprocessing system.
I built a Python‑based pipeline that:
  Reads raw heart‑rate files using file I/O
  Cleans malformed records using a custom data‑validation function
  Computes descriptive statistics — average, median, range — using base Python   and for‑loops
  Generates structured outputs for downstream analysis
  Logs skipped rows to quantify data quality issues
  
The dataset consisted of four raw files containing 5‑minute interval heart‑rate readings from a 30‑year‑old participant. My pipeline ensured that all malformed entries were filtered out, valid readings were converted to integers, and all statistics were rounded to two decimal places. The final deliverables included:
  A fully functioning data‑cleaning pipeline
  A suite of custom statistical functions implemented without external     libraries
  A rolling average feature for trend smoothing
  A written analysis in writeup.md summarizing data quality, trends, and insights
  This project demonstrates foundational data engineering skills: 
    data cleaning, 
    pipeline design, 
    error handling, 
    statistical computation, and 
    clear analytical communication.
