import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new_project2.settings')
django.setup()

import pickle
import pandas as pd

pickle_file_path = 'finalapp/lr_clf.pkl'
with open(pickle_file_path, 'rb') as f:
    model = pickle.load(f)

# Create test data with all required features in the right order
test_features = {
    'Database Fundamentals': 3,
    'Computer Architecture': 3,
    'Distributed Computing Systems': 3,
    'Cyber Security': 3,
    'Networking': 3,
    'Software Development': 3,
    'Programming Skills': 3,
    'Project Management': 3,
    'Computer Forensics Fundamentals': 3,
    'Technical Communication': 3,
    'AI ML': 3,
    'Software Engineering': 3,
    'Business Analysis': 3,
    'Communication skills': 3,
    'Data Science': 3,
    'Troubleshooting skills': 3,
    'Graphics Designing': 3,
    'Openness': 4,
    'Conscientousness': 4,  # Note the misspelling
    'Extraversion': 4,
    'Agreeableness': 4,
    'Emotional_Range': 4,
    'Conversation': 4,
    'Openness to Change': 4,
    'Hedonism': 4,
    'Self-enhancement': 4,
    'Self-transcendence': 4,
}

testdata = pd.DataFrame(test_features, index=[0])
print("Features in testdata:")
print(list(testdata.columns))
print("\nModel expects:")
print(list(model.feature_names_in_))
print("\nMatches:", list(testdata.columns) == list(model.feature_names_in_))

# Try prediction
try:
    pred = model.predict(testdata)
    print(f"\nPrediction successful: {pred}")
    proba = model.predict_proba(testdata)
    print(f"Prediction probabilities shape: {proba.shape}")
except Exception as e:
    print(f"\nPrediction failed: {e}")
