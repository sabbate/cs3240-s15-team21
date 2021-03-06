from django.contrib import admin
import SecureWitness.models


class FileAdmin(admin.ModelAdmin):
    fields = ('docfile', 'file_name', 'author', 'report')


class ReportAdmin(admin.ModelAdmin):
    fields = (
        'report_name', 'author_id', 'folder_id', 'group_id', 'short_desc', 'long_desc', 'location', 'keywords',
        'private', 'create_date', 'last_update_date')


class FolderAdmin(admin.ModelAdmin):
    fields = ('folder_name', 'author_id', 'parent', 'GID')


class UserToGroupAdmin(admin.ModelAdmin):
    fields = ('user_id', 'group_id', 'leader')


#class ReportUserSharingAdmin(admin.ModelAdmin):
 #    fields = ('report', 'user')

class ReportGroupSharingAdmin(admin.ModelAdmin):
    fields = ('report', 'group')


admin.site.register(SecureWitness.models.File, FileAdmin)
admin.site.register(SecureWitness.models.Report, ReportAdmin)
admin.site.register(SecureWitness.models.Folder, FolderAdmin)
admin.site.register(SecureWitness.models.UserToGroup, UserToGroupAdmin)
#admin.site.register(SecureWitness.models.ReportUserSharing, ReportUserSharingAdmin)
admin.site.register(SecureWitness.models.ReportGroupSharing, ReportGroupSharingAdmin)
#admin.site.register(SecureWitness.models.ReportGroupSharing, ReportGroupSharingAdmin)

