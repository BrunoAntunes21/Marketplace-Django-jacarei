from django.db import models
from django.contrib.auth.models import User
#criação do modelo de dados
class Category(models.Model):
    name=models.CharField(max_length=255)
    #configurando para mostrar o db categorias
    class Meta:
        ordering=('name',)
        verbose_name_plural= "Categories"
        #configurando para mostrar as tebelas do db
    def __str__(self):
        return self.name
#criando os campos do db Item
class Item(models.Model):
    category=models.ForeignKey(Category,related_name='Item',on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    price=models.FloatField()
    image=models.ImageField(upload_to='item_images',blank=True,null=True)
    is_sold=models.BooleanField(default=False)
    created_by=models.ForeignKey(User,related_name='Items',on_delete=models.CASCADE)
    create_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name


