import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/product"

st.set_page_config(
    page_title="Product Lookup",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Product Lookup (HashMap)")

st.markdown("---")

st.write(
    """
Retrieve complete product information using the
HashMap-based lookup engine.
"""
)

product_name = st.text_input(
    "Enter Exact Product Name",
    placeholder="Example: BB Royal Idli Rice"
)

if st.button("🔍 Lookup Product", use_container_width=True):

    if product_name.strip() == "":

        st.warning("Please enter a product name.")

    else:

        try:

            response = requests.get(
                API_URL,
                params={
                    "name": product_name
                }
            )

            if response.status_code == 200:

                result = response.json()

                if result.get("status") == "error":

                    st.error(result["message"])

                else:

                    st.success("Product Found")

                    st.markdown("---")

                    col1, col2 = st.columns(2)

                    with col1:

                        st.metric(
                            "Price",
                            f"₹ {result['price']}"
                        )

                        st.metric(
                            "Rating",
                            result["rating"]
                        )

                        st.metric(
                            "Stock",
                            result["stock"]
                        )

                    with col2:

                        st.metric(
                            "Brand",
                            result["brand"]
                        )

                        st.metric(
                            "Category",
                            result["category"]
                        )

                        st.metric(
                            "Supplier",
                            result["supplier"]
                        )

                    st.markdown("### Product Name")

                    st.info(result["product_name"])

                    st.markdown("### Description")

                    st.write(result["description"])

            else:

                st.error(response.text)

        except Exception as e:

            st.error(str(e))