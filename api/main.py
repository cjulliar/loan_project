from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from model_utils import load_model, prediction
import pandas as pd

app = FastAPI()

class FeaturesInput(BaseModel):
    State: str 
    Bank: str 
    BankState: str
    Term: int
    NoEmp: int
    NewExist: str
    FranchiseCode: str 
    UrbanRural: str
    RevLineCr: str 
    LowDoc: str 
    GrAppv: int
    SBA_Appv: int 
    Zip2: str 
    NAICS2: str 
    RealEstate: str 

class PredictionOutput(BaseModel):
    category: int

model = load_model()

@app.post('/predict')
def prediction_model(feature_input: FeaturesInput):
    # Création d'un dictionnaire à partir des valeurs de l'objet FeaturesInput
    feature_input_dict = {
        'State': feature_input.State,
        'Bank': feature_input.Bank,
        'BankState': feature_input.BankState,
        'Term': feature_input.Term,
        'NoEmp': feature_input.NoEmp,
        'NewExist': feature_input.NewExist,
        'FranchiseCode': feature_input.FranchiseCode,
        'UrbanRural': feature_input.UrbanRural,
        'RevLineCr': feature_input.RevLineCr,
        'LowDoc': feature_input.LowDoc,
        'GrAppv': feature_input.GrAppv,
        'SBA_Appv': feature_input.SBA_Appv,
        'Zip2': feature_input.Zip2,
        'NAICS2': feature_input.NAICS2,
        'RealEstate': feature_input.RealEstate
    }

    # Création du DataFrame à partir du dictionnaire
    feature_input_df = pd.DataFrame([feature_input_dict])

    # Conversion des types des colonnes
    feature_input_df = feature_input_df.astype({
        'State': 'category',
        'Bank': 'object',
        'BankState': 'category',
        'Term': 'int64',
        'NoEmp': 'int64',
        'NewExist': 'category',
        'FranchiseCode': 'object',
        'UrbanRural': 'category',
        'RevLineCr': 'category',
        'LowDoc': 'category',
        'GrAppv': 'int64',
        'SBA_Appv': 'int64',
        'Zip2': 'category',
        'NAICS2': 'category',
        'RealEstate': 'category'
    })

    # Appel à la fonction de prédiction avec le DataFrame
    pred = prediction(model, feature_input_df)
    
    # Retour de la prédiction sous forme de réponse JSON
    return PredictionOutput(category=pred)
