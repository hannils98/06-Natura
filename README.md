# 06-Natura
HUR MAN KÖR KODEN

Kolla så du har minst Python 3.3, annars ladda ner det först.

1.PIP 	Du borde se till så att du har gjort pip till en path
	Det gör det genom att skriv path i CMD:n och du bör ha något som slutar på .../Scripts
	Ifall du har det så gå till steg 3.

2.PIP	Ifall du inte har pip som path så skriv följande i CMD:n 
	(OBS kanske inte funkar i PowerShell så byt till CMD då)
	setx PATH "C:\HÄR SKRIVER DU DIN PATH TILL PIP;%PATH%" 
	Tips! Borde ligga i din Python-mapp
	Ex. setx PATH "C:\Users\A\Python\Python38-32\Scripts;%PATH%" 
	Sen borde du få bekräftelse genom 'SUCCESS: Specified value was saved.'
	Går det inte så får du googla dig fram till hur du gör det.

3.GIT 	Gå in på GitHub Desktop och tryck på 'File' sedan 'Clone a repository' 
	och gå till sista flien som heter URL
	Skriv in https://github.com/hannils98/06-Natura och clona
	Fetcha och pulla det senaste och se till att du har Natura_v4 och app.py däri

4.VENV	Öppna CMD (du kan vara i vilken vilken directory du vill ex. Skrivbordet eller Dokument, 
	cd + hela sökvägen för att byta dir)
	Skriv i CMD: py -m venv venv
	Det borde komma upp en mapp som heter venv (där du var inne ex. Skrivbord eller Dokument)
	Kopiera hela venv-mappen

5.VENV	Gå till GitHub mappen på din dator och hitta Natura_v4
	Tryck på den och däri kommer du hitta en mapp som heter venv
	Ersätt denna fil med din egen venv (klistra in så kommer den automatiskt att ersätta)

6.ACTIVATE
	Gå in i din venv till på Natura_v4 och tryck på Scripts
	Kopiera hela sökvägen ex. C:\Users\A\Documents\GitHub\06-Natura\Natura_v4\venv\Scripts
	Gå in i CMD och skriv cd + sökvägen ovan så du kommer in i Scripts
	Skriv sedan /activate
	Det borde dyka upp en (venv) ex. '(venv) C:\Users\A\Documents......'
	Då har du lyckats! Annars gör om och gör rätt.

7. LADDA NER REQUIREMENTS
	Eftersom det finns massa paket du måste ladda ner så behöver du göra följande steg.
	Skriv cd.. i CMD:n två gånger så du är inne i Natura_v4 dir
	Sedan skriver du pip install -r requirements.txt och då borde alla paket laddas ner

8. STARTA PROGRAMMET
	Sen skriver du i CMD (fortfarande i Natura_v4 dir):
	set flask_app=app.py
	sedan:
	set flask_env=development
	sedan:
	flask run
	Sen borde det komma upp liknande:
	'Running on http://127.0.0.1:5000/' gå in där och så har du hittat rätt.

Om du inte kan så hör av dig till mig, Amanda, så kan jag försöka hjälpa dig. Men försök iallafall följa stegen.
	
	