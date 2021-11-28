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
#Coding Complete, docstring needed

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
    test_list = []
    test_list2 = []
    #pets per capita
    print(np.shape(pets_registration))
    cats_per_cap, dogs_per_cap, pets_per_cap = {}, {}, {}
    index = 5
    for row in pets_registration:
        population = communities_data[index][3]
        cats_per_cap[row[0]] = row[1] / population
        dogs_per_cap[row[0]] = row[2] / population
        pets_per_cap[row[0]] = row[3] / population
        index += 1
        test_list.append(population)
        test_list2.append(row[0])
    print('\n', test_list, '\n')
    print('\n', test_list2, '\n')    

    print(dogs_per_cap)

    # print(community_list)
    # print(NE_communities)
    # print(NW_communities)
    # print(SW_communities)
    # print(SE_communities)

    # pet_registration
    
    # quadrant_array = np.ndarray((4,), [NE_communities, NW_communities, SW_communities, SE_communities], dtype=str) #DOESNT WORK YET
    # print(quadrant_array) 
    pets_per_capita = {}
    return pets_registration, cats_per_cap, dogs_per_cap, pets_per_cap, community_list, NE_communities, NW_communities, SW_communities, SE_communities
#In Progress

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
#Coding Complete, docstring needed

def print_main_menu():
    print('This is the main menu. Please select one of the following options:\n')
    print('{selection_option:>4} : {reason}'.format(selection_option = 'Pets', reason = 'To learn more about the pet distribution in Calgary'))
    print('{selection_option:>4} : {reason}'.format(selection_option = 'Vets', reason = 'To learn more about the veterinarian distribution in Calgary'))
    print('{selection_option:>4} : {reason}'.format(selection_option = 'End', reason = 'To end the program'))
    return
#Coding Complete, docstring needed

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
            area_most_least_pets_total(pets_data, communities_data, vets_data,initial_pet_calculations)
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
#Coding Complete, docstring needed

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
#Coding Complete, docstring needed

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
#In Progress

def graph_time_vs_new_registration(pets_data, communities_data, vets_data,initial_pet_calculations):
    pass
#Not started

def area_most_least_pets_total(initial_pet_calculations):
    '''This function allows the user to select cat, dog or both and quadrant of city.
       This then causes the program to print out the three most animal populated communities and three least populated communities.
       The user is then given the choice to exit the function or do another selection.

       This specific funtion generates the necesarry data for pets, calls upon a function to determine the user's selection, converts that to an array and then uses a second function to determine and print the max and mins.
    
       parameters:
       initial_pet_calculations: A tuple containing many pieces of data. The ones used in this function and the ones it calls upon are
            index 0: 2D array. Col. 0 is all communities, Col. 1 is total cats, Col.2 is total dogs, Col.3 is total cats and dogs
            index 5: List. Contains all the communities in the NE
            index 6: List. Contains all the communities in the NW
            index 7: List. Contains all the communities in the SW
            index 8: List. Contains all the communities in the SE

       returns: none
    '''
    #Converts 2-D array to three dictionaries that pair all communities with their cats, dogs, and cats and dogs combined
    all_pets_data = initial_pet_calculations[0]
    all_communities_cats, all_communities_dogs, all_communities_cats_dogs = {}, {}, {}
    for row in all_pets_data:
        all_communities_cats[row[0]] = row[1]
        all_communities_dogs[row[0]] = row[2]
        all_communities_cats_dogs[row[0]] = row[3]
    
    #Following part runs infinitely until user chooses to exit
    while True:
        #Runs function that returns a dictionary with the only the area of Calgary the user specifies and the number per community for the type of pet the user specifies. Also returns what that quadrant is and the pet
        valid_communities_dict, area, animal = most_least_pets_step_1(all_communities_cats, all_communities_dogs, all_communities_cats_dogs, initial_pet_calculations)

        #Creates array of just the valid animal population sizes based on a dictionary involving communities and pet numbers
        num_of_pets_array = np.fromiter(valid_communities_dict.values(), dtype=int)
        
        #Runs function that uses the the num_of_pets_array and valid_communities_dict to generally determine the 3 highest and lowest pet populations for within the dictionary
        most_least_pets_step_2(num_of_pets_array, valid_communities_dict, area, animal , '')
    
        #Either ends this section of the code or repeats whole thing
        print('\nPlease type Return to use other parts of the program otherwise hit enter to learn more about the minimum and maximum number of pets for communities in Calgary')
        if input() == 'Return':
            return
