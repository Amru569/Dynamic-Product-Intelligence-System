# Dynamic Product Intelligence Platform

## Overview

A full-stack product analytics platform built using FastAPI and Streamlit.

Supports

• Dynamic CSV Upload
• Automatic Column Mapping
• Data Validation
• Trie Search
• HashMap Lookup
• Min Heap Price Intelligence
• Analytics Dashboard

## Tech Stack

Python
FastAPI
Streamlit
SQLite
SQLAlchemy
Pandas
Plotly

## Data Structures

Trie
HashMap
Min Heap

## APIs

POST /upload
GET /search
GET /product
GET /cheapest
GET /top-cheapest
GET /products

## Run

Backend

uvicorn app.main:app

Frontend

streamlit run frontend/app.py