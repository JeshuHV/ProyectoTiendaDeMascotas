from dataclasses import fields
from django import forms
from .models import Contacto, Producto

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = ["nombre",
                "nombre_mascota",
                "tipo_consulta", 
                "mensaje", 
                "avisos"]

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__'