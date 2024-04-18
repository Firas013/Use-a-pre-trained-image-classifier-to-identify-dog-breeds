#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: FIRAS AL-DAWSARI
# DATE CREATED: 17/04/2024
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):


    """"
    print("Model: ", model)

    # Print total number of images
    print("Number of Images: ", results_stats_dic.get('n_images', 0))

    # Print total number of dog images
    print("Number of Dog Images: ", results_stats_dic.get('n_dogs_img', 0))

    # Print total number of "Not-a-Dog" images
    print("Number of Not-a-Dog Images: ", results_stats_dic.get('n_notdogs_img', 0))

    # Print percentage of correct dog classifications
    print("Percentage of Correct Dog Classifications: ", results_stats_dic.get('pct_correct_dogs', 0))

    # Print percentage of correct breed classifications
    print("Percentage of Correct Breed Classifications: ", results_stats_dic.get('pct_correct_breed', 0))

    # Print percentage of correct "Not-a-Dog" classifications
    print("Percentage of Correct 'Not-a-Dog' Classifications: ", results_stats_dic.get('pct_correct_notdogs', 0))

    # Print percentage of match
    print("Percentage of Match: ", results_stats_dic.get('pct_match', 0))

    # Print incorrect dog classifications if requested
    if print_incorrect_dogs:
        incorrect_dogs = [(key, results_dic[key]) for key in results_dic if
                          isinstance(results_dic[key], tuple) and sum(results_dic[key][3:]) == 1]
        if incorrect_dogs:
            print("\nIncorrect Dog Classifications:")
            for key, (pet_label, classifier_label, correct_class, is_dog, _) in incorrect_dogs:
                print("Pet Label: ", pet_label)
                print("Classifier Label: ", classifier_label)

    # Print incorrect breed classifications if requested
    if print_incorrect_breed:
        incorrect_breeds = [(key, results_dic[key]) for key in results_dic if
                            isinstance(results_dic[key], tuple) and sum(results_dic[key][3:]) == 2 and
                            results_dic[key][2] == 0]
        if incorrect_breeds:
            print("\nIncorrect Breed Classifications:")
            for key, (pet_label, classifier_label, _, is_dog, _) in incorrect_breeds:
                print("Pet Label: ", pet_label)
                print("Classifier Label: ", classifier_label)

# usage of the function
    print_results(results_stats_dic, results_dic, model, print_incorrect_dogs=True, print_incorrect_breed=True)
"""
    # Print model architecture used
    print("Model: ", model)

    # Print total number of images
    print("Number of Images: ", results_stats_dic['n_images'])

    # Print total number of dog images
    print("Number of Dog Images: ", results_stats_dic['n_dogs_img'])

    # Print total number of "Not-a-Dog" images
    print("Number of Not-a-Dog Images: ", results_stats_dic['n_notdogs_img'])

    # Print percentage of correct dog classifications
    print("Percentage of Correct Dog Classifications: ", results_stats_dic['pct_correct_dogs'])

    # Print percentage of correct breed classifications
    print("Percentage of Correct Breed Classifications: ", results_stats_dic['pct_correct_breed'])

    # Print percentage of correct "Not-a-Dog" classifications
    print("Percentage of Correct 'Not-a-Dog' Classifications: ", results_stats_dic['pct_correct_notdogs'])
    print('Percentage of Match: ', results_stats_dic['pct_match'])
    # Print incorrect dog classifications if requested
    if ( results_stats_dic['n_dogs_img'] + results_stats_dic['n_notdogs_img'] != results_stats_dic['n_images']):
        print("\nIncorrect Dog Classifications:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 1:
                print("Pet Label: ", results_dic[key][0])
                print("Classifier Label: ", results_dic[key][1])

    # Print incorrect breed classifications if requested
    if(results_stats_dic['n_dogs_img'] != results_stats_dic['n_correct_breed']):
        print("\nIncorrect Breed Classifications:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                print("Pet Label: ", results_dic[key][0])
                print("Classifier Label: ", results_dic[key][1])



# I dont know what's the problem if I solved it by first method
# It's displayed to my an recursion erorr for printing the model in line 37 ?
