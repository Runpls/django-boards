from django.urls import path

from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.BoardListView.as_view(), name='home'),
    # path('boards/<int:pk>/', views.board_topics, name='board_topics'),
    path('boards/<int:pk>/', views.TopicListView.as_view(),
         name='board_topics'),
    path('boards/<int:pk>/new/', views.new_topic, name='new_topic'),
    path('boards/<int:pk>/topics/<int:topic_pk>/',
         views.PostListView.as_view(), name='topic_posts'),
    path('boards/<int:pk>/topics/<int:topic_pk>/reply/', views.reply_topic,
         name='reply_topic'),
    path('boards/<int:pk>/topics/<int:topic_pk>/posts//<int:post_pk>/edit/',
         views.PostUpdateView.as_view(), name='edit_post'),
]
