from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('nombreusuario', 'password')}),
        ('Personal info', {'fields': ('nombre', 'apellido', 'email', 'documento', 'telefono', 'genero', 'id_direccion', 'id_tipousuario', 'id_tipodocumento')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nombreusuario', 'nombre', 'apellido', 'password1', 'password2'),
        }),
    )
    list_display = ('nombreusuario', 'nombre', 'apellido', 'email', 'is_staff', 'is_superuser')
    search_fields = ('nombreusuario', 'nombre', 'apellido', 'email')
    ordering = ('nombreusuario',)

admin.site.register(CustomUsuario, CustomUserAdmin)


class DetallecasausuarioAdmin(admin.ModelAdmin):
    list_display = ('id_detallecasausuario', 'descripcion', 'fechaingreso', 'id_casa', 'id_usuario')
    list_filter = ('id_casa', 'id_usuario')
    search_fields = ('id_casa__nombre', 'id_usuario__nombreusuario', 'descripcion')
    ordering = ('id_detallecasausuario',)  # Cambiado de 'id' a 'id_detallecasausuario'

admin.site.register(Detallecasausuario, DetallecasausuarioAdmin)


# Register your models here.

admin.site.register(Casa)
admin.site.register(Categoriaproducto)
admin.site.register(Detalleoferta)
admin.site.register(Detallepedido)
admin.site.register(Detallestockproducto)
admin.site.register(Direccion)
admin.site.register(Estadooferta)
admin.site.register(Estadopedido)
admin.site.register(Oferta)
admin.site.register(Organizacion)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Stock)
admin.site.register(Tipodocumento)
admin.site.register(Tipousuario)
admin.site.register(Transporte)
admin.site.register(Unidadmedida)