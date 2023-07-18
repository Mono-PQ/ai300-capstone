import requests

url = 'http://13.213.40.73/api/predict'

model_inputs = {
                    "tenure": "3",
                    "referrals": "3",
                    "internet": "Yes",
                    "internet-type": "Fiber Optic", 
                    "unlimited-data": "Yes",
                    "phone-service": "Yes",
                    "multiple-lines": "No", 
                    "premium-support": "Yes",
                    "online-security": "No", 
                    "online-backup": "No",
                    "device-protection": "No", 
                    "contract-type": "Month-to-Month",
                    "paperless-billing": "Yes",
                    "payment-method": "Credit Card",
                    "long-distance-fee": "22.14",
                    "stream-tv": "Yes", 
                    "stream-movie": "No",
                    "stream-music": "No",
                    "monthly-fee": "80.90",
                    "gender": "Female",
                    "senior": "Yes",
                    "married": "No",
                    "dependents": "0",
                    "zipcode": "93010",
                    "city": "Camarillo"
                  } 

response = requests.post(url, json=model_inputs)
print(f"Response: {response}")
print(f"Content: {response.text}")