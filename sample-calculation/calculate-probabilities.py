# -*- coding: utf-8 -*-
import json, os

import numpy as np
import pandas as pd 

database = json.load(open(os.path.join('.','database.json'),'rb'))

#Create data table
#Assume JSON is completely regular. NOT a good assumption. HACK. 
diseases = database["diseases"]
symptoms = database["symptoms"]


probabilities = np.zeros((len(diseases),len(symptoms)))

#Conditional probabilities
for i,disease in enumerate(diseases):
	for j,symptom in enumerate(symptoms):
		probabilities[j,i] = database[disease][symptom] * database["gen"][symptom]/database[disease]['general']

conditional_probabilities = np.prod(probabilities, axis=1)
df = pd.DataFrame(np.c_[[conditional_probabilities,
	[database[disease]['general'] for disease in diseases]]],
	index=['prior','posterior'],columns = diseases)

df.to_csv(os.path.join('.','sample-dataframe.csv'))