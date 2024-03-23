from django.db import models

class Book(models.model):
    judul = models.charfield(max_length=200)
    publish = models.DateTimeField("Tanggal publikasi")

    def __str__(self):
        return self.judul 
    
