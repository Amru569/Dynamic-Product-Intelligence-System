import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/upload"

st.set_page_config(
    page_title="Upload Dataset",
    page_icon="📁",
    layout="wide"
)

st.title("📁 Upload Product Dataset")

st.markdown("---")

st.write(
    "Upload any Product or Inventory CSV file. "
    "The backend automatically maps columns, validates data, "
    "stores it into SQLite, and rebuilds the search indexes."
)

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    st.success(f"Selected File: {uploaded_file.name}")

    if st.button("🚀 Upload Dataset", use_container_width=True):

        with st.spinner("Uploading dataset..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "text/csv"
                )
            }

            try:

                response = requests.post(
                    API_URL,
                    files=files
                )

                if response.status_code == 200:

                    result = response.json()

                    st.success("Dataset uploaded successfully!")

                    col1, col2 = st.columns(2)

                    with col1:

                        st.metric(
                            "Total Records",
                            result["total_records"]
                        )

                        st.metric(
                            "Inserted",
                            result["inserted_records"]
                        )

                    with col2:

                        st.metric(
                            "Cleaned",
                            result["cleaned_records"]
                        )

                        st.metric(
                            "Skipped",
                            result["skipped_records"]
                        )

                    st.balloons()

                else:

                    st.error(response.text)

            except Exception as e:

                st.error(str(e))