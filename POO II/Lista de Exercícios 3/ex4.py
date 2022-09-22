'''Uma pista de Kart permite 10 voltas para cada um de 6 corredores.
Escreva um programa que leia todos os tempos em segundos e os guarde em um
dicionário, onde a chave é o nome do corredor. Ao final diga de quem foi a melhor volta
da prova e em que volta; e ainda a classificação final em ordem (1o o campeão). O
campeão é o que tem a menor média de tempos.'''

num_of_racers = 6 # It is supposed to be 6
num_of_laps = 10 # It is supposed to be 10
race_dict = {}

for i in range(num_of_racers):
    racer_name = input("Insert racer name: ")
    race_dict.setdefault(racer_name)
    lap_times_ls = [None]*num_of_laps

    for j in range(num_of_laps):

        lap_mark = float(input(f'Lap {j} time mark: '))

        while lap_mark <= 0:
            print("Insert a value higher than 0!")
            lap_mark = float(input(f'Lap {j} time mark: '))

        lap_times_ls[j] = lap_mark # If the time is higher than 0, it is safely set.
    
    race_dict.update({racer_name: lap_times_ls})


def get_best_lap(race_dict):
    lowest_time = 10**20
    fastest_racer = None
    fastest_lap = None

    for racer in race_dict:
        if min(race_dict[racer]) < lowest_time:
            lowest_time = min(race_dict[racer])
            fastest_racer = racer
            fastest_lap = race_dict[racer].index(lowest_time)

    print(f'The fastest lap was made in {lowest_time} seconds, on lap number {fastest_lap+1}, by {fastest_racer}!')


def get_champ(race_dict):
    classification = []
    for racer in race_dict:
        classification.append( (( sum(race_dict[racer])/len(race_dict[racer]) ), racer) )
    
    classification.sort()

    pos = 1
    print("The classification for this race is: ")
    for position in classification:
        print(f'{position[1]}, with an average time of {position[0]} seconds, got place number {pos}.')
        pos += 1

get_best_lap(race_dict)
get_champ(race_dict)