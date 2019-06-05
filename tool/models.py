from django.db import models
from dashboard.models import CustomUser as User

# Create your models here.
class Tool(models.Model):
    title = models.CharField(max_length = 100)
    link = models.URLField(max_length = 255)
    desc = models.TextField()
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )

    def __unicode__(self):
       return '%s' % self.title