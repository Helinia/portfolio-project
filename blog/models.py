from django.db import models


class Blog(models.Model):
    #Create a blog models
    #title
    title = models.CharField(max_length = 255)
    #publication date
    pub_date = models.DateTimeField()
    #body
    blog_body = models.TextField()
    #image
    image = models.ImageField(upload_to = 'images/')



#add the blog app to the settings
#create a migration in terminal
#migrate
#add to admin
