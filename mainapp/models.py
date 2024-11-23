from django.db import models
from django.core.exceptions import ValidationError

APPOINTMENT_TIMES = [
    (f"{hour:02}:00", f"{hour:02}:00") for hour in range(7, 24)
] + [(f"{hour:02}:30", f"{hour:02}:30") for hour in range(7, 23)]

APPOINTMENT_TIMES.sort()

class Order(models.Model):
    

    apartment_number = models.PositiveIntegerField("Номер квартиры")
    pet_name = models.CharField("Кличка питомца", max_length=50)
    pet_breed = models.CharField("Порода питомца", max_length=100)
    walk_date = models.DateField("Дата прогулки")
    walk_time = models.TimeField("Время прогулки", choices=APPOINTMENT_TIMES)
    walker = models.CharField(
        "Кто выгуливает", max_length=10, choices=[("Петр", "Петр"), ("Антон", "Антон")]
    )

    def clean(self):
        if self.walk_time not in dict(APPOINTMENT_TIMES):
            raise ValidationError("Прогулка должна начинаться либо в начале часа, либо в половину.")
        
        overlapping_orders = Order.objects.filter(
            walk_date=self.walk_date,
            walk_time=self.walk_time,
            walker=self.walker
        ).exists()
        if overlapping_orders:
            raise ValidationError("Этот временной слот уже занят.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
