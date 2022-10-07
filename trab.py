import random


animalList = []


def createAnimal(peso,genero,especie,var): 
    animalObj = {}

    if var != -1:
        id = random.randint(1,100)
        for i in range(0,len(animalList)):
            if id != animalList[i]['id']:
            
                animalObj['id']      = id
                animalObj['peso']    = peso
                animalObj['genero']  = genero
                animalObj['especie'] = especie

                animalList.append(animalObj)
            else:
                createAnimal(peso,genero,especie,var)
    else:   
        animalObj['id']      = random.randint(1,100)
        animalObj['peso']    = peso
        animalObj['genero']  = genero
        animalObj['especie'] = especie

        animalList.append(animalObj) 
    
    print('\n\nAnimal cadastrado!')
    print('ID: {}  Peso: {} Genero: {}  Especie: {}'.format(animalObj['id'],animalObj['peso'],animalObj['genero'], animalObj['especie']))



def updateAnimal(id,newPeso): 
    for i in range(0,len(animalList)):

        if(animalList[i]['id'] == id):
            difPeso = animalList[i]['peso'] + newPeso

            if difPeso < animalList[i]['peso']:
                print('\n\n\nO animal perdeu {} kg\n\n\n'.format(newPeso))
    
            elif difPeso >animalList[i]['peso']:
                print('\n\n\nO animal ganhou {} kg\n\n\n'.format(newPeso))

            elif difPeso == animalList[i]['peso']:
                print('\n\n\nO animal nao ganhou peso\n\n\n')

            animalList[i]['peso'] = difPeso;
            print('ID: {}  Peso: {} Genero: {}  Especie: {}'.format(animalList[i]['id'],animalList[i]['peso'],animalList[i]['genero'], animalList[i]['especie']))

    


        
def NumberAnimals():
    if  len(animalList) == 0:
        return -1
    else:
        return len(animalList)

def InsertAnimal(var):
        
    peso    = float(input('Digite o peso do animal:'))
    genero  = input('Digite o genero do animal:')
    especie = input('Digite a especie do animal:')
    
    createAnimal(peso,genero,especie,var)

def searchAnimal(id):
    for i in range(0, len(animalList)):
        if id == animalList[i]['id']:
            return animalList[i]

    return -1

# server prog -----------------------------------------
def Menu():
    print('\nDigite sua opcao')
    print(' 1 -- Informar o numero de Animais')
    print(' 2 -- Cadastar Animal')
    print(' 3 -- Pesquisar Animal')
    print(' 4 -- Atualizar Peso do Animal')
    print(' 5 -- Listar todos os animais')
    print(' 0 -- Sair do Programa')
    
    ops = int(input('Opcao:'))
    
    if ops == 1:
        var = NumberAnimals()
        if var ==-1:
            print('Nao ha animais cadastrados!')
        else:
            print('Existem {} animais cadastrados'.format(var))
    
    elif ops == 2:
        var = NumberAnimals()
        InsertAnimal(var)
    
    elif ops == 3:

        id = int(input('\n\n\nDigite o id do animal:'))
        var = NumberAnimals()
        if var != -1:
            animalobj = searchAnimal(id)
            if animalobj !=-1:
                print('\n\n\nPeso: {} \n Genero: {} \n Especie: {}\n\n\n'.format(animalobj['peso'],animalobj['genero'], animalobj['especie']))
        
            else:
                print('\n\n\nO id esta incorreto\n\n\n')
        else:
            print('\n\n\nNao ha animais cadastrados\n\n\n')

        
            
    elif ops ==4:
        id   = int(input('\n\n\nDigite o id do animal:'))
        peso = float(input('\n\n\nDigite o peso do animal:'))
        var = NumberAnimals()
        if var !=-1:
            animalobj = searchAnimal(id)
            if animalobj !=-1:
                updateAnimal(id,peso)
                print('Peso do animal alterado com sucesso!')
            else:
                print('\n\nO id esta incorreto\n\n')
                  
        else:
            print('\n\n\nNao existe animais cadastrados!\n\n\n')        
    
    elif ops == 5:
        var = NumberAnimals()
        if var !=-1:
            print('\n\nAnimais cadastrados!')
            for i in range(0,len(animalList)):
                print('ID: {}  Peso: {} Genero: {}  Especie: {}'.format(animalList[i]['id'],animalList[i]['peso'],animalList[i]['genero'], animalList[i]['especie']))
        else: 
            print('\n\n\nNao existe animais cadastrados!\n\n\n')        

                    
    elif ops == 0: 
        return 0;

    else:
        print('Opcao invalida!')
    
    return Menu()


Menu()