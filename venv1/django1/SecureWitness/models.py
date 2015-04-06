from django.db import models
from django.contrib import admin
from django import forms
from datetime import datetime


class User(models.Model):
    UID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    reg_date = models.DateTimeField('date of registration')
    admin = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return self.username


class Group(models.Model):
    GID = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=100)
    size = models.IntegerField(default=1)
    users = models.ManyToManyField(User, through='UserToGroup')

    def __str__(self):
        return self.group_name


class File(models.Model):
    fileID = models.AutoField(primary_key=True)
    authorID = models.IntegerField()
    # author = models.ForeignKey(Users)
    ReportID = models.IntegerField()
    # report = models.ForeignKey(Reports) #many (files) to one (report) relationship
    content = models.CharField(max_length=1000)  #some kind of link to the actual file
    file_name = models.CharField(max_length=100)

    def __str__(self):
        return self.file_name


class Report(models.Model):
    RID = models.AutoField(primary_key=True)
    folderID = models.ForeignKey(File)  # the folder that this current report belongs to
    # folder = models.ForeignKey(Folders)
    authorID = models.IntegerField()
    # author = models.ForeignKey(Users)
    create_date = models.DateTimeField('date created')
    last_update_date = models.DateTimeField('date of last modification')
    report_name = models.CharField(max_length=200)

    def __str__(self):
        return self.report_name


class Folder(models.Model):
    folderID = models.AutoField(primary_key=True)
    authorID = models.IntegerField()
    # author = models.ForeignKey(Users)
    folder_name = models.CharField(max_length=100)
    parent = models.IntegerField()  # the folderID of the parent folder
    GID = models.IntegerField()

    def __str__(self):
        return self.folder_name


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
    pass


class ReportSharingGroup(models.Model):
    id = models.AutoField(primary_key=True)
    GID = models.ForeignKey(Group)
    sharing_date = models.DateTimeField(datetime.now())