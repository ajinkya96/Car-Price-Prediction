# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 18:46:01 2019

@author: user
"""


################# Car Price Prediction #########################
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
import pickle
from babel.numbers import format_number

        
def preprocessing(d):
    data = pd.read_csv("Car_Analysis_Data.csv")
    
    data.drop(['Unnamed: 0','Page Title','Image Links','Series','Compression Ratio','Steering','Front Rim(inches)','Rear Rim(inches)','Features','Front Suspension',
           'Rear Suspension', 'Loan Monthly Payment','Interest Rate','Front Tyres','Rear Tyres'],axis=1,inplace=True)
    

    data["Car Price"] = data["Car Price"].apply( lambda x : x.replace("RM","").strip().replace(" ",""))
    
    data = data.replace("   ","NaN").replace("-","NaN").replace(" -","NaN").replace('- ',"NaN")
    data = data.replace("NaN",np.nan)

    datadrop = data.dropna()
    category_type = ['Item Condition','Brand','Variant', 'Type', 'Transmission', 'Fuel Type', 'Front Brakes', 'Rear Brakes']
    continuous_type = ['Car Price', 'Peak Power (Bhp)', 'Height(mm)','Fuel Tank (litres)']
    
    datadrop[continuous_type]=datadrop[continuous_type].astype(float)
     
    datadrop=datadrop.loc[:,['Item Condition', 'Brand', 'Mileage',
            'Variant', 'Type',
            'Transmission', 'Engine CC', 'Peak Power (Bhp)',
           'Fuel Type',
            'Height(mm)',
           'Fuel Tank (litres)', 'Front Brakes', 'Rear Brakes']]
    
    datadrop.reset_index(drop=True,inplace=True)
    
    
    for i in category_type:
        datadrop[i] = datadrop[i].apply(lambda x: x.strip())
    
    datadrop.loc[len(datadrop)]=d
    
#        
    ordinal_encoder=OrdinalEncoder()

    datadrop.loc[:,category_type]=ordinal_encoder.fit_transform(datadrop[category_type])
    datadrop.loc[:,['Mileage']]=ordinal_encoder.fit_transform(datadrop[['Mileage']])
    
    sc_X = StandardScaler()
    X= sc_X.fit_transform(datadrop)
    
    return X[-1]



def predict(new):
    file_name='finalized_model.sav'
    model=pickle.load(open(file_name,'rb'))
    y_pred=model.predict(new.reshape(1,-1))
    y_pred=str(round(y_pred[0],2))
    y_pred="RM "+str(format_number(y_pred,locale='en_US'))
    
    return y_pred
