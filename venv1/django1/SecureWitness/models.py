from django.db import models
from datetime import datetime


class User(models.Model):
    UID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    reg_date = models.DateTimeField('date of registration')
    admin = models.BooleanField(default=False)
    email = models.EmailField()
    privilege = models.CharField(max_length=100, default='DEFAULT VALUE')

    def __str__(self):
        return self.username


class Group(models.Model):
    GID = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, through='UserToGroup')

    def __str__(self):
        return self.group_name


class Folder(models.Model):
    folderID = models.AutoField(primary_key=True)
    authorID = models.ForeignKey(User)
    folder_name = models.CharField(max_length=100)
    parent = models.ForeignKey("self")
    GID = models.ForeignKey(Group)

    def __str__(self):
        return self.folder_name


class Report(models.Model):
    RID = models.AutoField(primary_key=True)
    folderID = models.ForeignKey(Folder)
    authorID = models.ForeignKey(User)
    create_date = models.DateTimeField('date created')
    last_update_date = models.DateTimeField('date of last modification')
    report_name = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=150, default='DEFAULT VALUE')
    long_desc = models.CharField(max_length=300, default='DEFAULT VALUE')
    location = models.CharField(max_length=300, default='DEFAULT VALUE')
    incident_date = models.CharField(max_length=300, default='DEFAULT VALUE')
    keywords = models.CharField(max_length=300, default='DEFAULT VALUE')
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.report_name


class File(models.Model):
    fileID = models.AutoField(primary_key=True)
    authorID = models.ForeignKey(User)
    ReportID = models.ForeignKey(Report)
    docfile = models.FileField(upload_to='files/', default=False)
    file_name = models.CharField(max_length=100)

    def __str__(self):
        return self.file_name


class UserToGroup(models.Model):
    # Intermediary model between User and Group
    ID = models.AutoField(primary_key=True)
    UID = models.ForeignKey(User)
    GID = models.ForeignKey(Group)
    leader = models.BooleanField(default=False)
    request_join = models.BooleanField(default=False)  # If true, user is not in group, but wants to join


class ReportSharingUser(models.Model):
    id = models.AutoField(primary_key=True)
    UID = models.ForeignKey(User)
    sharing_date = models.DateTimeField(datetime.now())


class ReportSharingGroup(models.Model):
    id = models.AutoField(primary_key=True)
    GID = models.ForeignKey(Group)
    sharing_date = models.DateTimeField(datetime.now())