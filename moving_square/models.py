from django.db import models

# Create your models here.
class GameResponse(models.Model):

    student_id = models.CharField(max_length=20)
    class_name = models.CharField(max_length=50)
    rolling_square = models.CharField(max_length=50)  # Specific value related to the Rolling Square system
    chapter = models.CharField(max_length=50)
    total_points = models.IntegerField()
    points_obtained = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)