from django.db import models
'''from django.utils import timezone

# Create your models here.
class TestModel(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField()
    phone_number = models.PositiveIntegerField(null=False, error_messages={
        "null": "This field cannot be null",
    })
    amount = models.FloatField()
    extra_name = models.CharField(max_length=250, editable=False, default='null')
    is_alive = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = 'Test Model'

    def save(self, *args, **kwargs):
        # Overriding the save method
        self.extra_name = f"{self.name} - {self.phone_number}"
        super().save(*args, **kwargs)'''


'''class ModelX(models.Model):
    test_content = models.ForeignKey(TestModel, on_delete=models.CASCADE, related_name='test_content')
    mileage = models.FloatField()

    def __str__(self):
        return f"{self.test_content.name} - {self.mileage}"

    class Meta:
        verbose_name_plural = "ModelX"
        ordering = ["-mileage"]'''



class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        