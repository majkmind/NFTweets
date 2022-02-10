from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32)


class Tag(models.Model):
    text = models.CharField(max_length=32)


class TwitterAcc(models.Model):
    username = models.CharField(max_length=64)
    user_id = models.BigIntegerField()
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    bio = models.CharField(max_length=200, blank=True)
    followers = models.ManyToManyField('self')


class NFT(models.Model):
    name = models.CharField(max_length=128)
    symbol = models.CharField(max_length=16, blank=True)
    url = models.CharField(max_length=128, blank=True)
    description = models.CharField(max_length=256, blank=True)
    tags = models.ManyToManyField('mood.Tag')


class Tweet(models.Model):
    author = models.ForeignKey('mood.TwitterAcc', on_delete=models.CASCADE)
    tags = models.ManyToManyField('mood.Tag')
    text = models.CharField(max_length=500)

