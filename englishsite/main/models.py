from django.db import models


class Tiles(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='tiles/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Course books'
        verbose_name_plural = 'Course books'
        ordering = ['id']


class RBooks(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='rbooks/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Books to read'
        verbose_name_plural = 'Books to read'
        ordering = ['id']


class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='games/images/')
    language = models.CharField(max_length=50)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class Dialogue(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    words = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class Voc(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class Word(models.Model):
    name = models.CharField(max_length=50)
    pronunciation = models.FileField(upload_to='vocabulary/audio/')
    transcription = models.CharField(max_length=50)
    definition = models.CharField(max_length=100)
    cat = models.ForeignKey('Voc', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name
