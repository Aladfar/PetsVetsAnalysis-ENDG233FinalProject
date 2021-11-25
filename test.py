import numpy as np
import matplotlib.pyplot as plt

class Neighborhood:
    def __init__(self, name, population, pets_per_capita, vets):
        self.name = name
        self.population = population
        self.pets_per_capita = pets_per_capita
        self.vets = vets

#Main Program
def main():
    pets_data = np.genfromtxt('pets_data.csv',  dtype=('U100','U100','U100','U100',int), delimiter=',', skip_header = True)

    communities_data = np.genfromtxt('communities_data.csv',  dtype=['U100',int,int,int,int,int], delimiter=',', skip_header = True)

    vets_data = np.genfromtxt('vets_data.csv',  dtype=('U100','U100',int), delimiter=',', skip_header = True)

    # print(pets_data)
    print(communities_data)
    # print(vets_data)

    initial_pet_calculations = run_initial_pet_calculations(pets_data, communities_data, vets_data)
    
    print('Welcome to a program examining the pet and veterinarian distributions across Calgary\n')
    
    main_menu(pets_data, communities_data, vets_data,initial_pet_calculations)
    return

#Imports
def import_pets_data():
    pass

def import_communities_data():
    pass

def import_vets_data():
    pass

#Start of Program Calculations
def run_initial_pet_calculations(pets_data, communities_data, vets_data):
    '''Runs initial calculations
    
    returns
        Dictionary pairing communities with the most recent pet registration numbers (for pets per capita, figure 1, )
        Dictionary pairing communities with pets per capita (for figure 2 and generating statistics)
        Array listing each quadrants communities 
        List containing Calgary, quadrants then communities (for graphing and checking if valid usere input)
    '''
    #TODO get a list of communities
    # community_list = ['Calgary', 'NE', 'NW', 'SW', 'SE']
    community_list, NE_communities, NW_communities, SW_communities, SE_communities = [], [], [], [], []
    for x in communities_data:
        community_list.append(x[0])
        if x[5] == 1:
            NE_communities.append(x[0])
        elif x[5] == 2:
            NW_communities.append(x[0])
        elif x[5] == 3:
            SW_communities.append(x[0])
        elif x[5] == 4:
            SE_communities.append(x[0])

    # print(community_list)
    # print(NE_communities)
    # print(NW_communities)
    # print(SW_communities)
    # print(SE_communities)
    
    # quadrant_array = np.ndarray((4,), [NE_communities, NW_communities, SW_communities, SE_communities], dtype=str) #DOESNT WORK YET
    # print(quadrant_array)


   
    pets_per_capita = {}
    pass

#Main menu
def main_menu(pets_data, communities_data, vets_data,initial_pet_calculations):
    print_main_menu()
    while True:
        user_input = input()
        if user_input == 'Pets':
            pets_menu(pets_data, communities_data, vets_data,initial_pet_calculations)
            print_main_menu()
        elif user_input == 'Vets':
            vets_menu(pets_data, communities_data, vets_data,initial_pet_calculations)
            print_main_menu()
        elif user_input == 'End':
            exit()
        else:
            print('That was an invalid entry. Please try again using one of the above options')
    return

def print_main_menu():
    print('This is the main menu. Please select one of the following options:\n')
    print('{selection_option:>4} : {reason}'.format(selection_option = 'Pets', reason = 'To learn more about the pet distribution in Calgary'))
    print('{selection_option:>4} : {reason}'.format(selection_option = 'Vets', reason = 'To learn more about the veterinarian distribution in Calgary'))
    print('{selection_option:>4} : {reason}'.format(selection_option = 'End', reason = 'To end the program'))
    return

#Pets menu
def pets_menu(pets_data, communities_data, vets_data,initial_pet_calculations):
    print()
    print_pets_menu()
    while True:
        user_input = input()
        if user_input == 'Income':
            graph_income_vs_pets_by_capita(pets_data, communities_data, vets_data,initial_pet_calculations)
            print_pets_menu()
        elif user_input == 'Registration': 
            graph_time_vs_new_registration(pets_data, communities_data, vets_data,initial_pet_calculations)
            print_pets_menu()
        elif user_input == 'Total Pets':
            area_most_least_pets(pets_data, communities_data, vets_data,initial_pet_calculations)
            print_pets_menu()
        elif user_input == 'Pets Per Capita':
            area_most_least_pets_capita(pets_data, communities_data, vets_data,initial_pet_calculations)
            print_pets_menu()
        elif user_input == 'Return':
            print()
            return
        elif user_input == 'End':
            exit()
        else:
            print('That was an invalid entry. Please try again using one of the above options')
    

def print_pets_menu():
    print('This is the pet statistics menu. Please select one of the following options:\n')
    print('{selection_option:>15} : {reason}'.format(selection_option = 'Income', reason = 'To see a graph comparing income by community compared to pet ownership'))
    print('{selection_option:>15} : {reason}'.format(selection_option = 'Registration', reason = 'To see a graph comparing the change in pets for the last three years'))        
    print('{selection_option:>15} : {reason}'.format(selection_option = 'Total Pets', reason = 'To learn more about the areas in Calgary with the most or least pets'))
    print('{selection_option:>15} : {reason}'.format(selection_option = 'Pets Per Capita', reason = 'To learn more about the areas in Calgary with the most or least pets per capita'))
    print('{selection_option:>15} : {reason}'.format(selection_option = 'Return', reason = 'To return to the main menu'))        
    print('{selection_option:>15} : {reason}'.format(selection_option = 'End', reason = 'To end the program'))
    return

#Pets related functions
def graph_income_vs_pets_by_capita(pets_data, communities_data, vets_data,initial_pet_calculations):
    pass

def graph_time_vs_new_registration(pets_data, communities_data, vets_data,initial_pet_calculations):
    pass

def area_most_least_pets(pets_data, communities_data, vets_data,initial_pet_calculations):
    pass

def area_most_least_pets_capita(pets_data, communities_data, vets_data,initial_pet_calculations):
    pass

#Vets menu
def vets_menu(pets_data, communities_data, vets_data,initial_pet_calculations):
    print()
    print_vets_menu()
    while True:
        user_input = input()
        if user_input == 'Pets Per Vet':
            graph_community_vs_income_and_pets_per_vet(pets_data, communities_data, vets_data,initial_pet_calculations)
            print_pets_menu()
        elif user_input == 'Vets In Area': 
            vets_in_area(pets_data, communities_data, vets_data,initial_pet_calculations)
            print_pets_menu()
        elif user_input == 'Return':
            print()
            return
        elif user_input == 'End':
            exit()
        else:
            print('That was an invalid entry. Please try again using one of the above options')
    

def print_vets_menu():
    print('This is the veterinarian statistics menu. Please select one of the following options:\n')
    print('{selection_option:>12} : {reason}'.format(selection_option = 'Pets Per Vet', reason = 'To see a graph comparing the number of pets per veterinarian for different areas in Calgary'))
    print('{selection_option:>12} : {reason}'.format(selection_option = 'Vets In Area', reason = 'To learn more about the veterinarian services offered for different areas of Calgary'))        
    print('{selection_option:>12} : {reason}'.format(selection_option = 'Return', reason = 'To return to the main menu'))        
    print('{selection_option:>12} : {reason}'.format(selection_option = 'End', reason = 'To end the program'))
    return

#Pets related functions
def graph_community_vs_income_and_pets_per_vet(pets_data, communities_data, vets_data,initial_pet_calculations):
    pass

def vets_in_area(pets_data, communities_data, vets_data,initial_pet_calculations):
    pass

if __name__ == '__main__':
    main()