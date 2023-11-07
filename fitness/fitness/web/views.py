from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import FeedbackForm
from .models import Feedback, Post, Telebot
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse

def index(request):
	if request.method == 'POST':
		form = FeedbackForm(request.POST)
		if form.is_valid():
			feedback = Feedback(
				name=form.cleaned_data.get('name'),
				phone=form.cleaned_data.get('phone'),
			)
			feedback.save()
			url = reverse('index')
			return HttpResponseRedirect(f'{url}?sent=1')
	else:
		form = FeedbackForm()

	context = {'title': 'Фитнес-клуб «Богатырь»','form': form, 'posts': Post.objects.all(), 'sent':request.GET.get('sent')}
	return render(request, 'web/index.html', context=context)

class FeedbackListView(LoginRequiredMixin,ListView):
	model = Feedback
	context_object_name = 'feedbacks'
	paginate_by = 10
	template_name = 'web/feedback_list.html'

	# def get_queryset(self):
	# 	return Feedback.objects.order_by('-created_at')

	def get_context_data(self, **kwargs):
		context = super(FeedbackListView, self).get_context_data(**kwargs)
		context['title'] = 'Список заявок на обратный звонок'
		return context

	def get_ordering(self):
		ordering = self.request.GET.get('orderby')
		return ordering

class FeedbackUpdateView(LoginRequiredMixin,UpdateView):
	model = Feedback
	fields = ['name', 'phone', 'created_at', 'complete']

	success_url = 'http://127.0.0.1:8000/feedback-list'

	def get_context_data(self, **kwargs):
		context = super(FeedbackUpdateView, self).get_context_data(**kwargs)
		context['title'] = 'Изменить запись'
		return context

class TelebotListView(LoginRequiredMixin,ListView):
	model = Telebot
	context_object_name = 'telebots'
	paginate_by = 10
	template_name = 'web/telebot_list.html'

	def get_context_data(self, **kwargs):
		context = super(TelebotListView, self).get_context_data(**kwargs)
		context['title'] = 'Запись на тренировки через Telegram бота'
		return context

	def get_ordering(self):
		ordering = self.request.GET.get('orderby')
		return ordering


class TelebotUpdateView(LoginRequiredMixin,UpdateView):
	model = Telebot
	fields = ['user_id_telegram', 'username_telegram', 'user_name_telegram', 'user_name_client', 'user_time_client', 'status',
			  'type_train', 'trener', 'user_phone_client']

	success_url = 'http://127.0.0.1:8000/telebot-list'

	def get_context_data(self, **kwargs):
		context = super(TelebotUpdateView, self).get_context_data(**kwargs)
		context['title'] = 'Изменить запись'
		return context

class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title', 'content']

	success_url = 'http://127.0.0.1:8000/post-list'

	def get_context_data(self, **kwargs):
		context = super(PostCreateView, self).get_context_data(**kwargs)
		context['title'] = 'Создать запись'
		return context

class PostListView(LoginRequiredMixin,ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'web/post_list.html'

	def get_context_data(self, **kwargs):
		context = super(PostListView, self).get_context_data(**kwargs)
		context['title'] = 'Список всех публикаций'
		return context

class PostUpdateView(LoginRequiredMixin,UpdateView):
	model = Post
	fields = ['title', 'content']

	success_url = 'http://127.0.0.1:8000/post-list'

	def get_context_data(self, **kwargs):
		context = super(PostUpdateView, self).get_context_data(**kwargs)
		context['title'] = 'Изменить запись'
		return context

class PostDeleteView(LoginRequiredMixin,DeleteView):
	model = Post

	success_url = 'http://127.0.0.1:8000/post-list'

	def get_context_data(self, **kwargs):
		context = super(PostDeleteView, self).get_context_data(**kwargs)
		context['title'] = 'Удалить запись'
		return context
