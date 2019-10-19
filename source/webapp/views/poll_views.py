from django.core.paginator import Paginator
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
    template_name = 'poll/poll.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        choices = context['poll'].choices.all()
        self.paginate_choices_to_context(choices, context)
        return context

    def paginate_choices_to_context(self, choices, context):
        paginator = Paginator(choices, 3, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['tasks'] = page.object_list
        context['is_paginated'] = page.has_other_pages()


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

