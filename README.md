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

## 🛠️ Required Setup

If you are running this for the very first time on a new machine, make sure you install the required dependencies:

```bash
pip install -r requirements.txt
```
*(Common dependencies include: Django, pandas, scikit-learn, numpy)*

---

## 🎓 Course Mapping
Instead of retraining the ML model, the 17 technical skill domains required by the model have been intelligently mapped directly to standard university courses. For example:
- **Database Fundamentals** -> CSE 311 & CSE 411
- **Computer Architecture** -> CSE 332 & CSE 433
- **Programming Skills** -> CSE 215, CSE 225, CSE 401
- **AI / ML** -> CSE 440 & CSE 445

This allows students to intuitively rate their skills based on the exact courses they have completed!