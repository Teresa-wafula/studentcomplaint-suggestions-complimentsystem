from django.shortcuts import render, redirect
from .models import *

def suggestionform(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        description = request.POST.get('description')
        solution = request.POST.get('solution')

        # Determine the specific suggestion model based on the selected category
        suggestion_model = None

        if category == 'academic':
            suggestion_model = AcademicSuggestions
        elif category == 'infrastructure':
            suggestion_model = InfrastructureSuggestion
        elif category == 'outreach':
            suggestion_model = OutreachSuggetion
        elif category == 'technology':
            suggestion_model = TechnologySuggestion
        elif category == 'others':
            suggestion_model = OtherSuggetions

        # Create a new instance of the determined suggestion model and save it
        suggestion = suggestion_model.objects.create(
            category=category,
            description=description,
            solution=solution
        )
        print(suggestion)
        # Optionally, you can add a success message
        # Redirect to a success page or wherever needed
        return redirect('/')

    return render(request, 'suggestion.html')
# from django.http import HttpResponse

# def suggestionform(request):
 
  # if request.method == 'POST':
  #   category = request.POST.get('category')
  #   description = request.POST.get('description')
  #   solution = request.POST.get('solution')

  #   if not category or not description or not solution:
  #     return HttpResponse('Please fill in all required fields.')

  #   if category == 'academic':
  #     model = AcademicSuggestions
  #   elif category == 'infrastructure':
  #     model = InfrastructureSuggestion
  #   elif category == 'technology':
  #     model = TechnologySuggestion
  #   elif category == 'outreach':
  #     model = OutreachSuggetion
  #   else:
  #     model = OtherSuggetions

  #   suggestion = model(category=category, description=description, solution=solution)
  #   suggestion.save()

  #   return HttpResponse('Suggestion submitted successfully!')
  # else:
  #   return HttpResponse('Invalid request method. Please use POST.')
