# app.py
import streamlit as st
from recommend import df, recommend_songs

# Set custom Streamlit page config
st.set_page_config(
    page_title="Music Recommender",
    page_icon="🎧",
    layout="centered"
)

# Custom CSS for minimal styling
st.markdown("""
    <style>
    .main {
        background: #0a0a0a;
        color: white;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    h1 {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.05);
        border: 2px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #667eea;
    }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 1rem;
        font-weight: 600;
        margin-top: 2rem;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
    }
    
    .dataframe thead tr th {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
    }
    
    .dataframe tbody tr:hover td {
        background: rgba(102, 126, 234, 0.1) !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Music Recommender")

song_list = sorted(df['song'].dropna().unique())
selected_song = st.selectbox("Select a song:", song_list)

if st.button("Find Similar Songs"):
    with st.spinner("Analyzing..."):
        recommendations = recommend_songs(selected_song)
        
        if recommendations is None:
            st.warning("Song not found.")
        else:
            st.success(f"Similar to {selected_song}")
            st.table(recommendations)