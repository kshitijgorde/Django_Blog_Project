from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    ''' This is a generic class to handle blog Posts made by a superuser '''

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now())
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        ''' Flexibility to publish at current date or save as a draft '''

        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        ''' The Blog User can approve the comments first, only then they can appear in the post. '''
        return self.comments.filter(approved_comments = True) #Filter comments which are True

    def get_absolute_url(self):
        # Let's go back to the blog details page after creating one.
        return reverse("post_detail", kwargs = {'pk': self.pk})


    def __str__(self):
        ''' String representation of the POST class '''
        return self.title

class Comment(models.Model):
    ''' Generic class to represent user comments connected to a blog post '''

    post = models.ForeignKey('blog_app.Post', related_name = 'comments')
    author = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now())
    approved_comment = models.BooleanField(default = False) # By default, the comment will not be approved. Only su can approve

    def approve(self):
        ''' Approve a comment '''
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        # Go back to the main homepage
        return reverse('post_list')

    def __str__(self):
        return self.text
