class Mapper:
    def __init__(self):
        None
    
    def map_binary(self, input_feature):
        values = {"no": 0, "yes":1}
        input_feature = input_feature.lower()
        return values[input_feature] 
    
    def map_gender(self, input_feature):
        values = {"male": 0, "female": 1}
        input_feature = input_feature.lower()
        return values[input_feature] 
    
    def map_contract(self, input_feature):
        values = {"month-to-month": 0, "one year": 1, "two year": 2}
        input_feature = input_feature.lower()
        return values[input_feature] 
    
    def map_payment(self, input_feature):
        values = {"bank withdrawal": 0, "credit card": 1, "mailed check": 2}
        input_feature = input_feature.lower()
        return values[input_feature] 
    
    def map_internet(self, input_feature):
        values = {"none": 0, "fiber optic": 1, "dsl": 2, "cable": 3}
        input_feature = input_feature.lower() 
        return values[input_feature] 