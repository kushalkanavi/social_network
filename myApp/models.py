from django.db import models
from django.contrib.auth.models import User

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others')
)


class UserProfile(models.Model):
    user_profile_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=120, null=True)
    lastname = models.CharField(max_length=120, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=20, choices=GENDER, default='')
    location = models.CharField(max_length=120, null=True)
    photo = models.ImageField(upload_to='User_Profile/%Y/%m/%d/', default='blank')
    interests = models.CharField(max_length=120, null=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname

class UserFriends(models.Model):
    user_friend_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='from_user', to_field='user_profile_id', null=True)
    friend_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='to_user', to_field='user_profile_id', null=True)

    def __str__(self):
        return str(self.user)
