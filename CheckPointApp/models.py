from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class CpInputModel(models.Model):
    STATUS_CHOICES = (
        (True, 'Ya'),
        (False, 'Tidak')
    )

    mp_jumlah = models.BooleanField(choices=STATUS_CHOICES, default=False, null=False)
    mp_pos = models.BooleanField(choices=STATUS_CHOICES, default=False, null=False)
    material_jumlah = models.BooleanField(choices=STATUS_CHOICES, default=False,null=False)
    material_std = models.BooleanField(choices=STATUS_CHOICES, default=False, null=False)
    mesin_normal = models.BooleanField(choices=STATUS_CHOICES, default=False, null=False)
    metode_sesuai = models.BooleanField(choices=STATUS_CHOICES, default=False, null=False)
    plan_vs_actual = models.BooleanField(choices=STATUS_CHOICES, default=False, null=False)
    environment_aman = models.BooleanField(choices=STATUS_CHOICES, default=False, null=False)
    tanggal_check = models.DateTimeField(auto_now_add=True, null=False)
    person = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('success', kwargs={'pk': self.pk})
    
    def __str__(self):
        return f'Check Point {self.pk} by {self.person}'

