from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Poll
from webapp.forms import PollForm


class PollIndexView(ListView):
    context_object_name = 'polls'
    model = Poll
    template_name = 'poll/poll_index.html'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1


class PollView(DetailView):
    context_object_name = 'poll'
    model = Poll
    pk_url_kwarg = 'pk'
    template_name = 'poll/poll.html'


class PollCreateView(CreateView):
    model = Poll
    template_name = 'poll/poll_create.html'
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_index')


class PollUpdateView(UpdateView):
    model = Poll
    template_name = 'poll/poll_update.html'
    form_class = PollForm
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_index')


class PollDeleteView(DeleteView):
    model = Poll
    context_object_name = 'poll'
    template_name = 'poll/poll_delete.html'
    success_url = reverse_lazy('poll_index')

