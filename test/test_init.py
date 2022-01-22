import unittest

import init


class TestInit(unittest.TestCase):

    def test_init_pioche_fichier_1(self):
        self.assertEqual(init.init_pioche_fichier("text/data_init_32.txt"),
                         [{'valeur': 'V', 'couleur': 'C'}, {'valeur': '8', 'couleur': 'P'},
                          {'valeur': 'V', 'couleur': 'K'}, {'valeur': 'A', 'couleur': 'C'},
                          {'valeur': '10', 'couleur': 'P'}, {'valeur': '8', 'couleur': 'T'},
                          {'valeur': '8', 'couleur': 'K'}, {'valeur': '9', 'couleur': 'T'},
                          {'valeur': 'V', 'couleur': 'P'}, {'valeur': 'A', 'couleur': 'P'},
                          {'valeur': '10', 'couleur': 'K'}, {'valeur': '9', 'couleur': 'P'},
                          {'valeur': '7', 'couleur': 'T'}, {'valeur': 'R', 'couleur': 'T'},
                          {'valeur': '10', 'couleur': 'C'}, {'valeur': '9', 'couleur': 'K'},
                          {'valeur': '9', 'couleur': 'C'}, {'valeur': 'D', 'couleur': 'T'},
                          {'valeur': 'R', 'couleur': 'C'}, {'valeur': '8', 'couleur': 'C'},
                          {'valeur': 'D', 'couleur': 'K'}, {'valeur': '7', 'couleur': 'C'},
                          {'valeur': 'A', 'couleur': 'T'}, {'valeur': '7', 'couleur': 'P'},
                          {'valeur': 'V', 'couleur': 'T'}, {'valeur': '7', 'couleur': 'K'},
                          {'valeur': 'D', 'couleur': 'C'}, {'valeur': 'A', 'couleur': 'K'},
                          {'valeur': 'D', 'couleur': 'P'}, {'valeur': '10', 'couleur': 'T'},
                          {'valeur': 'R', 'couleur': 'K'}, {'valeur': 'R', 'couleur': 'P'}],
                         "Le texte avec les cartes devrait toujours être le même "
                         "pour 32 carte ")

    def test_init_pioche_fichier_2(self):
        self.assertEqual(init.init_pioche_fichier(),
                         [{'valeur': 'V', 'couleur': 'C'}, {'valeur': '8', 'couleur': 'P'},
                          {'valeur': 'V', 'couleur': 'K'},
                          {'valeur': 'A', 'couleur': 'C'}, {'valeur': '10', 'couleur': 'P'},
                          {'valeur': '8', 'couleur': 'T'}, {'valeur': '8', 'couleur': 'K'},
                          {'valeur': '9', 'couleur': 'T'}, {'valeur': 'V', 'couleur': 'P'},
                          {'valeur': 'A', 'couleur': 'P'}, {'valeur': '10', 'couleur': 'K'},
                          {'valeur': '9', 'couleur': 'P'}, {'valeur': '7', 'couleur': 'T'},
                          {'valeur': 'R', 'couleur': 'T'}, {'valeur': '10', 'couleur': 'C'},
                          {'valeur': '9', 'couleur': 'K'}, {'valeur': '9', 'couleur': 'C'},
                          {'valeur': 'D', 'couleur': 'T'}, {'valeur': 'R', 'couleur': 'C'},
                          {'valeur': '8', 'couleur': 'C'}, {'valeur': 'D', 'couleur': 'K'},
                          {'valeur': '7', 'couleur': 'C'}, {'valeur': 'A', 'couleur': 'T'},
                          {'valeur': '7', 'couleur': 'P'}, {'valeur': 'V', 'couleur': 'T'},
                          {'valeur': '7', 'couleur': 'K'}, {'valeur': 'D', 'couleur': 'C'},
                          {'valeur': 'A', 'couleur': 'K'}, {'valeur': 'D', 'couleur': 'P'},
                          {'valeur': '10', 'couleur': 'T'}, {'valeur': 'R', 'couleur': 'K'},
                          {'valeur': 'R', 'couleur': 'P'}, {'valeur': '2', 'couleur': 'C'},
                          {'valeur': '2', 'couleur': 'K'}, {'valeur': '2', 'couleur': 'P'},
                          {'valeur': '2', 'couleur': 'T'}, {'valeur': '3', 'couleur': 'C'},
                          {'valeur': '3', 'couleur': 'P'}, {'valeur': '3', 'couleur': 'K'},
                          {'valeur': '3', 'couleur': 'T'}, {'valeur': '4', 'couleur': 'C'},
                          {'valeur': '4', 'couleur': 'K'}, {'valeur': '4', 'couleur': 'P'},
                          {'valeur': '4', 'couleur': 'T'}, {'valeur': '5', 'couleur': 'C'},
                          {'valeur': '5', 'couleur': 'K'}, {'valeur': '5', 'couleur': 'T'},
                          {'valeur': '5', 'couleur': 'P'}, {'valeur': '6', 'couleur': 'K'},
                          {'valeur': '6', 'couleur': 'T'}, {'valeur': '6', 'couleur': 'C'},
                          {'valeur': '6', 'couleur': 'P'}], "Le texte avec les cartes devrait toujours être le même "
                                                            "pour 52 carte "
                         )

    def test_init_pioche_alea_2(self):
        for carte in init.init_pioche_alea(32):
            assert carte in [{'valeur': 'V', 'couleur': 'C'}, {'valeur': '8', 'couleur': 'P'},
                             {'valeur': 'V', 'couleur': 'K'}, {'valeur': 'A', 'couleur': 'C'},
                             {'valeur': '10', 'couleur': 'P'}, {'valeur': '8', 'couleur': 'T'},
                             {'valeur': '8', 'couleur': 'K'}, {'valeur': '9', 'couleur': 'T'},
                             {'valeur': 'V', 'couleur': 'P'}, {'valeur': 'A', 'couleur': 'P'},
                             {'valeur': '10', 'couleur': 'K'}, {'valeur': '9', 'couleur': 'P'},
                             {'valeur': '7', 'couleur': 'T'}, {'valeur': 'R', 'couleur': 'T'},
                             {'valeur': '10', 'couleur': 'C'}, {'valeur': '9', 'couleur': 'K'},
                             {'valeur': '9', 'couleur': 'C'}, {'valeur': 'D', 'couleur': 'T'},
                             {'valeur': 'R', 'couleur': 'C'}, {'valeur': '8', 'couleur': 'C'},
                             {'valeur': 'D', 'couleur': 'K'}, {'valeur': '7', 'couleur': 'C'},
                             {'valeur': 'A', 'couleur': 'T'}, {'valeur': '7', 'couleur': 'P'},
                             {'valeur': 'V', 'couleur': 'T'}, {'valeur': '7', 'couleur': 'K'},
                             {'valeur': 'D', 'couleur': 'C'}, {'valeur': 'A', 'couleur': 'K'},
                             {'valeur': 'D', 'couleur': 'P'}, {'valeur': '10', 'couleur': 'T'},
                             {'valeur': 'R', 'couleur': 'K'},
                             {'valeur': 'R', 'couleur': 'P'}], "Une carte ne se trouve pas dans la liste"

    def test_init_pioche_alea_1(self):
        for carte in init.init_pioche_alea(52):
            assert carte in [{'valeur': 'V', 'couleur': 'C'}, {'valeur': '8', 'couleur': 'P'},
                             {'valeur': 'V', 'couleur': 'K'}, {'valeur': 'A', 'couleur': 'C'},
                             {'valeur': '10', 'couleur': 'P'},
                             {'valeur': '8', 'couleur': 'T'}, {'valeur': '8', 'couleur': 'K'},
                             {'valeur': '9', 'couleur': 'T'}, {'valeur': 'V', 'couleur': 'P'},
                             {'valeur': 'A', 'couleur': 'P'}, {'valeur': '10', 'couleur': 'K'},
                             {'valeur': '9', 'couleur': 'P'}, {'valeur': '7', 'couleur': 'T'},
                             {'valeur': 'R', 'couleur': 'T'}, {'valeur': '10', 'couleur': 'C'},
                             {'valeur': '9', 'couleur': 'K'}, {'valeur': '9', 'couleur': 'C'},
                             {'valeur': 'D', 'couleur': 'T'}, {'valeur': 'R', 'couleur': 'C'},
                             {'valeur': '8', 'couleur': 'C'}, {'valeur': 'D', 'couleur': 'K'},
                             {'valeur': '7', 'couleur': 'C'}, {'valeur': 'A', 'couleur': 'T'},
                             {'valeur': '7', 'couleur': 'P'}, {'valeur': 'V', 'couleur': 'T'},
                             {'valeur': '7', 'couleur': 'K'}, {'valeur': 'D', 'couleur': 'C'},
                             {'valeur': 'A', 'couleur': 'K'}, {'valeur': 'D', 'couleur': 'P'},
                             {'valeur': '10', 'couleur': 'T'}, {'valeur': 'R', 'couleur': 'K'},
                             {'valeur': 'R', 'couleur': 'P'}, {'valeur': '2', 'couleur': 'C'},
                             {'valeur': '2', 'couleur': 'K'}, {'valeur': '2', 'couleur': 'P'},
                             {'valeur': '2', 'couleur': 'T'}, {'valeur': '3', 'couleur': 'C'},
                             {'valeur': '3', 'couleur': 'P'}, {'valeur': '3', 'couleur': 'K'},
                             {'valeur': '3', 'couleur': 'T'}, {'valeur': '4', 'couleur': 'C'},
                             {'valeur': '4', 'couleur': 'K'}, {'valeur': '4', 'couleur': 'P'},
                             {'valeur': '4', 'couleur': 'T'}, {'valeur': '5', 'couleur': 'C'},
                             {'valeur': '5', 'couleur': 'K'}, {'valeur': '5', 'couleur': 'T'},
                             {'valeur': '5', 'couleur': 'P'}, {'valeur': '6', 'couleur': 'K'},
                             {'valeur': '6', 'couleur': 'T'}, {'valeur': '6', 'couleur': 'C'},
                             {'valeur': '6', 'couleur': 'P'}], "Une carte ne se trouve pas dans la liste"
