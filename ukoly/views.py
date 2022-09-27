from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from . import models
from django.contrib.auth.models import User

def suma(cislo):
    return (cislo * (cislo +1))/2

def ukoly_index(request):
    cislo = int(request.GET.get("cislo",0))
    vysledek = suma(cislo)
    print(vysledek)
    return render(request, "ukoly/ukoly-index.html",context=dict(vysledek=vysledek))

def ukoly_login(request):
    users = User.objects.all()
    return render(request, "ukoly/ukoly-login.html",context=dict(users=users))

def ukoly_kontakty(request):
    return render(request, "ukoly/ukoly-kontakty.html")

def seznam_ukolu(request):
    def get_ids():
        seznam_id = []
        for key in request.POST:
            if key.startswith("ukol_id_"):
                pk = key.split("ukol_id_")[1]
                seznam_id.append(pk)
        return seznam_id
    if request.method == "POST":
        ids = get_ids()
        models.Ukol.objects.filter(id__in=ids).update(stav=True)
        models.Ukol.objects.exclude(id__in=ids).update(stav=False)
        return redirect("ukoly:seznam_ukolu")


    jmeno = request.GET.get("jmeno")
    if jmeno:
        ukoly = models.Ukol.objects.filter(jmeno_autora=jmeno)
    else:
        ukoly = models.Ukol.objects.all
    # return HttpResponse('<h1 style="color:red;">Toto je seznam úkolů</h1>')
    return render(request,'ukoly/seznam-ukolu.html', context=dict(ukoly=ukoly, jmeno=jmeno))

def detail_ukolu(request, index_ukolu):
    ukol = get_object_or_404(models.Ukol, id=index_ukolu)

    if request.method == "POST":
        nazev = request.POST["nazev"]
        autor = request.POST["autor"]
        stav = request.POST.get("stav")
        ukol.nazev = nazev
        ukol.autor = autor
        ukol.stav = bool(stav)
        ukol.save()
        print(nazev,autor,stav)
        return redirect(ukol.get_absolute_url())
    return render(request,"ukoly/detail-ukolu.html", context=dict(ukol=ukol,index_ukolu=index_ukolu))