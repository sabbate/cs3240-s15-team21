from django.contrib import admin
import SecureWitness.models


class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'password', 'reg_date', 'admin', 'email', 'privilege')


class GroupAdmin(admin.ModelAdmin):
    pass


class FileAdmin(admin.ModelAdmin):
    fields = ('docfile', 'file_name')


class ReportAdmin(admin.ModelAdmin):
    fields = ('report_name', 'short_desc', 'long_desc', 'location', 'keywords', 'private')


class FolderAdmin(admin.ModelAdmin):
    fields = ('folder_name', 'parent', 'GID')


class UserToGroupAdmin(admin.ModelAdmin):
    fields = ('UID', 'GID', 'leader', 'request_join')


admin.site.register(SecureWitness.models.User, UserAdmin)
admin.site.register(SecureWitness.models.Group, GroupAdmin)
admin.site.register(SecureWitness.models.File, FileAdmin)
admin.site.register(SecureWitness.models.Report, ReportAdmin)
admin.site.register(SecureWitness.models.Folder, FolderAdmin)
admin.site.register(SecureWitness.models.UserToGroup, UserToGroupAdmin)