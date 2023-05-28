
from django.shortcuts import render, redirect

class RedirectIfLogin():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            return render(request, '404.html')
        return response

    def process_view(self, request, view_fun, view_args, view_kwargs):
        url = request.META.get('PATH_INFO')
        if ((url == '/members/login/' or url == '/members/register/') and (str(request.user).lower() != 'anonymoususer')):
            return redirect(to='all_songs')
        
        



