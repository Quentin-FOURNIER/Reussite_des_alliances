##########################################
# TITRE : PROJET SOLITAIRE DES ALLIANCES #
# AUTEUR : Quentin FOURNIER              #
# NIVEAU : L1 SPI                        #
##########################################

import init
import affichage
import regle

# affichage


#affichage


# affichage
def ecrire_fichier_reussite(nom_fich, pioche):
    '''Cette fonction permet de sauvegarder une pioche dans un fichier texte
    '''
    # On importe copy pour ne pas modifier la pioche :
    import copy
    # On crée les str tiret et espace pour la mise en forme :
    tiret = '-'
    esp = ' '
    # On crée la chaine dans laquelle on va réécrire le texte :
    chaine = ''
    # On copie la pioche pour ne pas modifier l'argument :
    copypioche = copy.copy(pioche)
    # On réecrit ou crée le fichier texte nom_fich :
    fichier = open(nom_fich, "w", encoding="utf-8")
    # On crée une boucle pour que cela fonctionne pour toutes les cartes :
    while len(copypioche) != 0:
        # On place la supprime la première carte de la liste et on la place dans data :
        data = copypioche.pop(0)
        # On récupère la valeur de cette carte :
        val = data["valeur"]
        # On récupère la couleur de cette carte :
        cou = data["couleur"]
        # On ajoute les morceaux à la chaine :
        chaine = chaine + val + tiret + cou
        # A part si la carte était la dernière on ajoute un espace à la fin :
        if len(copypioche) != 0:
            chaine = chaine + esp
    # On recopie la chaine dans le fichier texte
    fichier.write(chaine)
    # On ferme le fichier texte :
    fichier.close()

# règle


# règle
def reussite_mode_auto(pioche, affiche=False):
    '''Cette fonction permet à l'ordinateur de jouer tout seul de façcon parfaite, il joue une partie complette. Si affiche vaut True on voit toutes les étapes, sinon on ne voit rien. Cette fonction ne modifi pas la liste pioche en argument.
    '''

    # On import copy
    import copy
    # On crée le tas sur la table, qui ne contient initialement aucune carte.
    liste_tas = []
    # On copie la liste pioche en argument pour ne pas la modifier et modifier uniquement la copie
    copypioche = copy.copy(pioche)

    # On crée une boucle qui va tourner jusqu'a ce que la pioche soit vide (que la partie soit donc terminée)

    if affiche != False:
        affichage.affichage_jeu(copypioche)
    while copypioche != []:
        # Si affiche vaut False l'ordinateur fait la partie seul mais ne montre rien : on ne voit pas les étapes
        if affiche == False:
            regle.une_suite_de_sauts(liste_tas, copypioche)
        # Sinon (affiche vaut True) l'ordinateur fait seul la partie mais l'utilisateur voit toutes les étapes que fait l'ordinateur
        else:
            regle.une_suite_de_sauts(liste_tas, copypioche, True)
    # En retourne la liste des cartes qu'il reste sur la table a la fin :
    return liste_tas

# règle
def reussite_mode_auto_modeF(liste_tas, pioche):
    '''Cette fonction permet à l'ordinateur de jouer tout seul de façon parfaite, il finit une partie.
    '''
    while pioche != []:
        regle.une_suite_de_sauts(liste_tas, pioche, True)

