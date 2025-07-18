import uuid
from django.shortcuts import render, redirect
from .forms import MessageForm, UserInfoForm
from .chat_message import ChatMessage
from . import dialogflow_client, questions, sheets

DIALOGFLOW_TOKEN = 'YOUR_DIALOGFLOW_CLIENT_ACCESS_TOKEN'


def chat_view(request):
    if 'messages' not in request.session:
        request.session['messages'] = []

    if not request.session.get('user_info_submitted'):
        if request.method == 'POST':
            info_form = UserInfoForm(request.POST)
            if info_form.is_valid():
                data = info_form.cleaned_data
                request.session['user_info'] = data
                request.session['user_info_submitted'] = True
                sheets.append_row([
                    data['name'],
                    data['contact'],
                    data['email'],
                    data['location'],
                ])
                return redirect('chat')
        else:
            info_form = UserInfoForm()
        return render(request, 'chatapp/user_info.html', {'form': info_form})

    messages = [ChatMessage(**msg) for msg in request.session['messages']]

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            user_text = form.cleaned_data['message']
            messages.append(ChatMessage(text=user_text, is_user=True))
            try:
                reply = dialogflow_client.get_response(
                    DIALOGFLOW_TOKEN, user_text, str(uuid.uuid4())
                )
            except Exception as exc:
                reply = f'Error: {exc}'
            messages.append(ChatMessage(text=reply, is_user=False))
            request.session['messages'] = [m.__dict__ for m in messages]
            return redirect('chat')
    else:
        form = MessageForm()

    return render(
        request,
        'chatapp/chat.html',
        {
            'form': form,
            'messages': messages,
            'questions': questions.QUESTIONS,
        },
    )
