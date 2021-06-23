from graphviz import Digraph

class Automate:
    def __init__(self):
        # Brief : cette fonction déclare les différentes variables. 

        # Variable
        self.states = [] #Liste des Etats
        self.alphabet = [] #Liste des Symbols de l'alphabet
        self.transitions = [] #Liste des transitions classé par état d'origine
        self.initial = [] #Liste des Etats initiaux
        self.finals = [] #Liste des Etats finaux
        self.accessibles = [] #Liste des Etats accessible
        self.co_accessibles = [] #Liste des Etats co-accessible
        self.list_co = [] #Liste temporaire des Etats potentiellement co-accessible
        # Lancement du programme
        self.entry()

    def entry(self) : 
        # Brief : cette fonction demande à l'utilisateur si il veut importer un automate ou l'écrire lui-même.
        
        # Choix d'entrée
        entree = input("1 - Ecrire un automate\n2 - Charger un automate\n3 - Quitter\n")
        #Si il entre 1
        if (entree == "1") :
            #Entrée manuelle de l'automate
            #Etats
            etats = input("Quels sont les Etats (ex: 1,2,3 ) : ")
            self.ajout_etat(etats.split(","))
            #Alphabet
            symbols = input("Quels est l'alphabet (ex: a,b ) : ")
            self.def_alphabet(symbols.split(","))
            #Transition
            transitions = input("Quels sont les transitions (ex: 1-a-2,2-b-3 ) : ")
            self.ajout_transition(transitions.split(","))
            #Etats initiaux
            initiaux = input("Quels sont les états initiaux (ex: 1,2 ) : ")
            self.add_initiaux(initiaux.split(","))
            #Etats finaux
            finaux = input("Quels sont les états finaux (ex: 2,3 ) : ")
            self.add_finaux(finaux.split(","))
        #Si il entre 2
        elif (entree == "2"):
            # Entrée via un fichier
            # Demande nom du fichier
            nom_fichier = input("Entrer le nom du fichier : ")
            mon_fichier = open(nom_fichier, 'r')
            commandes = []
            # Parcours le fihier
            for ligne in mon_fichier:
                commandes.append(ligne)
            # Complète les variables automatiquement
            self.ajout_etat(commandes[0][:-1].split(","))
            self.def_alphabet(commandes[1][:-1].split(","))
            self.ajout_transition(commandes[2][:-1].split(","))
            self.add_initiaux(commandes[3][:-1].split(","))
            self.add_finaux(commandes[4].split(","))
        #Si il entre 3
        elif(entree == "3"):
            #Quitte le programme
            exit()
        #Sinon
        else:
            print("Rentrez une valeur valable !")
            self.entry()
        #Lance la suite du programme
        self.choice()

    def choice(self):
        #brief : cette fonction demande l'action à effectuer sur l'automate. 

        choix = input("\n1 - Afficher\n2 - Afficher les Etats Accessible\n3 - Compléter\n4 - Déterminiser\n5 - Sauvegarder\n6 - Quitter\n")
        # Afficher
        if(choix == "1"):
            self.afficher()
        # Accessible / Co-Accessible
        elif(choix == "2"):
            # Pour chaque états initiaux : 
            for i in self.initial:
                # Ajout de l'état initial aux états accessible
                self.accessibles.append(str(i))
                # Appel à la fonction "accessible()"
                self.accessible(i)
            # Affichage des Etats accessible
            print("\nLes Etats Accessibles : " + str(self.accessibles))
            # Pour chaque états : 
            for i in self.states:
                # Appel à la fonction "co_accessible()"
                self.co_accessible(i)
                # Réinialisation de la liste des états potentiellement co-accessible
                self.list_co = []
            # Affichage des Etats co_accessible
            print("Les Etats Co-Accessibles : " + str(self.co_accessibles))     
        # Compléter
        elif(choix == "3"):
            self.completer()
        # Déterminiser
        elif(choix == "4"):
            self.determiniser()
        # Sauvergarde
        elif(choix == "5"):
            self.sauvegarder()
        # Quitter
        elif(choix == "6"):
            exit()
        # Sinon
        else:
            # Si aucun des choix précedent alors affiche ce message 
            print("Rentrez une valeur valable !")
        # Redemande un choix à l'utilisateur
        self.choice()   

    def ajout_etat(self, state) : 
        # brief : Cette fonction ajoute les Etats dans la liste "self.states" si ils n'y sont pas. 
        # Param state : Liste des Etat à rajouter

        # Parcours les états de liste rentrée en parametre
        for s in state:
            # Verifie si il est en doublon dans la liste "self.states"
            if s in self.states :
                #si oui affiche : 
                print("Error : state '" + s + "' already exists.")
                return
            #sinon il l'ajoute
            self.transitions.append([])
            self.states.append(s)
        
    def def_alphabet(self,alphabet):
        # Brief : Cette fonction ajoute la liste rentrée en parametre dans la liste "self.alphabet"
        # Param alphabet : Liste contenant les différents symbols constituant l'alphabet

        # Parcours la liste rentrée en parametre
        for a in alphabet:
            # Si le symbol n'existe pas déja, il l'ajoute
            if a not in self.alphabet:
                self.alphabet.append(a)

    def ajout_transition(self, liste_transition):
        # Brief : Cette fonction ajoute la liste de transitions rentrée en parmaetre dans la liste "self.transitions"
        # Param liste_transition : Contient une liste avec les différentes transitions

        # Parcours les transitions
        for t in liste_transition:
            # Séparation de chaque parametre de la transition
            parametre = t.split("-")

            # Vérifie si la transition n'es pas déjà existante
            # Si oui :
            if t in self.transitions :
                print("Error : transition '" + t + "' already exists.")
            # Sinon :
            else:
                verif = True
                # Vérification si les parametres de la transition sont valables
                # Vérifie si l'état d'origine existe
                if parametre[0] not in self.states :
                    print("Error : state '" + parametre[0] + "' doesnt exist.")
                    verif = False
                # Vérifie si le symbol appartient à l'alphabet
                if parametre[2] not in self.states :
                    print("Error : state '" + parametre[2] + "' doesnt exist.")
                    verif = False
                # Vérifie si l'état de destination existe
                if parametre[1] not in self.alphabet :
                    print("Error : symbol '" + parametre[1] + "' doesnt exist.")
                    verif = False
                # Si la transition est bonne, alors on l'ajoute :
                if verif :
                    self.transitions[int(parametre[0])-1].append(t)

    def add_initiaux(self,liste_initiaux):
        # Brief : Ajouts des Etats initiaux dans la liste "self.initial"
        # Param liste_initiaux : liste contenant les états initiaux
        
        for i in liste_initiaux:
            # Vérifie si l'etat n'est pas déja dans la liste des initiaux. 
            if i not in self.initial:
                self.initial.append(i)
            
    def add_finaux(self,liste_finaux):
        # Brief : Ajouts des Etats finaux dans la liste "self.finals"
        # Param liste_finaux : liste contenant les états finaux

        for f in liste_finaux:
            # Vérifie si l'etat n'est pas déja dans la liste des finaux. 
            if f not in self.finals:
                self.finals.append(f)

    def afficher(self): 
        # Brief : Affiche l'automate à l'aide du logiciel graphviz

        g = Digraph('G', filename='automate.gv')
        # Affichage des Etats
        for i in self.states :
            # Si l'état est final
            if i in self.finals:
                # Création d'un état en forme de double cercle
                g.attr('node', shape='doublecircle')
                g.node(str(i))
            # Si l'état n'est pas final
            else:
                # Création d'un état en forme de cercle
                g.attr('node', shape='circle')
                g.node(str(i))
            # Si l'état est un état initial :
            if i in self.initial:
                # Création d'un état point
                g.attr('node', shape='point')
                g.node("I"+str(i))
                # Création d'une liaison entre le point et l'état initial
                g.edge("I"+str(i),str(i))
                        
        # Affichage des transitions
        # Parcours chaque transitions classé par état d'origine 
        for i in self.transitions:
            # Définition d'une variable qui va stock les différentes transitions ayant la même origine déjà ajoutées
            ajout = []
            # Parcours chaque transitions ayant le même état d'origine
            for j in i:
                # Séparation de chaque parametre de la transition
                parametre = j.split("-")
                # Définition d'une liste contenant tous les symboles des transitions avec la même destination 
                symbole = [parametre[1]]
                # Vérifie si la transition n'a pas déja été ajouté
                if j not in ajout: 
                    # Retiens que la transition va être ajoutée
                    ajout.append(j)
                    # Parcours chaque transitions ayant le même état d'origine 
                    for k in i:
                        dst = k.split("-")
                        # Si une autre transition à la même destination que l'état qui va être ajouté :
                        if dst[2] == parametre[2] and k != j:
                            # Retiens que la transition va également être ajoutée
                            ajout.append(k)
                            # Ajout du symbole de la nouvelle transition
                            symbole.append(dst[1])
                    # Ajoute une transition contenant tous les symboles allant vers la même destination
                    g.edge(parametre[0],parametre[2],','.join(symbole))

        g.view()

    def accessible(self,x):
        # Brief : Recherche tout les état accessible
        # Param x : Etat d'ou part la recherche des états accessibles
        try:
            # Parcours les transitions partant de x
            for i in self.transitions[int(x)-1]:
                parametre = i.split("-")
                # Si la destination de la transition n'est pas déjà dans "self.accessible", aors on l'ajoute
                if parametre[2] not in self.accessibles:
                    self.accessibles.append(parametre[2])
                    # On rappel la fonction accessible() avec comme départ la destination
                    self.accessible(parametre[2])
        except:
            return
    
    def co_accessible(self, x):
        # Brief : Recherche tout les état co-accessible
        # Param x : Etat d'ou part la recherche des états co-accessibles

        try:
            # Parcours les transitions partant de x
            for i in self.transitions[int(x)-1]:
                parametre = i.split("-")
                # Si l'état actuel n'est pas dans la liste des états co-accessible ni dans la liste des état potentiellement co-accessible :
                if parametre[0] not in self.co_accessibles and parametre[0] not in self.list_co:
                    self.list_co.append(parametre[0])
                # Si l'état de destination est final :
                if parametre[2] in self.finals:
                    # Et si il n'est pas dans la liste des états co-accessible ni dans la liste des état potentiellement co-accessible :
                    if parametre[2] not in self.co_accessibles and parametre[2] not in self.list_co:
                        self.list_co.append(parametre[2])
                    # Et on les ajoutes aux états co-accessible
                    for j in self.list_co:
                        self.co_accessibles.append(j)
                    self.list_co = []
                # Si l'état de destination n'est pas final 
                else :
                    # Vérifie si l'état ne boucle pas sur lui-même et si l'état de destination n'est pas dans la list "list_co"
                    if(parametre[0] != parametre[2] and parametre[2] not in self.list_co): 
                         # On rappel la fonction co_accessible() avec comme départ la destination
                        self.co_accessible(parametre[2])    
        except:
            return

    def completer(self):
        # Brief : Complete l'automate 

        # Ajout de l'état "poubelle"
        self.states.append('p')
        for s in self.states:
            # Liste des symboles des transitions existantes 
            r_transitions = []
            try:
                # Parcours les transitions de l'état
                for t in self.transitions[int(s)-1]:
                    parametre = t.split('-')
                    # Ajoutes les symboles utilisés
                    r_transitions.append(parametre[1])
                # Ajoute les transitions vers 'P' pour les symboles non existants
                for a in self.alphabet:
                    if a not in r_transitions:
                        self.ajout_transition([s+'-'+a+'-'+'p']) 
            except:
                return

    def determiniser(self):
        # Brief : Déterminise l'automate
        # Return : Affiche un tableau déterminisé

        # Variables
        colonne = [] # Liste contenant les états actuels  
        lignes = [] # Listes contenant les états suivants
        cmpt_ligne = 0 # Compteur pour les lignes

        # Ajout de la première ligne
        lignes.append([]) 
        # Ajout de l'état initial par agrégation des états initiaux
        colonne.append(self.initial) 

        for i in colonne:
            cmpt_colonnes = 0 #Compteur pour les colonnes (lettres)
            for a in self.alphabet:
                # Ajout de la "case" pour la lettre à la ligne n° cmpt_ligne
                lignes[cmpt_ligne].append([])
                # Parcours les états actuelles à la ligne n° cmpt_ligne
                for e in colonne[cmpt_ligne]:
                    if e != 'p': # Evite de créer un état actuels pour l'état "poubelle"
                        for t in self.transitions[int(e)-1]:
                            param = t.split('-')
                            # Recherche les transitions qui ont pour destination la colonne dans laquelle on se trouve
                            if param[1] == a and param[2] not in lignes[cmpt_ligne][cmpt_colonnes]:
                                lignes[cmpt_ligne][cmpt_colonnes].append(param[2])
                                # Range les états dans l'ordre 
                                lignes[cmpt_ligne][cmpt_colonnes] = sorted(lignes[cmpt_ligne][cmpt_colonnes])
                # Ajout aux états actuels  
                if lignes[cmpt_ligne][cmpt_colonnes] != [] and lignes[cmpt_ligne][cmpt_colonnes] not in colonne and lignes[cmpt_ligne][cmpt_colonnes] != ['p'] :
                    colonne.append(lignes[cmpt_ligne][cmpt_colonnes])
                    lignes.append([])
                cmpt_colonnes += 1
            cmpt_ligne +=1

        # Affichage
        try:
            # Affichage de l'alphabet
            print("{:^15}".format(" "), end=' | ')
            for a in self.alphabet:
                print("{:^15}".format(str(a)), end=' | ')
            print("\n")
            # Affichage des lignes
            for i in range(cmpt_ligne + 1):
                # Affichage des états actuels
                print("{:^15}".format(str(colonne[i])), end=' | ')
                # Affichage des états suivants
                for j in range(cmpt_colonnes):
                    # Si les états ne sont pas vides
                    if lignes[i][j] != []:
                        print("{:^15}".format(str(lignes[i][j])), end=' | ')
                    # Si les états sont vides
                    else:
                        print("{:^15}".format(" "), end=' | ')
                print("\n")
        except:
            return

    def sauvegarder(self):
        # Brief : Sauvegarde l'automate sous le format adéquate

        # Demande le nom du fichier
        nom_fichier = input("Entrez le nom du fichier : ")
        fichier = open(nom_fichier, 'w')
        # Ecriture des Etats
        fichier.write(str(self.states[0]))
        for i in self.states[1:] :
            fichier.write(","+str(i))
        fichier.write("\n")
        # Ecriture de l'alphabet
        fichier.write(str(self.alphabet[0]))
        for i in self.alphabet[1:] :
            fichier.write(","+str(i))
        fichier.write("\n")
        # Ecriture des transitions
        fichier.write(self.transitions[0][0])
        for i in self.transitions[0][1:]  :
            fichier.write(","+str(i))
        for i in self.transitions[1:] :
            for j in i :
                fichier.write(","+str(j))
        fichier.write("\n")
        # Ecriture des Etats initiaux
        fichier.write(str(self.initial[0]))
        for i in self.initial[1:] :
            fichier.write(","+str(i))
        fichier.write("\n")
        # Ecriture des Etats finaux
        fichier.write(str(self.finals[0]))
        for i in self.finals[1:] :
            fichier.write(","+str(i))
        fichier.close()

 
Automate()