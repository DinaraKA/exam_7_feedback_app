from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from webapp.models import Answer, Choice, Poll


class AnswerPollChoiceCreateView(View):
    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        return render(request, 'answers.html', {'poll': poll})

    def post(self, request, *args, **kwargs):
        poll_id = kwargs.get('pk')
        choice_id = int(request.POST.get('answer'))
        poll = get_object_or_404(Poll, pk=poll_id)
        choice = get_object_or_404(Choice, pk=choice_id)
        answer = Answer()
        answer.poll = poll
        answer.choice = choice
        answer.save()
        return redirect('poll_index')


class AnswersCount(View):
    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choices = Choice.objects.filter(pk=poll.pk).annotate(num_answers=Count('choice'))
        return  choices



