# 📉 Vodafone Idea Business Analysis & Forecasting

## 📌 Project Overview

This project is a comprehensive data-driven case study on **Vodafone Idea (Vi)** — one of India's major telecom operators — focusing on:

- 📉 **Understanding the causes behind Vodafone Idea's financial decline**
- 📊 **Analyzing historical business and operational data**
- 🔮 **Forecasting future performance using time series models**
- ⚖️ **Comparing trends with industry competitors like Airtel and Jio**

---

## 🎯 Objective

> To investigate the decline of Vodafone Idea through financial analysis, identify core issues (like AGR dues, subscriber churn, and low ARPU), and forecast future performance assuming current trends continue.

---

## 🗂️ Project Structure

```bash
vodafone-idea-analysis/
│
├── data/                   # All datasets used
│   ├── raw/                # Original PDFs, web scrapes
│   ├── processed/          # Cleaned CSVs, Excel files
│   └── reference/          # TRAI, competitor, industry data
│
├── notebooks/              # Jupyter notebooks for analysis
│   ├── EDA.ipynb
│   ├── forecasting_arima.ipynb
│   └── competitors_analysis.ipynb
│
├── scripts/                # Python scripts for scraping and processing
│   ├── scrape_moneycontrol.py
│   ├── extract_pdf_reports.py
│   └── download_yahoo_stock.py
│
├── visuals/                # Graphs and dashboard exports
├── reports/                # Final PDF summary, PPT
├── README.md
└── requirements.txt
