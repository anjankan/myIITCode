# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 05:38:33 2022

@author: Anjaneya Sastry K
"""

import streamlit as st
import pandas as pd

st.write("""
# Anjaneya Sastry K TDS Project
""")
#Get Input

st.header('Welcome to my simple Calculator')

#res1=0
def user_input_features():

    value1 = st.number_input("VALUE_1",min_value=0.0,max_value=2000000.0)
    value2 = st.number_input("VALUE_2",min_value=0.0,max_value=2000000.0)

    
    data = {'VALUE_1': value1,
            'VALUE_2': value2,
            'RESULT' : value1 - value2
            }

    features = pd.DataFrame(data, index=[0])

    return features

df = user_input_features()

st.subheader('Simple Calculator using NGROK')
#st.write(df.to_dict())


#continous_features = ['VALUE_1','VALUE_2', 'RESULT']


st.subheader('Result of Subtraction')
st.table(df)

#st.subheader('Class labels and their corresponding index number')
#st.write(pd.DataFrame({'Labels': ['Approved','Declined']}))


#st.write(pd.DataFrame({'Labels': ['Result', res1]}))

st.subheader('Thanks!')
