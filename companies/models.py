# models.py

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Company(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)

    address = models.CharField(max_length=100, default='Not Found')
    phone = models.CharField(max_length=20, default='Not Found')
    website = models.URLField(default='Not Found')
    products = models.TextField(default='Not Found')
    linkedin_url = models.URLField(default='Not Found')

    def get_contacts(self):
        return self.contact_set.all()

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class FollowUp(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    date = models.DateField()
    notes = models.TextField()

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed')
    ]

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Follow up for {self.company.name}"
