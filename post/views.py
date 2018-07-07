from django.shortcuts import render

# Create your views here.
def create_post(request):
    render(request,"create_post.html")
def edit_post(request):
    render(request,"cedit_post.html")
def read_post(request):
    render(request,"read_post.html")
def post_list(request):
    render(request,"post_post.html")
def search(request):
    render(request,"search.html")
