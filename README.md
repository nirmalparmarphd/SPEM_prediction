# SPEM_prediction
Salt Production Enhancement Method (SPEM): Machine and Deep Learning data-driven solution to predict the salt production

> The project is in development stage. The ANN model will be re-trained with 2023 data.

# Research Work Collaboration
This resesach work was carried out with collbration of Nirmal Parmar (Data Drive Solution & Deep Learning; Research Scientist at ICPF, Prague, CZ) and Bipin Vyas (Experimental Work; Scientist at CSMCRI, CSIR, India).
The first aim of the research work is to conduct an experiment with the SPEM method and collect data. The second aim was to find a data-driven solution to predict salt production in different weather conditions in Bhavnagar, Gujarat, India.

# MWE (Minimum Working Example)
Please use mwe.py file to predict the sea water eveporation as a function of weather parametrs or/and with the SPEM method integration.


## Sea Water Eveporation Prediction MWE

```python:
from module import *

# enter data for ['Day','Max_T[C]','Min_T[C]', 'RH(%)', 'WS(mps)','Density(Be)']

data = [3.0,37.7,21.9,37.0,3.8,5.7]

# Sea water eveporation prediction as per weather data without SPEM
prediction = sw_prediction(data)

# Sea water eveporation prediction as per weather data with SPEM
prediction = spem_prediction(data)
```
Example Output for Sea Water

```python:
1/1 [==============================] - 0s 125ms/step
----------------------------------------------------------------------
 Sea water eveporation prediction by ANN (Artifical Neural Network)
 as per the weather data collected at the Salt Farm, Bhavnagar, Gujarat.

----------------------------------------------------------------------
   Day  Max_T[C]  Min_T[C]  RH(%)  WS(mps)  Density(Be)  Eveporatoin Prediction (mm)
0  3.0      37.7      21.9   37.0      3.8          5.7                      4.01898
----------------------------------------------------------------------
```

Example Output of Sea Water Eveporation with SPEM
```python:
1/1 [==============================] - 0s 72ms/step
----------------------------------------------------------------------
 Sea water eveporation prediction with intigration of SPEM (Salt Production Enhancement Method) 
 by ANN (Artifical Neural Network) as per the weather data collected at the Salt Farm, Bhavnagar, Gujarat.

----------------------------------------------------------------------
   Day  Max_T[C]  Min_T[C]  RH(%)  WS(mps)  Density(Be)  SPEM - Eveporatoin Prediction (mm)
0  3.0      37.7      21.9   37.0      3.8          5.7                            5.442142
----------------------------------------------------------------------
```
