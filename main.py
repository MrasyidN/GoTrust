import streamlit as st
from faker import Faker
import pandas as pd
from nicegui import ui
import random
import requests

# uri = 'http://localhost/api/get_users'

# data_users = requests.get(uri)

st.title("Order")

def change_user(usr):
    score = 0
    if(usr == ''):
       score = -1
    else:
        score = random.randint(1,100)
   
    return {
      "score": score,
      "resp_text": usr + " integrity account score is " + str(score)
    }

i = False

my_color = st.selectbox('Users', ['','user_1471','user_1607','user_1001','user_11792','user_10008'])
resp = change_user(my_color)
z = False
if(resp['score'] >= 70):
    st.success(f"{resp['resp_text']}")
    i = True
    payment_method = st.selectbox('Payment Method', ['credit','ewallet','cod'])
elif(resp['score'] < 70 and resp['score'] >= 40):
    payment_method = st.selectbox('Payment Method', ['credit','ewallet'])
    st.warning(f"We restrict your payment method because {resp['resp_text']}")
elif(resp['score'] >= 0 and resp['score'] < 40):
    st.error(f"Sorry, you can't order now because {resp['resp_text']}")
    z = True
else:
    st.error(f"Select user please")
# if(i == True):
#     if(payment_method == "cod"):
#         z = True
#     else:
#         z = False

st.button("Submit order",disabled=z)