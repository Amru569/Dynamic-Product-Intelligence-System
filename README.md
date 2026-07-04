# 📊 Dynamic Product & Inventory Catalog Intelligence Platform

A full-stack **Product & Inventory Catalog Intelligence Platform** built with **FastAPI**, **Streamlit**, **SQLite**, and **Python**.

The platform allows users to upload supported **Product Catalog CSV datasets**, automatically validate and store the data, build efficient in-memory indexes using **Trie**, **HashMap**, and **Min Heap**, and interactively search and analyze products through a modern Streamlit dashboard.

---

# 🚀 Overview

Product catalogs are widely used in retail, e-commerce, warehouses, and inventory management. Searching and analyzing large catalogs manually is time-consuming.

This platform automates the process by providing:

- CSV Upload
- Automatic Column Mapping
- Data Validation
- SQLite Storage
- Trie-based Product Search
- HashMap-based Product Lookup
- Min Heap Price Intelligence
- Interactive Analytics Dashboard

---

# 🎯 Problem Statement

Organizations frequently work with product catalogs received from suppliers, retailers, warehouses, or e-commerce platforms.

Finding products, comparing prices, and analyzing catalog information manually becomes inefficient as datasets grow larger.

This project provides an intelligent backend and dashboard for efficiently managing and exploring product catalog datasets.

---

# ✨ Features

## 📁 Dynamic CSV Upload

Upload supported Product Catalog CSV files directly from the Streamlit interface.

After upload, the platform automatically:

- Reads the CSV
- Maps supported column names
- Cleans and validates the dataset
- Stores data into SQLite
- Builds in-memory indexes

---

## 🔄 Automatic Column Mapping

Different datasets use different column names.

The platform automatically recognizes supported alternatives.

### Product Name

- product
- product_name
- item
- item_name
- name
- title

### Price

- price
- sale_price
- selling_price
- cost
- mrp
- market_price
- unit_price

### Brand

- brand
- company
- manufacturer

### Category

- category
- group
- department

### Stock

- stock
- inventory
- quantity

### Rating

- rating
- stars
- review

### Supplier

- supplier
- vendor

### Description

- description
- details

---

## ✅ Data Validation

Before storing data, the platform validates the uploaded dataset.

Validation includes:

- Required column checking
- Missing value handling
- Data type conversion
- Invalid record removal
- Dataset cleaning

---

## 💾 SQLite Storage

Validated records are stored in SQLite.

This allows persistent storage and fast retrieval.

---

## 🔍 Trie Search Engine

Product searching is implemented using the **Trie Data Structure**.

Supports:

- Prefix Search
- Fast Searching
- Auto-complete style suggestions

Example

Search:

```
ri
```

Results:

```
Rice
Rice Flour
Rice Bran Oil
Rice Vermicelli
```

---

## ⚡ HashMap Product Lookup

Uses a **HashMap** for constant-time product retrieval.

Returns product information including:

- Product Name
- Brand
- Category
- Supplier
- Price
- Rating
- Stock
- Description

---

## 💰 Min Heap Price Intelligence

Uses a **Min Heap** to efficiently retrieve:

- Cheapest Product
- Top Cheapest Products

without sorting the complete dataset every time.

---

## 📈 Analytics Dashboard

Interactive dashboard built with Streamlit and Plotly.

Displays:

- Total Products
- Average Price
- Lowest Price
- Highest Price
- Category Distribution
- Price Distribution
- Rating Distribution
- Cheapest Products
- Most Expensive Products

---

# 📂 Supported Dataset Types

The platform is designed for **Product & Inventory Catalog datasets**.

Examples include:

- Grocery Product Catalog
- Electronics Catalog
- Mobile Phone Catalog
- Book Catalog
- Furniture Catalog
- Pharmacy Product Catalog
- Fashion Product Catalog
- Retail Product Catalog
- Warehouse Product Catalog
- E-commerce Product Listings

---

# ⚠ Dataset Requirements

The uploaded CSV **must contain**:

## Required Columns

| Column | Description |
|---------|-------------|
| Product Name (or supported equivalent) | Searchable product identifier |
| Price (or supported equivalent) | Product selling price |

## Optional Columns

- Brand
- Category
- Stock
- Rating
- Supplier
- Description

> **Note:** Datasets that contain only Product IDs without a searchable product name are **not supported** in the current version.

---

# 🧠 Data Structures Used

## Trie

Purpose

- Prefix Search
- Product Search

Complexity

```
Search → O(length of prefix)
```

---

## HashMap

Purpose

- Product Lookup

Complexity

```
Lookup → O(1)
```

---

## Min Heap

Purpose

- Cheapest Product Retrieval

Complexity

```
Cheapest Product → O(1)

Top K Cheapest → O(k log n)
```

---

# 🛠 Technology Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- SQLite

## Frontend

- Streamlit
- Plotly
- Pandas

## Libraries

- Requests
- Heapq
- Python Multipart

---

# 📂 Project Structure

```
dynamic-product-intelligence-platform/

│

├── app/

│   ├── main.py

│   ├── routes.py

│   ├── services.py

│   ├── models.py

│   ├── database.py

│   ├── loader.py

│   ├── mapper.py

│   ├── validator.py

│   ├── trie.py

│   ├── hashmap.py

│   ├── heap.py

│   ├── search.py

│   ├── lookup.py

│   ├── compare.py

│   ├── product_index.py

│   └── index_manager.py

│

├── frontend/

│   ├── app.py

│   ├── utils.py

│   └── pages/

│       ├── 1_Upload_Dataset.py

│       ├── 2_Product_Search.py

│       ├── 3_Product_Lookup.py

│       ├── 4_Cheapest_Products.py

│       └── 5_Dashboard.py

│

├── database/

├── data/

├── requirements.txt

├── README.md

└── .gitignore
```

---

# 🌐 REST APIs

| Method | Endpoint | Description |
|----------|-----------|-------------------------------|
| POST | `/upload` | Upload Product Catalog |
| GET | `/search?q=rice` | Trie Product Search |
| GET | `/product?name=Rice` | Product Lookup |
| GET | `/cheapest` | Cheapest Product |
| GET | `/top-cheapest?limit=10` | Top Cheapest Products |
| GET | `/products` | Retrieve All Products |

---

# 🖥 Streamlit Pages

- Home
- Upload Dataset
- Product Search
- Product Lookup
- Cheapest Products
- Analytics Dashboard

---

# ▶ Installation

Clone Repository

```bash
git clone https://github.com/<YOUR_USERNAME>/dynamic-product-intelligence-platform.git
```

Move into the project

```bash
cd dynamic-product-intelligence-platform
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Run Backend

```bash
uvicorn app.main:app --reload
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# ▶ Run Frontend

Open another terminal.

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

Run Streamlit

```bash
streamlit run frontend/app.py
```

Frontend

```
http://localhost:8501
```

---

# 📸 Application Workflow

1. Start FastAPI backend
2. Start Streamlit frontend
3. Upload a supported Product Catalog CSV
4. Search products using Trie
5. Lookup product information using HashMap
6. Find cheapest products using Min Heap
7. Explore analytics through the dashboard

---

# 🚀 Future Enhancements

- PostgreSQL Support
- User Authentication
- Product Recommendation Engine
- Price Trend Prediction
- Machine Learning Models
- Export Reports (PDF / Excel)
- Cloud Deployment (AWS / Azure / Render)

---

# 👨‍💻 Author

Developed using **Python**, **FastAPI**, **Streamlit**, **SQLite**, **SQLAlchemy**, **Pandas**, **Plotly**, **Trie**, **HashMap**, and **Min Heap**.
