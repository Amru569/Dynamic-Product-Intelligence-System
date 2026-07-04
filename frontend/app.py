import streamlit as st

st.set_page_config(
    page_title="Dynamic Product Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dynamic Product Intelligence Platform")

st.markdown("---")

st.markdown(
"""
Welcome to the **Dynamic Product Intelligence Platform**.

This application allows you to

- 📁 Upload Product Catalog CSV
- 🔍 Search Products using Trie
- ⚡ Instant Product Lookup using HashMap
- 💰 Find Cheapest Products using Min Heap
- 📈 Analyze Product Dataset
"""
)

st.info(
"""
Use the left sidebar to navigate between pages.
"""
)