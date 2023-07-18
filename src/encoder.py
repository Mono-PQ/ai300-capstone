import joblib
import sys 
sys.path.append("../")

class CityEncoder:
    def __init__(self):
        self.city_encoder = joblib.load('artifact/label_encoder_city.pkl')

    def transform(self, input_features):
        return self.city_encoder.transform(input_features)


class ZipcodeEncoder:
    def __init__(self):
        self.zipcode_encoder = joblib.load('artifact/label_encoder_zipcode.pkl')

    def transform(self, input_features):
        return self.zipcode_encoder.transform(input_features)