# affichage
def menu():
    '''Cette fonction affiche un menu, demande a l'utilisateur quelle entrée il veut choisir dans le menu, vérifit si elle est correcte, puis renvoit sa réponse
    '''
    # On affiche une barre de séparation à chaque menu pour bien les distinguer :
    print("//////////////////////MENU//////////////////////\n")
    # On affiche les quatres possibilitées du menu :
    print("Découvrir une carte de la pioche (P)")
    print("Saisir un saut à faire (S)")
    print("Laisser l'ordinateur finir la réussite (F)")
    print("Abandonner la partie (Q)\n")
    # On demande au joueur quel action il souhaite effectuer :
    action = input("Quelle action souhaitez-vous effectuer : ")
    # Si le joueur saisit une commande en dehors des quatres possibilitées on lui redemande jusqu'à ce qu'il tape une commande correcte :
    while action != "P" and action != "S" and action != "F" and action != "Q":
        # On réecrit le menu :
        print("")
        print(
            "Vous avez saisit une commande erronée ! Veuillez choisir une commande valide dans la liste ci-dessous :\n")
        print("Découvrir une carte de la pioche (P)")
        print("Saisir un saut à faire (S)")
        print("Laisser l'ordinateur finir la réussite (F)")
        print("Abandonner la partie (Q)\n")
        # On redemande a chaque fois quelle action il souhaite effectuer :
        action = input("Quelle action souhaitez-vous effectuer : ")
    # On affiche une barre de fin de menu pour bien le distinguer :
    print("////////////////////////////////////////////////")
    # Enfin on retourne l'action une fois qu'elle est correcte :
    return action

# règle
def abandon_modeQ(liste_tas, pioche):
    '''Cette fonction réagit à l'abandon d'un joueur, Cela met une a une toutes les cartes sur la table sans effectuer de saut
    '''
    # On va effectuer l'action pour chaque carte qu'il reste dans la poche :
    while len(pioche) != 0:
        # On stock la premiere carte de la pioche et on la retire :
        a = pioche.pop(0)
        # On la rajoute sur la table :
        liste_tas.append(a)
        # On affiche chaque étapes :
        affichage.affichage_jeu(liste_tas)

# règle
def pioche_modeP(liste_tas, pioche):
    '''Cette fonction permet d'effectuer une simple pioche manuelement, puis d'afficher l'etape
    '''
    # On stock la premiere carte de la pioche et on la retire :
    a = pioche.pop(0)
    # On la rajoute sur la table :
    liste_tas.append(a)
    # On affiche l'étape :
    affichage.affichage_jeu(liste_tas)

# règle
def reussite_mode_manuel(pioche, nb_tas_max=2):
    # On effectue une copie de la pioche pour ne pas modifier la liste en argument :
    import copy
    copypioche = copy.copy(pioche)
    # On affiche le début de la partie :
    print("Nouvelle partie de : LA REUSSITE DES ALLIANCES !\n")
    # On définit un drapeau, lorsque ce drapeau vaudra vrai la partie touchera à sa fin :
    end = False
    # On initialise une liste contenant les tas sur la table (initialement vide) :
    liste_tas = []
    # On va effectuer des action jusqu'a la fin de la partie
    while end == False:
        # On récupère le choix de l'utilisateur :
        action = menu()
        # F : l'utilisateur demande à l'ordinateur de finir la partie seul :
        if action == 'F':
            # La partie sera donc terminer, pas besoin de recommencer la boucle :
            end = True
            reussite_mode_auto_modeF(liste_tas, copypioche)
        # Q : l'utilisateur veut abandonner la partie
        elif action == "Q":
            # La partie sera donc terminer, pas besoin de recommencer la boucle :
            end = True
            abandon_modeQ(liste_tas, copypioche)
        # P : L'utilisateur veut piocher une carte :
        elif action == "P":
            pioche_modeP(liste_tas, copypioche)
        # S : L'utilisateur souhaite effectuer un saut :
        elif action == "S":
            # On définit un drapeau de validité de l'indice
            nombrevalide = False
            # Cette boucle vérifit que l'utilisteur entre un entier, si ce n'est pas le cas elle redemande un entier :
            while nombrevalide == False:
                try:
                    indice = int(input(
                        "Saisir le tas que vous souhaitez faire sauter (le premier tas correspond à l'indice 0, le deuxieme à l'indice 1 ...) : "))
                    nombrevalide = True
                except:
                    print("")
                    print("Indice invalide\n")
            print("")
            # Si aucun saut n'a été effectuer on retourne au menu
            if regle.saut_si_possible(liste_tas, indice) == False:
                print("Saut impossible\n")
            # Si un saut à été effectué on affiche l'étape :
            else:
                affichage.affichage_jeu(liste_tas)
    # On vérifit ensuite si le joueur à gagné ou perdu :
    if len(liste_tas) <= nb_tas_max:
        print("GAGNE !!!")
    else:
        print("PERDU")

    # On retourne la liste des cartes sur la table :
    return liste_tas

