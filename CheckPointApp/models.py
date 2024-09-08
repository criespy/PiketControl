from django.db import models
from django.contrib.auth.models import User

class CpInputModel(models.Model):
    STATUS_CHOICES = (
        (True, 'Ya'),
        (False, 'Tidak')
    )

    mp_jumlah = models.BooleanField(choices=STATUS_CHOICES, default=False)
    mp_pos = models.BooleanField(choices=STATUS_CHOICES, default=False)
    material_jumlah = models.BooleanField(choices=STATUS_CHOICES, default=False)
    material_std = models.BooleanField(choices=STATUS_CHOICES, default=False)
    mesin_normal = models.BooleanField(choices=STATUS_CHOICES, default=False)
    metode_sesuai = models.BooleanField(choices=STATUS_CHOICES, default=False)
    plan_vs_actual = models.BooleanField(choices=STATUS_CHOICES, default=False)
    environment_aman = models.BooleanField(choices=STATUS_CHOICES, default=False)
    tanggal_check = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey(User, on_delete=models.CASCADE)

