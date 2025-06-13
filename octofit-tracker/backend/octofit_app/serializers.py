from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, required=False)
    class Meta:
        model = Team
        fields = ['id', 'name', 'members']

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'timestamp']

class LeaderboardSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'points']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'difficulty']
