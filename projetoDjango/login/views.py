from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def loginScreen(request):
    if request.method == 'POST':
        # Obtenha as credenciais do usuário enviadas na solicitação
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verifique no banco de dados se o usuário existe
        # Faça as validações e autenticação necessárias

        # Exemplo simples de verificação de usuário
        if username == 'teste@123.com' and password == '123':
            # Usuário válido
            return JsonResponse({'message': 'Login bem-sucedido'})
        else:
            # Credenciais inválidas
            return JsonResponse({'message': 'Credenciais negadas'}, status=401)
    else: 
        return render(request, 'login/login.html')

    
