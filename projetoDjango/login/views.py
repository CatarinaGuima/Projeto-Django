from django.shortcuts import render
from django.http import JsonResponse
from database.models import Login


def login(request):
    if request.method == 'POST':
        # Credenciais do usuário enviadas na solicitação
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verifica no banco de dados se o usuário existe
        try:
            user = Login.objects.get(username=username)
        except Login.DoesNotExist:
            # Usuário não existe
            return JsonResponse({'message': 'Usuário não encontrado'}, status=404)

        # validações e autenticação 
        if user.password == password:
            # Credenciais válidas
            return JsonResponse({'message': 'Login bem-sucedido'})
        else:
            # Credenciais inválidas
            return JsonResponse({'message': 'Credenciais negadas'}, status=401)
    
    return render(request, 'login/login.html')
