from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
POSITIONS = (
    ('Asisten Ahli', 'Asisten_Ahli'),
    ('Lektor', 'Lektor'),
    ('Lektor Kepala', 'Lektor_Kepala'),
    ('Guru Besar/Professor', 'Guru_Besar_Professor')
)

class User(AbstractUser):
    POSITION_CHOICES = POSITIONS

    ROLE_CHOICES = (
        ('Dosen', 'Dosen'),
        ('Reviewer', 'Reviewer'),
        ('SDM PT', 'SDM_PT'),
        ('Admin', 'Admin')
    )

    username = models.CharField(max_length=254, primary_key=True, unique=True, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    password = models.CharField(max_length=254, blank=False)
    full_name = models.CharField(max_length=254, blank=False)
    university = models.CharField(max_length=254, blank=True, null=True)
    nip = models.PositiveIntegerField(null=True, blank=True)
    field_of_study = models.CharField(max_length=254, blank=True, null=True)
    position = models.CharField(max_length=254, choices=POSITION_CHOICES, blank=False)
    role = models.CharField(max_length=254, choices=ROLE_CHOICES, blank=False)
    approved = models.BooleanField(default=False)

    REQUIRED_FIELDS = []


class KaryaIlmiah(models.Model):
    STATUS_CHOICES = (
        ('Not Reviewed Yet', 'Not_Reviewed_Yet'),
        ('In Review', 'In_Review'),
        ('Done', 'Done'),
        ('Not Assigned Yet', 'Not_Assigned_Yet'),
        ('Requested', 'Requested'),
        ('Done', 'Done')
    )

    PROMOTION_LEVELS = POSITIONS

    karil_id = models.AutoField(primary_key=True)
    pemilik = models.ForeignKey(User, on_delete=models.CASCADE)
    judul = models.TextField(max_length=254)
    journal_data = models.TextField(max_length=None, blank=True, null=True)
    link_origin = models.TextField(max_length=None, blank=True, null=True)
    link_repo = models.TextField(max_length=None, blank=True, null=True)
    link_indexer = models.TextField(max_length=None, blank=True, null=True)
    link_simcheck = models.TextField(max_length=None, blank=True, null=True)
    link_correspondence = models.TextField(max_length=None, blank=True, null=True)
    indexer = models.TextField(max_length=254, blank=True, null=True)
    category = models.TextField(max_length=None)
    status = models.CharField(max_length=254, choices=STATUS_CHOICES)
    promotion = models.CharField(max_length=254, choices=PROMOTION_LEVELS)
    reviewers = models.ManyToManyField(User, blank=True, related_name='assigned_reviewers')
    reviews = models.ManyToManyField('Review', blank=True)

    REQUIRED_FIELDS = []


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    karil_id = models.ForeignKey(KaryaIlmiah, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    plagiarism_percentage = models.TextField(max_length=None)
    linearity = models.CharField(max_length=254)
    score_1 = models.DecimalField(max_digits=5, decimal_places=2)
    score_2 = models.DecimalField(max_digits=5, decimal_places=2)
    score_3 = models.DecimalField(max_digits=5, decimal_places=2)
    score_4 = models.DecimalField(max_digits=5, decimal_places=2)
    max_1 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    max_2 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    max_3 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    max_4 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    max_total = models.IntegerField(default=0)
    score_total = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    comment_1 = models.TextField(max_length=None, blank=True)
    comment_2 = models.TextField(max_length=None, blank=True)
    comment_3 = models.TextField(max_length=None, blank=True)
    comment_4 = models.TextField(max_length=None, blank=True)
    chosen_proposer = models.TextField(max_length=None, blank=True)
    score_proposer = models.DecimalField(max_digits=5, decimal_places=2)

    REQUIRED_FIELDS = []
