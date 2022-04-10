from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Message

@login_required
def load_messages(request, pk):
    other_user = get_object_or_404(User, pk=pk)
    messages = Message.objects.filter(
        Q(receiver=request.user, sender=other_user)
    )
    messages.update(seen=True)
    context = {
        "other_user": other_user,
        "user_messages": messages,
        "users": User.objects.all()
    }
    return render(request, "chatroom.html", context)