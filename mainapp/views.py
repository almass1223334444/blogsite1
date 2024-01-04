from django.shortcuts import render, redirect

# Create your views here.

posts = [
    {
        "Title": "titlename",
        "Description": "description",
        "Author": "author",
        "Date": "12.12.12"
    }
]



def indexpage(request):
    return render(request, "index.html", {"articles": posts, "page":"index"})

def aboutpage(request):
    return render(request, "about.html", {"page": "about"})

def contactpage(request):
    if request.method == 'GET':
        return render(request, "contact.html",{"page":"contact"})
    else:
        print(request.POST)
        with open("C:/Users/almas/Desktop/django/blogsite/mainapp/user_info.txt", "a") as file:
            file.writelines(f"\n Name:{request.POST['name']},\n Email:{request.POST['email']},\n Subject:{request.POST['subject']}")
        return redirect(contactpage)


def postpage(request):
    return render(request, "post.html",{"page":"post"})
#
# def main(request):
#     return render(request,"main.html", {"page":"main"})

def loginpage(request):
    return render(request,"login.html", {"page":"login"})
