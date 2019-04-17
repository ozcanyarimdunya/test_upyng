from django.db import models as models
from django.urls import reverse_lazy


class Demo(models.Model):
    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    logo = models.ImageField(upload_to="upload/images/")
    document = models.FileField(upload_to="upload/files/")

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('demo:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse_lazy('demo:update', args=(self.pk,))

    def get_delete_url(self):
        return reverse_lazy('demo:delete', args=(self.pk,))
