from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def get_response(request):
    if request.method == 'GET':
        user_message = request.GET.get('msg', '')
        
        # 챗봇 모델을 통해 응답 생성
        chatbot_response = generate_chatbot_response(user_message)
        
        # 응답을 JSON 형식으로 반환
        return JsonResponse({'response': chatbot_response})
