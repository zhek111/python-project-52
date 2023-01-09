from django.urls import reverse
from users.models import User
from django.test import TestCase


class TestUserModels(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name='Test', last_name='User', username='testuser')

    def test_user_create(self):
        user = User.objects.create(
            first_name='TestNew', last_name='User', username='testnewuser')

        self.assertEqual(user.first_name, 'TestNew')
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(user.last_name, 'User')
        self.assertEqual(user.username, 'testnewuser')

    def test_user_update(self):
        self.user.first_name = 'Updated'
        self.user.last_name = 'Name'
        self.user.save()
        self.assertEqual(self.user.first_name, 'Updated')
        self.assertEqual(self.user.last_name, 'Name')

    def test_user_delete(self):
        self.user.delete()
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(pk=self.user.pk)


class TestUserViews(TestCase):

    def test_user_create(self):
        response = self.client.post('/users/create/',
                                    {
                                        'first_name': 'zhek',
                                        'last_name': 'zhek',
                                        'username': 'zhek',
                                        "password1": "v09vu3rcu3r8j",
                                        "password2": "v09vu3rcu3r8j"
                                    })
        self.assertEqual(response.status_code, 302)

        user = User.objects.get(username="zhek")
        self.assertEqual(user.username, "zhek")
        self.assertEqual(self.client.get('/users/').context['users'].count(),
                         1)
        self.assertEqual(user.last_name, 'zhek')

    def test_user_update(self):
        User.objects.create_user(first_name='Test', last_name='User',
                                 username='testname', password='password123')
        user = User.objects.get(username="testname")

        self.client.login(username='testname', password='password123')
        response = self.client.post((reverse('update_user', args=[user.pk])), {
            'first_name': 'zhek',
            'last_name': 'zhek',
            'username': 'zhek',
            'password1': 'v09vu3rcu3r8j',
            'password2': 'v09vu3rcu3r8j'
        })
        self.assertEqual(response.status_code, 302)
        user.refresh_from_db()
        self.assertEqual(user.last_name, 'zhek')
        self.assertEqual(user.first_name, 'zhek')

    def test_user_delete(self):
        User.objects.create_user(first_name='Test', last_name='User',
                                 username='testname', password='password123')
        user = User.objects.get(username="testname")
        self.assertEqual(User.objects.count(), 1)
        self.client.login(username='testname', password='password123')
        response = self.client.post((reverse('delete_user', args=[user.pk])))
        self.assertEqual(response.status_code, 302)

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username='johndoe')
        self.assertEqual(User.objects.count(), 0)
