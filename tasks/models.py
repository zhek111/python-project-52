from django.db import models
from labels.models import Label
from statuses.models import Status
from users.models import User
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        verbose_name=_('name')

    )
    description = models.TextField(verbose_name=_('description'))
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='tasks',
        verbose_name=_('status'))
    author = models.ForeignKey(User,
                               on_delete=models.PROTECT,
                               related_name='tasks_author',
                               verbose_name=_('author'))
    executor = models.ForeignKey(User,
                                 on_delete=models.PROTECT,
                                 related_name='tasks_executor',
                                 verbose_name=_('executor'))
    created_at = models.DateTimeField(auto_now_add=True)
    labels = models.ManyToManyField(Label,
                                    through='TaskLabel',
                                    blank=True,
                                    verbose_name=_('labels'))

    def __str__(self) -> str:
        return self.name


class TaskLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT, blank=True)
