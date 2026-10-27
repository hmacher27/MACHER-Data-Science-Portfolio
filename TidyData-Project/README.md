# Tidy Data Project: Federal R&D Spending

## What This Project Is About

For this project, I cleaned a messy dataset on U.S. federal R&D budgets (1976-2017) using tidy data principles. The original data had the year and GDP stuck together in the column names, so I used `melt()` and `str.split()` to reshape it and split it into two tables. Then I made three visualizations and a pivot table. I found that DOD spends the most by far, and that R&D dropped from about 4.8% of GDP in 1976 to under 1% in 2017.

## How This Fits Into My Portfolio

My previous project, [DC Homes Finder](../basic_streamlit_app), was a Streamlit app that lets people filter DC home listings by price, bedrooms, bathrooms, and ward. That project was about building something interactive on top of a dataset. This one focuses on getting messy data into a clean format. I learned that a lot of data work is cleaning, and once the data is tidy, things like `groupby()` and plotting get way easier. Together, these projects show I can prepare real-world data and then turn it into something people can use.

## How to Run It

1. Install the packages: `pip install pandas matplotlib seaborn jupyter`
2. Put `fed_rd_year&gdp.csv` in the same folder as the notebook.
3. Open `[your-notebook-name].ipynb` in Jupyter and run all the cells.

## References

- [Federal R&D Budgets dataset (TidyTuesday, 2019-02-12)](https://github.com/rfordatascience/tidytuesday/tree/main/data/2019/2019-02-12)
