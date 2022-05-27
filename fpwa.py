# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 16:11:29 2022

@author: vamsi
"""

import numpy as np
import pickle 
import streamlit as st

load_model = pickle.load(open('D:/imp/train_model.sav','rb'))

def flourine_prediction(input_data):

    input_numpy=np.asarray(input_data)

    input_reshape=input_numpy.reshape(1,-1)

    prediction=load_model.predict(input_reshape)
    
    if(prediction[0]==1):
        
        return 'the flourine content is low so, this water is suitable for drinking'
    
    elif(prediction[0]==2):
        
        return 'the flourine content is medium so,this water is suitable for drinking but there will be mild effects'
    
    else:  
        
        return 'the flourine content is high so, this water is not suitable for drinking'
    
def main():
    
    st.title('Flourine prediction')    
    
    Mandal = st.text_input('Enter the value of mandal')
    
    pH = st.text_input('Enter the value of pH')
    
    TDS = st.text_input('Enter the value of TDS')
    
    EC = st.text_input('Enter the value of EC')
    
    TH = st.text_input('Enter the value of TH')
    
    HCO3 = st.text_input('Enter the value of HCO3')
    
    Ca = st.text_input('Enter the value of Ca')
    
    Cl = st.text_input('Enter the value of Cl')
    
    Mg = st.text_input('Enter the value of Mg')
    
    
    result=''
    
    if st.button('Get Result'):
        
        result = flourine_prediction([Mandal,pH,TDS,EC,TH,HCO3,Ca,Cl,Mg])
    
    st.success(result)
    
if __name__=='__main__':
    main()    
    
    
    
    
    
    
    
    
    
    