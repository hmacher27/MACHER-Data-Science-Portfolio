import streamlit as st
import pandas as pd

st.title("Washington DC Apartments")
st.write("This app was built to help alleviate the stress of sorting through hundreds of apartment listings and narrow down the options to what you're looking for!")

st.write("First, what's the maximum for your monthly budget?")
df = pd.read_csv('data/FILE.csv') 
min_price = int(df['#RENT'].min())
max_price = int(df['#RENT'].max())
st.slider('Slide me', min_value=min_price, max_value=max_price)

df = df.dropna(subset=['BEDRM'])
bedroom_options = sorted(df['BEDRM'].unique())
bedrooms = st.selectbox('Number of bedrooms', bedroom_options)
filtered_df = df[df['BEDRM'] == bedrooms]

st.write(f"Found {len(filtered_df)} listings with {bedrooms} bedroom(s)")
st.dataframe(filtered_df)