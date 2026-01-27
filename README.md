# Music Recommender System

A content-based music recommendation system developed using Natural Language Processing (NLP) techniques.  
The system recommends songs by analyzing lyrical similarity using TF-IDF vectorization and cosine similarity.

---

## Project Overview

With the rapid growth of digital music platforms, discovering songs that match user preferences has become challenging.  
This project addresses that challenge by recommending songs based on the similarity of their lyrics rather than popularity or user behavior.

The application is implemented as a Streamlit web application for interactive use.

---

## Features

- Content-based song recommendation using lyrics
- Text preprocessing using NLTK
- TF-IDF vectorization of song lyrics
- Cosine similarity-based recommendation
- Interactive web interface using Streamlit

---

## Technologies Used

- Python
- Pandas and NumPy
- NLTK
- Scikit-learn
- Streamlit
- Matplotlib
- WordCloud

---

## Dataset

Spotify Million Song Dataset  
Source: Kaggle  

The dataset contains song names, artists, and lyrics.  
Due to its large size, the dataset is not included in this repository.

---

## How to Run the Project

### Step 1: Clone the repository
```
git clone
```
```
cd music-recommender
```
### Step 2: Create a virtual environment (optional)
```
python -m venv venv
```
```
venv\Scripts\activate
```
### Step 3: Install required dependencies
```
pip install -r requirements.txt
```
### Step 4: Run the application
```
python -m streamlit run main.py
```

---

## Future Enhancements

- Integration of audio feature-based recommendations
- Improved user interface design
- Deployment on Streamlit Cloud
- Hybrid recommendation system
