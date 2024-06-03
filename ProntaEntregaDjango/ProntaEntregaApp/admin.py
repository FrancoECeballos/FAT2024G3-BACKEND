from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('nombreusuario', 'password')}),
        ('Personal info', {'fields': ('nombre', 'apellido', 'email', 'documento', 'telefono', 'genero', 'id_direccion', 'id_tipousuario', 'id_tipodocumento', 'fecha_union')}),
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

admin.site.register(Usuario, CustomUserAdmin)

# Register your models here.

admin.site.register(Casa)
admin.site.register(Categoriaproducto)
admin.site.register(Detallecasausuario)
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