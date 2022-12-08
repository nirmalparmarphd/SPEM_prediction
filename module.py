# Module code to predict salt production in Bhavnagar salt farm, Gujarat, India

# import load model
from tensorflow.keras.models import load_model
import joblib
import pandas as pd

# prediction with model for sea water natural condition and eveporation 
class sw_prediction:
    def __init__(self,input_data):
        input_data = pd.DataFrame([input_data])
        print(input_data)
        model = load_model('sw_model.h5')
        scaler = joblib.load('sw_scaler.pkl')
        input_data_scaled = scaler.transform(input_data)
        prediction = model.predict(input_data_scaled)
        prediction_df = pd.DataFrame(prediction)
        result = pd.concat([input_data,prediction_df], axis =1, ignore_index=True)
        line = '-'*60
        result.columns = ['Date April','Max_T','Min_T', 'RH(%)', 'WS(mps)','Den(Be)','Eveporatoin Prediction (mm)']
        print(line)
        info = ''' Sea water eveporation prediction by ANN (Artifical Neural Network)
        as per weather data collected at the Salt Farm, Bhavnagar, Gujarat.
        '''
        print(info)
        print(line)
        print(result)
        print(line)