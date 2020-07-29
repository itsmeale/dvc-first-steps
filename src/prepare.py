# -*- coding: utf-8 -*-
import pandas as pd
from pathlib import Path


RAW_DATA_FOLDER = Path("data", "raw")
ITERIM_DATA_FOLDER = Path("data", "iterim")



def preprocesing(df: pd.DataFrame):
    prep_df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin", "Embarked"])
    prep_df = pd.concat([prep_df, pd.get_dummies(prep_df.Sex, drop_first=True)], axis=1)
    prep_df = prep_df.drop(columns=["Sex"])
    return prep_df.dropna()
    

preprocesing(
    pd.read_csv(RAW_DATA_FOLDER.joinpath("train.csv"))
).to_csv(ITERIM_DATA_FOLDER.joinpath("train.csv"), index=False)

preprocesing(
    pd.read_csv(RAW_DATA_FOLDER.joinpath("test.csv"))
).to_csv(ITERIM_DATA_FOLDER.joinpath("test.csv"), index=False)
