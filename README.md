DataVision AI – AI-Powered Data Analyst Web Application
Overview

DataVision AI is a Flask-based web application designed to simplify data analysis for users without requiring technical expertise. The system allows users to upload datasets, automatically generates visualizations, and provides AI-driven insights along with an interactive chatbot.

Features
User login with session handling
Upload datasets in CSV or Excel format
Automatic data processing using Pandas
Generation of multiple charts (bar, line, pie, scatter, histogram)
AI-generated key insights in structured bullet format
Custom chart creation by selecting columns and chart types
Interactive chatbot for querying dataset information
Display of dataset fields and structure
Tech Stack
Frontend
HTML
CSS
JavaScript
Backend
Flask (Python)
Data Processing
Pandas
Visualization
Matplotlib
AI Integration
Ollama (Local LLM)
Project Structure
project/
│── app.py
│── data_analyzer.py
│── ollama_helper.py
│
├── templates/
│   ├── home.html
│   ├── login.html
│   └── upload.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── charts/
│
├── uploads/
│
└── requirements.txt
Installation and Setup
Clone the repository
git clone https://github.com/your-username/datavision-ai.git
cd datavision-ai
Install dependencies
pip install -r requirements.txt
Run Ollama
ollama run llama3
Run the application
python app.py
Open in browser
http://127.0.0.1:5000
Workflow
User logs in to the system
Uploads dataset (CSV or Excel)
Backend processes data using Pandas
Charts are generated using Matplotlib
AI generates insights using Ollama
Dashboard displays insights, charts, and dataset fields
User can create custom charts
Chatbot answers queries related to the dataset
AI Functionality
Prompt-based insight generation
Context-aware responses using dataset preview
Conversational chatbot interface
Structured output control using prompt engineering
Supported Charts
Bar Chart
Line Chart
Pie Chart
Scatter Plot
Histogram

Author

Gopika
AI and Data Analytics Enthusiast
