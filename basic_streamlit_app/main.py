import streamlit as st
import pandas as pd

st.title("Washington DC Homes for Sale")
st.write("This app lets you filter through DC home listings to find houses that match what you're looking for!")

# load the dataset
df = pd.read_csv('data/DC_Properties.csv')

# get rid of rows that don't have a price and only keep qualified sales
df = df.dropna(subset=['PRICE'])
df = df[df['QUALIFIED'] == 'Q']

st.subheader("Filter the listings")

# price slider
min_price = int(df['PRICE'].min())
max_price = 1000000  # capping it at $1 million so the slider isn't super long
price_range = st.slider("Price range", min_price, max_price, (min_price, max_price))
df = df[(df['PRICE'] >= price_range[0]) & (df['PRICE'] <= price_range[1])]

# bedrooms dropdown
df = df.dropna(subset=['BEDRM'])
bedrooms = st.selectbox("Number of bedrooms", sorted(df['BEDRM'].unique()))
df = df[df['BEDRM'] == bedrooms]

# bathrooms dropdown
df = df.dropna(subset=['BATHRM'])
bathrooms = st.selectbox("Number of bathrooms", sorted(df['BATHRM'].unique()))
df = df[df['BATHRM'] == bathrooms]

# ward checkboxes (multiselect)
df = df.dropna(subset=['WARD'])
wards = st.multiselect("Ward", sorted(df['WARD'].unique()), default=sorted(df['WARD'].unique()))
df = df[df['WARD'].isin(wards)]

# show how many listings are left
st.write("Number of listings found:", len(df))

# show map of the listings since data includes latitude and longitudes
df_map = df.dropna(subset=['LATITUDE', 'LONGITUDE'])
df_map = df_map.rename(columns={'LATITUDE': 'lat', 'LONGITUDE': 'lon'})
st.map(df_map)

# show the table
st.subheader("Listings")
st.dataframe(df)