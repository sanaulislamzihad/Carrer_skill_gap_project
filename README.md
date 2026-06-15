# AI Career Guidance System

An intelligent web-based application that helps university students find their ideal career path by analyzing their technical skills (mapped to specific university courses) and their personality traits.

## 🚀 How to Run the Project

We have added handy batch files for Windows users to start and stop the server with just a double-click!

### **Starting the Server:**
Simply double-click the **`start.bat`** file in the project folder. 
*This will automatically start the Django local server and open the application in your default web browser (http://127.0.0.1:8000).*

### **Stopping the Server:**
Simply double-click the **`stop.bat`** file.
*This will safely close the server process running on port 8000 in the background.*

*(Alternatively, you can manually run `python manage.py runserver` from your terminal or command prompt).*

---

## 🧩 Project Architecture & Connections

This project integrates a **Machine Learning Model** with a **Django Web Framework**. Here is how everything is connected:

### 1. Frontend (UI/UX)
- **Files:** `finalapp/templates/index.html` & `finalapp/templates/result.html`
- **Tech Stack:** HTML5, Tailwind CSS (via CDN)
- **Role:** The frontend provides a modern, dark-themed, glassmorphism UI. In the `index.html` file, users are asked to rate 17 technical domains (which are mapped directly to University Major/Core Courses) and 32 personality trait questions based on the OCEAN model. 

### 2. Backend (Web Framework)
- **Files:** `finalapp/views.py`, `finalapp/urls.py`, `new_project2/settings.py`
- **Tech Stack:** Python, Django
- **Role:** 
  - When the user submits the form, the data is sent to the `predict` function in `views.py`.
  - `views.py` processes the 49 inputs (17 technical, 32 personality).
  - It mathematically aggregates the personality traits into the "Big Five" (OCEAN) features, calculating averages for attributes like Extraversion, Agreeableness, Conscientiousness, etc.
  - It formats this data into a DataFrame matching the model's required input structure.

### 3. Machine Learning Model (Prediction Engine)
- **File:** `finalapp/lr_clf.pkl`
- **Algorithm:** Logistic Regression (`lr_clf`)
- **Role:** 
  - The pre-trained `.pkl` model file is loaded into memory when the Django view is executed.
  - It receives the structured DataFrame of features from `views.py`.
  - It outputs numerical predictions (`scoreval`) and probability scores (`predict_proba`) for 16 different IT/Software career roles (e.g., AI/ML Specialist, Database Administrator, Project Manager, Software Developer).
  - `views.py` sorts these probabilities to find the **Top 3** recommended careers.
  - The results are finally rendered back to the user via the `result.html` template.

---

## 🧠 Model Training & Algorithm Details

The predictive engine of this system is built using **Machine Learning**, specifically the **Logistic Regression** algorithm. 

**Why Logistic Regression?**
Although Logistic Regression is often used for binary classification (Yes/No), this project utilizes its **Multinomial (Multiclass)** capability to categorize students into one of 16 distinct career paths. It calculates the probability of a student belonging to each career category based on their input features and selects the careers with the highest probabilities.

**Training Process:**
1. **Dataset:** The model was trained on a dataset (`dataset9000.csv`) containing records of students' technical ratings (1-7 scale) and their mapped OCEAN personality traits.
2. **Feature Engineering:** The raw personality questionnaire answers are mathematically combined to generate final scores for Openness, Conscientiousness, Extraversion, Agreeableness, and Emotional Range. These, along with 17 technical skill ratings, serve as the input features (X).
3. **Target Variable:** The target variable (y) is the recommended career role (encoded from 0 to 15).
4. **Training:** The dataset was split into training and testing sets. The Logistic Regression model learned the correlations between specific skill/personality combinations and successful career outcomes. 
5. **Serialization:** After achieving satisfactory accuracy, the trained model was exported as a serialized pickle file (`lr_clf.pkl`), allowing the Django application to make real-time predictions instantly without needing to retrain the model.

---

## 🛠️ Step-by-Step Manual Setup (Recommended)

If you are running this for the very first time on a new machine, follow these steps to set up the project manually without using the batch files.

### 1. Prerequisites
Ensure you have **Python 3.8+** installed on your system. You can check your Python version by running:
```bash
python --version
```

### 2. Create a Virtual Environment (Optional but recommended)
It is best practice to create a virtual environment to keep project dependencies isolated. Run this in your terminal:
```bash
python -m venv venv
```
Activate the virtual environment:
- **Windows:**
  ```cmd
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Required Packages
Install all the necessary dependencies (such as Django, Pandas, Scikit-learn, Numpy) from the requirements file using `pip`:
```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations (Optional)
Before running the application, make sure the local SQLite database is fully set up:
```bash
python manage.py migrate
```

### 5. Run the Local Server
Start the Django development server manually:
```bash
python manage.py runserver
```

### 6. Access the Application
Open your web browser and navigate to:
```text
http://127.0.0.1:8000/
```

---

## 🎓 Course Mapping
Instead of retraining the ML model, the 17 technical skill domains required by the model have been intelligently mapped directly to standard university courses. For example:
- **Database Fundamentals** -> CSE 311 & CSE 411
- **Computer Architecture** -> CSE 332 & CSE 433
- **Programming Skills** -> CSE 215, CSE 225, CSE 401
- **AI / ML** -> CSE 440 & CSE 445

This allows students to intuitively rate their skills based on the exact courses they have completed!

---

## 📁 Folder Structure

Here is a quick overview of the project's directory structure and the purpose of each folder/file:

```text
AI-Career-Guidance-System-main/
├── db.sqlite3            # SQLite database file for the Django project
├── manage.py             # Django command-line utility for administrative tasks
├── requirements.txt      # List of Python dependencies required for the project
├── start.bat / stop.bat  # Batch scripts to easily start and stop the local server
├── debug_model.py        # Script used for debugging the machine learning model
├── test_prediction.py    # Script to test the model's prediction functionality
├── assets/               # Contains static assets like images (e.g., background images)
├── Dataset/              # Contains the dataset(s) used for training the model (e.g., dataset9000.csv)
├── finalapp/             # The main Django application folder
│   ├── templates/        # HTML templates for the web interface (homepage, results, etc.)
│   ├── lr_clf.pkl        # The saved/pickled Logistic Regression machine learning model
│   └── ...               # Django app specific files (views.py, models.py, urls.py, etc.)
├── new_project2/         # The core Django project configuration folder (settings.py, urls.py)
├── Notebooks/            # Jupyter notebooks used for data exploration, model training, and analysis
└── Versions/             # Older versions or alternate implementations of the app (e.g., Streamlit versions)
```