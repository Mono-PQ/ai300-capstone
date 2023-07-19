import joblib
import sys
sys.path.append("../")

class Model:
    def __init__(self):
        self.model = joblib.load('../artifact/catboost_model.pkl')

    def predict(self, input_features):
        return self.model.predict(input_features)
