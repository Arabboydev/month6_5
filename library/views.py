from django.shortcuts import render


def library_list(request):
    return render(request, 'library.html')
