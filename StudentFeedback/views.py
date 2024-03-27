from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import EmailMessage
from StudentFeedback.forms import ComplaintForm
from .models import *
from django.contrib import messages
# Create your views here.
# def register(request):
#     if request.method == 'POST':
#         user = Student(fullname=request.POST['fullname'], email=request.POST['email'],
#                 password1= request.POST['password1'], password2= request.POST['password2'])
#         user.save()
#         return redirect('login')
#     else:
#         return render(request, 'register.html')



def register(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            message = "Passwords do not match."
            return render(request, 'register.html', {'message': message})
            # messages.error(request, "passwords do not match")
            # return render(request, 'register.html')
        if Student.objects.filter(email=email).exists():
            message = "Email already exists."
            return render(request, 'register.html', {'message': message})

        user = Student(fullname=fullname, email=email, password1=password1, password2=password2)
        user.save()
        return redirect('login')
     

    else:
        return render(request, 'register.html')



def login(request):
    if request.method == 'POST':
        if Student.objects.filter(email=request.POST['email'],
                                 password2=request.POST['password2']).exists():
            student = Student.objects.get(email=request.POST['email'],
                                        password2=request.POST['password2'])
            return render(request, 'complaintform.html', {'student': student})
            
        else:
            message="You entered wrong credentials"
            return render(request, 'login.html',{'message':message})
    else:
        return render(request, 'login.html')
 

def index(request):
    return render(request, 'index.html')


def submit_complaint(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            email=request.user.email if request.user.is_authenticated else form.cleaned_data['email']
            complaint = form.save(commit=False)
            complaint.email='Anonymous'
            complaint.save()
            notifications(complaint)
            return redirect('/')
        


    else:
        form=ComplaintForm()
    return render(request, 'complaintform.html', {'form': form})

def notifications(complaint):
    subject = 'A new submission has been added'
    message= f'Category: {complaint.category} \n  Description: {complaint.description} \n Submitted By: {complaint.email}'
    admin_email=settings.ADMIN_EMAIL
    email=EmailMessage(subject, message,'wafula.nambande@kyu.ac.ke', [admin_email])
    email.send(fail_silently=False)


# def complaintform(re:quest):
#     if request.method == 'POST':
#         # Extract form data from request.POST
#         category = request.POST.get('category')
#         date= request.POST.get('date')
#         location = request.POST.get('location')
#         description = request.POST.get('description')
#         evidence = request.FILES.get('evidence')

#         # Determine the specific complaint model based on the selected category
#         if category == 'rape':
#             complaint_model = RapeComplaint
#         elif category == 'sexual_misconduct':
#             complaint_model = SexualMisconductComplaint
#         elif category == 'other':
#             complaint_model = Other
#         elif category == 'harassment':
#             complaint_model = HarassmentComplaint
        
#         # Create a new instance of the determined complaint model and save it
#         complaint = complaint_model.objects.create(
#             category=category,
#             date=date,
#             location=location,
#             description=description,
#             evidence=evidence
#         )

#         # print(complaint)

#         # Redirect to a page confirming successful submission
#         return redirect('/')

#     return render(request, 'complaintform.html')

