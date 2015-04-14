from django.contrib import admin
import SecureWitness.models


class UserAdmin(admin.ModelAdmin):
    pass


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


admin.site.register(SecureWitness.models.User, UserAdmin)
admin.site.register(SecureWitness.models.Group, GroupAdmin)
admin.site.register(SecureWitness.models.File, FileAdmin)
admin.site.register(SecureWitness.models.Report, ReportAdmin)
admin.site.register(SecureWitness.models.Folder, FolderAdmin)
admin.site.register(SecureWitness.models.UserToGroup, UserToGroupAdmin)