# règle
def lance_reussite(mode, nb_cartes=32, affiche=False, nb_tas_max=2):
    '''Cette fonction permet de lancer une réussite en mode auto ou manuel, avec 32 ou 52 cartes, en affichant les étapes ou non pour le mode auto et en donnant le nombre de tas max pour une victoire pour le mode manuel
    '''
    # On crée une pioche mélangé :
    pioche = init.init_pioche_alea(nb_cartes)
    # Pour le mode automatique :
    if mode == 'auto':
        save = reussite_mode_auto(pioche, affiche)
    # Pour le mode manuel
    elif mode == 'manuel':
        save = reussite_mode_manuel(pioche, nb_tas_max)
    # On retourne la liste de carte que compose le tas
    return save

# règle
def lance_reussite_meilleur_echange_consecutif(mode, nb_cartes=32, affiche=False, nb_tas_max=2):
    '''Cette fonction permet de lancer une réussite en mode auto ou manuel, avec 32 ou 52 cartes, en affichant les étapes ou non pour le mode auto et en donnant le nombre de tas max pour une victoire pour le mode manuel (adapté pour faire un meilleur échange consécutif)
    '''
    # On crée une pioche mélangé :
    pioche1 = init.init_pioche_alea(nb_cartes)
    # On fait le meilleur echange consécutif
    pioche, poubelle = meilleur_echange_consecutif(pioche1)

    # Pour le mode automatique :
    if mode == 'auto':
        save = reussite_mode_auto(pioche, affiche)
    # Pour le mode manuel
    elif mode == 'manuel':
        save = reussite_mode_manuel(pioche, nb_tas_max)
    # On retourne la liste de carte que compose le tas
    return save

# simulation
def res_multi_simulation(nb_sim, nb_cartes=32):
    '''Cette fonction permet de simuler plusieurs reussite mode auto et de renvoyer une liste des nombre tas de fin de partie pour chaque partie
    '''
    # On cree une liste vide dans laquelle on va enregistrer nos résultats
    data = []
    # On crée une boucle pour que la fonction tourne pour chaque simulation
    for i in range(nb_sim):
        # On sauvegarde la liste des cartes sur la table dans save
        save = lance_reussite("auto", nb_cartes)
        # On récupère le nombre de carte dans la liste
        tas_save = len(save)
        # On l'ajoute à nos résultats
        data.append(tas_save)
    # On retourne la liste contenant les résultats de la simulation
    return data

# simulation
def res_multi_simulation_meilleur_echange_consecutif(nb_sim, nb_cartes=32):
    '''Cette fonction permet de simuler plusieurs reussite mode auto et de renvoyer une liste des nombre tas de fin de partie pour chaque partie (adapté pour stats de meilleur échange consécutif
    '''
    # On cree une liste vide dans laquelle on va enregistrer nos résultats
    data = []
    # On crée une boucle pour que la fonction tourne pour chaque simulation
    for i in range(nb_sim):
        # On sauvegarde la liste des cartes sur la table dans save
        save = lance_reussite_meilleur_echange_consecutif("auto", nb_cartes)
        # On récupère le nombre de carte dans la liste
        tas_save = len(save)
        # On l'ajoute à nos résultats
        data.append(tas_save)
    # On retourne la liste contenant les résultats de la simulation
    return data

