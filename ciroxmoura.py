from zodiac import *
from phantom_team import *

nome = "Ciro"
resposta = int(print("Ciro, o que você deseja ser? (1) Humano (2) Hunter (3) Genei Ryodan (4) Zodiaco: "))
data = input("Digite sua data de nascimento: ")

if resposta == 1:
    ciro = Human(nome, data)
    
elif resposta == 2:
    ciro = Hunter(input('em que data você fez o exame? '), nome, data)
    
elif resposta == 3:
    ciro = PhantomTeamMember(input("Quando você virou um membro? "), input("Qual sua categoria? "),nome, data)
    if input("Você quer ser o lider? (SIM, NÃO) ").upper() == "SIM":
        ciro._become_leader()
    if input("Você quer roubar? (SIM/NÃO) ").upper() == "NÃO":
        ciro.stealing()
    else:
        print("Muito bem...")

