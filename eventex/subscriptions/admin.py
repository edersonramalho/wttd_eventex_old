from django.contrib import admin
from django.utils.timezone import now

from eventex.subscriptions.models import Subscription


class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'cpf', 'create_at',
                    'subscribed_today')
    #para criar uma hierarquia de datas
    date_hierarchy = 'create_at'
    #pesquisa
    search_fields = ('name', 'email', 'phone', 'cpf', 'create_at')
    
    list_filter = ('create_at',)
    
    def subscribed_today(self, obj):#metodo padrão do django
        return obj.create_at == now().date()
    
    #injetando um atributo no obj "subscribed_today" 
    subscribed_today.short_description = 'inscrito hoje?'
    subscribed_today.boolean = True
    

admin.site.register(Subscription, SubscriptionModelAdmin)