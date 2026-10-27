# MACHER-Data-Science-Portfolio

## Purpose

This repository contains code and projects completed for the Introduction to Data Science course. It serves as a portfolio documenting my work throughout the class, including data exploration, visualizations, and modeling exercises.

## Organization Plan

All projects will live within this repository, each following a consistent naming convention (e.g., `project-name`) so individual projects are easy to locate and identify at a glance.

Each project will include:

- A short description explaining what the project covers, in case the name alone doesn't fully convey it
- At least one visual (chart, plot, or graphic) summarizing key results, since including visuals tends to make project READMEs clearer and more engaging

## Projects

### 1. DC Homes Finder
**Folder:** [basic_streamlit_app](./basic_streamlit_app)

I'm moving to DC, so I built a Streamlit app that lets you filter DC home listings by price, bedrooms, bathrooms, and ward. It shows how many listings match, plots them on a map, and has a table of the results. The data comes from the DC Residential Properties dataset on Kaggle. This project taught me how to turn a dataset into something interactive that other people can actually use.

**Tools:** Python, pandas, Streamlit

### 2. Tidy Data Project: Federal R&D Spending
**Folder:** [TidyData-Project](./TidyData-Project)

For this project, I cleaned a messy dataset on U.S. federal R&D budgets (1976-2017) using tidy data principles. The original data had the year and GDP stuck together in the column names, so I used `melt()` and `str.split()` to reshape it and split it into two tables. Then I made three visualizations and a pivot table. I found that DOD spends the most by far, and that R&D dropped from about 4.8% of GDP in 1976 to under 1% in 2017.

**Tools:** Python, pandas, matplotlib, seaborn, Jupyter Notebook

## How These Projects Fit Together

My first project, DC Homes Finder, showed that I can build an interactive tool on top of a dataset. The Tidy Data project covers what comes before that: getting messy data into a clean format so it's ready to analyze. I learned that a lot of data work is cleaning, and once the data is tidy, things like `groupby()`, pivot tables, and plotting get way easier. Together, these projects show I can prepare real-world data and then turn it into something people can use, and I plan to keep building on both skills in the rest of the course.
