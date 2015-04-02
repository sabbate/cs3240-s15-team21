from django.contrib import admin
from SecureWitness.models import *


class GroupAdmin(admin.ModelAdmin):
    fields = ('group_name', 'size')


class FileAdmin(admin.ModelAdmin):
    pass


class ReportAdmin(admin.ModelAdmin):
    pass


class FolderAdmin(admin.ModelAdmin):
    pass


class UserToGroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(Group, GroupAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Folder, FolderAdmin)
admin.site.register(UserToGroup, UserToGroupAdmin)