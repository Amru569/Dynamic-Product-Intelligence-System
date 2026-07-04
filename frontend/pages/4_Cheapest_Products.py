import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/top-cheapest"

st.set_page_config(
    page_title="Cheapest Products",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Cheapest Products (Min Heap)")

st.markdown("---")

st.write(
    """
Find the cheapest products using the Min Heap
data structure.
"""
)

limit = st.slider(

    "Number of Products",

    min_value=1,

    max_value=50,

    value=10

)

if st.button("💰 Find Cheapest Products", use_container_width=True):

    try:

        response = requests.get(

            API_URL,

            params={

                "limit": limit

            }

        )

        if response.status_code == 200:

            result = response.json()

            if result["count"] == 0:

                st.warning("No products available.")

            else:

                df = pd.DataFrame(

                    result["products"]

                )

                df.insert(

                    0,

                    "Rank",

                    range(1, len(df)+1)

                )

                st.success(

                    f"Top {len(df)} Cheapest Products"

                )

                st.dataframe(

                    df,

                    use_container_width=True,

                    hide_index=True

                )

                st.markdown("---")

                st.metric(

                    "Cheapest Price",

                    f"₹ {df['price'].min()}"

                )

        else:

            st.error(response.text)

    except Exception as e:

        st.error(str(e))