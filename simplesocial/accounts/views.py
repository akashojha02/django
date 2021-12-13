from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from . import forms

# Create your views here.
from django.contrib.auth import get_user_model
User= get_user_model()


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url= reverse_lazy('login')
    template_name='accounts/signup.html'


def search_profile(request):
    if request.method=='POST':
        searched= request.POST['searched']
        user_list = User.objects.all()
        # print(user_list)
        searched_result = user_list.filter(username__icontains = searched)
        # print(searched_result)
        values = searched_result.values('username')
        # print(values)
        name=[]
        for value in values:
            print(value)
            name.append(value['username'])
        # print(name)
        return render(request, 'accounts/search_people.html',{'searched':searched,
                        'name':name})
    else:
        return render(request, 'accounts/search_people.html',{})
