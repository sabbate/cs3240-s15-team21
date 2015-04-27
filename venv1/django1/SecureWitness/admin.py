from django.contrib import admin
import SecureWitness.models


class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'password', 'reg_date', 'admin', 'email', 'privilege')


class GroupAdmin(admin.ModelAdmin):
    pass


class FileAdmin(admin.ModelAdmin):
    fields = ('docfile', 'file_name', 'author', 'report')


class ReportAdmin(admin.ModelAdmin):
    fields = (
        'report_name', 'author_id', 'folder_id', 'group_id', 'short_desc', 'long_desc', 'location', 'keywords',
        'private')


class FolderAdmin(admin.ModelAdmin):
    fields = ('folder_name', 'author_id', 'parent', 'GID')


class UserToGroupAdmin(admin.ModelAdmin):
    fields = ('user_id', 'group_id', 'leader')


# admin.site.register(SecureWitness.models.User, UserAdmin)
# admin.site.register(SecureWitness.models.Group, GroupAdmin)
admin.site.register(SecureWitness.models.File, FileAdmin)
admin.site.register(SecureWitness.models.Report, ReportAdmin)
admin.site.register(SecureWitness.models.Folder, FolderAdmin)
admin.site.register(SecureWitness.models.UserToGroup, UserToGroupAdmin)