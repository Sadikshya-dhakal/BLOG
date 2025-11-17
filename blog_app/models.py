from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.title




## 1 - 1 relation
# user can have only one profile => 1
# 1 profile belongs to only one user => 1
# OneToOneField() => any Model

## 1 - M relation
# user can add multiple posts => M
# 1 post belongs to only one user => 1
# ForeignKey() => use in Many side model

## M - M relation
# 1 student can learn from multiple teachers => M
# 1 teacher can teach multiple students => M
# ManyToManyField() => any place