<template>
  <q-page class="row justify-center q-pa-md">
    <q-card class="col-12 col-md-8">
      <q-card-section>
        <q-select
          v-model="currentLanguage"
          :options="languages"
          @update:model-value="changeLanguage" />
      </q-card-section>

      <q-card-section>
        <q-input v-model="searchQuery" :label="$t('search')" />
        <q-btn :label="$t('search')" @click="searchMovies" color="primary" class="q-mt-md" />
      </q-card-section>

      <q-card-section v-if="movies.length > 0">
        <h4>{{ $t('recommendation') }}</h4>
        <q-list>
          <q-card class="my-card" flat bordered v-for="movie in movies" :key="movie.id" clickable>
            <q-card-section>
              <div class="text-h6 q-mb-xs">{{ movie.title }}</div>
              <div class="row no-wrap items-center">
                <q-item-label caption>{{ $t('rating') }}: {{ movie.vote_average }}</q-item-label>
              </div>
              <img :src="`https://image.tmdb.org/t/p/w200${movie.poster_path}`" :alt="movie.title" />
            </q-card-section>
          </q-card>
        </q-list>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useI18n } from 'vue-i18n';
import { useStore } from 'vuex';

const { locale } = useI18n();

const languages = [
  { label: 'English', value: 'en' },
  { label: '한국어', value: 'ko' },
];
const currentLanguage = ref(locale.value);

const changeLanguage = (lang) => {
  locale.value = lang;
};

const searchQuery = ref('');
const store = useStore();

const movies = computed(() => store.getters.movies);

const searchMovies = async () => {
  await store.dispatch('fetchMovies', searchQuery.value);
};
</script>
