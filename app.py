import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('iris_.csv')

# Sidebar options
st.sidebar.header('Options')
plot_type = st.sidebar.selectbox('Select a plot type', ('Histogram', 'Boxplot', 'Scatterplot'))

# Plotting
st.header('Data Visualization Dashboard')

if plot_type == 'Histogram':
    feature = st.selectbox('Select a feature', data.columns)
    fig, ax = plt.subplots()
    ax.hist(data[feature])
    st.pyplot(fig)

elif plot_type == 'Boxplot':
    feature = st.selectbox('Select a feature', data.columns)
    fig, ax = plt.subplots()
    ax.boxplot(data[feature])
    st.pyplot(fig)

else:
    x_feature = st.selectbox('Select a feature for x-axis', data.columns)
    y_feature = st.selectbox('Select a feature for y-axis', data.columns)
    fig, ax = plt.subplots()
    ax.scatter(data[x_feature], data[y_feature])
    st.pyplot(fig)

# Data table
st.header('Data Table')
st.write(data)
