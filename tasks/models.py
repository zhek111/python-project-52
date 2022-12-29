
from django.db import models

from labels.models import Labels
from statuses.models import Statuses
from users.models import User

from django.utils.translation import gettext as _


class Tasks(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        verbose_name=_('name')

    )
    description = models.TextField(verbose_name=_('description'))
    status = models.ForeignKey(
        Statuses,
        on_delete=models.PROTECT,
        related_name='tasks')
    author = models.ForeignKey(User,
                               on_delete=models.PROTECT,
                               related_name='tasks_author',
                               verbose_name=_('author'))
    executor = models.ForeignKey(User,
                                 on_delete=models.PROTECT,
                                 related_name='tasks_executor',
                                 verbose_name=_('executor'))
    created_at = models.DateTimeField(auto_now_add=True)
    labels = models.ManyToManyField(Labels, through='TaskLabel')

    def __str__(self) -> str:
        return self.name


class TaskLabel(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.PROTECT)
    label = models.ForeignKey(Labels, on_delete=models.PROTECT)
