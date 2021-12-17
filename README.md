# Casa-Delivery-App

This application is developed using python language and Django web framework. It is characterized by the use of genetic algorithms which aim to obtain an approximate solution to an optimization problem.
The main objective of this application is to allow the user who is in our case a delivery man to find the optimal path to follow by browsing a number of given landmarks of Casablanca city in order to reduce costs and also to reduce stress of delivery men and respect their working hours thus providing a better quality of service to customers.

	Côté Utilisateur (Livreur) :
	
	Page d’authentification de livreur:

Pour s’authentifier, l’utilisateur doit remplir le formulaire ci-dessous en saisissant son
« Identifiant » et son « Mot de passe ». Si les informations saisies sont valides, il sera redirigé vers la page d’accueil. Sinon un message d’erreur sera affiché.
![image](https://user-images.githubusercontent.com/78702422/146614730-3ee4b22e-ad03-4880-ad7a-a4732200b416.png)

	Page d’accueil de l’utilisateur:
La figure ci-dessous représente l’entête de la page d’accueil de l’utilisateur, elle affiche le lien de la partie des services et la partie de la déconnexion.
![image](https://user-images.githubusercontent.com/78702422/146614811-de499e7b-ad89-46bc-8a63-9e5224cd5900.png)

La figure ci-dessous représente la partie services de l’application, elle affiche les liens vers les services de l’application « Chemin optimal » , « Ma localisation» et «Contactez nous » .
![image](https://user-images.githubusercontent.com/78702422/146614848-210f223d-0b96-444e-9404-0e81651f3b81.png)

La figure ci-dessous représente les privilèges de l’application.
![image](https://user-images.githubusercontent.com/78702422/146614881-ac93df51-9563-4cd7-b231-4efcf5dd4118.png)

La figure ci-dessous représente la partie des témoignages des livreurs, qui ont la possibilité d’afficher leurs sincères avis sur le fonctionnement de l'application.
![image](https://user-images.githubusercontent.com/78702422/146614908-d541089e-10a9-42a0-aae0-7100095af491.png)

	Informations des repères:
Parmi les pages que nous avons dans l’application, la page de différents repères populaires, sur cette page nous avons une image pour chaque repère qui indique ses caractéristiques principales.
![image](https://user-images.githubusercontent.com/78702422/146614972-6aaf83fb-687a-4f17-ba6d-9a85d814fbc1.png)

	Détermination du chemin optimal des repères sélectionnés:
En cliquant sur le service « Chemin optimal », Le livreur doit sélectionner les endroits souhaités afin que le système lui donne le chemin optimal du trajet.
![image](https://user-images.githubusercontent.com/78702422/146615013-dbe6337b-bea6-41f8-9d92-95065b78e64c.png)

Après la sélection d’un nombre de repères, en cliquant sur le bouton rechercher on aura le trajet que doit suivre le livreur.
![image](https://user-images.githubusercontent.com/78702422/146615097-941e8fa9-831a-4bf0-ae7e-981af4043321.png)

	Détermination de la localisation :
En cliquant sur le service « Ma localisation », ce service permet à chaque livreur de savoir sa localisation actuelle.
![Uploading image.png…]()

	Page de «Contactez-nous »:
Le livreur a le droit de nous contacter directement sur notre boite à mails au cas d’un problème dans l’application ou bien pour savoir plus d’informations, il doit juste remplir le formulaire par le sujet de besoin ,son email, et le message qu’il veut envoyer ,et le message sera envoyer directement sur notre email en utilisant le serveur SMTP.
![image112](https://user-images.githubusercontent.com/78702422/146615585-9afdc20d-8bab-4982-af2f-7af4fe034658.jpg)

Après la saisie des informations demandées :
![image114](https://user-images.githubusercontent.com/78702422/146615623-41be56dd-1dc2-47fd-8a36-d9aa35794ad6.png)

Le message est bien reçu sur notre boîte de réception :
![image116](https://user-images.githubusercontent.com/78702422/146615649-b8f231b2-dec6-40c3-902e-78be5a2ca331.jpg)
 

	Côté administrateur :
  
	 Page d’authentification de l’administrateur :
Pour s’authentifier, l’administrateur doit remplir le formulaire ci-dessous en saisissant son
« Identifiant » et son « Mot de passe ». Si les informations saisies sont valides, il sera redirigé vers la page d’accueil. Sinon un message d’erreur sera affiché.
![image](https://user-images.githubusercontent.com/78702422/146613480-dba385c5-0d32-4af7-af68-d6ec924cb621.png)

	Page d’accueil de l’administrateur :
La figure ci-dessous représente la page d’accueil de l’administrateur qui affiche les tables que l’admin peut gérer (Accounts, Reperes...) ainsi que ses activités récentes sur l’application.
![image](https://user-images.githubusercontent.com/78702422/146613533-57da9948-21de-479e-9ce3-195f0a29557b.png)

	Page d’affichage des comptes des livreurs :
La figure ci-dessous représente la page d’affichage des comptes des livreurs qui consiste à une table « Accounts » qui contient les informations relatives aux livreurs (identifiant, nom, prénom, statut…).
![image](https://user-images.githubusercontent.com/78702422/146613572-4778bcc0-bcce-425d-941d-ae03d2b8e2f6.png)

	Recherche d’un livreur par l’administrateur :

L’administrateur a le droit de rechercher un livreur qui a un compte sur l’application par son identifiant ou son nom en utilisant une barre de recherche par filtrage. La figure ci-dessous représente un exemple de recherche par nom d’un livreur en tapant les premières lettres de son nom seulement.

Figure 27: Recherche d’un livreur par l’administrateur.
 
	Page de modification et suppression des informations d’un livreur :

L’administrateur a le droit de modifier les informations relatives aux livreurs (identifiant, mot de passe, nom, prénom...) et de supprimer un livreur. La figure ci-dessous représente un exemple de la page de modification et de suppression.

Figure 28: La page de modification et suppression des informations d’un livreur.
	Page d’affichage de la table de repères :

La figure ci-dessous représente la page d’affichage des repères qui consiste à une table
« Reperes » qui contient tous les repères qu’on va utiliser dans notre application. Il s’agit des quartiers connus de la ville Casablanca.

Figure 29: La page d’affichage de la table de repères

