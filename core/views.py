from django.shortcuts import render

def e404(request):
	return render(request, 'core/404.html', {})