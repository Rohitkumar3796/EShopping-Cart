from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        # for POST REQUEST AND THIS FUNCTION CALL FROM signup
        # we have taken firstname that is in the brackets from signup.html
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        error_msg = None
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        error_msg = self.validateCustomer(customer)

        if (not error_msg):

            print(first_name, last_name, phone, email, password)

            # this for hashing password
            customer.password = make_password(customer.password)

            customer.register()

            return redirect('homepage')
            # we are fetching home page again so first we have to go to pass name to app urls then you can access in views from redirect
        else:
            data = {
                'error': error_msg,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_msg = None
        if (not customer.first_name):
            error_msg = "First Name is Required!!"
        elif len(customer.first_name) < 3:
            error_msg = "First Name should be long"
        elif (not customer.last_name):
            error_msg = "Last Name is Required!!"
        elif len(customer.last_name) < 3:
            error_msg = "Last Name should be long"
        elif (not customer.phone):
            error_msg = "Phone Number is Required"
        elif len(customer.phone) < 10:
            error_msg = "Phone Number Must be 10 char long"
        elif (not customer.email):
            error_msg = "Email is Required"
        elif (len(customer.email) < 5):
            error_msg = "Email must be 5 char long "
        elif (not customer.password):
            error_msg = "Password is Required"
        elif (len(customer.password) < 5):
            error_msg = "Password must be 5 char long "

        elif customer.isExist():
            error_msg = 'Email Address Already Registered'

        return error_msg
