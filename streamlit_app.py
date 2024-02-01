import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title='Bs First App', layout='wide', page_icon=':guitar:')

# This is the header
t1, t2 = st.columns((1, 13))

with t1:
    st.image('images/dashboard_icon.png', width=150, use_column_width="always")

with t2:
    st.title("B's First Application")
    st.markdown("**tel:*** ****| website:** https://www.github.com/wellsbury **| email:** mailto: b@github.com")

## Data

st.header('Testing Data Visualization')
st.subheader('My Charts')

with st.spinner('Updating Report...'):
    
    #Metrics setting and rendering

    
    m1, m2 = st.columns((1,2))
    
    excel_file_path = "membership_data.xlsx"  # Replace with the actual path
    df = pd.read_excel(excel_file_path, sheet_name="Sheet_0")

 
    # Extract the value from cell A1
    value_a1 = df.iloc[0, 0]



    # Display the value in Streamlit
    m1.metric("Total Users", value_a1)

    fgdf = pd.read_excel('membership_data.xlsx', sheet_name='Sheet_1')

    # Sort the DataFrame by the 'Count' column in descending order
    fgdf = fgdf.sort_values(by='Count', ascending=True)

    # Take the top 20 entries
    top_20_df = fgdf.tail(20)

    fig = px.bar(top_20_df, x='Count', y='Job Title', template='seaborn',
                labels={'count': 'Job Title'}, orientation='h',
                category_orders={'Job Title': list(reversed(top_20_df['Job Title'].tolist()))})

    fig.update_traces(marker_color='#264653')

    fig.update_layout(title_text="Top 20 Customers by Job Title", title_x=0, margin=dict(l=0, r=10, b=10, t=30),
                    yaxis_title=None, xaxis_title=None)

    m2.plotly_chart(fig, use_container_width=True)





