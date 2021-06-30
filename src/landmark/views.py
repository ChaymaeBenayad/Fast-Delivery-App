from django.shortcuts import render
from landmark.forms import LandmarkForm
from landmark.forms import mot_cle
from account.models import Account
import random
from itertools import combinations
import pandas as pd
import numpy as np
import json
from landmark.models import Repere
import googlemaps
from itertools import combinations

# Create your views here.

def home_view(request):

    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
  
    return render(request, "landmark/home.html", context)


landmarks = []
mes_reperes = []
def display_destination_reperes(request): 

    if request.method == "POST":
        form = LandmarkForm(request.POST)
        if form.is_valid():
            landmarks = form.cleaned_data.get('landmarks')
            pass
        pass
    else:
        form = LandmarkForm
        reperes = Repere.objects.all()
    return render(request, 'landmark/display_reperes.html', {'form': form, 'display_reperes' : reperes} )


def webpage1(request):
	if request.method == "POST":
		form = LandmarkForm(request.POST)
		if form.is_valid():
			landmarks = form.cleaned_data.get('landmarks')
	else:
		form = LandmarkForm
	return render(request,'landmark/display_reperes.html', {'form': form})


def webpage2(request):
    landmarks = []
    mylist = []
    global mes_reperes
    if request.method == "POST":
        reperes = Repere.objects.all()
        form = LandmarkForm(request.POST)
        if form.is_valid():
            landmarks.append(form.cleaned_data.get('landmarks'))
            mes_reperes = landmarks[0]
            #print(f" landmarks :{landmarks}")
            # do something with your results
            mylist = genetique_algo(generations = 5000, population_size= 100)
    else:
        form = LandmarkForm
        reperes = Repere.objects.all()
    return render(request, 'landmark/optimal_road.html', {'form': form, 'landmarks':mes_reperes, 'mylist':mylist, 'display_reperes' : reperes} )

def palce_proche(request):
    if request.method == "POST":
        form = mot_cle(request.POST)
        if form.is_valid():
            lemot = form.cleaned_data.get('mot_cle')
            return render(request, 'landmark/trouver.html',{'form':form,'lemot':lemot})
    else:
        form = mot_cle
    return render(request,'landmark/trouver.html',{'form':form})    

#THIS BlOCK IF YOU WANT PREPARE YOUR OWN DATA 
#change this list with your locations 
# reperes = ["Aïn Chock","Aïn Sebaâ","Hay Mohammadi","Ben M'sick","Hay Hassani","CASA Tachfine Center","Sbata","Sidi Maârouf","Bourgogne","Aïn Borja","Maârif","Hay El Houda","Hay El Baraka","Hay Al Amal","Mers Sultan","Hay Essalam","ANFA","El Oulfa","Lissasfa","Sidi Bernoussi","Hay El Farah","Al Fida","BACHKOU","Hay Woroud","LA GIRONDE","Derb Ghallef","Sidi Moumen","Hay Arrahma","Hay Moulay Rachid 4","Bournazel"]
# #utilisation de l API "Distance Matrix" qui vas nous aider a calculer les distances entre les repères
# gm_api = googlemaps.Client(key="AIzaSyAV90fRNoKOf92JItkGfroPSHjoUgvQrzA")
# distance_reperes = {}
# duree_reperes ={}
# # calculer la distance et la duree entre chaque repères en mode "driving" avec le service distance_matrix de google maps 
# for (repere1, repere2) in combinations(reperes, 2):
#       route = gm_api.distance_matrix(origins=[repere1],
#                                  destinations=[repere2],
#                                  mode="driving",
#                                  language="English",
#                                  units="metric")

#   #retourn une valeur (distance entre 2 repères) en metres
#       distance = route['rows'][0]['elements'][0]['distance']['value']
#   #retourn une valeur (duree entre 2 repères) en seconds
#       duree = route['rows'][0]['elements'][0]['duration']['value']

#   #stocker ses valeur dans un set
#       distance_reperes[frozenset([repere1,repere2])] = distance
#       duree_reperes[frozenset([repere1,repere2])] = duree
# # stocker notre sets dans un seul fichier tsv
# with open("mes_reperes_dist_dur2.tsv", "w") as mes_reperes:
#   mes_reperes.write("\t".join(["repere1","repere2","distance_m","duree_s"]))
#   for (repere1, repere2) in distance_reperes.keys():
#     #stockage sou forme repere1\repere2\dist_m\dur_s
#     #transformer la distance et la duree a une chaine de character
#     mes_reperes.write("\n" +
#                        "\t".join([repere1,
#                                   repere2,
#                                   str(distance_reperes[frozenset([repere1, repere2])]),
#                                   str(duree_reperes[frozenset([repere1, repere2])])]))
# distance_reperes = {}
# duree_reperes ={}
# #list ==> set 
# reperes = set()
# #tsv file ==> dataframe avec pandas
# reperes_data = pd.read_csv("mes_reperes_dist_dur2.tsv", sep="\t")

