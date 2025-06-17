from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200 )
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_imgae=models.CharField(max_length=500, default="https://www.thefuzzyduck.co.uk/wp-content/uploads/2024/05/image-coming-soon-placeholder-01-660x660.png")
    
    def __str__(self):
        return str(self.item_name)
    