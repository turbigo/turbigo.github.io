import os
import qrcode

	
def gen(name,surnme): 

	os.system('cp '+name+surnme+'.html repo/rickycurci.github.io/')
	os.system('cd repo/rickycurci.github.io/ && git add . && git commit -m "HTML" && git push origin HEAD:main')

	qr = qrcode.make('http://rickycurci.github.io/'+name+surnme+'.html')
	type(qr); qr.save(name+surnme+'qrcode.jpg')


def create_profile(name,surname,data_di_nascita,age,luogo_di_nascita,città_di_residenza,domicilio): 
	
	os.system("cd repo/rickycurci.github.io/src/media/ && mkdir "+name+surname)
	
	os.system("mv photo.jpg repo/rickycurci.github.io/src/media/"+name+surname+"/")
	os.system("mv firma.jpg repo/rickycurci.github.io/src/media/"+name+surname+"/")
	
	fx = open("index.html",'r'); old = fx.read(); fx.close()
	fx = open(name+surname+".html",'w'); 
	fx.write(old+f"""
	</head>
	<div class='content'>
		<div class='title-content'>
			<h1 class='title'> Città di Turbigo </h1>
		</div>
		<img class='profile-img' src='src/media/{name}{surname}/photo.jpg'>
		<img class='logo-turbigo-img' src='src/static/logo-turbigo.jpg'> 
		<img class='firma-img' src='src/media/{name}{surname}/firma.jpg'> 
		<img class='bollo' src='src/static/bollo.jpg'> 
		<p style="position: absolute;top:800px;left:50px;"> Name: {name} </p>
		<p style="position: absolute;top:875px;left:50px;"> Surname: {surname} </p>
		<p style="position:absolute;top:1000px;left:50px;font-size:50px;"> Data di nascita: {data_di_nascita} </p>
		<p style="position: absolute;top:1075px;left:50px;font-size:55px;"> Età: {age} </p>
		<p style="position: absolute;top:1200px;left:50px;font-size:45px;"> Luogo di Nascita: {luogo_di_nascita}</p>
		<p style="position: absolute;top:1350px;left:50px;font-size:45px;"> Città di Residenza: {città_di_residenza}</p>
		<p style="position: absolute;top:1425px;left:50px;font-size:50px;"> Domicilio: {domicilio}</p>
		
		<div class='outro' > 
			<h1 class='outro-1'> FIGA & FATTURATO </h1>
			<h2 class='outro-2'> (all anti-comunisti) </h2>
		</div>
	</div> 
<html>
 """)


name = input('NAME > ')
surname = input('SURNAME > ')
data_di_nascita = input('DATA DI NASCITA > ')
age = input('ETÀ > ')
luogo_di_nascita = input('LUOGO DI NASCITA > ')
città_di_residenza = input('CITTÀ DI RESIDENZA > ')
domicilio = input('DOMICILIO > ')

create_profile(name,surname,data_di_nascita,age,luogo_di_nascita,città_di_residenza,domicilio)
gen(name,surname)
