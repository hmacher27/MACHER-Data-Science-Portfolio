import streamlit as st
import pandas as pd

st.title("Hello, Streamlit!")
st.write("This is my first Streamlit app.")

if st.button("Click me!"):
    st.write("🎉 You clicked the button! Nice work! 🚀")
else:
    st.write("Click the button to see what happens...")

color = st.color_picker("Pick a color", "#00f900")
st.write(f"You picked: {color}")

# What I added for fun 
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def get_contrast_text_color(hex_color):
    r, g, b = hex_to_rgb(hex_color)
    luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
    return "black" if luminance > 0.5 else "white"

def lighten_color(hex_color, amount=0.7):
    r, g, b = hex_to_rgb(hex_color)
    r, g, b = (int(c + (255 - c) * amount) for c in (r, g, b))
    return f"#{r:02x}{g:02x}{b:02x}"

text_color = get_contrast_text_color(color)
light_color = lighten_color(color, amount=0.7)

# Helper: style a dataframe's header row and body cells using the picked color
def style_header(df):
    return df.style.set_table_styles(
        [
            {
                "selector": "th",
                "props": [("background-color", color), ("color", text_color)],
            },
            {
                "selector": "td",
                "props": [("background-color", light_color)],
            },
        ]
    )

import pandas as pd

st.subheader("Exploring Our Dataset")

# Load the CSV file
df = pd.read_csv("data/sample_data.csv")

st.write("Here's our data:")
st.table(style_header(df))

# Filter by city
city = st.selectbox("Select a city", df["City"].unique())
filtered_df = df[df["City"] == city]

st.write(f"People in {city}:")
st.table(style_header(filtered_df))

# Filter by occupation
occupation = st.selectbox("Select an occupation", df["Occupation"].unique())
filtered_df = df[(df["City"] == city) & (df["Occupation"] == occupation)]

st.write(f"{occupation}s in {city}:")
st.table(style_header(filtered_df))

# Show summary statistics
st.subheader("Summary Statistics")
st.table(style_header(df.describe()))