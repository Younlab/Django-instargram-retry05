from django.shortcuts import render

def post_list(request):
    if request.method == 'POST':
        pass

    return render(request, 'posts/post_list.html')