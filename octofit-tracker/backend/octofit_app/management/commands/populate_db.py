
from django.core.management.base import BaseCommand

from octofit_app.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from djongo.models import ObjectId
from datetime import timedelta
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'


    def handle(self, *args, **kwargs):
        # Drop collections using MongoClient
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(_id=ObjectId(), name='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
            User(_id=ObjectId(), name='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
            User(_id=ObjectId(), name='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword'),
            User(_id=ObjectId(), name='crashoverride', email='crashoverride@hmhigh.edu', password='crashoverridepassword'),
            User(_id=ObjectId(), name='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        blue_team = Team(_id=ObjectId(), name='Blue Team')
        gold_team = Team(_id=ObjectId(), name='Gold Team')
        blue_team.save()
        gold_team.save()
        for user in users:
            blue_team.members.add(user)
            gold_team.members.add(user)
        blue_team.save()
        gold_team.save()

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Cycling', duration=timedelta(hours=1)),
            Activity(_id=ObjectId(), user=users[1], activity_type='Crossfit', duration=timedelta(hours=2)),
            Activity(_id=ObjectId(), user=users[2], activity_type='Running', duration=timedelta(hours=1, minutes=30)),
            Activity(_id=ObjectId(), user=users[3], activity_type='Strength', duration=timedelta(minutes=30)),
            Activity(_id=ObjectId(), user=users[4], activity_type='Swimming', duration=timedelta(hours=1, minutes=15)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team=blue_team, points=100),
            Leaderboard(_id=ObjectId(), team=gold_team, points=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event', difficulty='medium'),
            Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition', difficulty='hard'),
            Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon', difficulty='medium'),
            Workout(_id=ObjectId(), name='Strength Training', description='Training for strength', difficulty='hard'),
            Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition', difficulty='medium'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
