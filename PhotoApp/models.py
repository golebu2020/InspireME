from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#User Profile
class Profile(models.Model):
  image = models.ImageField(default = "avater_design.png")
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  
  def __str__(self):
    return str(self.user) 
  
  
#Post Category
class Category(models.Model):
  category_name = models.CharField(max_length = 200, null=False)
  
  def __str__(self):
    return self.category_name
  
  
class Like(models.Model):
  like_no = models.IntegerField()
  view_no = models.IntegerField()
  
  
  def __str__(self):
    return str(self.like_no)
  
#User Post
class Post(models.Model):
  title = models.CharField(max_length = 200, null=False)
  description = models.TextField(null=False)
  post_image = models.ImageField(default = "avater_design.png", null=False, blank= False)
  category = models.ForeignKey(Category,on_delete = models.CASCADE)
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
  like = models.OneToOneField(Like, on_delete = models.CASCADE)
  
  def __str__(self):
    return self.title
  

#Likes


  

# #Save
# class Save(models.Model):
#   save_state = models.BooleanField(default = False)
#   like = models.OneToOneField(Like, on_delete = models.CASCADE)
  
#   def __str__(self):
#     return str(self.save_state)
  
  

  

  
  
  
  
  