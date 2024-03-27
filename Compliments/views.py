from django.shortcuts import render, redirect
from .models import Compliment

# # Create your views here.
# def compliment(request):
#     if request.method == 'POST':
#         compliments = Compliment(compliment=request.POST['compliment'],
#                                 reason=request.POST['reason'])
#         compliments.save()
#         return redirect('/')
#     else:
#         return render(request, 'compliment.html')


def compliment(request):
    if request.method == 'POST':
        compliment = request.POST.get('compliment')
        reason = request.POST.get('reason')

        Compliment.objects.create(
            compliment=compliment,
            reason=reason
        )

        return redirect('/')
    else:
        return render(request, 'compliment.html')
