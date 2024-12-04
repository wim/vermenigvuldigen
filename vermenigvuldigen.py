#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import sys
import datetime

first_fact_all = np.linspace(0,10,11, dtype=np.int8)

def new_yaml_timing(mult):
    """
    return empty dict for the requested multiplication exercise
    """
    mult_dict = {str(mult): {'date':[], 'timing': []}}
    return mult_dict

def new_yaml_file(username):
    """
    create a new (almost empty) yaml file that contains the timings of different exercises
    """

    yaml_dict = {'username':username, 'timings':new_yaml_timing(str(1))}
    
    return yaml_dict


def greet_user():
    '''
    get the user name and load statistics of previous exercises he/she made
    '''
    import os
    
    import getpass
    import yaml
    
    username = getpass.getuser()
    
    multi_dir = f'/home/{username}/.multi/'
    if not os.path.exists(multi_dir):
        os.mkdir(multi_dir)
    stats_file = multi_dir+f'{username}.stats'
    stats2_file = multi_dir+f'{username}_mult.yaml'
    
    # find a file in the user directory with data about past exercises.
    # if none found, make a new file
    if not os.path.isfile(stats_file):
        statsf = open(stats_file, 'w')
        again = ''
    else:
        statsf = open(stats_file, 'a')
        again = 'weer '

    # statistics file in yaml
    if not os.path.isfile(stats2_file):
        # yaml file needs to be created
        stats = new_yaml_file(username)
    else:
        with open(stats2_file) as stream:
            try:
                stats = yaml.safe_load(stream)
            except yaml.YAMLError as err:
                print(err)
        if stats is None or 'username' not in stats: # guard against empty or incomplete file
            stats = new_yaml_file(username)
    
        
    print(f'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print(f' Hallo {username}! Blij je {again}te zien!')
    print(f'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        
    
    return username, statsf, stats, stats2_file



def prep_exercise():
    '''
    prepare exercise
    '''
    
    single_table = False
    pos_answer = ['J', 'JA', 'Y', 'YES']
    
    spec_table = int( input( 'Wil je oefenen met een specifieke tafel (1=ja, 0=nee)? ' ) )
    do_divide = input( 'Wil je delen oefenen (1=ja, 0=nee)? ' )
    do_multi = True
    if do_divide.upper() in pos_answer or do_divide == 1: do_multi = False
    
    
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
                single_table = True
                try:
                    prac_tables = [int(prac_tables_spl[0])]
                except:
                    randtable = int((10.-1.)*np.random.random_sample()+1.)
                    print(f'Dat -> {prac_tables_spl[0]} <- snap ik niet, we zullen de tafel van {randtable} oefenen.')
                    prac_tables = [randtable]
            
        # setup the multiplications
        first_fact  = np.zeros((len(prac_tables),11), dtype=int )
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
        
    return first_fact, second_fact, do_multi, single_table


def do_exercise(first_fact, second_fact, do_multi, statsf):
    
    from ascii_art import print_ascii_art
    from datetime import datetime
    import time
    
    
    print('We beginnen eraan!')
    statsf.write(f'Exercise started on: {datetime.today()}\n')
    t0 = time.time()
    
    
    if not do_multi:
        # divisions
        dividend        = first_fact * second_fact
        dividor         = second_fact
        correct_results = first_fact
        first_fact      = dividend
        second_fact     = dividor
    else:
        # multiplications
        correct_results = first_fact * second_fact
    
    err_idx         = np.linspace(0,len(correct_results)-1,len(correct_results), dtype=int)
    your_res        = np.ones_like(correct_results, dtype=int)*(-1000)
    
    
    nmult = len(your_res)
    sign = 'x'
    if do_multi != 1: sign = ':'
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
            break
        else:
            err_idx = np.nonzero(correct_results - your_res)[0]
            if len(err_idx) > 1:
                print(f'Aj, {len(err_idx)} foutjes gemaakt, die doen we nog eens...')
            elif len(err_idx) == 1:
                print(f'Aj, {len(err_idx)} foutje gemaakt, die doen we nog eens...')
    
    t1 = time.time()
    dt = t1 - t0

    print(f'Totale tijd voor de hele oefening: {dt:8.3f} sec')
    print(f'Gemiddelde tijd per vermenigvuldiging/deling: {dt/float(nmult):8.3f} sec')
    statsf.write(f'Exercise finished in {dt:8.3f} sec\n')
    
    print_ascii_art()
    return dt
        
                
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
    
    import yaml
    import datetime

    # first greet user
    username, statsf, stats, stats2_file = greet_user()

    continue_exe = True
    while continue_exe:
        # prepare exercise
        first_fact, second_fact, do_multi, single_table = prep_exercise()

        # execute exercise
        dexe = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        texe = do_exercise(first_fact, second_fact, do_multi, statsf)
        
        #print(single_table)
        # when doing a single table, add the timing to the yaml file
        if single_table:
            table_value = str(second_fact[0])
            # add to correct dict of stats, if dict does not exist, add a new one
            #print('timings' in stats, table_value, stats['timings'])
            if 'timings' in stats:
                if table_value in stats['timings']:
                    # add new timing to current table
                    stats['timings'][table_value]['timing'].append(texe)
                    stats['timings'][table_value]['date'].append(dexe)
                else:
                    # current table value not practised before, add anew
                    new_timing_table = new_yaml_timing(table_value)
                    #stats['timings'][table_value] = new_timing_table[table_value]
                    stats['timings'][table_value] = new_yaml_timing(table_value)[table_value]
                    stats['timings'][table_value]['timing'].append(texe)
                    stats['timings'][table_value]['date'].append(dexe)
                    
            # write stats to yaml file
            with open(stats2_file,'w') as outf:
                yaml.dump(stats, outf, default_flow_style=False)


        # finish or do another round
        continue_exe = finish_exercise(username)
        
    statsf.close()
    
