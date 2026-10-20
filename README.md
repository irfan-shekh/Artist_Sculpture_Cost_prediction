<div align="center">

# 🏛️ SculptPrice AI — Artist Sculpture Cost Prediction

**A production-ready Django & Machine Learning web application predicting fair market valuation and total procurement costs for custom artist sculptures using Random Forest Regression.**

[![Python](https://img.shields.io/badge/Python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![R2 Accuracy](https://img.shields.io/badge/Test_R²_Accuracy-84.23%25-10B981?style=for-the-badge&logo=target&logoColor=white)](#-model-architecture--performance)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

[Quick Start](#-quick-start) • [Features](#-key-features) • [ML Architecture](#-model-architecture--performance) • [Project Structure](#-project-structure) • [Running the App](#-running-the-application) • [Testing](#-testing--validation)

</div>

---

## 🌟 Overview

Pricing custom sculptures and fine artwork is intricate; it requires balancing artist prestige, raw material density, physical dimensions, transit fragility, international tariffs, and specialized installation logistics. 

**SculptPrice AI** solves this challenge by leveraging an ensemble **Random Forest Regressor (200 estimators)** trained on historical art acquisition data to accurately forecast total acquisition costs with **84.2% test R² accuracy**.

The application features a luxury art gallery glassmorphic dark interface with real-time field validation, progress indicators, 1-click curated sculpture presets, and asynchronous AJAX predictions.

---

## ✨ Key Features

- **🎯 Machine Learning Valuation**: Trained Random Forest ensemble analyzing 15 distinct dimensions, material densities, and logistical factors.
- **🎨 Luxury Gallery Dark UI**: Custom obsidian & gold glassmorphic design (`Outfit` & `Cinzel` typography), responsive grid, and subtle micro-animations.
- **⚡ Zero-Reload AJAX Predictions**: Asynchronous in-place cost evaluation with loading state and smooth auto-scroll.
- **🪄 1-Click Curated Presets**: Instantly populate and test with predefined sculpture archetypes:
  - 🥉 *Bronze Masterpiece* (Classic high-value bronze casting with express air delivery)
  - 🏛️ *Marble Monument* (Heavyweight marble sculpture requiring specialized installation)
  - 🪵 *Woodwork Carving* (Contemporary domestic wooden carving)
- **📊 Real-time Progress Tracking**: Live visual completion bar (`0 to 15 Specified`) and dynamic input status dots.
- **📁 Multi-Path Execution**: Run seamlessly from the project root (`python app.py`, `python manage.py runserver`, or `run.bat`) or directly from the inner Django folder.

---

## 🚀 Quick Start

### 1. Prerequisites
- **Python 3.8+** (Fully compatible with Python 3.8 through 3.13)
- **pip** package installer

### 2. Clone / Open the Project
```bash
cd "Artist Sculpture Cost prediction"
```

### 3. Create & Activate Virtual Environment (Recommended)
```bash
# Initialize virtual environment
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on macOS / Linux:
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 💻 Running the Application

You can start the application using any of the following convenient options from the project root:

### Option A: Quick Application Runner (Recommended)
```bash
python app.py
```
*Optional custom port:* `python app.py 8080`

### Option B: Standard Django Management Command
```bash
python manage.py runserver
```

### Option C: 1-Click Windows Launcher
Double-click `run.bat` or run:
```cmd
run.bat
```

### Option D: From the Django Subdirectory
```bash
cd mysite
python manage.py runserver
```

Once started, open your web browser and navigate to:
👉 **`http://127.0.0.1:8000`**

---

## 📊 Model Architecture & Performance

```
┌────────────────────────────────────────────────────────┐
│               15 Multi-Domain Features                 │
│  (Artist Reputation, Height, Width, Weight, Material,  │
│   Base Price, Shipping, Transport, Fragility, etc.)    │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│          Categorical LabelEncoder & Cleaning           │
│     (Outlier bounding, DateTime Delta Extraction)      │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│             Random Forest Regressor (Ensemble)         │
│          (200 Estimators, Max Depth, Random 42)        │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│          Predicted Total Sculpture Cost ($ USD)        │
└────────────────────────────────────────────────────────┘
```

### Evaluated Attributes (15 Features)

| Category | Features Evaluated | Description & Values |
| :--- | :--- | :--- |
| **Artist Profile** | `Artist Name`, `Artist Reputation` | Scaled artist prestige metric (0.00 – 1.00) |
| **Physical Dimensions** | `Height`, `Width`, `Weight` | Height (m), Width (m), Mass in grams |
| **Medium & Baseline** | `Material`, `Price Of Sculpture`, `Base Shipping Price` | Aluminium, Brass, Bronze, Clay, Marble, Stone, Wood |
| **Freight Logistics** | `Transport Mode`, `International`, `Express Shipment` | Airways, Roadways, Waterways; Priority handling |
| **Specialized Handling**| `Fragile`, `Installation Included` | Fragility classification & on-site assembly |
| **Client & Location** | `Customer Information`, `Remote Location`, `Waiting time` | Wealthy vs Working Class; Remote transit days |

### Model Metrics
- **Dataset Size**: 2,765 verified sculpture transactions
- **Algorithm**: Random Forest Regressor (200 trees, parallel jobs)
- **Training R² Score**: `97.63%`
- **Testing R² Score (20% holdout)**: `84.23%`
- **Inference Latency**: `< 15ms`

---

## 📁 Project Structure

```
Artist Sculpture Cost prediction/
│
├── manage.py                    # Root Django management entry point
├── app.py                       # Root application runner & CLI test suite
├── test_models.py               # Automated ML model validation script
├── run.bat                      # 1-click Windows batch launcher
├── requirements.txt             # Python project dependencies
├── README.md                    # Project documentation
│
├── Artist Sculpture Cost.csv    # Historical training dataset
├── ArtistSculpture.ipynb        # EDA, Outlier Analysis & Model Training
│
└── mysite/                      # Django project core
    ├── manage.py                # Subdirectory Django script
    ├── requirements.txt         # Pinned dependency specifications
    ├── db.sqlite3               # SQLite database
    ├── mysite/                  # Django project configuration
    │   ├── settings.py          # App settings & static configuration
    │   ├── urls.py              # Main URL routing
    │   ├── wsgi.py              # WSGI entry point
    │   └── asgi.py              # ASGI entry point
    ├── static/                  # Static assets directory
    └── polls/                   # Cost prediction application
        ├── views.py             # Prediction handler & AJAX JSON API
        ├── urls.py              # App routes
        ├── Artist.pickle        # Trained Random Forest Regressor model
        └── templates/
            └── index.html       # Glassmorphic responsive frontend
```

---

## 🧪 Testing & Validation

The project includes an automated test script verifying model serialization, input vector compatibility, and valuation calculations.

### Run Tests via Root Test Runner
```bash
python test_models.py
```

### Or Run via `app.py`
```bash
python app.py test
```

**Expected Output:**
```text
🎨 Testing Artist Sculpture Cost Prediction ML Model
=======================================================
✅ Model file located: .../mysite/polls/Artist.pickle
✅ Model successfully loaded into memory

🧪 Input Features Shape: (1, 15)
💰 Predicted Sculpture Total Cost: $3,405.60 USD

✅ All model tests completed successfully!
```

---

## 🛠 Tech Stack

- **Backend Framework**: [Django 4.2+ / 5.x](https://www.djangoproject.com/)
- **Machine Learning**: [scikit-learn](https://scikit-learn.org/), [pandas](https://pandas.pydata.org/), [numpy](https://numpy.org/)
- **Frontend**: Vanilla HTML5, CSS3 Glassmorphism, Modern JavaScript (ES6+ Fetch API)
- **Typography & Icons**: [Google Fonts (Cinzel, Outfit, Plus Jakarta Sans)](https://fonts.google.com/), [Font Awesome 6](https://fontawesome.com/)
- **Production Server**: [Gunicorn](https://gunicorn.org/) / WSGI

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