#Complete

def area_most_least_pets_capita(initial_pet_calculations):
    '''This function allows the user to select cat, dog or both and quadrant of city.
       This then causes the program to print out the three most animal populated communities and three least populated communities per capita.
       The user is then given the choice to exit the function or do another selection.

       This specific funtion generates the necesarry data for pets, calls upon a function to determine the user's selection, converts that to an array and then uses a second function to determine and print the max and mins.
    
       parameters:
       initial_pet_calculations: A tuple containing many pieces of data. The ones used in this function and the ones it calls upon are
            index 1: Dict. The keys are communities and the values are that communities cats per capita
            index 2: Dict. The keys are communities and the values are that communities dogs per capita
            index 3: Dict. The keys are communities and the values are that communities cats and dogs per capita
            index 5: List. Contains all the communities in the NE
            index 6: List. Contains all the communities in the NW
            index 7: List. Contains all the communities in the SW
            index 8: List. Contains all the communities in the SE

       returns: none
    '''
    #Creates three dictionaries that pair all communities with their cats, dogs, and cats and dogs combined per capita
    all_communities_cats_dogs = initial_pet_calculations[3] 
    all_communities_cats = initial_pet_calculations[1]
    all_communities_dogs = initial_pet_calculations[2]

    while True:    
        #Runs function that returns a dictionary with the only the area of Calgary the user specifies and the number per community for the type of pet the user specifies. Also returns what that quadrant is and the pet        
        valid_communities_dict, area, animal = most_least_pets_step_1(all_communities_cats, all_communities_dogs, all_communities_cats_dogs, initial_pet_calculations)
    
        #Creates array of just the valid animal population sizes per capita based on a dictionary involving communities and pet numbers
        num_of_pets_array = np.fromiter(valid_communities_dict.values(), dtype=float)
        
        #Runs function that uses the the num_of_pets_array and valid_communities_dict to generally determine the 3 highest and lowest pet populations per capita for within the dictionary
        most_least_pets_step_2(num_of_pets_array, valid_communities_dict, area, animal , ' per capita')
        
        #Either ends this section of the code or repeats whole thing
        print('\nPlease type Return to use other parts of the program otherwise hit enter to learn more about the minimum and maximum number of pets for communities in Calgary')
        if input() == 'Return':
            return
#Complete

def most_least_pets_step_1(all_communities_cats, all_communities_dogs, all_communities_cats_dogs, initial_pet_calculations):
    '''This function is designed to take the users input for quadrant and type of pet and check if it is a valid input.
    If valid, it will select one of the dictionaries that are passed into the function and modify it to match the user's input.
    
    parameters:
    all_communities_cats: A dictionary with communities as the key and either total cat population or cats per capita specific to each community
    all_communities_dogs: A dictionary with communities as the key and either total dog population or dogs per capita specific to each community    
    all_communities_cats_dogs: A dictionary with communities as the key and either total cat and dog population or cats and dogs per capita specific to each community
    initial_pet_calculations: A tuple containing many pieces of data. The ones used in this function are:
        index 5: List. Contains all the communities in the NE
        index 6: List. Contains all the communities in the NW
        index 7: List. Contains all the communities in the SW
        index 8: List. Contains all the communities in the SE

    returns:
    A tuple with multiple pieces of data. 
        index 0: Dict. Contains only the communities the user wants as keys and the corresponding value for cats, dogs or cats and dogs based on what the user specifies
        index 1: String. Contains either NE, NW, SE, SW or Calgary dependent on what the user selected
        index 2: String. Contains either Cats, Dogs or Cats and Dogs dependent on what the user selected

    '''
    #Generates the list of communities for each quadrant
    northwest_communities = initial_pet_calculations[6]
    southwest_communities = initial_pet_calculations[7]
    northeast_communities = initial_pet_calculations[5]
    southeast_communities = initial_pet_calculations[8]

    
    #Gathers input to determine animal to look into. Prints out a menu, requests input. If valid it sets all_communities_with_selected_pet_type to that pets dictionary otherwise prompts user to re-enter input
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
    
    #Gathers input to determine where in Calgary. Prints out a menu, requests input. If valid it sets adds only the pairs from all_communities_with_selected_pet_type to valid_communities_dict if the community in the pair is within that area of Calgary otherwise prompts user to re-enter input
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
    return valid_communities_dict, area, animal
#Complete

