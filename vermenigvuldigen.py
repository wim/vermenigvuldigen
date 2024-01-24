#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import sys

first_fact_all = np.linspace(0,10,11, dtype=np.int8)


def greet_user():
    '''
    get the user name and load statistics of previous exercises he/she made
    '''
    import os
    
    import getpass
    
    username = getpass.getuser()
    
    multi_dir = f'/home/{username}/.multi/'
    if not os.path.exists(multi_dir):
        os.mkdir(multi_dir)
    stats_file = multi_dir+f'{username}.stats'
    # find a file in the user directory with data about past exercises.
    # if none found, make a new file
    if not os.path.isfile(stats_file):
        statsf = open(stats_file, 'w')
        print(f'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print(f' Hallo {username}! Blij je te zien!')
        print(f'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    else:
        statsf = open(stats_file, 'a')
        print(f'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print(f' Hallo {username}! Blij je weer te zien!')
        print(f'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        
        
    
    return username, statsf



def prep_exercise():
    '''
    prepare exercise
    '''
    
    pos_answer = ['J', 'JA', 'Y', 'YES']
    
    spec_table = int( input( 'Wil je oefenen met een specifieke tafel (1=ja, 0=nee)? ' ) )
    do_divide = input( 'Wil je delen oefenen (J/N)? ' )
    multi = True
    if do_divide.upper() in pos_answer: multi = False
    
    
    if spec_table == 1:
        prac_tables_str = str( input( 'Welke tafel(s) wil je oefenen (a=allemaal)? ' ) )
        # check if all tables requested
        if prac_tables_str == 'a':
            prac_tables = [i for i in range(11)]
        else:
            # check if values separated by spaces or a single one
            prac_tables_spl = prac_tables_str.split()
            if len(prac_tables_spl) > 1:
                prac_tables = [int(t) for t in prac_tables_spl]
            else:
                try:
                    prac_tables = [int(prac_tables_spl[0])]
                    #print(prac_tables)
                except:
                    randtable = int((10.-1.)*np.random.random_sample()+1.)
                    #print(randtable)
                    print(f'Dat -> {prac_tables_spl[0]} <- snap ik niet, we zullen de tafel van {randtable} oefenen.')
                    prac_tables = [randtable]
            
        # setup the multiplications
        first_fact = np.zeros((len(prac_tables),11), dtype=int )
        second_fact = np.zeros((len(prac_tables),11), dtype=int )
        for i in range(len(prac_tables)):
            fact_arr            = np.copy( first_fact_all )
            np.random.shuffle( fact_arr )
            first_fact[i,:]     = fact_arr
            second_fact[i,:]    = prac_tables[i]
        first_fact  = np.ravel(first_fact)    
        second_fact = np.ravel(second_fact)
            
    else:
        # do 10 random multiplications
        first_fact = np.copy( first_fact_all )
        np.random.shuffle( first_fact )
        second_fact = np.copy( first_fact_all )
        np.random.shuffle( second_fact )
        
    return first_fact, second_fact, multi


def do_exercise(first_fact, second_fact, multi, statsf):
    
    from ascii_art import print_ascii_art
    from datetime import datetime
    
    print('We beginnen eraan!')
    statsf.write(f'Exercise started on: {datetime.today()}\n')
    
    
    if not multi:
        # divisions
        dividend = first_fact * second_fact
        dividor  = second_fact
        correct_results = first_fact
        first_fact = dividend
        second_fact = dividor
    else:
        # multiplications
        correct_results = first_fact * second_fact
    
    err_idx         = np.linspace(0,len(correct_results)-1,len(correct_results), dtype=int)
    your_res        = np.ones_like(correct_results, dtype=int)*(-1000)
    
    
    
    sign = 'x'
    if multi != 1: sign = ':'
    while not np.array_equal(correct_results, your_res):
        for idx,i in enumerate(err_idx):
            good_input = False
            while not good_input:
                exe = f'{first_fact[i]} {sign} {second_fact[i]} = '
                inp = input(exe )
                try:
                    your_res[i] = int(inp)
                    good_input = True
                except:
                    print(f'Hmm, dat snap ik niet: {inp}. Probeer nog eens:')
            statsf.write(f'{exe} {your_res[i]}\n')
            
        if np.array_equal(correct_results, your_res):
            print('Goed zo, je hebt alles juist!')
            print_ascii_art()
            break
        else:
            err_idx = np.nonzero(correct_results - your_res)[0]
            if len(err_idx) > 1:
                print(f'Aj, {len(err_idx)} foutjes gemaakt, die doen we nog eens...')
            elif len(err_idx) == 1:
                print(f'Aj, {len(err_idx)} foutje gemaakt, die doen we nog eens...')
        
                
def finish_exercise(username):
    '''
    finish or do another round
    '''
            
    
    finish = input( 'Druk op 0 om te stoppen...of 1 om nog een oefening te maken. ' )
    if finish.isdigit():
        
        if int(finish) == 0:
            print(f'Toedeloe {username}, tot snel weer!')
            return False
        elif int(finish) == 1:
            print('Yes, we gaan nog een oefening maken!')
            return True
    else:
        print(f'Dat snap ik niet {username}, we zullen stoppen voor nu.')
        print('Daaag, tot de volgende keer!')
        return False
        
        

if __name__ == '__main__':
    
    # first greet user
    username, statsf = greet_user()

    continue_exe = True
    while continue_exe:
        # prepare exercise
        first_fact, second_fact, multi = prep_exercise()
        # execute exercise
        do_exercise(first_fact, second_fact, multi, statsf)
        # finish or do another round
        continue_exe = finish_exercise(username)
        
    statsf.close()
    
