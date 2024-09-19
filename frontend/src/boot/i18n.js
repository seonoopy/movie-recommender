// src/boot/i18n.js

import { createI18n } from 'vue-i18n';

const messages = {
  en: {
    search: 'Search for a movie',
    recommendation: 'Recommended Movies',
    rating: 'Rating',
  },
  ko: {
    search: '영화 검색',
    recommendation: '추천 영화',
    rating: '평점',
  },
};

const i18n = createI18n({
  locale: 'ko', // 기본 언어를 한국어로 설정
  fallbackLocale: 'en',
  messages,
});

export default ({ app }) => {
  app.use(i18n);
};
