from django.contrib import admin

# Registrando o modelos criado
from .models import Category,Item
admin.site.register(Category)
#incluindo uma vizualização das tabelas criadas
admin.site.register(Item)
