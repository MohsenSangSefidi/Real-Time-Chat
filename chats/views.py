from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from chats.models import ChatGroup
from .forms import CreateMessageForm


@login_required
def chat_view(request, *args, **kwargs):
    chat_group = get_object_or_404(ChatGroup, group_name='public_chat')
    chat_messages = chat_group.messages.all()[:30]
    form = CreateMessageForm()

    if request.htmx:
        form = CreateMessageForm(request.POST)

        if form.is_valid():
            massage = form.save(commit=False)
            massage.author = request.user
            massage.group = chat_group
            massage.save()
            context = {
                'message': massage,
                'user': request.user,
            }
            return render(request, 'partial_massage.html', context)

    return render(
        request, 'chats.html',
        {
            'chat_messages': chat_messages,
            'form': form,
        }
    )
