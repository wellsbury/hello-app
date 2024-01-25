import streamlit as st 
import pandas as pd

st.title('My First Application')

st.header('Testing Data Vizualiation')
st.subheader('My Charts')

# Replace 'your_file.csv' with the actual path to your CSV file
file_path = 'https://github.com/wellsbury/hello-app/blob/c04ed3787cb78ea22677397419a607e882081236/streamlit_test_data.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)
# Display the DataFrame
print(df.head())

