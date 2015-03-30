from django.db import models

# Create your models here.

class Users(models.Model):
    UID = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    reg_date = models.DateTimeField('date of registration')
    privilege = models.CharField(max_length=100)

class Reports(models.Model):
    RID = models.IntegerField()
    folderID = models.IntegerField() #the folder that this current report belongs to
    #folder = models.ForeignKey(Folders)
    authorID = models.IntegerField()
    #author = models.ForeignKey(Users)
    create_date = models.DateTimeField('date created')
    last_update_date = models.DateTimeField('date of last modification')


class Group(models.Model):
    GID = models.IntegerField()
    group_name = models.CharField(max_length=100)
    size = models.IntegerField(default=1)

class Files(models.Model):
    fileID = models.IntegerField()
    authorID = models.IntegerField()
    #author = models.ForeignKey(Users)
    ReportID = models.IntegerField()
    #report = models.ForeignKey(Reports) #many (files) to one (report) relationship
    content = models.CharField(max_length=1000) #some kind of link to the actual file
    file_name = models.CharField(max_length=100)

class Folders(models.Model):
    folderID = models.IntegerField()
    authorID = models.IntegerField()
    #author = models.ForeignKey(Users)
    folder_name = models.CharField(max_length=100)
    parent = models.IntegerField() #the folderID of the parent folder
    GID = models.IntegerField()

class Users_in_groups(models.Model):
    UID = models.IntegerField()
    GID = models.IntegerField()
    leader = models.BooleanField(default=False)





