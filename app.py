#importing the libraries
import streamlit as st
import pickle
import pandas as pd
import requests


#to get the posters of the movie
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=55d2bf5891bf6983b922b44b809427b4'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

#defining the function to be #recommended
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in  movies_list:
        movie_id = movies.iloc[i[0]].movie_id
#fetching the poster

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

#having the title of the system at the webpage
st.title('Movies Recommendation System')

# having the pickle files to be opened
movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)#changing it to dataframe

similarity = pickle.load(open('similarity.pkl','rb'))


#adding the s#elec#tbox
selected_movie_name = st.selectbox(
    "Enter the movie name to recommend",movies['title'].values
)
if st.button('Recommend'):
    names,posters =  recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

