from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

class Korisnici(AbstractUser):
    
    email = models.EmailField(verbose_name="email", max_length=64, unique=True )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']

    MENTOR = 'mentor'
    STUDENT = 'student'
    ROLES = (
        (MENTOR, _('mentor')),
        (STUDENT, _('student')),
    )
    role = models.CharField(_('role'), default=STUDENT, choices=ROLES, max_length=20)

    NONE = 'none'
    REDOVNI = 'redovni'
    IZVANREDNI='izvanredni'
    STATUSES=(
        (NONE, _('none')),
        (REDOVNI, _('redovni')),
        (IZVANREDNI, _('izvanredni')),
    )
    status = models.CharField(_('status'), default=NONE, choices=STATUSES, max_length=20)
    
    def __str__(self):
        return self.email



class Predmeti(models.Model):
    ime = models.CharField(max_length=255, unique=True)
    kod = models.CharField(max_length=16, primary_key=True, unique=True )
    program = models.CharField(max_length=225)
    ECTS = models.IntegerField()
    sem_redovni = models.IntegerField()
    sem_izvanredni = models.IntegerField()
    
    DA = 'da'
    NE = 'ne'
    IZBORNI=(
        (DA, _('da')),
        (NE, _('ne')),
    )
    izborni = models.CharField(_('izborni'), default=NE, choices=IZBORNI, max_length=10)

    def __str__(self):
        return self.ime

class Upisi(models.Model):
    student = models.ForeignKey(Korisnici, on_delete=models.CASCADE)
    predmet = models.ForeignKey(Predmeti, on_delete=models.CASCADE)

    POLOŽENO = 'položeno'
    NEPOLOŽENO = 'nepoloženo'
    IZBOR=(
        (POLOŽENO, _('položeno')),
        (NEPOLOŽENO, _('nepoloženo')),
    )

    status = models.CharField(_('status'), default=NEPOLOŽENO, choices=IZBOR, max_length=20)
    class Meta:
        unique_together = [['student','predmet']]