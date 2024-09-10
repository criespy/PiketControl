from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse

class UserDetail(AbstractUser):
    is_ldap = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

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
    person = models.ForeignKey(UserDetail, on_delete=models.CASCADE) #diubah dari User menjadi UserDetail

    def get_absolute_url(self):
        return reverse('success', kwargs={'pk': self.pk})
    
    def __str__(self):
        return f'Check Point {self.pk} by {self.person}'

