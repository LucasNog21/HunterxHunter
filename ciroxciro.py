from zodiac import *
from phantom_team import *

nome = "Ciro"
resposta = int(input("Ciro, o que você deseja ser? (1) Humano (2) Hunter (3) Genei Ryodan "))
data = input("Digite sua data de nascimento: ")

if resposta == 1:
    ciro = Human(nome, data)
    
elif resposta == 2:
    ciro = Hunter(input('em que data você fez o exame? '), nome, data)
    if input("Deseja atuar como hunter? (SIM/NÃO)").upper() == "SIM":
        ciro.hunting()
    if input("Deseja vender seu cartão hunter? (SIM/NÃO)").upper() == "SIM":
        ciro.sell_tiket()
    
elif resposta == 3:
    ciro = PhantomTeamMember(input("Quando você virou um membro? "), input("Qual sua categoria? "),nome, data)
    if input("Você quer ser o lider? (SIM, NÃO) ").upper() == "SIM":
        ciro._become_leader()
    if input("Você quer roubar? (SIM/NÃO) ").upper() == "SIM":
        ciro.stealing()
    else:
        print("Muito bem...")
    
print("hora de definir sua habilidade!")
treino = bool(input("Ciro, você deseja passar por um batismo de nen (0), ou treinar até despertar(1)?"))
if treino:
    while not ciro.is_awake():
        ciro._nen_train_awake()
else:
    ciro._nen_baptism()