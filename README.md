# DataVision AI – AI-Powered Data Analyst Web Application

## Overview

DataVision AI is a Flask-based web application that simplifies data analysis.  
It allows users to upload datasets, generate visualizations, and get AI-driven insights.

---

## Features

- User login with session handling
- Upload datasets in CSV or Excel format
- Automatic data processing using Pandas
- Generate charts (bar, line, pie, scatter, histogram)
- AI-generated key insights (5 bullet points)
- Custom chart creation using selected columns
- Chatbot for dataset-related queries
- Display dataset fields dynamically

---

## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Flask (Python)

### Data Processing
- Pandas

### Visualization
- Matplotlib

### AI Integration
- Ollama (Local LLM)
- project/
│── app.py
│── data_analyzer.py
│── ollama_helper.py
│
├── templates/
│ ├── home.html
│ ├── login.html
│ └── upload.html
│
├── static/
│ ├── style.css
│ ├── script.js
│ └── charts/
│
├── uploads/
│
└── requirements.txt


---

## Workflow

- User logs in
- Uploads dataset (CSV or Excel)
- Backend processes data using Pandas
- Charts are generated using Matplotlib
- AI generates insights using Ollama
- Dashboard displays results
- User creates custom charts
- Chatbot answers dataset queries

---

## AI Functionality

- Prompt-based insight generation
- Context-aware responses using dataset preview
- Conversational chatbot interface
- Controlled output formatting

---

## Supported Charts

- Bar Chart
- Line Chart
- Pie Chart
- Scatter Plot
- Histogram



## Author

Gopika

---

