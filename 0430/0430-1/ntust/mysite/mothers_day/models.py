from django.db import models

# Create your models here.
class Message(models.Model):
	username=models.CharField(max_length=256)
	title=models.CharField(max_length=512)
	content=models.TextField(max_length=256)
	publish=models.DateTimeField("Time")

	def __str__(self):
		return self.username +"("+ self.publish.strftime('%Y-%m-%d %H:%M')+"):"+self.title