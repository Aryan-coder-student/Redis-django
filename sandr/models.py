from django.db import models
import uuid
# Create your models here.
class tags(models.Model):
    discount = models.BooleanField(default=False)
    
    
class products_model(models.Model):
    product_image = models.ImageField(upload_to="product_img/",db_index=True)
    products_name = models.CharField(max_length=200,db_index=True)
    product_id =  models.UUIDField(primary_key=True,default =uuid.uuid4,db_index=True)
    dis = models.ForeignKey(tags , on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.products_name
    
