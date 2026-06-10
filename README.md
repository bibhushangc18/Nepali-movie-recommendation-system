 Nepali Movie Recommendation System

A Content-Driven Movie Recommendation System for Nepali Cinema built as a Major Project at Everest Engineering College.

 Team Members
 Ashish Khatri [22120112]
 Bibhusan GC [22120115]
 Dip Prajwal Pandey [22120120]
 Diwakar Yadav [22120122]

 About
This system recommends similar Nepali movies based on content features like genre and plot using TF-IDF and Cosine Similarity.

 Technologies Used
- Python
- Pandas
- Scikit-learn (TF-IDF, Cosine Similarity)
- NLTK (Stemming)
- Streamlit (Web UI) — Coming Soon
- TMDB API (Movie Posters) — Coming Soon

Dataset
- 800 Nepali movies scraped from IMDb
- Features: Title, Genre, Plot, Rating, Year, Runtime

 Completed So Far
- Loaded and explored 800 Nepali movies (EDA)
- Data Cleaning and Preprocessing
- Feature Engineering (Tags creation)
- Stemming using NLTK
- TF-IDF Vectorization (800 x 3354 matrix)
- Cosine Similarity Engine (800 x 800 matrix)
- Recommendation Function (Top 5 movies)
- Model saved as movies.pkl and similarity.pkl

 Coming Soon
- Streamlit Web App
- Movie Posters via TMDB API
- Deployment on Streamlit Cloud
