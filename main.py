#python back-end
"""
class créer personne() pour l'ensemble
des informations liées à la creation ou 
modification du robot
""" 
class CreerPersonne():
        def __init__(self,nom="magnus",prenom="X",tache="aucune"):
            #un constructeur avec des valeurs par defaut au cas ou l'utilisateur ne les remplissent op
            self.nom = nom
            self.prenom = prenom
            self.tache = tache
            #tache = ce que le robot est capable de faire
        def constructeurPersonne(self,nom="magnus",prenom="X",tache="aucune"):
            """
            fonction constructeurPersonne pour créer un robot le mot personne veut dire robot
            """
            self.dictPersonnes = {
                "nom": nom,
                "prenom":prenom,
                "taches":tache
              }
            #dictionnaire pour stocker les données la clé (nom) stock le nom qu on va passer en parametre ainsi de suite
            print(self.dictPersonnes)
        def aujoutRobot(self):
            dictPersonnes+=dictPersonnes
            #créer un robot dictPersonnes+=dictPersonnes permet d'ajouter de nouveau
            #dictionnaire pour enregestrer des données si on execute cette fonction
def run():
    Donnees=[]
    #liste vide pour stocker les informations de l'utilisateur nom prenom age
    print("")
    print(" veuillez entrez vos informations")
    print("")
    nom = input("quel est votre nom ")
    prenom = input('quel est votre prenom ')
    age = input("quel est votre age ")
    print('')
    save = input(' souhaitez-vous enregestrer vos données personnelles ? ')
    print("")
    #si la reponse est "oui" l'objet append permet de recupérer l'info saisi 
    # et l'ajouter à notre liste vide
    if save == 'oui':
        Donnees.append(nom)
        Donnees.append(prenom)
        Donnees.append(age)
        print("données enregestrer avec succées ")
        print('')
        see = input('voulez vous revoir vos données ')
        print("")
        if see == "oui":
            print(Donnees)
            #si l'utilisateur veut revoir ses données on fait appel à la liste ou les données sont stockés
            print('')
            print('')
            print('informations personnes => nom: {} prenom: {} age: {} '.format (nom, prenom , age))
            #l'objet format permet de recupérer respectivement le nom prenom et age pour remplacer les crochets
        else:
            print("")
            print("aucune donnée sauvegardées !")
    else:
        print("merci")
        print('')
    print('')
    print('felicitation vous venez de gagner votre pemier robot enfant')
    print("")
run()
print("")
voirRobot = input('voulez-vous voir votre robot ')
if voirRobot == 'oui bien sur':
    Personne = CreerPersonne()
    print('')
    Personne.constructeurPersonne()
else:
    print("d'accord !")
print("")
question = input('personnaliser votre robot ? ')
if question == "oui":
    nouveauNom = input('entrez un nouveau nom ')
    nouveauPrenom = input('entrez un nouveau prenom ')
    nouveauTache = 'veuillez l entrainer'
    Personne = CreerPersonne()
    #personne = notre class CreerPersonne pour pouvoir modifier le contenu de notre class
    print('')
    Personne.constructeurPersonne(nom=nouveauNom,prenom=nouveauPrenom,tache=nouveauTache)
    """
    la ligne ci-dessus permet de faire appel à la  fonction constructeurPersonne de notre class
    en lui incrémentant de nouvelles pour le nom prenom et la tache 
    bref cette ligne permet à l'utilisateur de changer les noms par defaut de son
    robot afin d'utiliser ses propres appélations
    """
else:
    print('ok....')
listeTaches = []
#liste vide pour stocker les données d'apprentissage
etude = input("souhaitez-vous entrainez votre robot ? ")
if etude != "non" or etude != "meme pas" or etude != "pas maintenant":
    stock = input('entrez ce que tu souhaite lui apprendre ')
    # != signifie différent
else:
    print('nous vous remercierons de votre participation ')
#j ai pas encore testé ces derniers ligne de code si jamais vous rencontrez des erreus