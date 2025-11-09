from pathlib import Path

from src.Functional_approach.app import GenerateMemorablePassword, GeneratePinPassword, GenerateRandomPassword

import streamlit as st
import pyperclip

def copy_to_clipboard(password:str):
    pyperclip.copy(password)

BASE_DIR = Path(__file__).resolve().parent


st.image(f"{BASE_DIR}/images/image.png")
st.title(':zap: Password generator')

option = st.radio(
    'Select a password generation method',
    ('Random password', 'Memorable password', 'Pin code')
)

if option == 'Pin code':
    length = st.slider('Choose length of password', 4, 40, 8)
    password = GeneratePinPassword(length=length)
    st.write(f'Your password is : **```{password}```**') 
    st.button(':clipboard: copy to clipboard', on_click=copy_to_clipboard, args=[password])

elif option == 'Random password':
    length = st.slider('Choose length of password', 4, 40, 8)
    is_num = st.toggle('Include number', False)
    is_symbol = st.toggle('Include symbol', False)
    password = GenerateRandomPassword(length, is_num, is_symbol)
    st.write(f'Your password is : **```{password}```**') 
    st.button(':clipboard: copy to clipboard', on_click=copy_to_clipboard, args=[password])


elif option == 'Memorable password':
    length = st.slider('Choose length of password', 2, 10, 3)
    seprator = st.text_input('Words seprator', value='-')
    cap = st.toggle('Capitalize words', False)
    password = GenerateMemorablePassword(length, seprator, cap)
    st.write(f'Your password is : **```{password}```**') 
    st.button(':clipboard: copy to clipboard', on_click=copy_to_clipboard, args=[password])
