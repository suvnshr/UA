from django.db import models
import idna

# Create your models here.


class Person(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_email(self):
        i = self.email.index("@")

        first = self.email[:i]
        last = self.email[i+1:]

        f = str(idna.decode(first))
        s = str((idna.decode(last)))

        return(f+"@"+s)


    def save(self, *args, **kwargs):

        i = self.email.index("@")
        first = self.email[:i]
        last = self.email[i+1:]
        
        f = str(idna.encode(first))
        f = f[2:len(f)-1]
        s=str((idna.encode(last)))
        s = s[2:len(s)-1]

        new_email = f + "@" + s

        self.email = new_email
    
        return super().save(*args, **kwargs)
        
