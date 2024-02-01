import streamlit as st
import pandas as pd

st.set_page_config(page_title='Bs First App', layout='wide', page_icon=':guitar:')

# This is the header
t1, t2 = st.columns((1, 13))

with t1:
    st.image('images/dashboard_icon.png', width=150, use_column_width="always")

with t2:
    st.title("B's First Application")
    st.markdown("**tel:*** ****| website:** https://www.github.com/wellsbury **| email:** mailto:b@github.com")

## Data

st.header('Testing Data Visualization')
st.subheader('My Charts')

with st.expander("Hidden Data Table"):
    # Replace 'your_file.csv' with the actual path to your CSV file
    file_path = 'https://raw.githubusercontent.com/wellsbury/hello-app/main/streamlit_test_data.csv'

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Display the DataFrame
    st.dataframe(df)


