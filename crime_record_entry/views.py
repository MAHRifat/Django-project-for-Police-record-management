# from django.shortcuts import render,redirect
# from .forms import Record_entry_form_DOB

# # Create your views here.

# def record_entry_form_DOB(request):
#     if request.method == "POST":
#         form = Record_entry_form_DOB(request.POST, request.FILES, prefix = 'form')
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.save()
#             return redirect('homepage')
#         else:
#             print(form.errors)
#     else:
#         form = Record_entry_form_DOB(prefix= 'form')

#     return render(request, 'record_entry_DOB.html', {'form' : form})