# DC Homes Finder

Moving to (or around) Washington, DC and trying to find a place to live can be overwhelming, with hundreds of listings to sort through and no easy way to narrow them down, especially if you're not from DC. I built this app because I'm moving to DC and wanted to become more informed about the residential housing market and what prices look like if I decide to stay in the area long-term. The app helps make that process a little less stressful by letting you filter through DC home listings by price, bedrooms, bathrooms, and location to find options that actually match what you're looking for.

## Data Source

The data comes from the [DC Residential Properties dataset](https://www.kaggle.com/datasets/christophercorrea/dc-residential-properties?select=DC_Properties.csv) on Kaggle.

## What the App Does

- Filter listings by price range, number of bedrooms, number of bathrooms, and ward
- See how many listings match the filters
- View the matching listings on a map
- Browse the full results in a table

## Folder Structure

```
basic_streamlit_app/
├── README.md
├── main.py
├── data/
│   └── DC_Properties.csv
```

## How to Run It

1. Make sure `DC_Properties.csv` is inside the `data/` folder
2. Install the required packages:

   ```
   pip install streamlit pandas
   ```

3. From the project root, run:

   ```
   streamlit run basic_streamlit_app/main.py
   ```
