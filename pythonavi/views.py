import spotipy
from django.shortcuts import render,HttpResponse

# ---------------spotify api calling hua h yaha pr-------------------------


def spotify(request):
    album=''
    from spotipy.oauth2 import SpotifyClientCredentials

    birdy_uri = 'spotify:artist:1uNFoZAHBGtllmzznpCI3s'
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials
    (client_id="acb0a789940f4896a05d06c728ac69cd", client_secret="d18b649bdf764f5d814c8fd561e7ee30"))

    results = spotify.artist_albums(birdy_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'])
    # return HttpResponse(json.dumps(album),content_type='application/json')
    return render(request, "first.html", {"albums": album})


# /---------------------session try kiya h fir se ----------------

def see(request):
    session = request.session
    # session1 = request.session
    session["name"]= "avi"
    session["rollnumber"]= "10"
    print(session["rollnumber"])
    # print(session["name"])        this line is working return name's value which is avi
    for k,v in session.items():
        print(k,"and ",v)
    return render(request,"see.html",{"session":request.session.items()})


def see1(request):
    n=request.session.get("name")
    roll=request.session.get("rollnumber")
    print(n, roll)
    print(roll)
    return HttpResponse(roll)


def dell(request):
    try:
        del request.session["name"]
        del request.session["rollnumber"]
    except:
        return HttpResponse("session end")
    return render(request,"del.html")