import { createStore } from 'vuex';
import axios from 'axios';

export default createStore({
  state: {
    movies: [],
    recommendations: [],
  },
  mutations: {
    setMovies(state, movies) {
      state.movies = movies;
    },
    setRecommendations(state, recommendations) {
      state.recommendations = recommendations;
    },
  },
  actions: {
    async fetchMovies({ commit }, searchQuery) {
      const response = await axios.get('http://127.0.0.1:8000/search/', {
        params: { query: searchQuery },
      });
      commit('setMovies', response.data.results);
    },
    async fetchRecommendations({ commit }, movieId) {
      const response = await axios.get(`http://127.0.0.1:8000/recommendations/${movieId}`);
      commit('setRecommendations', response.data.results);
    },
  },
  getters: {
    movies: (state) => state.movies,
    recommendations: (state) => state.recommendations,
  },
});
