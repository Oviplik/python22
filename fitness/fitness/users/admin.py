from django.contrib import admin
from .models import Client, ClientAdmin, journalVisit, journalVisitAdmin, ArchiveJournalVisit, ArchiveJournalVisitAdmin, Trener, TrenerAdmin, Train, TrainAdmin
admin.site.register(Client, ClientAdmin)
admin.site.register(journalVisit, journalVisitAdmin)
admin.site.register(ArchiveJournalVisit, ArchiveJournalVisitAdmin)
admin.site.register(Trener, TrenerAdmin)
admin.site.register(Train, TrainAdmin)

