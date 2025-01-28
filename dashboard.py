import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Load data
data=pd.read_excel(r"C:\Users\faiza\ML case study\15. Capstone Case Study - NLP- Woman Clothing E-Commerce Platform\Womens Clothing Reviews Data.xlsx")  

data['Age Group'] = pd.cut(data['Customer Age'], bins=range(10, 101, 10), labels=[f"{i}-{i+9}" for i in range(10, 100, 10)])

# Preprocessing for sentiment analysis
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()
data['Sentiment Score'] = data['Review Text'].fillna('').apply(lambda x: sia.polarity_scores(str(x))['compound'])

# Sidebar for filtering
st.sidebar.header("Filters")
selected_category = st.sidebar.multiselect('Select Category', data['Category'].unique())
selected_location = st.sidebar.multiselect('Select Location', data['Location'].unique())
selected_channel = st.sidebar.multiselect('Select Channel', data['Channel'].unique())
selected_age = st.sidebar.multiselect('Select Age Group', data['Age Group'].unique())


# Filter data based on selections
filtered_data = data
if selected_category:
    filtered_data = filtered_data[filtered_data['Category'].isin(selected_category)]
if selected_location:
    filtered_data = filtered_data[filtered_data['Location'].isin(selected_location)]
if selected_channel:
    filtered_data = filtered_data[filtered_data['channel'].isin(selected_channel)]  
if selected_age:
    filtered_data = filtered_data[filtered_data['Age Group'].isin(selected_age)]  



# Dashboard Title
st.title("Product Review Dashboard")

# Display data overview
st.subheader("Data Overview")
st.write(filtered_data.head())


# Word cloud for review text
st.subheader("Word Cloud of Review Text")
wordcloud = WordCloud(stopwords=STOPWORDS, background_color='white').generate(' '.join(filtered_data['Review Text'].fillna('')))
plt.figure(figsize=(15, 7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot(plt.gcf())


# Plot frequency distribution of Channel
st.subheader("Distribution of Channel")
plt.figure(figsize=(10, 5))
sns.barplot(data=filtered_data['Channel'].value_counts())
plt.title('Distribution of Channel')
st.pyplot(plt.gcf())

# Plot frequency distribution of Location
st.subheader("Distribution of Location")
plt.figure(figsize=(10, 5))
sns.barplot(data=filtered_data['Location'].value_counts())
plt.title('Distribution of Location')
st.pyplot(plt.gcf())

# Plot frequency distribution of Category
st.subheader("Distribution of Category")
plt.figure(figsize=(10, 5))
sns.barplot(data=filtered_data['Category'].value_counts())
plt.title('Distribution of Category')
st.pyplot(plt.gcf())

# Plot frequency distribution of Subcategory1
st.subheader("Distribution of Subcategory1")
plt.figure(figsize=(10, 5))
sns.barplot(data=filtered_data['Subcategory1'].value_counts())
plt.title('Distribution of Subcategory1')
st.pyplot(plt.gcf())

# Plot frequency distribution of Subcategory1
st.subheader("Distribution of Subcategory2")
plt.figure(figsize=(10, 5))
sns.barplot(data=filtered_data['SubCategory2'].value_counts(),orient="h")
plt.title('Distribution of Subcategory2')
st.pyplot(plt.gcf())


# Plot frequency distribution of ratings
st.subheader("Distribution of Ratings")
plt.figure(figsize=(10, 5))
sns.histplot(filtered_data['Rating'], bins=4, color='blue')
plt.title('Distribution of Ratings')
st.pyplot(plt.gcf())


# Distribution of Age Group
st.subheader('Distribution of Age Group')
data['Age Group'] = pd.cut(data['Customer Age'], bins=range(10, 101, 10), labels=[f"{i}-{i+9}" for i in range(10, 100, 10)])
plt.figure(figsize=(12, 6))
sns.barplot(data['Age Group'].value_counts())
plt.title('Distribution of Age Group')
plt.xlabel('Age Group')
plt.ylabel('Frequency')
plt.show()
st.pyplot(plt.gcf())




# Sentiment Analysis Visualization

st.subheader("Sentiment Analysis by Channel")
avg_sentiment_by_category = filtered_data.groupby('Channel')['Sentiment Score'].mean().sort_values()
plt.figure(figsize=(12, 6))
avg_sentiment_by_category.plot(kind='bar', color='coral')
plt.title('Average Sentiment Score by Channel')
plt.xlabel('Channel')
plt.ylabel('Average Sentiment Score')
st.pyplot(plt.gcf())

# Visualize ratings by location
st.subheader("Average Rating by Location")
avg_rating_by_location = filtered_data.groupby('Location')['Rating'].mean().sort_values()
plt.figure(figsize=(15, 7))
avg_rating_by_location.plot(kind='bar', color='lightgreen')
plt.title('Average Rating by Location')
plt.xlabel('Location')
plt.ylabel('Average Rating')
st.pyplot(plt.gcf())


st.subheader("Sentiment Analysis by Category")
avg_sentiment_by_category = filtered_data.groupby('Category')['Sentiment Score'].mean().sort_values()
plt.figure(figsize=(12, 6))
avg_sentiment_by_category.plot(kind='bar', color='coral')
plt.title('Average Sentiment Score by Category')
plt.xlabel('Category')
plt.ylabel('Average Sentiment Score')
st.pyplot(plt.gcf())

# Visualize ratings by SubCategory
st.subheader("Average Rating by SubCategory1")
avg_rating_by_location = filtered_data.groupby('Subcategory1')['Rating'].mean().sort_values()
plt.figure(figsize=(15, 7))
avg_rating_by_location.plot(kind='bar', color='lightgreen')
plt.title('Average Rating by SubCategory1')
plt.xlabel('SubCategory1')
plt.ylabel('Average Rating')
st.pyplot(plt.gcf())

# Visualize ratings by SubCategory
st.subheader("Average Rating by SubCategory2")
avg_rating_by_location = filtered_data.groupby('SubCategory2')['Rating'].mean().sort_values()
plt.figure(figsize=(15, 7))
avg_rating_by_location.plot(kind='bar', color='lightgreen')
plt.title('Average Rating by SubCategory2')
plt.xlabel('SubCategory2')
plt.ylabel('Average Rating')
st.pyplot(plt.gcf())


# Sentiment distribution
st.subheader("Distribution of Sentiment Scores")
plt.figure(figsize=(10, 5))
sns.histplot(filtered_data['Sentiment Score'], kde=True, color='purple')
plt.title('Distribution of Sentiment Scores')
st.pyplot(plt.gcf())





# Sentiment by Age Group
st.subheader("Sentiment Analysis by Age Group")
filtered_data['Age Group'] = pd.cut(filtered_data['Customer Age'], bins=range(10, 101, 10), labels=[f"{i}-{i+9}" for i in range(10, 100, 10)])
avg_sentiment_by_age_group = filtered_data.groupby('Age Group')['Sentiment Score'].mean().sort_values()
plt.figure(figsize=(12, 6))
avg_sentiment_by_age_group.plot(kind='bar', color='orange')
plt.title('Average Sentiment Score by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Sentiment Score')
st.pyplot(plt.gcf())
