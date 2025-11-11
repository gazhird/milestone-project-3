from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Available"), (1, "Sold"))

class Add_Listing(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    colour = models.CharField(max_length=200)
    year = models.IntegerField(max_length=200)
    size = models.IntegerField(max_length=200)
    fuel = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    seller = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="listings") 
    # blog posts will need to be changed to reflect my project
    image1 = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    listed_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)





# stopped at (I Think Therefore I Blog  Models part 1  Building the Post model) 12 to include images 
# 12 https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101N+6/courseware/713441aba05441dfb3a7cf04f3268b3f/0758f42698bf498382b68a9cb8e72483/?child=first