from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import login, logout, authenticate
from .models import Subject, Question, Choice
from django.contrib.auth.decorators import login_required


@login_required(login_url='signin')
def quiz_home(request):
    subjects = Subject.objects.all()
    return render(request, 'quiz/home.html', {'subjects': subjects})

def quiz_page(request, subject_id, page=1):
    subject = Subject.objects.get(pk=subject_id)
    questions = Question.objects.filter(subject=subject)

    paginator = Paginator(questions, 5)  # Show 5 questions per page
    page_obj = paginator.get_page(page)

    if request.method == 'POST':
        # Process the form submission for the current page
        answers = request.POST.dict()
        csrf_token = answers.pop('csrfmiddlewaretoken', None)

        for question_id, answer_id in answers.items():
            question = Question.objects.get(pk=question_id)
            choice = Choice.objects.get(pk=answer_id)
            if choice.is_correct:
                request.session.setdefault('score', 0)
                request.session['score'] += 2

        if page_obj.has_next():
            return redirect('quiz_page', subject_id=subject_id, page=page_obj.next_page_number())
        else:
            return redirect('quiz_result')

    return render(request, 'quiz/page.html', {'subject': subject, 'page_obj': page_obj})

def quiz_result(request):
    score = request.session.pop('score', 0)
    return render(request, 'quiz/result.html', {'score': score})





























# from django.shortcuts import render, redirect
# from .models import Subject, Question, Choice
# from django.contrib import messages


# def quiz_home(request):
#     subjects = Subject.objects.all()
#     return render(request, 'quiz/home.html', {'subjects': subjects})

# def quiz_page(request, subject_id):
#     subject = Subject.objects.get(pk=subject_id)
#     questions = Question.objects.filter(subject=subject)

#     if request.method == 'POST':
#         answers = request.POST
#         for question in questions:
#             if str(question.id) not in answers:
#                 messages.error(request, 'All questions must be completed')
#                 return redirect('quiz_page', subject_id=subject_id)

#     return render(request, 'quiz/page.html', {'questions': questions})

# def quiz_result(request):
#     if request.method == 'POST':
#         answers = request.POST.dict()
#         subject_ids = set()

#         # Remove the CSRF token from the answers dictionary
#         csrf_token = answers.pop('csrfmiddlewaretoken', None)

#         score = 0
#         for question_id, answer_id in answers.items():
#             question = Question.objects.get(pk=question_id)
#             choice = Choice.objects.get(pk=answer_id)
#             if choice.is_correct:
#                 score += 2
#             subject_ids.add(question.subject_id)

#         # Check if all questions in each subject have been answered
#         for subject_id in subject_ids:
#             subject_questions = Question.objects.filter(subject_id=subject_id)
#             answered_questions = [int(question_id) for question_id in answers.keys()]
#             unanswered_questions = subject_questions.exclude(pk__in=answered_questions)
#             if unanswered_questions.exists():
#                 messages.error(request, 'All questions must be completed')
#                 return redirect('quiz_home')

#         return render(request, 'quiz/result.html', {'score': score})
#     return redirect('quiz_home')
