import random
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from . import models

# Create your views here.
def index(request):
    # if vfsession cookie and valid value -> redirect to dash page
    session_key = _convert(request.COOKIES.get('vfsession', ''))
    if session_key:
        # check for existence in db, if so then return redirect
        try:
            sesh = models.Session.objects.get(skey=session_key)
            # got sesh successfully so load it
            red = redirect('/dash')
            return red
        except:
            pass
    # else return basic homepage
    return render(request, 'dash/index.html', {})

def dashboard(request):
    # if vfsession cookie and valid value -> actually load user's dash
    session_key = _convert(request.COOKIES.get('vfsession', ''))
    if session_key:
        # check for existence in db, if so then return dash
        #try:
            sesh = models.Session.objects.get(skey=session_key)
            # got sesh successfully so load it
            uname = sesh.uname
            teams = models.Team.objects.filter(uname=uname)
            teams = sorted([t.city + " " + t.tname for t in teams])
            resp = render(request, 'dash/dash.html', {'teams': teams, 'name': uname.uname})
            return resp
        #except:
        #    pass
    # else return basic homepage
    return redirect("/")

def showlogin(request):
    session_key = _convert(request.COOKIES.get('vfsession', ''))
    if session_key:
        # check for existence in db, if so then return dash
        try:
            sesh = models.Session.objects.get(skey=session_key)
            # got sesh successfully so load it
            return redirect('/dash')
        except:
            pass
    # else return basic login/signup screen
    return render(request, 'dash/loginview.html', {})

def showteam(request, team_name):
    try:
        teamobj = models.Team.objects.get(tname=team_name)
        # team exists at this point
        context = {
            'owner': teamobj.uname,
            'city': teamobj.city,
            'name': teamobj.tname
        }
        return render(request, 'dash/showteam.html', context)
    except:
        return render(request, 'dash/showteam.html', {})

def allteams(request):
    teams = models.Team.objects.all()
    teams = [{'owner': t.uname.uname, 'name': t.city + " " + t.tname} for t in teams]
    teams = sorted(teams, key=lambda t: t['name'])
    return render(request, 'dash/allteams.html', {'teams': teams})

def makeateam(request):
    # if vfsession cookie and valid value -> actually load maketeam page
    session_key = _convert(request.COOKIES.get('vfsession', ''))
    if session_key:
        # check for existence in db, if so then return maketeam page
        #try:
            sesh = models.Session.objects.get(skey=session_key)
            # got sesh successfully so load it
            from cities import us_cities
            return render(request, 'dash/makeateam.html', {'cities': us_cities})
        #except:
        #    pass
    # else return basic homepage
    return redirect("/")

def login(request):
    # need name, pwd, register T/F
    name = _convert(request.POST["username"])
    pwd = _convert(request.POST["password"])
    register = "register" in request.POST
    users_w_name = models.User.objects.filter(uname=name)
    if register and users_w_name:
        return _showlogin_with_err(request, name, "User with that name already exists.")
    elif not (register or users_w_name):
        return _showlogin_with_err(request, name, "No user with that name exists.")
    else:
        if register:
            u = models.User(uname=name, pwd=pwd)
            u.save()
        else:
            try:
                u = models.User.objects.get(uname=name, pwd=pwd)
            except:
                return _showlogin_with_err(request, name, "Invalid password.")
        skey = "".join([chr(random.randint(0,127)) for i in range(128)])
        while models.Session.objects.filter(skey=skey):
            skey = "".join([chr(random.randint(0,127)) for i in range(128)])
        sesh = models.Session(uname=u, skey=skey)
        sesh.save()
        resp = redirect('/dash')
        resp.set_cookie('vfsession', skey)
        return resp

def _showlogin_with_err(request, username, err):
    return render(request, 'dash/loginview.html', {'err': "Error: " + err, 'name': username})

def signout(request):
    skey = _convert(request.COOKIES.get('vfsession', ''))
    try:
        sesh = models.Session.objects.get(skey=skey)
        sesh.delete()
        resp = redirect('/')
        resp.set_cookie('vfsession', '')
        return resp
    except:
        pass
    raise Http404("Couldn't sign out due to an unexpected error.")

def createteam(request):
    skey = _convert(request.COOKIES.get('vfsession', ''))
    try:
        sesh = models.Session.objects.get(skey=skey)
        user = sesh.uname
        uname = user.uname
    except:
        raise Http404("Could not make the team (no valid session)")

    atts = ("city", "tname", "primary_color", "secondary_color")
    (city, tname, prim, sec) = _convertall(request.POST[a.encode('ascii','ignore')] for a in atts)
    zipf = request.FILES['zip']
    if not zipf:
        raise Http404("rekt by zip file")
    # write to db and also make file
    t = models.Team(uname=user, city=city, tname=tname)
    t.save()
    with open("team/" + city + tname + ".zip", "w") as f:
        for chunk in zipf.chunks():
            f.write(chunk)
    return redirect('/dash')

def show_schedule(request):
    sched_file = "schedule.txt"
    with open(sched_file, "r") as f:
        contents = f.read()
    lines = (line.split(',') for line in contents.split("\n") if line != "")
    battles = [{"team1": team1, "team2": team2} for (team1, team2) in lines]
    return render(request, 'dash/schedule.html', {'battles': battles})

def _convert(ustr):
    return ustr.encode('ascii', 'ignore')

def _convertall(ustrs):
    return (_convert(us) for us in ustrs)
