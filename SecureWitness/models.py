from django.db import models
from datetime import *
from django.contrib.auth.models import User, Group, Permission
# notes: django's default group model has two fields, id and name. which is enough for our implementation

'''
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    reg_date = models.DateTimeField('date of registration')
    admin = models.BooleanField(default=False)
    email = models.EmailField()
    privilege = models.CharField(max_length=100, default='DEFAULT VALUE')

    def __str__(self):
        return self.username
'''


class GroupProfile(models.Model):
    group = models.OneToOneField(Group, unique=True)  # Group model imported from django
    datetime = models.DateTimeField('date created')

    def __str__(self):
        return self.group_name


'''
class File(models.Model):
    fileID = models.AutoField(primary_key=True)
    author_id = models.ForeignKey(User)
    report_id = models.ForeignKey(Report)
    content = models.CharField(max_length=1000)  # some kind of link to the actual file
    docfile = models.FileField(upload_to='files/', default=False)  # some kind of link to the actual file
    file_name = models.CharField(max_length=100)
'''


class Folder(models.Model):
    folder_id = models.AutoField(primary_key=True)
    author_id = models.ForeignKey(User)
    folder_name = models.CharField(max_length=100)
    parent = models.ForeignKey("self", blank=True, null=True)
    GID = models.ForeignKey(Group)

    def __str__(self):
        return self.folder_name


class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    # <<<<<<< HEAD
    folder = models.ForeignKey(Folder, default=0)
    author = models.ForeignKey(User)
    #create_date = models.DateTimeField('date created')
    #last_update_date = models.DateTimeField('date of last modification')
    # =======
    #folder_id = models.ForeignKey(Folder, blank=True, null=True)
    #group_id = models.ForeignKey(Group, blank=True, null=True)
    group = models.ForeignKey(Group, blank=True, null=True)
    #author_id = models.ForeignKey(User)
    create_date = models.DateTimeField('date created', default=datetime.now())
    last_update_date = models.DateTimeField('date of last modification', default=datetime.now())

    # >>>>>>> 34f645a9f0350f3f3fe5b36d71f7902221a8cfbf

    report_name = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=150, default='DEFAULT VALUE')
    long_desc = models.CharField(max_length=300, default='DEFAULT VALUE')
    location = models.CharField(max_length=300, default='DEFAULT VALUE')
    incident_date = models.CharField(max_length=300, default='DEFAULT VALUE')
    keywords = models.CharField(max_length=300, default='DEFAULT VALUE')
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.report_name + " by " + self.author_id.username


class File(models.Model):
    file_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User)
    report = models.ForeignKey(Report)
    docfile = models.FileField(upload_to='files/', default=False)
    file_name = models.CharField(max_length=100)

    def __str__(self):
        return self.file_name


class UserToGroup(models.Model):
    # Intermediary model between User and Group
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    group_id = models.ForeignKey(Group)
    leader = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id.username + " of " + self.group_id.name


class ActivationProfile(models.Model):
    activation_key = models.CharField(max_length=300, default='DEFAULT VALUE')
    user = models.OneToOneField(User, primary_key=True)
    key_expires = models.DateTimeField()
    # I commented out the old one, because it was giving me errors - Grant
    # key_expires = models.DateTimeField(default=datetime.date.today())


class ReportUserSharing(models.Model):
    # Stores sharing pairs of report-user
    report = models.ForeignKey(Report)
    user = models.ForeignKey(User)

    def __str__(self):
        return str(self.report) + " SHARED WITH " + str(self.user)


class ReportGroupSharing(models.Model):
    # Stores sharing pairs of report-group
    report = models.ForeignKey(Report)
    group = models.ForeignKey(Group)

    def __str__(self):
        return str(self.report) + " SHARED WITH " + str(self.group)
