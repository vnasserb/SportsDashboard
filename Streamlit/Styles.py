import pandas as pd
import numpy as np
import streamlit as st
import json
import matplotlib.pyplot as plt
import plotly.express as px

def highlight_positive(val):
    if val == 'W':
        color = 'green'
        text = 'white'
    elif val == 'L':
        color = 'red'
        text = 'white'
    elif val == 'D':
        color = 'gray'
        text = 'white'
    else:
        color = 'white'
        text = 'black'
    return f'background-color: {color}; color: {text}; text-align: center;'

def createBarChart(data, x_axis, y_axis, title, text):

    df = pd.DataFrame(data)
    fig = px.bar(df, x=x_axis, y=y_axis, title=title,
                 text=text  # Assign 'Value' to display values on top of the bars
                 )
    fig.update_layout(bargap=0.7)
    st.plotly_chart(fig)

def createLinePlot(data, x_axis, y_axis, title, hover=None):

    df = pd.DataFrame(data)
    fig = px.line(df, x=x_axis, y=y_axis, hover_data=hover,title=title)
    st.plotly_chart(fig)

def writeColumns(object, *args):
    columns = st.columns(len(args))
    if object == 'dataframe':
        for i in range(len(columns)):
            with columns[i]:
                st.write(args[i][0])
                st.dataframe(data=pd.DataFrame(args[i][1], columns=['Quantity', 'Percentage']), hide_index=True)

    elif object == 'metric':
        for i in range(len(columns)):
            with columns[i]:
                st.metric(label=args[i]['label'], value=args[i]['value'])

    elif object == "Bar plot":
        for i in range(len(columns)):
            with columns[i]:
                figure = createBarChart(data=args[i][0], x_axis=args[i][1]['x_axis'], y_axis=args[i][1]['y_axis'],
                               title=args[i][1]['title'], text=args[i][1]['text'])
                st.title(args[i][1]['title'])
                st.plotly_chart(figure)
