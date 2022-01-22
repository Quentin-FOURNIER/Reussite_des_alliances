import regle
import triche
import matplotlib.pyplot as plt


def res_multi_simulation(nb_sim, nb_cartes=32):
    """
    Cette fonction permet de simuler plusieurs réussites mode auto et de renvoyer une liste du nombre tas de fin de
    partie pour chaque partie

    @param nb_sim : Nombre de simulations
    @type nb_sim : int

    @param nb_cartes : nombre de cartes dans le jeu
    @type nb_cartes : int

    @return : liste des résultats
    @rtype : list
    """

    data = []

    for i in range(nb_sim):
        data.append(len(regle.lance_jeu("auto", nb_cartes)))

    return data


def statistiques_nb_tas(nb_sim, nb_cartes=32):
    """
    Cette fonction permet d'afficher le minimum, le maximum et la moyenne des valeurs obtenues apres avoir simulé des
    parties parfaites

    @param nb_sim : nombre de simulations
    @type nb_sim : int

    @param nb_cartes : Nombre de cartes dans le jeu
    @type nb_cartes : int
    """

    data = res_multi_simulation(nb_sim, nb_cartes)

    print("Statistique sur", nb_sim, "tentative(s) avec un jeu de", nb_cartes, "cartes :")
    print("minimum =", min(data))
    print("maximum =", max(data))
    print("moyenne =", moyenne_liste(data))


def moyenne_liste(liste):
    """
    Cette fonction permet d'effectuer la moyenne de tous les termes d'une liste de nombre

    @param liste : liste d'entiers
    @type liste : list

    @return : moyenne
    @rtype : int
    """

    somme = 0
    for i in liste:
        somme += i
    return somme / len(liste)


def stats_party(nb_cartes, affiche=False):
    """
    Cette fonction permet d'afficher les statistiques de beaucoup de parties et d'afficher le graphe contenant toutes
    les valeurs. Si affiche vaut vrai on affiche les valeurs obtenues pour chaque nombre de tas max. (Les résultats ne
    sont coherent qu'après un énorme nombre de tentatives, j'ai sauvegardé 2 fichiers contenant les résultats et le
    graphe pour 1 000 000 d'essais si besoin)

    @param nb_cartes :
    @type nb_cartes :

    @param affiche :
    @type affiche :

    @return :
    @rtype :
    """

    liste_win = []
    liste = res_multi_simulation(10000, nb_cartes)

    for i in range(2, nb_cartes + 1):
        liste_win.append(nb_win(liste, i) / 100)

    if affiche:
        print("Résultats pour un jeu de {} cartes :".format(nb_cartes))
        for i in range(nb_cartes - 1):
            print("{} tas sur la table : {} % de chance de victoire".format(liste_2_x(nb_cartes)[i], liste_win[i]))

    plt.plot(liste_2_x(nb_cartes), liste_win, color='green')
    plt.xlabel('Nombre de carte dans le jeu')
    plt.ylabel('Pourcentage de réussite')
    plt.title('Graphe du pourcentage de victoire par rapport au nombre de carte')
    plt.show()
    plt.close()


def nb_win(liste, maxi):
    """
    Cette fonction permet de donner le nombre de victoires avec la liste des tas restant sur plusieurs simulations de
    parties, avec le nombre de tas max pour gagner en deuxième argument

    @param liste : liste des fins de partie
    @type liste : list

    @param maxi : tas max pour gagner
    @type maxi : int

    @return : nombre de parties gagnées
    @rtype : int
    """

    win = 0

    for i in liste:
        if i <= maxi:
            win += 1

    return win


def liste_2_x(x):
    """
    Cette fonction renvoi une liste avec des termes allant de 2 à x

    @param x : fin
    @type x : int

    @return : liste de 2 à x
    @rtype : list
    """

    liste = []

    for i in range(2, x + 1):
        liste.append(i)

    return liste


def stats_partie_meilleur_switch(nb_cartes, affiche=False):
    """
    Cette fonction permet d'afficher les statistiques de beaucoup de parties et d'afficher le graphe contenant toutes
    les valeurs. Si affiche vaut vrai on affiche les valeurs obtenues pour chaque nombre de tas max. (Les résultats ne
    sont cohérents qu'après un énorme nombre de tentatives, j'ai sauvegardé 2 fichiers contenant les résultats et le
    graphe pour 1 000 000 d'essais si besoin) (adapté pour les stats de meilleur_switch)

    @param nb_cartes : nombre de cartes dans le jeu
    @type nb_cartes : int

    @param affiche : affichage
    @type affiche :bool
    """

    liste_win = []
    liste = triche.res_multi_simulation_meilleur_switch(10000, nb_cartes)
    for i in range(2, nb_cartes + 1):
        liste_win.append(nb_win(liste, i) / 100)

    if affiche:
        print("Résultats pour un jeu de {} cartes :".format(nb_cartes))
        for i in range(nb_cartes - 1):
            print("{} tas sur la table : {} % de chance de victoire".format(liste_2_x(nb_cartes)[i], liste_win[i]))

    plt.plot(liste_2_x(nb_cartes), liste_win, color='green')
    plt.xlabel('Nombre de carte dans le jeu')
    plt.ylabel('Pourcentage de réussite')
    plt.title('Graphe du pourcentage de victoire par rapport au nombre de carte')
    plt.show()
    plt.close()