from flask import Flask, request, render_template
from model import Model
from encoder import CityEncoder, ZipcodeEncoder
from mapper import Mapper
import pandas as pd



app = Flask(__name__)

# Load dataset for form list generation and validation
df = pd.read_csv('static/customer_churn_v0.csv')


# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST'])
def home():
    cities = list(df['city_name'].sort_values().unique()) 
    zipcodes = list(df['zip_code'].sort_values().unique())
    if request.method == 'POST':
        form_input = dict(request.form)
        print(form_input)

        tenure = int(form_input['tenure'])
        referrals = int(form_input['referrals'])
        internet = int(form_input['internet'])
        internet_type = int(form_input['internet-type'])
        unlimited_data = int(form_input['unlimited-data'])
        phone_service = int(form_input['phone-service'])
        multiple_lines = int(form_input['multiple-lines'])
        premium_support = int(form_input['premium-support'])
        online_security = int(form_input['online-security'])
        online_backup = int(form_input['online-backup'])
        device_protection = int(form_input['device-protection'])
        contract_type = int(form_input['contract-type'])
        paperless_billing = int(form_input['paperless-billing'])
        payment_method = int(form_input['payment-method'])
        longdistance_fee = float(form_input['long-distance-fee'])
        stream_tv = int(form_input['stream-tv'])
        stream_movie = int(form_input['stream-movie'])
        stream_music = int(form_input['stream-music'])
        monthly_fee = float(form_input['monthly-fee'])
        gender = int(form_input['gender'])
        senior = int(form_input['senior'])
        married = int(form_input['married'])
        dependents = int(form_input['dependents'])
        zipcode = ZipcodeEncoder().transform([form_input['zipcodes']])[0]
        city = CityEncoder().transform([form_input['cities']])[0]

        model_inputs = [tenure, referrals, internet, internet_type, unlimited_data, phone_service, multiple_lines, premium_support,
                        online_security, online_backup, device_protection, contract_type, paperless_billing, payment_method, longdistance_fee,
                        stream_tv, stream_movie, stream_music, monthly_fee, gender, senior, married, dependents, zipcode, city]
        prediction = Model().predict(model_inputs)
        
        if prediction == 0:
            result = "Customer is not likely to churn. No intervention is required."
        else: 
            result = "Customer is likely to churn. Intervention is required for the customer."
        return render_template('index.html', cities=cities, zipcodes=zipcodes, prediction=result)

    return render_template('index.html', cities=cities, zipcodes=zipcodes)


# Method 2: Via POST API
@app.route('/api/predict', methods=['POST'])
def predict():
    request_data = request.get_json()
    print(request_data)

    tenure = int(request_data['tenure'])
    referrals = int(request_data['referrals'])
    internet = Mapper().map_binary(request_data['internet'])
    internet_type = Mapper().map_internet(request_data['internet-type'])
    unlimited_data = Mapper().map_binary(request_data['unlimited-data'])
    phone_service = Mapper().map_binary(request_data['phone-service'])
    multiple_lines = Mapper().map_binary(request_data['multiple-lines'])
    premium_support = Mapper().map_binary(request_data['premium-support'])
    online_security = Mapper().map_binary(request_data['online-security'])
    online_backup = Mapper().map_binary(request_data['online-backup'])
    device_protection = Mapper().map_binary(request_data['device-protection'])
    contract_type = Mapper().map_contract(request_data['contract-type'])
    paperless_billing = Mapper().map_binary(request_data['paperless-billing'])
    payment_method = Mapper().map_payment(request_data['payment-method'])
    longdistance_fee = float(request_data['long-distance-fee'])
    stream_tv = Mapper().map_binary(request_data['stream-tv'])
    stream_movie = Mapper().map_binary(request_data['stream-movie'])
    stream_music = Mapper().map_binary(request_data['stream-music'])
    monthly_fee = float(request_data['monthly-fee'])
    gender = Mapper().map_gender(request_data['gender'])
    senior = Mapper().map_binary(request_data['senior'])
    married = Mapper().map_binary(request_data['married'])
    dependents = int(request_data['dependents'])
    zipcode = ZipcodeEncoder().transform([request_data['zipcode']])[0]
    city = CityEncoder().transform([request_data['city']])[0]

    model_inputs = [tenure, referrals, internet, internet_type, unlimited_data, phone_service, multiple_lines, premium_support,
                    online_security, online_backup, device_protection, contract_type, paperless_billing, payment_method, longdistance_fee,
                    stream_tv, stream_movie, stream_music, monthly_fee, gender, senior, married, dependents, zipcode, city]
    prediction = Model().predict(model_inputs)

    if prediction == 0:
            result = "Customer is not likely to churn. No intervention is required."
    else: 
        result = "Customer is likely to churn. Intervention is required for the customer."
    return {'prediction': result}

@app.route('/doc')
def doc():
    return render_template('doc.html')

if __name__ == '__main__':
    app.run()