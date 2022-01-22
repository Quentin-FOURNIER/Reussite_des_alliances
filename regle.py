import affichage
import init
import copy


def alliance(carte1, carte2):
    """
    Renvoi vrai si la valeur ou la couleur des deux cartes est identique

    @param carte1 : une carte
    @type carte1 : dict
    @param carte2 : une carte
    @type carte2 : dict
    @return : true si alliance, false sinon
    @rtype : bool
    """

    return carte1["valeur"] == carte2["valeur"] or carte1['couleur'] == carte2['couleur']


def saut_si_possible(liste_cartes_tas, num_tas):
    """
    Fait le saut s'il est possible

    @param liste_cartes_tas : cartes sur le tas
    @type liste_cartes_tas : list

    @param num_tas : numéro du tas
    @type num_tas : int

    @return : le saut à t-il été effectué ?
    @rtype : bool
    """

    if (len(liste_cartes_tas) > 2 and 0 < num_tas < (len(liste_cartes_tas) - 1)
            and alliance(liste_cartes_tas[num_tas - 1], liste_cartes_tas[num_tas + 1])):
        liste_cartes_tas.pop(num_tas - 1)
        return True

    return False


def une_suite_de_sauts(liste_tas, pioche, affiche=False):
    """
    L'ordinateur fait tous les sauts possibles à partir d'un premier si celui-ci est possible

    @param liste_tas : tas en cours
    @type liste_tas : list

    @param pioche : pioche
    @type pioche : list

    @param affiche : affiche ou non
    @type affiche : bool
    """

    carte_en_cours = pioche.pop(0)
    liste_tas.append(carte_en_cours)

    if affiche:
        affichage.affichage_jeu(liste_tas)

    if saut_si_possible(liste_tas, len(liste_tas) - 2) and affiche:
        affichage.affichage_jeu(liste_tas)

    while True:
        drapeau = False
        for carte in liste_tas:
            if saut_si_possible(liste_tas, liste_tas.index(carte)):
                if affiche:
                    affichage.affichage_jeu(liste_tas)
                drapeau = True
                break

        if not drapeau:
            return


def jeu_complet_mode_auto(pioche, affiche=False):
    """
    Permet à l'ordinateur de jouer tout seul de façon parfaite, il joue une partie complete.

    @param pioche : la pioche
    @type pioche : list

    @param affiche : Si affiche vaut True on voit toutes les étapes
    @type affiche : bool

    @return : le tas final
    @rtype : list
    """
    liste_tas = []
    copie_de_la_pioche = copy.copy(pioche)

    if affiche:
        affichage.affichage_jeu(pioche)

    while copie_de_la_pioche:
        une_suite_de_sauts(liste_tas, copie_de_la_pioche, affiche)

    return liste_tas


def jeu_mode_auto_modeF(liste_tas, pioche):
    """
    Fini la réussite

    @param liste_tas : cartes sur la table
    @type liste_tas : list

    @param pioche : cartes dans la pioche
    @type pioche : list
    """

    while pioche:
        une_suite_de_sauts(liste_tas, pioche, True)


def affichage_texte_menu():
    print("Découvrir une carte de la pioche (P)")
    print("Saisir un saut à faire (S)")
    print("Laisser l'ordinateur finir la réussite (F)")
    print("Abandonner la partie (Q)\n")
    return input("Quelle action souhaitez-vous effectuer : ")


def menu():
    """
    Menu

    @return: le choix de l'utilisateur
    @rtype: str
    """

    print("- - - - - - - - - - - - - MENU - - - - - - - - - - - - -\n")
    action = affichage_texte_menu()

    while action != "P" and action != "S" and action != "F" and action != "Q":
        print(
            "\nVous avez saisit une commande erronée ! Veuillez choisir une commande valide dans la liste ci-dessous "
            ":\n")
        action = affichage_texte_menu()

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    return action


def abandon_modeQ(liste_tas, pioche):
    """
    Fini le jeu sans faire de saut

    @param liste_tas : cartes sur la table
    @type liste_tas : list

    @param pioche : cartes dans la pioche
    @type pioche : list
    """

    while len(pioche) != 0:
        liste_tas.append(pioche.pop(0))
        affichage.affichage_jeu(liste_tas)


def pioche_modeP(liste_tas, pioche):
    """
    Pioche une carte et affiche l'état courant

    @param liste_tas : cartes sur la table
    @type liste_tas : list

    @param pioche : cartes dans la pioche
    @type pioche : list
    """

    liste_tas.append(pioche.pop(0))
    affichage.affichage_jeu(liste_tas)


def jeu_mode_manuel(pioche, nb_tas_max=2):
    """
    Jeu en mode manuel

    @param pioche : cartes dans la pioche
    @type pioche : list

    @param nb_tas_max : nombre de tas maximums pour gagner
    @type nb_tas_max : int

    @return : cartes sur la table
    @rtype : list
    """
    copie_pioche = copy.copy(pioche)
    print("Nouvelle partie de : LA RÉUSSITE DES ALLIANCES !\n")
    end = False

    # On initialise une liste contenant les tas sur la table (initialement vide) :
    liste_tas = []

    while not end:
        action = menu()
        # F : l'utilisateur demande à l'ordinateur de finir la partie seul :
        if action == 'F':
            end = True
            jeu_mode_auto_modeF(liste_tas, copie_pioche)

        # Q : l'utilisateur veut abandonner la partie
        elif action == "Q":
            end = True
            abandon_modeQ(liste_tas, copie_pioche)

        # P : L'utilisateur veut piocher une carte :
        elif action == "P":
            pioche_modeP(liste_tas, copie_pioche)

        # S : L'utilisateur souhaite effectuer un saut :
        elif action == "S":
            indice = int(input(
                "Saisir le tas que vous souhaitez faire sauter (le premier tas correspond à l'indice 0, "
                "le deuxième à l'indice 1 ...) : "))

            if not saut_si_possible(liste_tas, indice):
                print("Saut impossible\n")
            else:
                affichage.affichage_jeu(liste_tas)

    if len(liste_tas) <= nb_tas_max:
        print("GAGNE !!!")
    else:
        print("PERDU")

    # On retourne la liste des cartes sur la table :
    return liste_tas


def lance_jeu(mode, nb_cartes=32, affiche=False, nb_tas_max=2):
    """
    Cette fonction permet de lancer une réussite en mode auto ou manuel, avec 32 ou 52 cartes, en affichant les
    étapes ou non pour le mode auto et en donnant le nombre de tas max pour une victoire pour le mode manuel

    @param mode : manuel ou auto
    @type mode : str

    @param nb_cartes : nombre de cartes dans le jeu
    @type nb_cartes : int

    @param affiche : affichage des étapes
    @type affiche : bool

    @param nb_tas_max : nombre de cartes max à la fin pour gagner
    @type nb_tas_max : int

    @return : cartes sur la table à la fin
    @rtype : list
    """

    if mode == 'auto':
        return jeu_complet_mode_auto(init.init_pioche_alea(nb_cartes), affiche)
    else:
        return jeu_mode_manuel(init.init_pioche_alea(nb_cartes), nb_tas_max)
