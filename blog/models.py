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
    def summary(self):
        return self.blog_body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title


#Q: what is the next steps to add the model so that we can use it?
#A: 1.add the blog app to the settings
#2.create a migration in terminal
#3.migrate
#4.add to admin
