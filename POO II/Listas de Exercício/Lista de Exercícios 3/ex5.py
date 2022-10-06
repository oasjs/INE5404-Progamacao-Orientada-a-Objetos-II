'''Escreva um programa para armazenar uma agenda de telefones usando
um dicionário. Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o
nome completo da pessoa. Seu programa deve ter as seguintes funções:

incluir_novo_nome – essa função acrescenta um novo nome na agenda, com
um ou mais telefones. Ela deve receber como argumentos o nome e os telefones.

incluir_telefone – essa função acrescenta um telefone em um nome existente na
agenda. Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja
incluí-​lo. Caso a resposta seja afirmativa, use a função anterior para incluir o novo
nome.

excluir_telefone – essa função exclui um telefone de uma pessoa que
já está na agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da
agenda.

excluir_nome – essa função exclui uma pessoa da agenda.

consultar_telefone – essa função retorna os telefones de uma pessoa
na agenda.'''

contact_list = {

}

def get_contact_list():
    print(contact_list)

# refers to function "incluir_novo_nome"
def insert_contact(): 
    name = input("Please, insert the contact name: ")
    numbers = input("Please, insert their contact numbers: ").split()
    contact_list.update({name: numbers})
    print(f'The number(s) {numbers} were registered for {name}.')

# refers to fuction "incluir_telefone"
def insert_number():
    get_contact_list()
    name = input("Whom do you wish to add a phone number to? ")
    if name in contact_list:
        number = input("Insert a phone number: ")
        contact_list[name].append(number)
        print(f'Number {number} was successfully added to the contact {name}')
    else:
        print(f'{name} is not on the list. If you wish to add them, insert 1. Otherwise, insert 0.')
        check = int(input())
        if check:
            insert_contact({name: number})
        else:
            print("Operation canceled.")

# refers to function "excluir_nome"
def delete_contact():
    get_contact_list()
    name = input("Please, input them name of the contact you want to delete: ")
    try:
        contact_list.pop(name)
        print(f'{name} was removed from your contact list.')
    except KeyError:
        print("This name is not on the list. Please, insert a name present on the list.")
        delete_contact() 

# refers to function "excluir_telefone"
def delete_number():
    get_contact_list()
    name = input("Please, input the name of the contact you want to access: ")
    while name not in contact_list:
        print(f'{name} not on the list. Please, insert a valid name.')
        name = input("Please, input them name of the contact you want to access: ")

    print(f'{name} selected')
    print(f'{name} has the following contact numbers registered:')
    for i in range(len(contact_list[name])):
        print(f'{i+1}: {contact_list[name][i]}.')

    number = int(input("Please, insert the numeric index of the contact number you want to delete: ")) 
    while True:    
        index = number-1
        if index < len(contact_list[name]):
            contact_list[name].pop(index)
            print(f'Number successfully removed.')
        else:
            print("This is an invalid index!")
            number = int(input("Please, insert a valid index: ")) 

        print("Delete number operation finished.")
        break

    if contact_list[name] == []:
        contact_list.pop(name)
        print(f'The contact {name} had no registered numbers, and thus was deleted.')

# refers to function "consultar_telefone"
def get_numbers():
    get_contact_list()
    name = input("Please, input the name of the contact you want to access: ")
    while True:    
        try:
            print(f'The contact {name} has the following numbers: {contact_list[name]}')
            print(f'Number successfully removed.')
        except KeyError:
            print("There is no contact registered as {name} in your contact list.")
            name = input("Please, input a valid name: ")
        finally:
            print("Get contact number operation finished.")
            break