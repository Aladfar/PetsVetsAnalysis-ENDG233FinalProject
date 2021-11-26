import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import average

class Neighborhood:
    def __init__(self, name, population, pets_per_capita, vets):
        self.name = name
        self.population = population
        self.pets_per_capita = pets_per_capita
        self.vets = vets

#Main Program
def main():
    pets_data = np.genfromtxt('pets_data.csv',  dtype=('U1000','U1000','U1000','U1000',int), delimiter=',', skip_header = True)

    communities_data = np.genfromtxt('communities_data.csv',  dtype=['U1000',int,int,int,int,int], delimiter=',', skip_header = True)

    vets_data = np.genfromtxt('vets_data.csv',  dtype=('U1000','U1000',int), delimiter=',', skip_header = True)

    # print(pets_data)
    print(communities_data)
    # print(vets_data)
    # print(pets_data[1][1])

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
        Dictionary (or maybe array) pairing communities with the most recent pet registration numbers (for pets per capita, figure 1, )
        Dictionary (or maybe array) pairing communities with pets per capita (for figure 2 and generating statistics)
        Array listing each quadrants communities 
        List containing Calgary, quadrants then communities (for graphing and checking if valid usere input)
        Dictionary (or maybe array) pairing communities with their avergae income
    '''
    #TODO    Dictionary (or maybe array) pairing communities with pets per capita (for figure 2 and generating statistics)
    #TODO    Array listing each quadrants communities 
    #TODO    List containing Calgary, quadrants then communities (for graphing and checking if valid usere input)
    #TODO    Dictionary (or maybe array) pairing communities with their avergae income
    #TODO   Pets per vets if a new vet opened (vets in community + 1)
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
    
    pets_registration, combined_pets = [], []
    # print(pets_data)
    for x in pets_data:
        if x[0] == '2021-10-01' and x[2] in community_list:                        #Gets the most recent cats and dogs registration data
            pets_registration.append(x[2])
            pets_registration.append(x[4])
    pets_registration = np.array(pets_registration)                     #Creates a 1D array from the list
    pets_registration = pets_registration.reshape((int(len(pets_registration)/4)), 4)   #Turns the 1D array into a 2D array with 4 columns and (1D Array Length / 4) Rows
    pets_registration = np.delete(pets_registration, 2, 1)              #Deletes the third column (repeat of communtity name)
    for x in pets_registration:
        combined_pets.append(int(x[1]) + int(x[2]))
    pets_registration = np.c_[pets_registration, combined_pets]       #Formatting is community, cats, dogs, combined total
    pets_registration = list(zip(*pets_registration.T))
    dtp = np.dtype([('Name', 'U100'), ('Cats', '>i4'), ('Dogs', '>i4'), ('Total', '>i4')])
    pets_registration = np.array(pets_registration, dtype=dtp)          # Creates a structured array
    print(pets_registration)
    # print(pets_registration['Cats'])

    
    #pets per capita
    print(np.shape(pets_registration))
    cats_per_cap, dogs_per_cap, pets_per_cap = {}, {}, {}
    index = 5
    for row in pets_registration:
        cats_per_cap[row[0]] = row[1] / communities_data[index][3]
        dogs_per_cap[row[0]] = row[2] / communities_data[index][3]
        pets_per_cap[row[0]] = row[3] / communities_data[index][3]
        index += 1

    print(cats_per_cap, dogs_per_cap, pets_per_cap)

    # print(community_list)
    # print(NE_communities)
    # print(NW_communities)
    # print(SW_communities)
    # print(SE_communities)

    # pet_registration
    
    # quadrant_array = np.ndarray((4,), [NE_communities, NW_communities, SW_communities, SE_communities], dtype=str) #DOESNT WORK YET
    # print(quadrant_array) 
    pets_per_capita = {}
    return pets_registration, cats_per_cap, dogs_per_cap, pets_per_cap

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
        elif user_input == 'Area Info':
            pets_info(pets_data, communities_data, vets_data,initial_pet_calculations)
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
    print('{selection_option:>15} : {reason}'.format(selection_option = 'Area Info', reason = 'To see a variety of statistics related to pets within an area of Calgary'))
    print('{selection_option:>15} : {reason}'.format(selection_option = 'Return', reason = 'To return to the main menu'))        
    print('{selection_option:>15} : {reason}'.format(selection_option = 'End', reason = 'To end the program'))
    return

#Pets related functions
def graph_income_vs_pets_by_capita(pets_data, communities_data, vets_data,initial_pet_calculations):
    '''This function takes cats and dogs and income by community and graphs it
    The x-axis is the communities ordered from poorest to richest
    The x-axis is three lines, one for cats, one for dogs, one for cats and dogs

    parameters:
    UNCLEAR

    returns: none

        NOTES: Pretty much completed just needs correct incomes
    '''
    all_communities_income = {'a':9, 'b':4, 'c':5, 'd':6, 'e':7, 'f':8, 'g':8} #Placeholders
    all_communities_cats_dogs = {'a':19, 'b':8, 'c':11, 'd':13, 'e':11, 'f':15, 'g':15} #Placeholders
    all_communities_cats = {'a':10, 'b':2, 'c':6, 'd':9, 'e':8, 'f':13, 'g':7}
    all_communities_dogs = {'a':9, 'b':6, 'c':5, 'd':4, 'e':3, 'f':2, 'g':8}

    #This part pulls the income values, sorts them and then matches the communities back up with the incomes
    all_communities_sorted = {}
    income_sorted = sorted(all_communities_income.values())
    for sorted_income in income_sorted:
        for community, income in all_communities_income.items():
            if income == sorted_income:
                all_communities_sorted[community] = income

    #A list of the communities that has been sorted poorest to richest
    income_x_axis_labels = list(all_communities_sorted.keys())

    #Generates an order of numbers starting at 1 that has the same amount of numbers as then number of communities
    income_x_axis_points = []
    for i in range(len(income_x_axis_labels)):
        income_x_axis_points.append(i+1)

    #Creates the three y-axis data sets
    cats_dogs_y_axis = []
    cats_y_axis = []
    dogs_y_axis = []
    for community_sorted in all_communities_sorted.keys():
        for community,population in all_communities_cats_dogs.items():
            if community_sorted == community:
                cats_dogs_y_axis.append(population)
    for community_sorted in all_communities_sorted.keys():
        for community,population in all_communities_cats.items():
            if community_sorted == community:
                cats_y_axis.append(population)
    for community_sorted in all_communities_sorted.keys():
        for community,population in all_communities_dogs.items():
            if community_sorted == community:
                dogs_y_axis.append(population)

    #Graphs
    FIGURE1 = 1

    plt.figure(FIGURE1)

    #Plots points
    plt.plot(income_x_axis_points, cats_dogs_y_axis, 'bo--', label='Total Cats and Dogs') # Graphs all coordinates
    plt.plot(income_x_axis_points, cats_y_axis, 'go--', label='Total Cats')
    plt.plot(income_x_axis_points, dogs_y_axis, 'ro--', label='Total Dogs')

    #Creates a title and a legends
    plt.title('Pet Ownership Compared to Income')      
    plt.xlabel('Communities (Ordered from lowest average income to highest)')
    plt.ylabel('Number of pets')
    plt.legend(shadow=True)

    #Modifies x-axis labels
    plt.xticks(income_x_axis_points, income_x_axis_labels)
    
    #Displays graph
    plt.show()    

    print('You are now being returned to the pet statistics menu')

    return
    
def graph_time_vs_new_registration(pets_data, communities_data, vets_data,initial_pet_calculations):
    pass

def area_most_least_pets(pets_data, communities_data, vets_data,initial_pet_calculations):
    '''This function allows the user to select cat, dog or both and quadrant of city.
       This then causes the program to print out the three most animal populated communities and three least populated communities
       The user is then given the choice to exit the function or do another selection
    
       parameters:
       Unclear

       returns: 
       
       NOTES
       Need to figure out inputs. Created for dictionary's but can be quickly converted to arrays. 
       Acts very similar to pets by capita. Some use of shared functions will be helpful. For example, the second part of the code is exclusively dependent on 3-4 parameters

    '''
    all_communities_cats_dogs = {'a':3, 'b':4, 'c':5, 'd':6, 'e':7, 'f':8, 'g':8} #Placeholders
    all_communities_cats = {'a':2, 'b':2, 'c':4, 'd':5, 'e':8, 'f':0, 'g':2}
    all_communities_dogs = {'a':4, 'b':6, 'c':7, 'd':8, 'e':3, 'f':4, 'g':2}
    northwest_communities = ['a','b', 'c']
    southwest_communities = ['c','d','e']
    northeast_communities = ['f', 'b', 'a', 'c', 'd', 'e']
    southeast_communities = ['g', 'a', 'f']

    while True:
        #Gathers input to determine animal to look into
        print('\nPlease select whether you would like to learn more about cats, dogs, or total cats and dogs within Calgary')
        print('{selection_option:>13} : {reason}'.format(selection_option = 'Cats', reason = 'To learn more about the most and least cats'))
        print('{selection_option:>13} : {reason}'.format(selection_option = 'Dogs', reason = 'To learn more about the most and least dogs'))
        print('{selection_option:>13} : {reason}'.format(selection_option = 'Cats and Dogs', reason = 'To learn more about the most and least cats and dogs'))
        while True:
            animal = input()
            if animal == 'Cats':
                all_communities_with_selected_pet_type = all_communities_cats
                break
            elif animal == 'Dogs':
                all_communities_with_selected_pet_type = all_communities_dogs
                break
            elif animal == 'Cats and Dogs':
                all_communities_with_selected_pet_type = all_communities_cats_dogs
                break
            else: 
                print('That was an invalid entry. Please try again using one of the above options')
        
        #Gathers input to determine where in Calgary
        print('\nPlease select whether where in Calgary you would like to learn more about this pet')
        print('{selection_option:>7} : {reason}'.format(selection_option = 'Calgary', reason = 'To learn more about the pets in all of Calgary'))
        print('{selection_option:>7} : {reason}'.format(selection_option = 'NE', reason = 'To learn more about the pets in the North-East'))
        print('{selection_option:>7} : {reason}'.format(selection_option = 'NW', reason = 'To learn more about the pets in the North-West'))
        print('{selection_option:>7} : {reason}'.format(selection_option = 'SW', reason = 'To learn more about the pets in the South-West'))
        print('{selection_option:>7} : {reason}'.format(selection_option = 'NE', reason = 'To learn more about the pets in the North-East'))
        while True:
            area = input()
            if area == 'Calgary':
                valid_communities_dict = all_communities_with_selected_pet_type
                break
            elif area == 'NE':
                valid_communities_dict = {}
                for community,pets in all_communities_with_selected_pet_type.items():
                    if community in northeast_communities:
                        valid_communities_dict[community] = pets
                break
            elif area == 'NW':
                valid_communities_dict = {}
                for community,pets in all_communities_with_selected_pet_type.items():
                    if community in northwest_communities:
                        valid_communities_dict[community] = pets
                break
            elif area == 'SW':
                valid_communities_dict = {}
                for community,pets in all_communities_with_selected_pet_type.items():
                    if community in southwest_communities:
                        valid_communities_dict[community] = pets
                break
            elif area == 'SE':
                valid_communities_dict = {}
                for community,pets in all_communities_with_selected_pet_type.items():
                    if community in southeast_communities:
                        valid_communities_dict[community] = pets
                break
            else: 
                print('That was an invalid entry. Please try again using one of the above options')
        
        #Creates array of just the valid animal population sizes based on the above conditions
        num_of_pets_array = np.fromiter(valid_communities_dict.values(), dtype=int)
        
        #Finds top three max's
        print('The 3 communities in the {} with the most {}:'.format(area, animal.lower()))
        number_max_found = 0
        num_of_pets_array_finding_max = np.copy(num_of_pets_array)
        
        while number_max_found < 3:
            index = -1
            num_of_pets_max = np.amax(num_of_pets_array_finding_max)
            for community, max in valid_communities_dict.items():
                index += 1
                if max == num_of_pets_max:
                    number_max_found += 1
                    print('{} with {} {}'.format(community, max, animal))
                    num_of_pets_array_finding_max = np.where(num_of_pets_array_finding_max == max, -1, num_of_pets_array_finding_max)
        
        #Find bottom three min's
        print('\nThe 3 communities in the {} with the least {}:'.format(area, animal.lower()))
        number_min_found = 0
        num_of_pets_array_finding_min = np.copy(num_of_pets_array)
        while number_min_found < 3:
            index = -1
            num_of_pets_min= np.amin(num_of_pets_array_finding_min)
            for community, min in valid_communities_dict.items():
                index += 1
                if min == num_of_pets_min:
                    number_min_found += 1
                    print('{} with {} {}'.format(community, min, animal))
                    num_of_pets_array_finding_min = np.where(num_of_pets_array_finding_min == min, 10000000, num_of_pets_array_finding_min)
        
        #Either ends this section of the code or repeats whole thing
        print('\nPlease type Return to use other parts of the program otherwise hit enter to learn more about the minimum and maximum number of pets for communities in Calgary')
        if input() == 'Return':
            return

def area_most_least_pets_capita(pets_data, communities_data, vets_data,initial_pet_calculations):
    pass

def pets_info (pets_data, communities_data, vets_data,initial_pet_calculations):
    pass

#Vets menu
def vets_menu(pets_data, communities_data, vets_data,initial_pet_calculations):
    print()
    print_vets_menu()
    while True:
        user_input = input()
        if user_input == 'Pets Per Vet':
            graph_community_vs_income_and_pets_per_vet(pets_data, communities_data, vets_data,initial_pet_calculations)
            print_vets_menu()
        elif user_input == 'Vets In Area': 
            vets_in_area(pets_data, communities_data, vets_data,initial_pet_calculations)
            print_vets_menu()
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
    '''This functions takes pet per capita and income data and compares it on the same graph

    parameters:
    UNCLEAR

    returns: none

    NOTES: Communities may be a tight fit
    '''
    all_communities_income = {'a':9, 'b':4, 'c':5, 'd':6, 'e':7, 'f':8, 'g':8} #Placeholders
    all_communities_cats_dogs = {'a':19, 'b':8, 'c':11, 'd':13, 'e':11, 'f':15, 'g':15} #Placeholders

    income_x_axis_labels = list(all_communities_income.keys())
    #Generates an order of numbers starting at 1 that has the same amount of numbers as the number of communities
    income_x_axis_points = []
    for i in range(len(income_x_axis_labels)):
        income_x_axis_points.append(i+1)

    fig, ax1 = plt.subplots()
    #Plots cat, dog points
    ax1.plot(income_x_axis_points, all_communities_cats_dogs.values(), 'bo', label='Total Cats and Dogs') # Graphs all coordinates
    ax1.set_ylabel('Pets per Vetrinarians if a New Vetrinarian Opened in Each Community', color='blue')

    #Plots income points
    ax2 = ax1.twinx()
    ax2.plot(income_x_axis_points, all_communities_income.values(), 'go', label='Total Cats and Dogs') # Graphs all coordinates
    ax2.set_ylabel('Average Income for Each Community', color='green')

    #Creates a title and x-axis lables
    plt.title('Pets per Vetrinarian and Income for Each Community')      
    plt.xlabel('Communities')
    plt.xticks(income_x_axis_points, income_x_axis_labels)

    #Explains graph
    plt.figtext(0.5, 0.01, "This graph is designed to identify the best locations to start a new veterinarian practice.\nThe left y-axis is designed to demonstrate where there would be a large market of pets.\nThe right y-axis demonstrates which communities have more money to pay for veterinarian services", ha="center", fontsize=12)

    #Displays graph
    plt.show()    

    return

def vets_in_area(pets_data, communities_data, vets_data,initial_pet_calculations):
    pass
    

if __name__ == '__main__':
    main()