from django.urls import path
from . import views
from .views import ClientListView, ClientDetailView, ClientDeleteView, ClientUpdateView, ClientCreateView, journalVisitListView,\
	journalVisitCreateView, journalVisitUpdateView, ArchiveJournalVisitCreateView, TrenerListView, TrenerDetailView, TrainListView,\
	TrainUpdateView, TrainCreateView, TrainDeleteView, TrenerUpdateView, TrenerDeleteView

urlpatterns = [
	path('client-list', ClientListView.as_view(), name='client-list'),
	path('client/<int:pk>/', ClientDetailView.as_view(), name='client-profil'),
	path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),
	path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client-update'),
	path('client/new/', ClientCreateView.as_view(), name='client-create'),
	path('journal-list', journalVisitListView.as_view(), name='journal-list'),
	path('journal/new/', journalVisitCreateView.as_view(), name='journal-create'),
	path('journal/<int:pk>/update/', journalVisitUpdateView.as_view(), name='journal-update'),
	path('archivejournal-list', ArchiveJournalVisitCreateView.as_view(), name='archivejournal-list'),
	path('trener-list', TrenerListView.as_view(), name='trener-list'),
	path('trener/<int:pk>/', TrenerDetailView.as_view(), name='trener-profil'),
	path('trener/<int:pk>/update/', TrenerUpdateView.as_view(), name='trener-update'),
	path('trener/<int:pk>/delete/', TrenerDeleteView.as_view(), name='trener-delete'),
	path('train-list', TrainListView.as_view(), name='train-list'),
	path('train/<int:pk>/update/', TrainUpdateView.as_view(), name='train-update'),
	path('train/new/', TrainCreateView.as_view(), name='train-create'),
	path('train/<int:pk>/delete/', TrainDeleteView.as_view(), name='train-delete'),
]