# stat
def moyenne_liste(liste):
    '''Cette fonction permet d'effectuer la moyenne de tous les termes d'une liste de nombre
    '''
    # On effectue une copie de la liste pour ne pas modifier la liste en argument
    import copy
    copyliste = copy.copy(liste)
    # On définit une somme initialement égale à 0 dans laquelle on va ajouter chaque éléments de la liste
    somme = 0
    # On récupère le nombre d'élément à l'interieur de la list pour povoir diviser la somme par ce nombre
    nb_in_liste = len(liste)
    # Pour chaque élément de la liste on le supprime puis l'ajoute dans la somme
    while len(liste) != 0:
        data = liste.pop(0)
        somme += data
    # On divise la somme des éléments de la liste par le nombre d'élément de la liste
    moyenne = somme / nb_in_liste
    # On retourne la moyenne
    return moyenne

# stat
def statistiques_nb_tas(nb_sim, nb_cartes=32):
    '''Cette fonction permet d'afficher le minimum, le maximum et la moyenne des valeur obtenue apres avoir simulé des parties parfaites
    '''
    # On récupère la liste du nombre de tas qu'il reste a la fin des partie sur plusieurs simulation
    data = res_multi_simulation(nb_sim, nb_cartes)
    # On trie la liste
    data.sort()
    # On récupère le minimum
    minimum = data[0]
    # On récupère le maximum
    maximum = data[len(data) - 1]
    # On récupère la moyenne
    moyenne = moyenne_liste(data)
    # On affiche les résultats
    print("Statistique sur", nb_sim, "tentative(s) avec un jeu de", nb_cartes, "cartes :")
    print("minimum =", minimum)
    print("maximum =", maximum)
    print("moyenne =", moyenne)

# stat
def statistiques_nb_tas_moyenne(nb_sim, nb_cartes):
    '''Cette fonction permet de retourner la moyenne des valeur obtenue apres avoir simulé des parties parfaites
    '''
    # On récupère la liste du nombre de tas qu'il reste a la fin des partie sur plusieurs simulation
    data = res_multi_simulation(nb_sim, nb_cartes)
    # On récupère la moyenne
    moyenne = moyenne_liste(data)
    # On retourne la moyenne:
    return moyenne


# PARTIE extension###############################################################

# Statistique grahique :


def liste_2_x(x):
    '''Cette fonction renvoit une liste avec des termes allant de 2 à x
    '''
    # On crée une liste vide dans laquelle on mettre tous les termes
    l = []
    # On crée la boucle pour chaque terme
    for i in range(2, x + 1):
        l.append(i)
    # On retourne la liste
    return l


def nb_win(liste, maxi):
    '''Cette fonction permet de donner le nombre de victoire avec la listes des tas restant sur plusieurs simulation de parties, avec le nombre de tas max pour gagner en deuxieme argument
    '''
    # On commence par fixer les victoires à 0
    win = 0
    # Pour chaque élément on vérifit qu'il est gagnant
    for i in liste:
        if i <= maxi:
            # Et on l'ajoute si il l'est
            win += 1
    # On retourne la liste des éléments gagnants
    return win


