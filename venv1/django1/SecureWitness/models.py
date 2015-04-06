from django.db import models

# Create your models here.

class Users(models.Model):
    UID = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    reg_date = models.DateTimeField('date of registration')
    privilege = models.CharField(max_length=100, default='DEFAULT VALUE')

class Reports(models.Model):
	RID = models.AutoField(primary_key=True)
	folderID = models.IntegerField(default=0) #the folder that this current report belongs to
    #folder = models.ForeignKey(Folders)
	authorID = models.IntegerField(default=0)
    #author = models.ForeignKey(Users)
	create_date = models.DateTimeField('date created')
	last_update_date = models.DateTimeField('date of last modification')
	short_desc = models.CharField(max_length=150, default='DEFAULT VALUE')
	long_desc = models.CharField(max_length=300, default='DEFAULT VALUE')
	file = models.CharField(max_length=300,default='DEFAULT VALUE')
	location = models.CharField(max_length=300,default='DEFAULT VALUE')
	incident_date = models.CharField(max_length=300,default='DEFAULT VALUE')
	keywords = models.CharField(max_length=300,default='DEFAULT VALUE')
	private = models.BooleanField(default=False)
	def __str__(self):
		return self.short_desc

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





