from django.db import models


class Poll(models.Model):
    question=models.TextField(max_length=100, verbose_name='Question')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created date')

    def __str__(self):
        return self.question


class Choice(models.Model):
    text=models.TextField(max_length=500, verbose_name='Text')
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE, verbose_name='Poll')

    def __str__(self):
        return self.text


class Answer(models.Model):
    poll = models.ForeignKey(Poll, related_name='poll_answers', on_delete=models.CASCADE, verbose_name='Poll')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    choice = models.ForeignKey(Choice, related_name='choice_answers', on_delete=models.CASCADE, verbose_name='Choice')

    def __str__(self):
        return '{} | {}'.format(self.poll, self.choice)

