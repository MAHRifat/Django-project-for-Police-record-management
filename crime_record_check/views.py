from django.shortcuts import render,redirect
from .forms import Record_entry_form_NID,Record_entry_form_DOB,RegisterForm,SecureCodeModelForm,CustomAuthenticationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .models import Record_entry_NID,Record_entry_DOB


def homepage(request):
    return render(request, 'base.html')

def record_entry_form_NID(request):
    if request.method == "POST":
        form = Record_entry_form_NID(request.POST, request.FILES, prefix = 'form')
        if form.is_valid():
            task_list = form.save(commit=False)
            task_list.save()
            return redirect('record_entry_form_NID')
        else:
            print(form.errors)
    else:
        form = Record_entry_form_NID(prefix= 'form')

    return render(request, 'record_entry.html', {'form' : form})

def record_entry_form_DOB(request):
    if request.method == "POST":
        form = Record_entry_form_DOB(request.POST, request.FILES, prefix = 'form')
        if form.is_valid():
            task_list = form.save(commit=False)
            task_list.save()
            return redirect('homepage')
        else:
            print(form.errors)
    else:
        form = Record_entry_form_DOB(prefix= 'form')

    return render(request, 'record_entry_DOB.html', {'form' : form})


def signup(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        secure_code_form = SecureCodeModelForm(request.POST)

        if user_form.is_valid() and secure_code_form.is_valid():
            # Process both forms when they are valid
            user = user_form.save()
            secure_code = secure_code_form.save(commit=False)
            secure_code.user = user  # Assuming there is a ForeignKey relationship
            secure_code.save()

            return redirect('signin')  # Redirect to success page or another view
    else:
        user_form = RegisterForm()
        secure_code_form = SecureCodeModelForm()

    return render(request, 'signup.html', {'user_form': user_form, 'secure_code_form': secure_code_form})


def signin(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirect to the desired page after successful login
                return redirect('record_entry_form_NID')
            else:
                # Handle invalid login credentials
                # You may want to display an error message in the template
                pass
    else:
        form = CustomAuthenticationForm()

    return render(request, 'signin.html', {'form': form})


def search_feature_NID(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        posts = Record_entry_NID.objects.filter( nid_number = search_query )
        return render(request, 'search_item.html', {'query':search_query, 'post':posts})
    else:
        return render(request, 'search_item.html',{})
    


def recordcheckNID(request):
    return render(request, 'record_check.html')

def search_feature_DOB(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        posts = Record_entry_DOB.objects.filter( Birth_certification_number = search_query )
        return render(request, 'search_item_DOB.html', {'query':search_query, 'post':posts})
    else:
        return render(request, 'search_item_DOB.html',{})
    
def recordcheckDOB(request):
    return render(request, 'record_check_DOB.html')

def user_logout(request):
    logout(request)
    return redirect('signin')

    