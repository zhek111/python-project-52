from django.urls import reverse
from django.test import TestCase
from labels.models import Label
from users.models import User


class TestLabelsViews(TestCase):

    def setUp(self) -> None:
        User.objects.create_user(
            first_name='Test', last_name='User', username='testname',
            password='password123')
        self.client.login(username='testname', password='password123')

    def test_label_create(self):
        response = self.client.post('/labels/create/', {'name': 'label1'})
        self.assertEqual(response.status_code, 302)

        label = Label.objects.get(name="label1")
        self.assertEqual(label.name, "label1")
        self.assertEqual(self.client.get('/labels/').context['labels'].count(),
                         1)

    def test_label_update(self):
        self.client.post('/labels/create/', {'name': 'label1'})
        label = Label.objects.get(name="label1")
        response = self.client.post((reverse('update_label', args=[label.pk])),
                                    {'name': 'label2'})
        self.assertEqual(response.status_code, 302)
        label.refresh_from_db()
        self.assertEqual(label.name, 'label2')

    def test_label_delete(self):
        self.client.post('/labels/create/', {'name': 'label1'})
        label = Label.objects.get(name="label1")
        self.assertEqual(Label.objects.count(), 1)

        response = self.client.post(reverse('delete_label', args=[label.pk]))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Label.DoesNotExist):
            Label.objects.get(name='label1')
        self.assertEqual(Label.objects.count(), 0)
