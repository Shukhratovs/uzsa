from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    location_url = models.URLField()
    banner = models.ImageField(upload_to="events/")

    def __str__(self):
        return self.title

    def get_all_images(self):
        return self.eventimage_set.all()


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="events/images/")

    def __str__(self):
        return self.event.title
