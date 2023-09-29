from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html",context={"name":""})
def index(request):
    print("REQUEST METHODE:",request.method)
    print("PARAMS:",request.GET)
    data = request.GET.dict()
    data={"students":[
        {
            "name":"Sandip Rai",
            "address":"Kharthamchha",
            "age":19,
            "course":"BSc.CSIT"
        },
        {
            "name":"Sandip Rai",
            "address":"Kharthamchha",
            "age":19,
            "course":"BSc.CSIT"
        },
        {
            "name":"Sandip Rai",
            "address":"Kharthamchha",
            "age":19,
            "course":"BSc.CSIT"
        },

    ],"college":"KCT,"}



    return render(request,"index.html",context=data)
def contact(request):

    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")
