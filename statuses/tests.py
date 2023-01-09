from django.urls import reverse
from django.test import TestCase
from statuses.models import Status
from users.models import User


class TestStatusesViews(TestCase):

    def setUp(self) -> None:
        User.objects.create_user(first_name='Test', last_name='User',
                                 username='testname', password='password123')
        self.client.login(username='testname', password='password123')

    def test_status_create(self):
        response = self.client.post('/statuses/create/', {'name': 'status1'})
        self.assertEqual(response.status_code, 302)

        status = Status.objects.get(name="status1")
        self.assertEqual(status.name, "status1")
        self.assertEqual(
            self.client.get('/statuses/').context['statuses'].count(), 1)

    def test_status_update(self):
        self.client.post('/statuses/create/', {'name': 'status1'})
        status = Status.objects.get(name="status1")
        response = self.client.post(
            (reverse('update_status', args=[status.pk])), {'name': 'status2'})
        self.assertEqual(response.status_code, 302)
        status.refresh_from_db()
        self.assertEqual(status.name, 'status2')

    def test_status_delete(self):
        self.client.post('/statuses/create/', {'name': 'status1', })
        status = Status.objects.get(name="status1")
        self.assertEqual(Status.objects.count(), 1)

        response = self.client.post(reverse('delete_status', args=[status.pk]))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Status.DoesNotExist):
            Status.objects.get(name='status1')
        self.assertEqual(Status.objects.count(), 0)