def most_least_pets_step_2(num_of_pets_array, valid_communities_dict, area, animal, capita_vs_sum):
    '''This function is designed to take the users input for quadrant and type of pet and check if it is a valid input.
    If valid, it will select one of the dictionaries that are passed into the function and modify it to match the user's input.
    
    parameters:
    num_of_pets_array: A 1D array that contains all the pet populations in the same order as valid_communities dict. Int if called from most_least_pets_total, float if called from most_least_pets_capita
    valid_communities_dict: A dictionary that has a set of communities as keys and then their corresponding pet populations as values
    area: A string that contains either NE, NW, SE, SW or Calgary dependent on what the user selected
    animal: A string that contains either Cats, Dogs or Cats and Dogs depenent on what the user selected
    capita_vs_sum: A string used to determine whether this function is called from most_least_pets_total or most_least_pets_capita. It is blank for most_lest_pets_total but says ' per capita' for most_least_pets_capita

    returns: none
    '''

    #Finds top three max's
    print('The communities in the {} with the most {}{}:'.format(area, animal.lower(), capita_vs_sum)) #Specifies the area and the pet the program looks at and indicates if it is per capita

    number_max_found = 0
    #Creates an array that can be modified without impacting the original
    num_of_pets_array_finding_max = np.copy(num_of_pets_array)

    #Runs until 3 or more communities are found and printed    
    while number_max_found < 3:
        index = -1
        #Finds max in current set of data
        num_of_pets_max = np.amax(num_of_pets_array_finding_max)
        for community, max in valid_communities_dict.items():
            index += 1
            if max == num_of_pets_max:
                number_max_found += 1
                #Once max is found, prints it out with the community and animal. If this is for the per capita function that is specified and the max is multiplied 100 to set it to per 100 people
                if capita_vs_sum == ' per capita':
                    print('{} with {:.2f} {} per 100 people'.format(community, max * 100, animal))
                else:
                    print('{} with {} {}'.format(community, max, animal))
                #The array is modified such that the max found is replaced with -1. Therefore a new number will now be the max when this section loops
                num_of_pets_array_finding_max = np.where(num_of_pets_array_finding_max == max, -1, num_of_pets_array_finding_max)
        
    #Find bottom three min's
    print('\nThe communities in the {} with the least {}{}:'.format(area, animal.lower(), capita_vs_sum))
    
    number_min_found = 0
    #Creates an array that can be modified without impacting the original
    num_of_pets_array_finding_min = np.copy(num_of_pets_array)

    #Runs until 3 or more communities are found and printed    
    while number_min_found < 3:
        index = -1
        #Finds min in current set of data
        num_of_pets_min= np.amin(num_of_pets_array_finding_min)
        for community, min in valid_communities_dict.items():
            index += 1
            if min == num_of_pets_min:
                number_min_found += 1
                #Once min is found, prints it out with the community and animal. If this is for the per capita function that is specified and the min is multiplied 100 to set it to per 100 people
                if capita_vs_sum == ' per capita':
                    print('{} with {:.2f} {} per 100 people'.format(community, min * 100, animal))
                else:
                    print('{} with {} {}'.format(community, min, animal))
                #The array is modified such that the min found is replaced with 10000000. Therefore a new number will now be the min when this section loops
                num_of_pets_array_finding_min = np.where(num_of_pets_array_finding_min == min, 10000000, num_of_pets_array_finding_min)
    return
#Complete   

def pets_info (pets_data, communities_data, vets_data,initial_pet_calculations):
    pass
#Not started

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
#Coding Complete, docstring needed

def print_vets_menu():
    print('This is the veterinarian statistics menu. Please select one of the following options:\n')
    print('{selection_option:>12} : {reason}'.format(selection_option = 'Pets Per Vet', reason = 'To see a graph comparing the number of pets per veterinarian for different areas in Calgary'))
    print('{selection_option:>12} : {reason}'.format(selection_option = 'Vets In Area', reason = 'To learn more about the veterinarian services offered for different areas of Calgary'))        
    print('{selection_option:>12} : {reason}'.format(selection_option = 'Return', reason = 'To return to the main menu'))        
    print('{selection_option:>12} : {reason}'.format(selection_option = 'End', reason = 'To end the program'))
    return
#Coding Complete, docstring needed

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
#In Progress

def vets_in_area(pets_data, communities_data, vets_data,initial_pet_calculations):
    pass
#Not started    

if __name__ == '__main__':
    main()
#Complete    