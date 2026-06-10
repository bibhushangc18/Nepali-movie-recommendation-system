
import streamlit as st
import pickle
import requests

# Load saved model
df = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# TMDB poster fetch function
def fetch_poster(movie_title):
    try:
        api_key = "235462bbe53927b0648beb3d4639dc00"
        url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}&language=ne"
        response = requests.get(url)
        data = response.json()
        if data["results"] and data["results"][0].get("poster_path"):
            poster_path = data["results"][0]["poster_path"]
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except:
        pass
    return "https://placehold.co/500x750?text=No+Poster+Available"

# Recommendation function
def recommend(movie_title):
    idx = df[df["title"].str.lower() == movie_title.lower()].index
    if len(idx) == 0:
        return [], []
    idx = idx[0]
    distances = list(enumerate(similarity[idx]))
    sorted_movies = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]
    titles = []
    posters = []
    for i, (index, score) in enumerate(sorted_movies):
        title = df.iloc[index]["title"]
        titles.append(title)
        posters.append(fetch_poster(title))
    return titles, posters

# ===== STREAMLIT UI =====
st.set_page_config(
    page_title="Nepali Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# Header
st.title("🎬 Nepali Movie Recommendation System")
st.markdown("### Find similar Nepali movies you will love!")
st.markdown("---")

# Dropdown
movie_list = df["title"].values
selected_movie = st.selectbox("🔍 Select a Nepali Movie:", movie_list)

# Show selected movie details
movie_data = df[df["title"] == selected_movie].iloc[0]
st.markdown(f"**Genre:** {movie_data['genre']} | **Rating:** ⭐ {movie_data['rating']:.1f} | **Year:** {int(movie_data['year']) if str(movie_data['year']) != 'nan' else 'N/A'}")

st.markdown("---")

# Recommend button
if st.button("🎯 Get Recommendations"):
    with st.spinner("Finding best matches..."):
        titles, posters = recommend(selected_movie)

    if titles:
        st.markdown("## 🍿 Top 5 Recommended Movies:")
        cols = st.columns(5)
        for i, col in enumerate(cols):
            with col:
                st.image(posters[i], use_column_width=True)
                st.markdown(f"**{titles[i]}**")
                movie_info = df[df["title"] == titles[i]].iloc[0]
                st.caption(f"⭐ {movie_info['rating']:.1f}")
                st.caption(f"{movie_info['genre']}")
    else:
        st.error("Movie not found!")

st.markdown("---")
st.caption("Built with ❤️ for Nepali Cinema | Everest Engineering College | 2026")
