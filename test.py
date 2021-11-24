#Main Program
def main():
    pets_data = import_pets_data()

    communities_data = import_communities_data()

    vets_data = import_vets_data()

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