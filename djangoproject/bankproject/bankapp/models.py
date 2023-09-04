from django.db import models

class District(models.Model):
    name = models.CharField(max_length=100)
    wikipedia_url = models.URLField(blank=True)


    def __str__(self):
        return self.name

class SubArea(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    subarea = models.ForeignKey(SubArea, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AccountType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Customer(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    # username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20)
    mail_id = models.EmailField()
    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    subarea = models.ForeignKey(SubArea, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    materials_provide = models.ManyToManyField(Material, blank=True)


    def __str__(self):
        return self.name