# for i, row in reperes_data.iterrows():
#   distance_reperes[frozenset([row.repere1, row.repere2])] = row.distance_m
#   duree_reperes[frozenset([row.repere1, row.repere2])] = row.duree_s
#   reperes.update([row.repere1, row.repere2])
# ## 
# def compute_fitness(solution):
#   """ cette function return la distance totale du chemin courant entre les repères"""
#   solution_fitness = 0.0
#   for i in range(len(solution)):
#     repere1 = solution[i - 1]
#     repere2 = solution[i]
#     solution_fitness += distance_reperes[frozenset([repere1, repere2])]
#   return solution_fitness

# #### choix aleatoire
# def chemin_aleatoire():
#   """ creer un chemin aleatoire par l'ensembles des repères donnees """
#   new_chemin = list(reperes)
#   # melanger notre list
#   random.shuffle(new_chemin)
#   return tuple(new_chemin)
# #### mutation 1 : echange
# def mutation_agent(agent_genome, max_mutaions=3):
#   """ faire l echange au max de 3 repères dans notre set """
#   agent_genome = list(agent_genome)
#   num_mutation = random.randint(1,max_mutaions)
#   for mut in range(num_mutation):
#     index_echange1 = random.randint(0,len(agent_genome)-1)

#     index_echange2 = index_echange1
#     # pour eviter de choisir le meme index
#     while index_echange1 == index_echange2:
#       index_echange2 = random.randint(0,len(agent_genome)-1)
#     # faire l'echange
#     agent_genome[index_echange1], agent_genome[index_echange2] = agent_genome[index_echange2], agent_genome[index_echange1]
  
#   return tuple(agent_genome)

# #### mutation 2 : melange 
# def melange_mutation(agent_genome):
#   """
#    couper une sous list de taille aléatoire et la déplacer à un autre index aléatoire
#   """
#   agent_genome = list(agent_genome)

#   debut = random.randint(0, len(agent_genome)-1)
#   fin = debut + random.randint(2,10)

#   sous_genome = agent_genome[debut:fin]
#   agent_genome = agent_genome[:debut] + agent_genome[fin:]

#   index_insertion = random.randint(0, len(agent_genome)-1)
#   #index_insertion = random.randint(0,len(agent_genome)-1)
#   agent_genome = agent_genome[:index_insertion] + sous_genome + agent_genome[index_insertion:]
#   return tuple(agent_genome)

# ##### generer une population de differents chemin

# def generate_random_population(population_size):
#   random_population = []
#   for agent in range(population_size):
#     random_population.append(chemin_aleatoire())
#   return random_population

# ##### pour visualiser les resultats

# progress_visualisation_y = []
# progress_visualisation_x = []

# #####

# def genetique_algo(generations = 5000, population_size= 100):
#   """ fonction main de l algorithme genetique """
#   population_subset_size = int(population_size/10)
#   generation_sub = int(generations/10)
#   # creer une population
#   population = generate_random_population(population_size)

  

#   for generation in range(generations):
#     # calculer la distance entre les repères de tout la population
#     population_fitness = {}

#     for agent_genome in population:
#       if agent_genome in population_fitness:
#         continue
#       population_fitness[agent_genome] = compute_fitness(agent_genome)
    
#     # prendre 10% de la population qui a le chemin optimale et produire une offspring chacun d'eux
#     new_population = []
#     for rank, agent_genome in enumerate(sorted(population_fitness, key=population_fitness.get)[:population_subset_size]):
#       if (generation % generation_sub == 0 or generation == generations -1 ) and rank == 0:
#         print(f"Generation: {generation}, optimal chemin: {population_fitness[agent_genome]} m | unique genomes: {len(population_fitness)}")

#         progress_visualisation_y.append(population_fitness[agent_genome])
#         progress_visualisation_x.append(generation)

#         print(agent_genome)
#         print("--------------------------------------------------")
#       #### faire les mutation pour la 10% de la population
#       # creer une copie pour chaque chemin selectee
#       new_population.append(agent_genome)
#       # mutation 1 : creer 2 offspring par la mutation d'echange
#       for i in range(2):
#         new_population.append(mutation_agent(agent_genome, 3))
      
#       # mutation 2 : creer 7 offspring par la mutaion de melange
#       for i in range(7):
#         new_population.append(melange_mutation(agent_genome))
      
#       # remplacer population ==> new population de offspring
#     for i in range(len(population))[::-1]:
#       del population[i]
#     population = new_population
#   print("================ the optimal road ================")
#   print(agent_genome)
#   print("==================================================")
#   return list(agent_genome)



def map_view(request):

    context = {}
  
    return render(request, "landmark/map.html", context)

def location_view(request):
    return render(request, "landmark/MyLocation.html")

def Contact_view(request):
    return render(request, "landmark/ContactUs.html")

def optimalPath_view(request):
    return render(request, "landmark/optimalPath.html")    
