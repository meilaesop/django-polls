from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views import generic
from .models import Choice,Question
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        return the last five published questions(not including those set to be published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST["choice"])
    except (KeyError,Choice.DoesNotExist):
        # redisplay the questing choice voting form
        return render(
                request,
                "polls/detail.html",
                {
                    "question": question,
                    "error_message": "You didn't select a choice.",
                    }
                )
    else:
        selected_choice.votes=F("votes")+1
        selected_choice.save()
        # always return an HttpResponseRedirect after successfully dealing
        # with POST data.This prevents data from being posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results",args=(question.id,)))

# ============================================================================
# 用户认证视图
# ============================================================================
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

def register(request):
    """用户注册视图"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 注册后自动登录
            login(request, user)
            return redirect('polls:index')
    else:
        form = UserCreationForm()
    
    return render(request, 'polls/register.html', {'form': form})

def custom_login(request):
    """自定义登录视图"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('polls:index')
    else:
        form = AuthenticationForm()
    
    return render(request, 'polls/login.html', {'form': form})

@login_required
def profile(request):
    """用户个人资料页面"""
    return render(request, 'polls/profile.html', {'user': request.user})

def custom_logout(request):
    """自定义退出视图"""
    auth_logout(request)
    return redirect('polls:index')
