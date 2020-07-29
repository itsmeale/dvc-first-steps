# -*- coding: utf-8 -*-
from pathlib import Path

import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

TRAIN_FILE = Path("data", "iterim", "train.csv")
TEST_FILE = Path("data", "iterim", "test.csv")
MODEL_FOLDER = Path("models")
MODEL_NAME = "tree.joblib"


train_df = pd.read_csv(TRAIN_FILE)
test_df = pd.read_csv(TEST_FILE)

X = train_df.iloc[:, 1:].values
y = train_df["Survived"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=42)

classifier = RandomForestClassifier(n_estimators=110)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

print(confusion_matrix(y_test, y_pred))

with open(MODEL_FOLDER.joinpath(MODEL_NAME), "wb") as f:
    pickle.dump(classifier, f)
