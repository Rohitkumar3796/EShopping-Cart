
# This model email attribut not working for proper authenticate from here if your form email feild is empty so admin will not give error but if you add object from django admin so it will give an arror because you are able to leave empty field so it will give an error And if you want to do from here so you have to make a form then you can authenticate

from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False


    # this function for email verification if email is exist already exist 
    def isExist(self):
        if Customer.objects.filter(email=self.email):
            return True
            
        return False
        
