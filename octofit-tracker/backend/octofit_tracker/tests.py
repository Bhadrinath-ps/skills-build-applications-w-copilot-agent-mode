from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team='Test Team')
        self.activity = Activity.objects.create(user='testuser', team='Test Team', type='Running', duration=30)
        self.leaderboard = Leaderboard.objects.create(team='Test Team', points=100)
        self.workout = Workout.objects.create(name='Test Workout', description='Desc', suggested_for='Test Team')

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_activity_str(self):
        self.assertEqual(str(self.activity), 'testuser - Running')

    def test_leaderboard_str(self):
        self.assertEqual(str(self.leaderboard), 'Test Team: 100')

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Test Workout')
