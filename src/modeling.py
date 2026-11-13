import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.metrics import make_scorer, f1_score, precision_score, recall_score, roc_auc_score

FEATURES = ["s01a_03","s01a_02","depto","area"]
CAT = ["s01a_02","depto","area"]
NUM = ["s01a_03"]

def compare_models(df, target):
    d = df[FEATURES + [target]].dropna(subset=[target]).copy()
    X, y = d[FEATURES], d[target].astype(int)
    prep = ColumnTransformer([
        ("cat", Pipeline([("impute", SimpleImputer(strategy="most_frequent")),
                          ("ohe", OneHotEncoder(handle_unknown="ignore"))]), CAT),
        ("num", SimpleImputer(strategy="median"), NUM)
    ])
    models = {
        "RandomForest": RandomForestClassifier(n_estimators=300, min_samples_leaf=4,
            class_weight="balanced", random_state=42, n_jobs=-1),
        "ExtraTrees": ExtraTreesClassifier(n_estimators=300, min_samples_leaf=4,
            class_weight="balanced", random_state=42, n_jobs=-1)
    }
    try:
        from xgboost import XGBClassifier
        models["XGBoost"] = XGBClassifier(n_estimators=250, max_depth=3, learning_rate=0.04,
            subsample=0.85, colsample_bytree=0.85, eval_metric="logloss",
            random_state=42, n_jobs=-1)
    except Exception:
        pass
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scoring = {"f1":"f1", "precision":"precision", "recall":"recall",
               "roc_auc":"roc_auc", "balanced_accuracy":"balanced_accuracy"}
    rows = []
    for name, clf in models.items():
        pipe = Pipeline([("prep", prep), ("model", clf)])
        scores = cross_validate(pipe, X, y, cv=cv, scoring=scoring, n_jobs=-1)
        rows.append({"modelo":name, **{f"{k}_media":scores[f"test_{k}"].mean()
                     for k in scoring}, **{f"{k}_sd":scores[f"test_{k}"].std()
                     for k in scoring}})
    return pd.DataFrame(rows).sort_values("f1_media", ascending=False)
