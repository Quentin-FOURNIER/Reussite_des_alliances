import affichage
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
