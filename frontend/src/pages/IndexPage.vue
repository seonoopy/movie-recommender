<template>
  <q-page class="row justify-center q-pa-md">
    <q-card class="col-12 col-md-8">
      <q-card-section>
        <div class="text-h6">Movie Search</div>
      </q-card-section>

      <q-card-section>
        <q-input v-model="searchQuery" label="Search for a movie" />
        <q-btn
          label="Search"
          @click="searchMovies"
          color="primary"
          class="q-mt-md"
        />
      </q-card-section>

      <q-card-section v-if="movies.length > 0 && !loading">
        <q-list>
          <q-item
            v-for="movie in movies"
            :key="movie.id"
            clickable
            @click="goToMovieDetails(movie.id)"
          >
            <q-item-section avatar>
              <img
                :src="`https://image.tmdb.org/t/p/w200${movie.poster_path}`"
                :alt="movie.title"
              />
            </q-item-section>
            <q-item-section>
              <q-item-label>{{ movie.title }}</q-item-label>
              <q-item-label caption
                >Rating: {{ movie.vote_average }}</q-item-label
              >
            </q-item-section>
          </q-item>
        </q-list>
        <q-infinite-scroll @load="loadMoreMovies" />
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

const searchQuery = ref('');
const loading = ref(false); // 로딩 상태 관리
const page = ref(1); // 현재 페이지 상태
const store = useStore();
const router = useRouter();

const movies = computed(() => store.getters.movies);

const searchMovies = async () => {
  loading.value = true; // 로딩 시작
  page.value = 1; // 첫 페이지부터 검색
  await store.dispatch('fetchMovies', searchQuery.value);
  loading.value = false; // 로딩 종료
};

const loadMoreMovies = async () => {
  page.value += 1; // 페이지 증가
  await store.dispatch('fetchMovies', {
    query: searchQuery.value,
    page: page.value,
  }); // 다음 페이지의 영화 검색
};

const goToMovieDetails = (movieId) => {
  router.push(`/movie/${movieId}`);
};
</script>
