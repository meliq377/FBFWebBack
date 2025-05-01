from django.db import models

# Create your models here.


class Lesson(models.Model):
    lesson_title = models.CharField(max_length=100)
    lesson_description = models.CharField(max_length=1000)
    lesson_image = models.ImageField(upload_to='media/')
    lesson_video = models.FileField(upload_to='videos/', blank=True, null=True)

    def __str__(self):
        return self.lesson_title    
    
class Module(models.Model):
    module_title = models.CharField(max_length=100)
    module_description = models.CharField(max_length=1000)
    module_image = models.ImageField(upload_to='media/', blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.module_title
    
class Slide(models.Model):
    slide_title = models.CharField(max_length=100)
    slide_text = models.TextField(max_length=1000)
    slide_image = models.ImageField(upload_to='media/')
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.slide_title
    
class Quiz(models.Model):
    slide = models.ForeignKey(Slide, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=100)

    def __str__(self):
        return self.slide.slide_title