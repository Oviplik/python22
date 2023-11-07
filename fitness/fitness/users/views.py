from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Client, journalVisit, ArchiveJournalVisit, Trener, Train
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from datetime import timedelta
from .forms import ClientUpdateForm, journalVisitCreateForm, TrainCreateForm
from functools import reduce
import operator
from django.db.models import Q



class ClientListView(LoginRequiredMixin,ListView):
    model = Client
    context_object_name = 'clients'
    paginate_by = 10
    template_name = 'users/client_list.html'
    # ordering = ['-date_start_contract']

    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        context['title'] = 'Список клиентов фитнес-клуба'
        return context

    def get_ordering(self):
        ordering = self.request.GET.get('orderby')
        return ordering

    def get_queryset(self):
        result_search = super(ClientListView, self).get_queryset()
        query = self.request.GET.get('poisk')
        if query:
            query_list = query.split()
            result_search = result_search.filter(
                reduce(operator.and_,
                       (Q(lastname__icontains=poisk) for poisk in query_list)) |
                reduce(operator.and_,
                       (Q(firstname__icontains=poisk) for poisk in query_list)) |
                reduce(operator.and_,
                       (Q(patronymic__icontains=poisk) for poisk in query_list)) |
                reduce(operator.and_,
                       (Q(num_contract__icontains=poisk) for poisk in query_list)) |
                reduce(operator.and_,
                       (Q(num_membership__icontains=poisk) for poisk in query_list)) |
                reduce(operator.and_,
                        (Q(phone__icontains=poisk) for poisk in query_list))
            )
        return result_search



class ClientDetailView(LoginRequiredMixin,DetailView):
    model = Client

class ClientDeleteView(LoginRequiredMixin,DeleteView):
    model = Client
    success_url = '/'

    def test_func(self):
        if self.request.user == is_superuser:
            return True
        return False

class ClientUpdateView(LoginRequiredMixin,UpdateView):
    model = Client
    form_class = ClientUpdateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.time_period = form.cleaned_data.get('time_period')
        self.object.date_start_contract = form.cleaned_data.get('date_start_contract')
        self.object.date_end_contract = self.object.date_start_contract+timedelta(days=(self.object.time_period*30))
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')

class ClientCreateView(LoginRequiredMixin,CreateView):
    model = Client
    fields = ['lastname', 'firstname', 'patronymic', 'phone', 'email', 'num_contract', 'num_membership', 'date_start_contract', 'date_end_contract',
               'type_membership', 'time_period', 'status_membership', 'birthdate', 'gender', 'passport', 'photo']
    success_url = 'http://127.0.0.1:8000/users/client-list'

class journalVisitListView(LoginRequiredMixin,ListView):
    model = journalVisit
    context_object_name = 'clients'
    paginate_by = 10
    template_name = 'users/journal_list.html'

    def get_context_data(self, **kwargs):
        context = super(journalVisitListView, self).get_context_data(**kwargs)
        context['title'] = 'Посетители в зале'
        return context

    def get_queryset(self):
        result_search = super(journalVisitListView, self).get_queryset()
        query = self.request.GET.get('num_card')
        if query:
            query_list = query.split()
            result_search = result_search.filter(
                reduce(operator.and_,
                        (Q(num_membership__icontains=num_card) for num_card in query_list))
            )
        return result_search


class journalVisitCreateView(LoginRequiredMixin,CreateView):
    model = journalVisit
    form_class = journalVisitCreateForm

    success_url = 'http://127.0.0.1:8000/users/journal-list'

class journalVisitUpdateView(LoginRequiredMixin,UpdateView):
    model = journalVisit
    form_class = journalVisitCreateForm

    success_url = 'http://127.0.0.1:8000/users/journal-list'

class ArchiveJournalVisitCreateView(LoginRequiredMixin,ListView):
    model = ArchiveJournalVisit
    context_object_name = 'clients'
    paginate_by = 10
    template_name = 'users/archivejournal_list.html'

    success_url = 'http://127.0.0.1:8000/users/archivejournal-list'

class TrenerListView(LoginRequiredMixin,ListView):
    model = Trener
    context_object_name = 'treners'
    paginate_by = 10
    template_name = 'users/trener_list.html'

class TrenerDetailView(LoginRequiredMixin,DetailView):
    model = Trener

    def get_context_data(self, **kwargs):
        context = super(TrenerDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Посетители в зале'
        trener = Trener.objects.get(id=self.kwargs['pk'])
        train = Train.objects.filter(trener=trener).all()
        context['trains'] = train
        context['trains_soon'] = train.order_by('dateTime')
        return context

class TrenerUpdateView(LoginRequiredMixin,UpdateView):
    model = Trener
    fields = ['lastnameTrener', 'firstnameTrener', 'phone', 'type_trains', 'adwards', 'photo']

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')

class TrenerDeleteView(LoginRequiredMixin,DeleteView):
    model = Trener
    success_url = 'trener-list'

class TrainListView(LoginRequiredMixin,ListView):
    model = Train
    context_object_name = 'trains'
    paginate_by = 30
    template_name = 'users/train_list.html'

    def get_context_data(self, **kwargs):
        context = super(TrainListView, self).get_context_data(**kwargs)
        context['title'] = 'Архив тренеровок'
        return context

    def get_ordering(self):
        ordering = self.request.GET.get('orderby')
        return ordering

    def get_queryset(self):
        result_search = super(TrainListView, self).get_queryset()
        query = self.request.GET.get('poisk')
        if query:
            query_list = query.split()
            result_search = result_search.filter(
                reduce(operator.and_,
                       (Q(trener__lastnameTrener=poisk) for poisk in query_list))
            )
        return result_search


class TrainUpdateView(LoginRequiredMixin,UpdateView):
    model = Train
    form_class = TrainCreateForm


    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')

    def get_context_data(self, **kwargs):
        context = super(TrainUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Изменить запись'
        return context

class TrainDeleteView(LoginRequiredMixin,DeleteView):
    model = Train
    success_url = 'http://127.0.0.1:8000/users/train-list'


class TrainCreateView(LoginRequiredMixin,CreateView):
    model = Train
    form_class = TrainCreateForm
    success_url = 'http://127.0.0.1:8000/users/train-list'