def stats_party(nb_cartes, resultat=False):
    '''Cette fonction permet d'afficher les statistiques de beaucoup de parties et d'afficher le graphe contenant toutes les valeurs. Si resultat vaut vrai on affiche les valeurs obtenu pour chaque nombre de tas max. (Les resultats ne sont coherents qu'apres un enorme nombre de tentatives, j'ai savegardé 2 fichiers contenant les resulats et le graphe pour 1 000 000 d'essais si besoin)
    '''
    # On import pyplot on en a besoin pour le graphe
    import matplotlib.pyplot as plt
    # On crée la liste des valeurs gagnants en % initialement vide
    liste_win = []
    # On crée une liste contenant les valeurs de n simulations
    liste = res_multi_simulation(1000, nb_cartes)
    # Pour chaque valeur :
    for i in range(2, nb_cartes + 1):
        # On récupère le nombre de victoire pour chaque tax max :
        win = nb_win(liste, i)
        # On ramène le résultat sur 100 ( A augmenter si le nombre de simulation augmente) :
        win = win / 10000
        # On ajoute chaque nombre de victoire à la liste
        liste_win.append(win)
    # Si l'utilistateur a choisit d'afficher les résultats :
    if resultat == True:
        # On affiche tous les résultats
        print("Résultats pour un jeu de {} cartes :".format(nb_cartes))
        for i in range(nb_cartes - 1):
            print("{} tas sur la table : {} % de chance de victoire".format(liste_2_x(nb_cartes)[i], liste_win[i]))
    # On crée le graphe
    plt.plot(liste_2_x(nb_cartes), liste_win, color='green')
    plt.xlabel('Nombre de carte dans le jeu')
    plt.ylabel('Pourcentage de réussite')
    plt.title('Graphe du pourcentage de victoire par rapport au nombre de carte')
    plt.show()
    plt.close()


def stats_party_meilleur_echange_consecutif(nb_cartes, resultat=False):
    '''Cette fonction permet d'afficher les statistiques de beaucoup de parties et d'afficher le graphe contenant toutes les valeurs. Si resultat vaut vrai on affiche les valeurs obtenu pour chaque nombre de tas max. (Les resultats ne sont coherents qu'apres un enorme nombre de tentatives, j'ai savegardé 2 fichiers contenant les resulats et le graphe pour 1 000 000 d'essais si besoin) (adapté pour les stats de meilleur_echange_consecutif)
    '''
    # On import pyplot on en a besoin pour le graphe
    import matplotlib.pyplot as plt
    # On crée la liste des valeurs gagnants en % initialement vide
    liste_win = []
    # On crée une liste contenant les valeurs de n simulations
    liste = res_multi_simulation_meilleur_echange_consecutif(1000, nb_cartes)
    # Pour chaque valeur :
    for i in range(2, nb_cartes + 1):
        # On récupère le nombre de victoire pour chaque tax max :
        win = nb_win(liste, i)
        # On ramène le résultat sur 100 ( A augmenter si le nombre de simulation augmente) :
        win = win / 100
        # On ajoute chaque nombre de victoire à la liste
        liste_win.append(win)
    # Si l'utilistateur a choisit d'afficher les résultats :
    if resultat == True:
        # On affiche tous les résultats
        print("Résultats pour un jeu de {} cartes :".format(nb_cartes))
        for i in range(nb_cartes - 1):
            print("{} tas sur la table : {} % de chance de victoire".format(liste_2_x(nb_cartes)[i], liste_win[i]))
    # On crée le graphe
    plt.plot(liste_2_x(nb_cartes), liste_win, color='green')
    plt.xlabel('Nombre de carte dans le jeu')
    plt.ylabel('Pourcentage de réussite')
    plt.title('Graphe du pourcentage de victoire par rapport au nombre de carte')
    plt.show()
    plt.close()


# PARTIE meilleur_echange_consecutif#############################################


def echange_next(pioche, indice):
    '''Cette fonction permet d'échanger une carte d'indice 'indice' dans la pioche avec la carte suivante, puis de renvoyer le nombre de tas de fin de partie à la fin de la partie. Cette fonction ne modifie pas la pioche en argument
    '''
    # On importe copy et on copy la liste pour ne pas modifier la liste en argument
    import copy
    copypioche = copy.copy(pioche)
    # On fait l'échange entre les deux cartes
    copypioche[indice], copypioche[indice + 1] = copypioche[indice + 1], copypioche[indice]
    # On récupère la liste de cartes restant sur le tas
    outliste = reussite_mode_auto(copypioche, affiche=False)
    # On récupère le nombre de tas quil reste sur la table
    tas = len(outliste)
    # On retourne la pioche avec le nombre de tas après l'échange
    return copypioche, tas


