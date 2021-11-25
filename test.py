import numpy as np
import matplotlib.pyplot as plt

#Main Program
def main():
    pets_data = np.genfromtxt('pets_data.csv',  dtype=('U100','U100','U100','U100',int), delimiter=',', skip_header = True)

    communities_data = np.genfromtxt('communities_data.csv',  dtype=('U100',int,int,int,int,int), delimiter=',', skip_header = True)

    vets_data = np.genfromtxt('vets_data.csv',  dtype=('U100','U100',int), delimiter=',', skip_header = True)

    print(pets_data)
    print(communities_data)
    print(vets_data)

    initial_pet_calculations = run_initial_pet_calculations(pets_data, communities_data, vets_data)

    main_menu(pets_data, communities_data, vets_data,initial_pet_calculations)

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
    pass

#Main menu
def main_menu(pets_data, communities_data, vets_data,initial_pet_calculations):
    user_input = get_and_check_main_menu_input()

    if user_input == 3:#placeholder
        pets_menu(pets_data, communities_data, vets_data,initial_pet_calculations)
    elif user_input == 4:#placeholder 
        vets_menu(pets_data, communities_data, vets_data,initial_pet_calculations)
    else:
        exit()
    pass

def get_and_check_main_menu_input():
    pass

#Pets menu
def pets_menu(pets_data, communities_data, vets_data,initial_pet_calculations):
    user_input = get_and_check_pets_menu_input()

    if user_input == 3:#placeholder
        graph_income_vs_pets_by_capita(pets_data, communities_data, vets_data,initial_pet_calculations)
    elif user_input == 4:#placeholder 
        graph_time_vs_new_registration(pets_data, communities_data, vets_data,initial_pet_calculations)
    elif user_input == 4:#placeholder 
        area_most_least_pets(pets_data, communities_data, vets_data,initial_pet_calculations)
    elif user_input == 4:#placeholder 
        area_most_least_pets_capita(pets_data, communities_data, vets_data,initial_pet_calculations)
    elif user_input == 5:#pleacholder
        return
    else:
        exit()
    pass

def get_and_check_pets_menu_input():
    pass

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
    user_input = get_and_check_vets_menu_input()

    if user_input == 3:#placeholder
        graph_community_vs_income_and_pets_per_vet(pets_data, communities_data, vets_data,initial_pet_calculations)
    elif user_input == 4:#placeholder 
        vets_in_area(pets_data, communities_data, vets_data,initial_pet_calculations)
    elif user_input == 5:#pleacholder
        return
    else:
        exit()
    pass

def get_and_check_vets_menu_input():
    pass

#Pets related functions
def graph_community_vs_income_and_pets_per_vet(pets_data, communities_data, vets_data,initial_pet_calculations):
    pass

def vets_in_area(pets_data, communities_data, vets_data,initial_pet_calculations):
    pass

if __name__ == '__main__':
    main()