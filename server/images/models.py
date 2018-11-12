from django.db import models

class Image(models.Model):
<<<<<<< HEAD
    title = models.CharField(max_length=150)
    value = models.ImageField(upload_to='images')

    def __str__(self):
        return self.value.url
=======
    title = models.CharField(max_length = 150)
    value = models.ImageField(upload_to = "images")

    def __str__(self):
        return self.value.url



>>>>>>> 070b20a43dd7b4b011c26b3d783235212c88555d
