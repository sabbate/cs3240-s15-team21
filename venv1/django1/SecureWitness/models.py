from django.db import models
from django.contrib import admin


class User(models.Model):
    UID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    reg_date = models.DateTimeField('date of registration')
    admin = models.BooleanField(default=False)


class Group(models.Model):
    GID = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=100)
    size = models.IntegerField(default=1)


class File(models.Model):
    fileID = models.AutoField(primary_key=True)
    authorID = models.IntegerField()
    #author = models.ForeignKey(Users)
    ReportID = models.IntegerField()
    #report = models.ForeignKey(Reports) #many (files) to one (report) relationship
    content = models.CharField(max_length=1000) #some kind of link to the actual file
    file_name = models.CharField(max_length=100)


class Report(models.Model):
    RID = models.AutoField(primary_key=True)
    folderID = models.ForeignKey(File) #the folder that this current report belongs to
    #folder = models.ForeignKey(Folders)
    authorID = models.IntegerField()
    #author = models.ForeignKey(Users)
    create_date = models.DateTimeField('date created')
    last_update_date = models.DateTimeField('date of last modification')


class Folder(models.Model):
    folderID = models.AutoField(primary_key=True)
    authorID = models.IntegerField()
    # author = models.ForeignKey(Users)
    folder_name = models.CharField(max_length=100)
    parent = models.IntegerField() #the folderID of the parent folder
    GID = models.IntegerField()


class UserToGroup(models.Model):
    ID = models.AutoField(primary_key=True)
    UID = models.ManyToManyField(User)
    GID = models.ManyToManyField(Group)
    leader = models.BooleanField(default=False)

admin.site.register(Group)
admin.site.register(File)
admin.site.register(Report)
admin.site.register(Folder)
admin.site.register(UserToGroup)

