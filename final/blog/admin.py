from django.contrib import admin

# Register your models here.
from blog.models import *

admin.site.register(User)
admin.site.register(Message)
admin.site.register(Addfriend)
admin.site.register(Group)
admin.site.register(Groupmember)
admin.site.register(Photo)
admin.site.register(Blog)
admin.site.register(Comment)