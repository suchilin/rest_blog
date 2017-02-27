from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s' % self.title

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    @permalink
    def get_absolute_url(self):
        return ('post-detail',(),{
                'slug':self.slug
            })
