from django.urls import path
from . import views
from .views import FeedbackListView, FeedbackUpdateView, PostCreateView, PostListView, PostUpdateView, PostDeleteView, TelebotListView, TelebotUpdateView

urlpatterns = [
	path('', views.index, name='index'),
	path('feedback-list', FeedbackListView.as_view(), name='feedback-list'),
	path('feedback/<int:pk>/update/', FeedbackUpdateView.as_view(), name='feedback-update'),
	path('telebot-list', TelebotListView.as_view(), name='telebot-list'),
	path('telebot/<int:pk>/update/', TelebotUpdateView.as_view(), name='telebot-update'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post-list', PostListView.as_view(), name='post-list'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

