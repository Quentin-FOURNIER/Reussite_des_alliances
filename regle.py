import affichage


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

    carte_en_cours = pioche.pop(0)
    liste_tas.append(carte_en_cours)

    if affiche:
        affichage.affichage_jeu(liste_tas)

    if saut_si_possible(liste_tas, len(liste_tas) - 2) and affiche:
        affichage.affichage_jeu(liste_tas)

    while True:
        drapeau = False
        for carte in liste_tas:
            if saut_si_possible(liste_tas, liste_tas.index(carte)) and affichage:
                affichage.affichage_jeu(liste_tas)
                drapeau = True
                break

        if not drapeau:
            return
