import json
import datetime
from utils.pyorn.yorn import question

#subtrair dois datetimes usando datetime delta
num = [1,2,3]

class MyPet:

    def __init__(self):
        with open('pets.txt') as f:
            """ pets = f.readlines()
            pets = [p[0:-1] for p in pets] #remover \n
            all_pets = [p.split("//") for p in pets] #criar um array com todos os pets criados
            print(all_pets) """
            # print("Os pets cadastrados atualmente são:\n",'\n'.join(map(str,all_pets)))
        #print(datetime.datetime.today())

        """ while True:
            my_pet = input("Digite o nome do seu pet (digite exit para sair) -> ")
            if my_pet == "exit":
                print("Até breve!")
                exit()
            if my_pet in all_pets:
                if question(f"Deseja visitar {my_pet}?"):
                    self.my_pet = my_pet
                else:
                    continue
            else:
                if question(f"Deseja adotar um pet com o nome {my_pet}?"):
                    pass
                else:
                    continue """
    
    def _load_my_pet(self,pet_name):
        pass

MyPet()