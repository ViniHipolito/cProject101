import random

num = random.randint(1, 7)

continueGame = 0

print("Jogos dos dados")
print("Tire um 6 para ganhar um cheque de 100 mil mangas!!")

class rollDice:
        if num == 1:
            print('[-----]')
            print('[     ]')
            print('[  0  ]')
            print('[     ]')
            print('[-----]')
        elif num == 2:
            print('[-----]')
            print('[    0]')
            print('[     ]')
            print('[0    ]')
            print('[-----]')
        elif num == 3:
            print('[-----]')
            print('[0    ]')
            print('[  0  ]')
            print('[    0]')
            print('[-----]')
        elif num == 4:
            print('[-----]')
            print('[0   0]')
            print('[     ]')
            print('[0   0]')
            print('[-----]')
        elif num == 5:
            print('[-----]')
            print('[0   0]')
            print('[  0  ]')
            print('[0   0]')
            print('[-----]')
        elif num == 6:
            print('[-----]')
            print('[0   0]')
            print('[0   0]')
            print('[0   0]')
            print('[-----]')
            print('Você ganhou o cheque de 100 mil mangas! Para saber mais como que pegar esse cheque, veja esse video: https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        elif num == 7:
            print('[-----]')
            print('[0 0 0]')
            print('[0   0]')
            print('[0   0]')
            print('[-----]')
            print('Se você ja viu o segredo que coloquei, parabéns! De: Vini')

continueGame = input("Eu adoraria fazer um sistema de Continuar ou Sair, porém estou com falta de tempo então coloca no termina denovo 'python jogue-o-dado.py' beleza? ")

if continueGame == 'Beleza':
     print('Obrigado')
elif continueGame == 'Blz':
     print('Obg')
elif continueGame == 'Ok':
     print('Valeu ai')