def meilleur_echange_consecutif(pioche):
    '''Cette fonction permet de renvoyer la pioche avec le meilleur echange consecutif possible, ainsi que le nombre de tas restant après l'échange
    '''
    # On import copy pour ne pas modifier pioche
    import copy
    # mini correspond au nombre de tas de la pioche initiale
    mini = len(reussite_mode_auto(pioche, affiche=False))
    # mini2 est une copy de mini
    mini2 = mini
    # On crée minix qui correspond à l'amélioration après l'échange qui vaut au minimum 0 dans le cas ou aucun échange ne permet d'amèliorer la suite
    minix = 0
    # On copy la pioche
    minipioche = copy.copy(pioche)
    # Pour un jeu de 32 cartes
    if len(pioche) == 32:
        # On crée une boucle qui va tester pour chaque échange le quel est le meilleur et retourné la meilleur nouvelle pioche avec l'amélioration (nombres de tas gagnés)
        for i in range(31):
            copypioche, save = echange_next(pioche, i)
            if save <= mini:
                minix = mini2 - save
                minipioche = copypioche
                mini = save
        return (minipioche, minix)
    # Pour un jeu de 52 cartes
    elif len(pioche) == 52:
        # On crée une boucle qui va tester pour chaque échange le quel est le meilleur et retourné la meilleur nouvelle pioche avec l'amélioration (nombres de tas gagnés)
        for i in range(51):
            copypioche, save = echange_next(pioche, i)
            if save <= mini:
                minix = mini2 - save
                minipioche = copypioche
                mini = save
        return (minipioche, minix)


if __name__ == "__main__":
    pioche_trie = init.init_pioche_fichier()
    pioche_alea = init.init_pioche_alea(52)
    # affichage.affichage_jeu(pioche_alea)
    # regle.une_suite_de_sauts([{'valeur': 'V', 'couleur': 'C'},{'valeur': 'V', 'couleur': 'C'},{'valeur': 'V', 'couleur': 'C'},{'valeur': 'V', 'couleur': 'C'}, {'valeur': '8', 'couleur': 'P'}],[{'valeur': '10', 'couleur': 'C'}, {'valeur': '9', 'couleur': 'C'}],)
    regle.une_suite_de_sauts([{'couleur': 'T', 'valeur': 'R'}, {'couleur': 'C', 'valeur': 'D'}, {'couleur': 'P', 'valeur': '8'}, {'couleur': 'K', 'valeur': '8'}, {'couleur': 'T', 'valeur': 'D'}, {'couleur': 'T', 'valeur': '9'}, {'couleur': 'P', 'valeur': 'R'}, {'couleur': 'C', 'valeur': 'R'}, {'couleur': 'T', 'valeur': '7'}, {'couleur': 'T', 'valeur': 'V'}, {'couleur': 'C', 'valeur': '10'}, {'couleur': 'P', 'valeur': '7'}, {'couleur': 'P', 'valeur': 'D'}, {'couleur': 'T', 'valeur': '10'}, {'couleur': 'T', 'valeur': 'A'}], [{'couleur': 'P', 'valeur': '10'}, {'couleur': 'K', 'valeur': '10'}, {'couleur': 'K', 'valeur': '7'}], True)
    # print(reussite_mode_auto(init_pioche_alea(32),True))
    # print(reussite_mode_manuel(init_pioche_alea(32)))
    # print(lance_reussite('manuel',nb_cartes=52,affiche=True))
    # print(res_multi_simulation(1000,nb_cartes=32))
    # statistiques_nb_tas(2,nb_cartes=32)
    # stats_party(32,True)
   #  print(echange_next(init_pioche_fichier('Fichiers_a_fournir/data_init.txt'), 26))
   #  print(meilleur_echange_consecutif(init_pioche_fichier('Fichiers_a_fournir/data_init.txt')))
   #  stats_party_meilleur_echange_consecutif(32, True)
   #