from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

class Login(View):
    return_url=None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')


    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_msg = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                # this two for session
                # where the seeson is manage so you have go to sqlite db
                request.session['customer']=customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_msg = "Email or Password Invalid !!"
        else:
            error_msg = "Email or Password Invalid !!"
        print(email, password)
        return render(request, 'login.html', {'error': error_msg})


def logout(request):
    request.session.clear()
    return redirect('login')