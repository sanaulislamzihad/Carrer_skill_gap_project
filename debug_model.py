import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new_project2.settings')
django.setup()

import pickle
from pathlib import Path

pickle_file_path = Path('finalapp') / 'lr_clf.pkl'
print(f'Pickle file exists: {pickle_file_path.exists()}')

if pickle_file_path.exists():
    with open(pickle_file_path, 'rb') as f:
        model = pickle.load(f)
    print(f'Model type: {type(model)}')
    print(f'Number of features: {model.n_features_in_}')
    print(f'Feature names in: {model.feature_names_in_}')
    print(f'Classes: {model.classes_}')
