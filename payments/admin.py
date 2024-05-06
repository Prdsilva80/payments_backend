from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'amount', 'date', 'status')
    search_fields = ('payment_id',)

admin.site.register(Payment, PaymentAdmin)
