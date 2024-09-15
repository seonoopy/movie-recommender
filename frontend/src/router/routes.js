const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') },
      { path: 'movie/:id', component: () => import('pages/MovieDetails.vue') }, // 영화 상세 페이지 경로 추가
    ],
  },
];

export default routes;
