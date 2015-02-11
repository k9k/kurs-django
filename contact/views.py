from django.shortcuts import render

# Create your views here.

from django.views.generic import DetailView, FormView
from .models import Message
from .forms import MessageForm, ContactForm


#class MessageDetailView(DetailView):
#    model = Message


"""class MessageAddView(FormView):
    form_class = MessageForm
    template_name = 'contact/message_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.save() #form jest instancją ModelForm, który posiada metodę save()
        return super(MessageAddView, self).form_valid(form) #orginalnie form_valid nie robi nic, tylko zwraca 'success_url'
"""

class MessageAddView(FormView): # to co wyżej, druga metoda, bez korzystania z modelu, np. ankieta jakaś
    form_class = ContactForm
    template_name = 'contact/message_form.html'
    success_url = '/'
