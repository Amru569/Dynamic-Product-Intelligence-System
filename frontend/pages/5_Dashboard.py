import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://127.0.0.1:8000/products"

st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Product Analytics Dashboard")

st.markdown("---")

try:

    response = requests.get(API_URL)

    if response.status_code != 200:

        st.error("Unable to connect to backend.")

        st.stop()

    result = response.json()

    products = result["products"]

    if len(products) == 0:

        st.warning("No products available.")

        st.stop()

    df = pd.DataFrame(products)

except Exception as e:

    st.error(str(e))

    st.stop()


# ======================================================
# KPI SECTION
# ======================================================

st.subheader("📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Total Products",
        len(df)
    )

with col2:

    st.metric(
        "Average Price",
        f"₹ {round(df['price'].mean(),2)}"
    )

with col3:

    st.metric(
        "Lowest Price",
        f"₹ {df['price'].min()}"
    )

with col4:

    st.metric(
        "Highest Price",
        f"₹ {df['price'].max()}"
    )

st.markdown("---")

# ======================================================
# CATEGORY CHART
# ======================================================

st.subheader("📦 Products by Category")

category_df = (

    df["category"]

    .fillna("Unknown")

    .value_counts()

    .reset_index()

)

category_df.columns = [

    "Category",

    "Products"

]

fig = px.bar(

    category_df,

    x="Category",

    y="Products",

    title="Products by Category"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

# ======================================================
# PRICE DISTRIBUTION
# ======================================================

st.subheader("💰 Price Distribution")

fig = px.histogram(

    df,

    x="price",

    nbins=30,

    title="Price Distribution"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

# ======================================================
# TOP EXPENSIVE PRODUCTS
# ======================================================

st.subheader("🏆 Top 10 Expensive Products")

expensive = (

    df

    .sort_values(

        by="price",

        ascending=False

    )

    .head(10)

)

st.dataframe(

    expensive[

        [

            "product_name",

            "brand",

            "category",

            "price"

        ]

    ],

    use_container_width=True,

    hide_index=True

)

# ======================================================
# TOP CHEAPEST PRODUCTS
# ======================================================

st.subheader("💵 Top 10 Cheapest Products")

cheap = (

    df

    .sort_values(

        by="price"

    )

    .head(10)

)

st.dataframe(

    cheap[

        [

            "product_name",

            "brand",

            "category",

            "price"

        ]

    ],

    use_container_width=True,

    hide_index=True

)

# ======================================================
# RATINGS
# ======================================================

st.subheader("⭐ Rating Distribution")

fig = px.histogram(

    df,

    x="rating",

    nbins=10,

    title="Rating Distribution"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

# ======================================================
# COMPLETE DATASET
# ======================================================

st.subheader("📋 Complete Dataset")

st.dataframe(

    df,

    use_container_width=True,

    hide_index=True
)