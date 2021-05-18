import random
import dico
from players import Player


class Game(Player) : #GAME
    def __init__(self, character):
        Player.__init__(self, character)
        self.list_Sujet = list(dico.SujetPoints.keys())
        self.list_Verbe = list(dico.VerbePoints.keys())
        self.list_Complement = list(dico.ComplementPoints.keys())
        self.list_Conjonction = list(dico.ConjonctionPoints.keys())
        self.list_Bonus = list(dico.BonusPoints.keys())
        self.list_MotSpe = list(dico.MotSpesPoints.keys())

        self.choices_per_turn = [
            self.list_Sujet,
            self.list_Verbe,
            self.list_Complement,
            self.list_Conjonction,
            self.list_Bonus,
            self.list_MotSpe,
        ]

        self.points_per_turn = [
            dico.SujetPoints,
            dico.VerbePoints,
            dico.ComplementPoints,
            dico.ConjonctionPoints,
            dico.BonusPoints,
            dico.MotSpesPoints,
        ]

        self.players = [
            {'score': 0, 'resultat': ''},
            {'score': 0, 'resultat': ''},
        ]

        '''
        if character == "Jacqouille La Fripouille":
            self.name = "Jacqouille La Fripouille"
            self.Pv = 100
            self.list_MotSpe = 

        if character == "Perso 2":
            self.name = "Perso 2"
            self.Pv = 100
            self.list_MotSpe = 
        '''
#fonction choix des mots

    def choice(self, list, player_nb, condition):
        conditions = [
            "Joueur {} veuillez choisir un sujet en tapant le chiffre de celui-ci:".format(player_nb),
            "Joueur {}, Veuillez choisir un verbe:".format(player_nb),
            "Joueur {}, Veuillez choisir un complément:".format(player_nb),
            "Joueur {}, Veuillez choisir une conjonction:".format(player_nb),
            "Joueur {}, Veuillez choisir un bonus:".format(player_nb),
            "Joueur {}, Veuillez choisir un mot spécial:".format(player_nb)
        ]
        print(conditions[condition])

        j = 1
        while j<6 :
            print(j, " ", list[j-1])
            j += 1
        choix = int(input())

#message erreur si choix non valide.
        if choix >=1 and choix <=5 :
            return list[choix - 1]
        else :
            print ("RESPECTE MON AUTORITEEEEEEE")
        return self.choice(list,condition)
            

    def Start(self): #START
        round = 0
        while round <6:
            turn = 0
            while turn <= 5 :
                player = 0
                while player <= 1:
                    choice_score = self.Turn(player, turn)
                    player += 1
                turn += 1

            i = 0
            while i < self.players.__len__():
                print("Joueur {}, score: {}\nPhrase: {}\n".format(i + 1, self.players[i]['score'], self.players[i]['resultat']))
                i += 1
            round += 1
            print("Continuer la partie ? (oui) (non)")
            choix = input()
            if choix == "non":
                round = 6
        Winner = "Joueur1"
        if self.players[0]['score'] < self.players[1]['score']:
            Winner = "Joueur2"
        print(Winner+' à gagné')            



    def Turn(self, player_nb, turn):
        if turn >= 1:
            print("\nJoueur {} choix précédent: {}".format(player_nb + 1, self.players[player_nb]['resultat']))
        choices = self.choices_per_turn[turn]
        dico_points = self.points_per_turn[turn]
        random.shuffle(choices)
        choice = (self.choice(choices, player_nb + 1, turn))
        score = dico_points[choice]

        self.players[player_nb]['resultat'] = "{} {}".format(self.players[player_nb]['resultat'], choice)
        self.players[player_nb]['score'] += score
    
    