from django.shortcuts import render, redirect
from django.views import View
from django_project import models
from django_project.models import User, gift
# Create your views here.

ind = 0


class Home(View):
    def get(self, request):
        n = request.session.get("name", "")
        p = request.session.get("password", "")
        s = ""
        return render(request, 'home.html', {"s": s, "n": n, "p": p})

    def post(self, request):
        s = ""
        n = request.session.get("name", "")
        p = request.session.get("password", "")
        name = request.POST['name']
        password = request.POST['password']
        object1 = User.objects.all().values()
        list1 = list(object1)
        flag = 0
        request.session["name"] = name
        request.session["password"] = password
        request.session.set_expiry(300)
        for i in list1:
            if i['name'] == name and i['password'] == password:
                id = i['id']
                flag = 1
                s = "Hello, " + name + "!"
                return redirect(f"/gift/?value={id}")

        if flag == 0 or request.session.set_expiry(300):
            s = "Please check your username or password"
            return render(request, 'home.html', {"s": s, "n": n, "p": p})


class registration(View):
    def get(self, request):
        s = ""
        return render(request, 'registration.html', {"s": s})

    def post(self, request):
        s = ""
        p = models.User()
        email = request.POST['mail']
        password = request.POST['password']
        name = request.POST['name']
        obj1 = User.objects.all().values()
        list1 = list(obj1)
        id = -1
        f = 0
        for i in list1:
            if i['email'] == email or i['name'] == name:
                s = "Sorry, Username or Password is already taken. Please try again"
                id = i['id']
                f = 1

        if f == 1:
            return render(request, 'registration.html', {"s": s})
        else:
            p.name, p.email, p.password = name, email, password
            p.save()
            return redirect(f"/gift/?value={id}")


class users(View):
    def get(self, request):
        if (request.session.get("name") is None or request.session is None):
            return redirect("/error/")
        else:
            obj2 = list(User.objects.all())
            string_name = request.GET['value']
            print(string_name, type(string_name))
            return render(request, 'user.html', {
                "item": obj2,
                "Str": string_name
            })


class gifts(View):
    def get(self, request):
        print(request.session.get("name"))
        if (request.session.get("name") is None or request.session is None):
            return redirect("/error/")
        else:
            print(request.GET['value'])
            self.key = 0 if type(request.GET['value']) != int else int(
                request.GET['value'])
            obj3 = list(gift.objects.all())
            return render(request, 'gift.html', {
                "gift": obj3,
                "key": self.key
            })

    def post(self, request):
        a = request.POST['gift']
        self.key = int(request.GET['value'])
        q = models.gift()
        q.id_1 = self.key
        q.giftname = a
        q.save()
        obj3 = list(gift.objects.all())
        return render(request, 'gift.html', {"gift": obj3, "key": self.key})


class othersgift(View):
    def get(self, request):
        if (request.session.get("name") is None or request.session is None):
            return redirect("/error/")
        else:
            obj5 = list(gift.objects.all().values())
            print(obj5)
            name = int(request.GET['value'])

            obj4 = list(gift.objects.all())

            return render(request, 'othersgift.html', {
                "gift": obj4,
                "name": name
            })


class Error(View):
    def get(self, request):
        return render(request, 'error.html')


class Logout(View):
    def get(self, request):
        request.session["name"] = None
        request.session["password"] = None
        return render(request, 'error.html')
