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


#Q: what is the next steps to add the model so that we can use it?
#A: 1.add the blog app to the settings
#2.create a migration in terminal
#3.migrate
#4.add to admin
