from django.contrib import admin

# We want to register our models
from .models import Event,PLOT,FARM,CONSTRUCTION,AGRICULTURE,CONSULTANT,UNDERGRADUATE,MICROCREDIT,EDUCATION,Broker,Contact,Suscribe
admin.site.register(Event)
admin.site.register(PLOT)
admin.site.register(FARM)
admin.site.register(CONSTRUCTION)
admin.site.register(AGRICULTURE)
admin.site.register(CONSULTANT)
admin.site.register(UNDERGRADUATE)
admin.site.register(MICROCREDIT)
admin.site.register(EDUCATION)
admin.site.register(Broker)
admin.site.register(Contact)
admin.site.register(Suscribe)


# To modify Django Site Administration
admin.site.site_header='CDQLINK Admininistration' # default Django Administration
admin.site.index_title='CDQLINK Panel'    # default Site Administration
admin.site.site_title='CDQLINK site Admin'  # default Django site admin

# username='admin'
# password='cdqlink123'


