<template>
<q-page class="row justify-center q-pa-md">
    <q-card class="col-12 col-md-8">
    <q-card-section>
        <div class="text-h6">{{ movie.title }}</div>
        <div>{{ movie.overview }}</div>
    </q-card-section>

    <q-card-section v-if="recommendations.length > 0">
        <h4>Recommended Movies</h4>
        <q-list>
        <q-item v-for="rec in recommendations" :key="rec.id" clickable>
            <q-item-section>{{ rec.title }}</q-item-section>
        </q-item>
        </q-list>
    </q-card-section>
    </q-card>
</q-page>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import axios from 'axios';

const route = useRoute();
const movieId = route.params.id;
const store = useStore();

const movie = ref({});
const recommendations = computed(() => store.getters.recommendations);

const fetchMovieDetails = async () => {
  const response = await axios.get(`https://api.themoviedb.org/3/movie/${movieId}`, {
    params: { api_key: 'your_tmdb_api_key' },
  });
  movie.value = response.data;
};

const fetchRecommendations = async () => {
  await store.dispatch('fetchRecommendations', movieId);
};

onMounted(() => {
  fetchMovieDetails();
  fetchRecommendations();
});
</script>
