# 📊 Dynamic Product Intelligence Platform

A full-stack Product Intelligence Platform built with **FastAPI**, **Streamlit**, **SQLite**, and **Python** that can analyze **any Product or Inventory CSV dataset**.

The platform automatically uploads, validates, stores, indexes, searches, and analyzes product datasets using advanced Data Structures like **Trie**, **HashMap**, and **Min Heap**.

---

# 🚀 Project Overview

Traditional product datasets require manual searching, filtering, and analysis.

This platform automates the entire workflow.

Simply upload any Product/Inventory CSV file and the platform will:

- Automatically detect columns
- Validate and clean the dataset
- Store records into SQLite
- Build in-memory indexes
- Enable lightning-fast searching
- Enable instant product lookup
- Identify cheapest products
- Display interactive analytics dashboards

---

# 🎯 Problem Statement

Organizations receive thousands of product records from suppliers, warehouses, retailers, or marketplaces.

Searching and analyzing these datasets manually is time-consuming.

This project provides a dynamic platform capable of working with **any product/inventory CSV dataset** without requiring code changes.

---

# ✅ What This System Provides

## 1. Dynamic CSV Upload

Upload any Product or Inventory CSV.

Example datasets:

- Grocery Products
- Electronics
- Mobile Phones
- Books
- Furniture
- Pharmacy Products
- Automobile Parts
- Fashion Products
- Warehouse Inventory
- Retail Inventory
- Ecommerce Catalogs

No code modification required.

---

## 2. Automatic Column Mapping

The system automatically detects columns like

- Product Name
- Price
- Brand
- Category
- Stock
- Rating
- Supplier
- Description

Even if uploaded datasets use different column names.

Example

Instead of

```
Product Name
```

it also understands

```
Item Name
Item
Title
Product
Name
```

---

## 3. Data Validation

The platform

- Removes invalid records
- Cleans missing values
- Converts data types
- Handles inconsistent datasets

---

## 4. SQLite Storage

Validated products are stored into SQLite.

Provides persistent storage.

---

## 5. Trie Search Engine

Uses the Trie Data Structure.

Supports

- Prefix Search
- Fast Searching
- Autocomplete

Example

Search

```
ri
```

Returns

```
Rice
Rice Flour
Rice Bran Oil
Rice Vermicelli
```

---

## 6. HashMap Product Lookup

Provides O(1) lookup.

Retrieve complete product details instantly.

---

## 7. Min Heap Price Intelligence

Uses Min Heap to identify

- Cheapest Product
- Top Cheapest Products

without sorting the entire dataset.

---

## 8. Analytics Dashboard

Interactive dashboard built using Streamlit.

Displays

- Total Products
- Average Price
- Lowest Price
- Highest Price
- Category Distribution
- Price Distribution
- Rating Distribution
- Cheapest Products
- Expensive Products

---

# 🧠 Data Structures Used

## Trie

Purpose

Fast Prefix Search

Complexity

Search

O(length of word)

---

## HashMap

Purpose

Instant Product Lookup

Complexity

Lookup

O(1)

---

## Min Heap

Purpose

Cheapest Product Retrieval

Complexity

Cheapest Product

O(1)

Top K Cheapest

O(k log n)

---

# ⚙️ Technology Stack

Backend

- Python
- FastAPI
- SQLAlchemy
- SQLite

Frontend

- Streamlit
- Plotly
- Pandas

Libraries

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

│   ├── index_manager.py

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

## Upload Dataset

```
POST /upload
```

Uploads Product CSV.

---

## Search Products

```
GET /search?q=rice
```

Trie Search.

---

## Product Lookup

```
GET /product?name=BB Royal Idli Rice
```

HashMap Lookup.

---

## Cheapest Product

```
GET /cheapest
```

Returns cheapest product.

---

## Top Cheapest Products

```
GET /top-cheapest?limit=10
```

Returns Top N Cheapest Products.

---

## All Products

```
GET /products
```

Returns all products.

---

# 🖥️ Streamlit Pages

- Home
- Upload Dataset
- Product Search
- Product Lookup
- Cheapest Products
- Analytics Dashboard

---

# ▶️ Installation

Clone Repository

```bash
git clone https://github.com/<YOUR_USERNAME>/dynamic-product-intelligence-platform.git
```

Move into project

```bash
cd dynamic-product-intelligence-platform
```

Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Backend

```bash
uvicorn app.main:app --reload
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Frontend

Open another terminal

```bash
venv\Scripts\activate
```

Run

```bash
streamlit run frontend/app.py
```

Frontend URL

```
http://localhost:8501
```

---

# 📈 Example Workflow

1. Start Backend
2. Start Frontend
3. Upload CSV
4. Search Products
5. Lookup Product
6. Find Cheapest Products
7. Explore Analytics Dashboard

---

# 🔮 Future Improvements

- PostgreSQL Support
- User Authentication
- Price Prediction using Machine Learning
- Product Recommendation System
- Multi-Dataset Comparison
- Export Analytics Reports (PDF/Excel)
- Cloud Deployment (Render/AWS/Azure)

---

# 👨‍💻 Author

Developed using Python, FastAPI, Streamlit, SQLAlchemy, SQLite, Pandas, Plotly, Trie, HashMap, and Min Heap.
