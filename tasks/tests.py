from django.urls import reverse
from django.test import TestCase
from labels.models import Label
from statuses.models import Status
from tasks.models import Task
from users.models import User


class TestTaskViews(TestCase):

    def setUp(self) -> None:
        User.objects.create_user(
            first_name='Test', last_name='User', username='testname',
            password='password123')
        self.client.login(username='testname', password='password123')
        self.client.post('/statuses/create/', {'name': 'status1'})
        self.client.post('/labels/create/', {'name': 'label1'})

    def test_task_create(self):
        self.assertEqual(User.objects.first().id, 7)
        self.assertEqual(Status.objects.first().id, 4)
        self.assertEqual(Label.objects.first().id, 4)
        response = self.client.post('/tasks/create/',
                                    {
                                        'name': 'task1',
                                        'description': 'descriptiontask1',
                                        'executor': User.objects.first().id,
                                        'status': 4,
                                        'labels': Label.objects.first().id,
                                        'author': User.objects.first().id
                                    })
        self.assertEqual(response.status_code, 302)
        task = Task.objects.get(name="task1")
        self.assertEqual(task.name, "task1")
        self.assertEqual(self.client.get('/tasks/').context['tasks'].count(),
                         1)

    def test_task_update(self):
        self.assertEqual(User.objects.first().id, 8)
        self.assertEqual(Status.objects.first().id, 5)
        self.assertEqual(Label.objects.first().id, 5)
        response = self.client.post('/tasks/create/',
                                    {
                                        'name': 'task1',
                                        'description': 'descriptiontask1',
                                        'executor': 8,
                                        'status': 5,
                                        'labels': 5,
                                        'author': 8
                                    })
        self.assertEqual(response.status_code, 302)
        task = Task.objects.get(name="task1")
        response = self.client.post((reverse('update_task', args=[task.pk])),
                                    {
                                        'name': 'task2',
                                        'description': 'descriptiontask2',
                                        'executor': 8,
                                        'status': 5,
                                        'labels': 5,
                                        'author': 8
                                    })
        self.assertEqual(response.status_code, 302)
        task.refresh_from_db()
        self.assertEqual(task.name, 'task2')
