from django.contrib import admin

from .models import Status, Services, Visits, Client, Products, Sale, Post, SaleCheck, Salerman, Discount


class VisitsAdminSite(admin.ModelAdmin):
    actions = ['delete']
    model = Visits
    list_display = ( 'visit_number', 'service_name', 'fio_client', 'fio_staff', 'price')
    fields = ['visit_number', 'service_name', 'fio_client', 'fio_staff', 'price']

    def delete(self, request, queryset):
        row_update = queryset.update(price=0, visit_number=0, fio_client='', service_name='', fio_staff='')

    delete.short_description = "Отчистить"
    delete.allowed_permissions = ('change',)


admin.site.register(Status)
admin.site.register(Products)
admin.site.register(Post)
admin.site.register(Salerman)
admin.site.register(Services)
admin.site.register(Sale)
admin.site.register(SaleCheck)
admin.site.register(Visits, VisitsAdminSite)
admin.site.register(Client)
admin.site.register(Discount)

