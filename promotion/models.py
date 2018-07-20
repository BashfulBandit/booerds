from django.db import models

# Create your models here.
class Promotion(models.Model):
	name = models.CharField(
		max_length=255,
		blank=False,
	)
	valid_from = models.DateField(
		blank=False,
	)
	valid_to = models.DateField(
		blank=False,
	)
	promocode = models.CharField(
		max_length=10,
		blank=False,
	)
	discount = models.DecimalField(
		decimal_places=2,
		max_digits=10,
		blank=False,
	)
	details = models.TextField(
		blank=False,
	)
	frontpage = models.BooleanField(
		default=False,
	)

	def __str__(self):
		return self.name
