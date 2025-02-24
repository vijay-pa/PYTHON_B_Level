import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load Titanic Dataset
@st.cache
def load_data():
    data = pd.read_csv(os.path.expanduser("~/Downloads/titanic dataset.csv"))
    return data

data = load_data()

# Title and description
st.title("Exploratory Data Analysis of Titanic Dataset")
st.write("This is a EDA on the Titanic dataset.")
st.write("First Few rows of the dataset:")
st.dataframe(data.head())

# Data Cleaning Section
st.header("Missing Values")
missing_data = data.isnull().sum()
st.write(missing_data)

if st.checkbox("Fill Missing Age with Median"):
    data['Age'].fillna(data['Age'].median(), inplace= True)
    st.write("Missing Age values filled with median")

if st.checkbox("Fill Missing Embarked with Mode"):
    data['Embarked'].fillna(data['Embarked'].mode()[0], inplace= True)
    st.write("Missing Embarked values filled with mode")

if st.checkbox("Drop Duplicates"):
    data.drop_duplicate(inplace=True)
    st.write("Dropped Duplicates")

st.subheader("Cleaned Dataset")
st.dataframe(data.head())

#EDA(Exploratory Data Analysis) - Section
st.subheader("Statistical Summary of the Data")
st.write(data.describe())

#Age Distribution
st.subheader("Age Distribution")
fig, ax = plt.subplots()
sns.histplot(data['Age'], kde =True, ax=ax)
ax.set_title("Age Distribution")
st.pyplot(fig)

#Gender Distribution
st.subheader("Gender Distribution")
fig, ax = plt.subplots()
sns.countplot(x ='sex', data = data, ax = ax)
ax.set_title('Gender Distribution')
sns.pyplot(fig)

# PClass vs Survived
st.subheader("PClass vs Survived")
fig, ax = plt.subplots()
sns.countplot(x ='Pclass', hue = 'Survived', data = data, ax = ax)
ax.set_title('PClass vs Survived')
sns.pyplot(fig)

'''
# Correlation Heatmap
st.subheader("Correlation Heatmap")
fig, ax = plt.subplots()
sns.heatmap(data.corr(), annot = True, cmap ='coolwarm', ax = ax)
ax.set_title('Correlation Heatmap')
st.pyplot(fig)
'''

#Feature Engineering Section
st.header("Feature Engineering: Family Size")
data['FamilySize'] = data['SibSp'] + data['Parch']
fig, ax = plt.subplots()
sns.histplot(data['FamilySize'], kde =True, ax=ax)
ax.set_title("Family Size Distribution")
st.pyplot(fig)

#Conclusion Section
st.header("Key Insights")
insights = '''
- Females have higher survival rate than males
- Passengers in 1st class had the highest survival rate
- The majority of passengers are in PClass 3.
- Younger passengers tended to survive more often.
'''
st.write(insights)










