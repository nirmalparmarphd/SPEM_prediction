# Module code to predict salt production in Bhavnagar salt farm, Gujarat, India

# import load model
from tensorflow.keras.models import load_model
import joblib
import pandas as pd

# prediction with model for sea water natural condition and eveporation 
class sw_prediction:
    def __init__(self,input_data):
        input_data = pd.DataFrame([input_data])
        model = load_model('sw_model.h5')
        scaler = joblib.load('sw_scaler.pkl')
        input_data_scaled = scaler.transform(input_data)
        prediction = model.predict(input_data_scaled)
        prediction_df = pd.DataFrame(prediction)
        result = pd.concat([input_data,prediction_df], axis =1, ignore_index=True)
        line = '-'*70
        result.columns = ['Day','Max_T[C]','Min_T[C]', 'RH(%)', 'WS(mps)','Density(Be)','Eveporatoin Prediction (mm)']
        print(line)
        info = ''' Sea water eveporation prediction by ANN (Artifical Neural Network)
        as per weather data collected at the Salt Farm, Bhavnagar, Gujarat.
        '''
        print(info)
        print(line)
        print(result)
        print(line)
        
class spem_prediction:
    def __init__(self,input_data):
        input_data = pd.DataFrame([input_data])
        model = load_model('spem_model.h5')
        scaler = joblib.load('spem_scaler.pkl')
        input_data_scaled = scaler.transform(input_data)
        prediction = model.predict(input_data_scaled)
        prediction_df = pd.DataFrame(prediction)
        result = pd.concat([input_data,prediction_df], axis =1, ignore_index=True)
        line = '-'*70
        result.columns = ['Day','Max_T[C]','Min_T[C]', 'RH(%)', 'WS(mps)','Density(Be)','SPEM - Eveporatoin Prediction (mm)']
        print(line)
        info = ''' Sea water eveporation prediction with intigration of SPEM (Salt Production Enhancement Method) by ANN (Artifical Neural Network) as per weather data collected at the Salt Farm, Bhavnagar, Gujarat.
        '''
        print(info)
        print(line)
        print(result)
        print(line)
        
        