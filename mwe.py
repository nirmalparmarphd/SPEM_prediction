from module import *

# enter data for ['Day','Max_T[C]','Min_T[C]', 'RH(%)', 'WS(mps)','Density(Be)']

data = [3.0,37.7,21.9,37.0,3.8,5.7]

# Sea water eveporation prediction as per weather data to prodduce salt
prediction = sw_prediction(data)

# Sea water eveporation prediction with SPEM
prediction = spem_prediction(data)
