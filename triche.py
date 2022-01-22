import regle
import copy
import init


def switch_next(pioche, indice):
    """
    Cette fonction permet d'échanger une carte d'indice 'indice' dans la pioche avec la carte suivante,
    puis de renvoyer le nombre de tas de fin de partie à la fin de la partie. Cette fonction ne modifie pas la pioche
    en argument

    @param pioche : pioche classique
    @type pioche : list

    @param indice : indice à échanger
    @type indice : int

    @return : nouvelle pioche, longueur du tas de fin de partie
    @rtype : list, int
    """

    copie_pioche = copy.copy(pioche)
    copie_pioche[indice], copie_pioche[indice + 1] = copie_pioche[indice + 1], copie_pioche[indice]
    return copie_pioche, len(regle.jeu_complet_mode_auto(copie_pioche, affiche=False))


def meilleur_switch(pioche):
    """
    Cette fonction permet de renvoyer la pioche avec le meilleur échange consécutif possible, ainsi que le nombre
    de tas améliorés

    @param pioche : pioche
    @type pioche : list

    @return : pioche truquée
    @rtype : list
    """

    # nb_carte_pioche_classique_fin = len(regle.jeu_complet_mode_auto(pioche, affiche=False))
    #
    # upgrade = 0
    # pioche_triche = copy.copy(pioche)
    #
    # for i in range(len(pioche)-1):
    #     copie_pioche, carte_table_switch_fin = switch_next(pioche, i)
    #     if carte_table_switch_fin <= nb_carte_pioche_classique_fin:
    #
    #         upgrade = nb_carte_pioche_classique_fin - carte_table_switch_fin
    #
    #         pioche_triche = copie_pioche
    #         # nb_carte_pioche_classique_fin = carte_table_switch_fin
    #
    # return pioche_triche, upgrade

    tas_fin_classique = len(regle.jeu_complet_mode_auto(pioche, affiche=False))
    upgrade = 0
    pioche_triche = copy.copy(pioche)
    meilleur_tas = tas_fin_classique
    for i in range (len(pioche) - 1):
        switch_pioche, switch_tas = switch_next(pioche, i)
        if switch_tas <= meilleur_tas:
            print(tas_fin_classique)
            print("-> " + str(switch_tas))
            upgrade = tas_fin_classique - switch_tas
            pioche_triche = copy.copy(switch_pioche)
            meilleur_tas = switch_tas

    return pioche_triche, upgrade


def lance_meilleur_switch(mode, nb_cartes=32, affiche=False, nb_tas_max=2):
    """
    Cette fonction permet de lancer une réussite en mode auto ou manuel, avec 32 ou 52 cartes, en affichant les
    étapes ou non pour le mode auto et en donnant le nombre de tas max pour une victoire pour le mode manuel (adapté
    pour faire un meilleur échange consécutif)

    @param mode: auto ou manuel
    @type mode: str
    @param nb_cartes: nombre de cartes dans le jeu
    @type nb_cartes: int
    @param affiche: affichage
    @type affiche: bool
    @param nb_tas_max: tas max pour gagner
    @type nb_tas_max: int
    @return:
    @rtype:
    """

    pioche_init = init.init_pioche_alea(nb_cartes)
    pioche, poubelle = meilleur_switch(pioche_init)

    if mode == 'auto':
        return regle.jeu_complet_mode_auto(pioche, affiche)
    elif mode == 'manuel':
        return regle.jeu_mode_manuel(pioche, nb_tas_max)


def res_multi_simulation_meilleur_switch(nb_sim, nb_cartes=32):
    """
    Cette fonction permet de simuler plusieurs réussites mode auto et de renvoyer une liste des nombres tas de fin de
    partie pour chaque partie adapté pour stats de meilleur échange consécutif


    @param nb_sim : nombre de simulations
    @type nb_sim : int

    @param nb_cartes : nombre de cartes dans le jeu
    @type nb_cartes : int

    @return : liste des tas de fin de partie
    @rtype : list
    """

    data = []

    for i in range(nb_sim):
        save = lance_meilleur_switch("auto", nb_cartes)
        data.append(len(save))

    return data

