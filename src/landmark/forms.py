from django import forms

class LandmarkForm(forms.Form):
	OPTIONS = (("Aïn Chock","Aïn Chock"),("Aïn Sebaâ","Aïn Sebaâ"),("Hay Mohammadi","Hay Mohammadi"),("Ben M'sick","Ben M'sick"),
		("Hay Hassani","Hay Hassani"),("CASA Tachfine Center","CASA Tachfine Center"),("Sbata","Sbata"),("Sidi Maârouf","Sidi Maârouf"),("Bourgogne","Bourgogne"),
		("Aïn Borja","Aïn Borja"),("Maârif","Maârif"),("Hay El Houda","Hay El Houda"),("Hay El Baraka","Hay El Baraka"),("Hay Al Amal","Hay Al Amal"),
		("Mers Sultan","Mers Sultan"),("Hay Essalam","Hay Essalam"),("ANFA","ANFA"),("El Oulfa","El Oulfa"),("Lissasfa","Lissasfa"),
		("Sidi Bernoussi","Sidi Bernoussi"),("Hay El Farah","Hay El Farah"),("Al Fida","Al Fida"),("BACHKOU","BACHKOU"),("Hay Woroud","Hay Woroud"),
		("LA GIRONDE","LA GIRONDE"),("Derb Ghallef","Derb Ghallef"),("Sidi Moumen","Sidi Moumen"),("Hay Arrahma","Hay Arrahma"),("Hay Moulay Rachid 4","Hay Moulay Rachid 4"),
		("Bournazel","Bournazel"),)
	landmarks = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={
		'id':'form-control','size': 10,
		}),choices=OPTIONS
		)

class mot_cle(forms.Form):
	mot_cle = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'Que cherchez-vous?'}))        