import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/search"

st.set_page_config(
    page_title="Product Search",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Product Search (Trie Search Engine)")

st.markdown("---")

st.write("""
Search products using the Trie Search Engine.

As you type a prefix, the backend searches matching products using the Trie data structure.
""")

keyword = st.text_input(
    "Enter Product Name",
    placeholder="Example: rice, milk, sugar..."
)

if st.button("🔍 Search", use_container_width=True):

    if keyword.strip() == "":

        st.warning("Please enter a product name.")

    else:

        try:

            response = requests.get(

                API_URL,

                params={

                    "q": keyword

                }

            )

            if response.status_code == 200:

                result = response.json()

                st.success(

                    f"{result['count']} Products Found"

                )

                if result["count"] == 0:

                    st.warning("No matching products found.")

                else:

                    df = pd.DataFrame(

                        result["results"],

                        columns=["Product Name"]

                    )

                    st.dataframe(

                        df,

                        use_container_width=True,

                        hide_index=True

                    )

            else:

                st.error(response.text)

        except Exception as e:

            st.error(str(e))