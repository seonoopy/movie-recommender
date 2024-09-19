import { createStore } from 'vuex';
import axios from 'axios';
import '@material/web/button/filled-button.js';
import '@material/web/button/outlined-button.js';
import '@material/web/checkbox/checkbox.js';

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
    movies(state) {
      // eslint-disable-next-line no-console
      console.log(state.movies);
      return state.movies;
    },
    recommendations: (state) => state.recommendations,
  },
});
