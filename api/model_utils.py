from joblib import load

def load_model(path='./model_cb.pkl'):
    model = load(path)
    return model

def prediction(model, data):
    predictions = model.predict(data)
    return predictions
