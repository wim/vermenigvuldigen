#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import sys

first_fact_all = np.linspace(0,10,11, dtype=np.int8)

def print_ascii_art(all=False):
    art = [
r"""
                ;'-. 
    `;-._        )  '---.._
      >  `-.__.-'          `'.__
     /_.-'-._         _,   ^ ---)
jgs  `       `'------/_.'----```
                     `
""",\
r"""
   |\---/|
   | ,_, |
    \_`_/-..----.
 ___/ `   ' ,""+ \  sk
(__...'   __\    |`.___.';
  (_,...'(_,.`__)/'.....+
""",\
r"""
     |\_/|                  
     | @ @   Woof! 
     |   <>              _  
     |  _/\------____ ((| |))
     |               `--' |   
 ____|_       ___|   |___.' 
/_/_____/____/_______|
""",\
r"""
   /|       |\
`__\\       //__'
   ||      ||
 \__`\     |'__/
   `_\\   //_'
   _.,:---;,._
   \_:     :_/
     |@. .@|
     |     |
     ,\.-./ \
     ;;`-'   `---__________-----.-.
     ;;;                         \_\
     ';;;                         |
      ;    |                      ;
       \   \     \        |      /
        \_, \    /        \     |\
          |';|  |,,,,,,,,/ \    \ \_
          |  |  |           \   /   |
          \  \  |           |  / \  |
           | || |           | |   | |
           | || |           | |   | |
           | || |           | |   | |
           |_||_|           |_|   |_|
          /_//_/           /_/   /_/
""" ,\
r"""
            .''
  ._.-.___.' (`\
 //(        ( `'
'/ )\ ).__. ) 
' <' `\ ._/'\
   `   \     \
""",\
r"""
                     /\    .-" /
                    /  ; .'  .' 
                   :   :/  .'   
                    \  ;-.'     
       .--''''--..__/     `.    
     .'           .'    `o  \   
    /                    `   ;  
   :                  \      :  
 .-;        -.         `.__.-'  
:  ;          \     ,   ;       
'._:           ;   :   (        
    \/  .__    ;    \   `-.     
 bug ;     "-,/_..--"`-..__)    
     '""--.._:
""",\
r"""
      (\-'''-/)
       |     |
       \ ^ ^ /  .-.
        \_o_/  / /
       /`   `\/  |
      /       \  |
      \ (   ) /  |
     / \_) (_/ \ /
    |   (\-/)   |
    \  --^o^--  /
     \ '.___.' /
jgs .'  \-=-/  '.
   /   /`   `\   \
  (//./       \.\\)
   `"`         `"`
""",\
r"""
            __,__
   .--.  .-"     "-.  .--.
  / .. \/  .-. .-.  \/ .. \
 | |  '|  /   Y   \  |'  | |
 | \   \  \ 0 | 0 /  /   / |
  \ '- ,\.-"`` ``"-./, -' /
   `'-' /_   ^ ^   _\ '-'`
       |  \._   _./  |
       \   \ `~` /   /
jgs     '._ '-=-' _.'
           '~---~'
""",\
r"""
 __         __
/  \.-'''-./  \
\    -   -    /
 |   o   o   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`
""",\
r"""
       _.--.__                                             _.--.
    ./'       `--.__                                   ..-'   ,'
  ,/               |`-.__                            .'     ./
 :,                 :    `--_    __                .'   ,./'_.....
 :                  :   /    `-:' _\.            .'   ./..-'   _.'
 :                  ' ,'       : / \ :         .'    `-'__...-'
 `.               .'  .        : \@/ :       .'       '------.,
    ._....____  ./    :     .. `     :    .-'      _____.----'
              `------------' : |     `..-'        `---.
                         .---'  :    ./      _._-----'
.---------._____________ `-.__/ : /`      ./_-----/':
`---...--.              `-_|    `.`-._______-'  /  / ,-----.__----.
   ,----' ,__.  .          |   /  `\.________./  ====__....._____.'
   `-___--.-' ./. .-._-'----\.                  ./.---..____.--.
         :_.-' '-'            `..            .-'===.__________.'
                                 `--...__.--'
""",\
r"""
                        ____
                   .---'-    \
      .-----------/           \
     /           (         ^  |   __
&   (             \        O  /  / .'
'._/(              '-'  (.   (_.' /
     \                    \     ./
      |    |       |    |/ '._.'
       )   @).____\|  @ |
   .  /    /       (    | mrf
  \|, '_:::\  . ..  '_:::\ ..\).
""",\
r"""
               _,.---.---.---.--.._ 
           _.-' `--.`---.`---'-. _,`--.._
          /`--._ .'.     `.     `,`-.`-._\
         ||   \  `.`---.__`__..-`. ,'`-._/
    _  ,`\ `-._\   \    `.    `_.-`-._,``-.
 ,`   `-_ \/ `-.`--.\    _\_.-'\__.-`-.`-._`.
(_.o> ,--. `._/'--.-`,--`  \_.-'       \`-._ \
 `---'    `._ `---._/__,----`           `-. `-\
           /_, ,  _..-'                    `-._\
           \_, \/ ._(
            \_, \/ ._\
             `._,\/ ._\
               `._// ./`-._
        LGB      `-._-_-_.-'
""",\
r"""
                         .       .
                        / `.   .' \
                .---.  <    > <    >  .---.
                |    \  \ - ~ ~ - /  /    |
                 ~-..-~             ~-..-~
             \~~~\.'                    `./~~~/
   .-~~^-.    \__/                        \__/
 .'  O    \     /               /       \  \
(_____,    `._.'               |         }  \/~~~/
 `----.          /       }     |        /    \__/
       `-.      |       /      |       /      `. ,~~|
           ~-.__|      /_ - ~ ^|      /- _      `..-'   f: f:
                |     /        |     /     ~-.     `-. _||_||_
                |_____|        |_____|         ~ - . _ _ _ _ _>
""",\
r"""
         . 
        /'
       //
   .  //           
   |\//7
  /' " \
 .   . .  
 | (    \     '._
 |  '._  '    '. '
 /    \'-'_---. ) )
.              :.' 
|               \
| .    .   .     .
' .    |  |      |
 \^   /_-':     /
 / | |    '\  .'
/ /| |     \\  |
\ \( )     // /
 \ | |    // /
  L! !   // / Monoceros'95
   [_]  L[_|  R.B.Cleary
""",\
r"""
                                  _.._
                             .--'` .-,)
                           .'     /
            ,             /      /
           /\            ;      ;
           | `.__..__    |      |
           |         `''-\      ;
            \             `      \
             '.                   `.
               '--.,__   __..-'-.   '. 
                      ```        `.   '.
                                   `.   `\
                   _.._              \    `\
                _.'    '-._ .__       |     `\
              .'/        .-'   `\     |       \
            .'  :           .-.  |    /        \
  _        /     \         /_  | /_..-`"-.     ;
 / '.     |  .    )  .-')_/` \.'`         \    |
;    \    /_.'  .'_.' .-. .-./       .--._/    ;
|   _ '-'`      ` /  /o )(o (       (   __    /
;  ( '           ///     _) |'.      `'`  `'-;
 \  `   _       ////  ,__   /  `,            _)
  '. ' ( `--.__.\  '.  `"` /              .-'
    '.  '      .-)  /-.__.'`-.  (     .  /
      \  ' __.' /  /          \  '---'  |
       `-.'-=\.'  /     _._\   \        /
         '===/   /`'._.'   _\_  \-.__.-'
           `|   /`-...--'''      |
            \__/`-._       __.-'`
                    `'''''`

""",\
r"""
     .-----.
   .' -   - '.
  /  .-. .-.  \
  |  | | | |  |
   \ \o/ \o/ /
  _/    ^    \_
 | \  '---'  / |
 / /`--. .--`\ \
/ /'---` `---'\ \
'.__.       .__.'
    `|     |`
     |     \
     \      '--.
      '.        `\
        `'---.   |
   jgs     ,__) /
            `..'
""",\
r"""
                               ._                             
                              |* ;                            
            `*-.              |"":                            
             \  \             |""                             
              .  \            |   :                           
              `   \           |                               
               \   \          |    ;               +.         
                .   \         |                   *._`-.      
                `    \        |     :          .-*'  `. `.    
                _\    \.__..--**--...L_   _.-*'      .'`*'    
               /  `*-._\   -.       .-*"*+._       .'         
              :        ``*-._*.     \      _J.   .'           
          .-*'`*-.       ;     `.    \    /   `.'             
      .-*'  _.-*'.     .-'       `-.  `-.:   _.'`-.           
   +*' _.-*'      `..-'             `*-. `**'      `-.        
    `*'          .-'      ._            `*-._         `.      
       [bug]  .-'         `.`-.____..+-**""'         .*"`.    
         ._.-'          _.-*'':$$$;._$              /     `.  
      .-'  `.      _.-*' `*-.__T$P   `"**--..__    :        `.
.'..-'       \_.-*'                            `"**--..___.-*'
`. `.    _.-*'                                                
  `. `:*'                                                     
    `. `.                                                     
      `*

""",\
r"""
---------------+---------------
          ___ /^^[___              _
         /|^+----+   |#___________//
       ( -+ |____|    ______-----+/
        ==_________--'            \
          ~_|___|__

""",\
r"""
                  ~.
           Ya...___|__..aab     .   .
            Y88a  Y88o  Y88a   (     )
             Y88b  Y88b  Y88b   `.oo'
             :888  :888  :888  ( (`-'
    .---.    d88P  d88P  d88P   `.`.
   / .-._)  d8P''''|''''-Y8P      `.`.
  ( (`._) .-.  .-. |.-.  .-.  .-.   ) )
   \ `---( O )( O )( O )( O )( O )-' /
    `.    `-'  `-'  `-'  `-'  `-'  .' CJ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""",\
r"""
        _..._
      .'     '.      _
     /    .-""-\   _/ \
   .-|   /:.   |  |   |
   |  \  |:.   /.-'-./
   | .-'-;:__.'    =/
   .'=  *=|NASA _.='
  /   _.  |    ;
 ;-.-'|    \   |
/   | \    _\  _\
\__/'._;.  ==' ==\
         \    \   |
         /    /   /
         /-._/-._/
  jgs    \   `\  \
          `-._/._/
""",\
r"""
                           ,
                          //\
                         / | ;
                         | /_|
                       .-"`  `"-. 
                     /`          `\
                    /              \
              .-.,_|      .-''''-. |
             |     `",_,-'  (((-. '(  
              \ (`"=._.'/   (  (o>'-`"#
   ,           '.`"-'` /     `--`  '==;
  /\\            `'--'`\         _.'~~
 / | \                  `.,___,-} 
 | |  |                   )  {  }
  \ \ (.--==---==-------=' o {  }
   ",/` (_) (_)  (_)    (_)   \ /
    / ()   o   ()    ()        ^|
    \   ()  (    () o        ;  /
     `\      \         ;    / } |
       )      \       /   /`  } /
    ,-'       |=,_   |   /,_ ,'/
    |    _,.-`/   `"=\   \\   \
    | ."` \  |        \   \`\  \
    | |    \ \         `\  \ `\ \
    | |     \ \          `\ \  \ \
    | |      \ \           \ \  \ \
    | |       \ \           \ \  \ \
    | |        \ \           \ \  \ \
    | |         ) \           \ \  ) \
jgs `) \        ^ww            ) \ ^ww
     ^ww                       ^ww
""",\
r"""
                   _
                  ( \
       __         _)_\_
      ' \;---.-._S_____2_
        /   / /_/       (______
     __(  _;-'    =    =|____._'.__
    /   _/     _  @\ _(@(      '--.\
    (_ /      /\  _   =( ) ___     \\
      /      /\ \_ '.___'-.___~.    '\
snd  /      /\ \__'--') '-.__c` \    |
    |     .'  )___'--'/  /`)     \   /
    |    |'-|    _|--'\_(_/       '.'
    |    |   \_  -\
     \   |     \ /`)
      '._/      (_/
""",\
r"""
             .
             |~
            /|\
           |-.-|
           '-:-'
            [|]
            [|]
            [|]
            [|]
            [|]
           .[|].
           :/|\:
           [/|\]
           [/|\]
         .:_#|#_:.
         |_ '-' _|
         /\:-.-:/\
        /\|_[|]_|/\
      _/\|~ [|] ~|/\_
      [''=-.[|].-='']
      :-._   |   _.-:
      //\;::-:-::;/\\
     /\.'-\\/|\//-'./\
   .'\/'   :\|/:   '\/'.
 .//\('    [\|/]    ')/\\.
'':][\.'  .[\|/].  './][:''
    ''    :/\|/\:    ''
         .[\/|\/].
           '.|.'
             '
""",\
r"""
                                  |>>>
                                  |
                    |>>>      _  _|_  _         |>>>
                    |        |;| |;| |;|        |
                _  _|_  _    \\.    .  /    _  _|_  _
               |;|_|;|_|;|    \\:. ,  /    |;|_|;|_|;|
               \\..      /    ||;   . |    \\.    .  /
                \\.  ,  /     ||:  .  |     \\:  .  /
                 ||:   |_   _ ||_ . _ | _   _||:   |
                 ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  |
                 ||:   ||.    .     .      . ||:  .|
                 ||: . || .     . .   .  ,   ||:   |       \,/
                 ||:   ||:  ,  _______   .   ||: , |            /`\
                 ||:   || .   /+++++++\    . ||:   |
                 ||:   ||.    |+++++++| .    ||: . |
              __ ||: . ||: ,  |+++++++|.  . _||_   |
     ____--`~    '--~~__|.    |+++++__|----~    ~`---,              ___
-~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~~

""",\
r"""
        .n.                     |
       /___\          _.---.  \ _ /
       [|||]         (_._ ) )--;_) =-
       [___]           '---'.__,' \
       }-=-{                    |
       |-" |
       |.-"|                p
~^=~^~-|_.-|~^-~^~ ~^~ -^~^~|\ ~^-~^~-
^   .=.| _.|__  ^       ~  /| \
 ~ /:. \" _|_/\    ~      /_|__\  ^
.-/::.  |   |""|-._    ^   ~~~~
  `===-'-----'""`  '-.              ~
                 __.-'      ^

""",\
r"""
                               _
                           ,--.\`-. __
                         _,.`. \:/,"  `-._
                     ,-*" _,.-;-*`-.+"*._ )
                    ( ,."* ,-" / `.  \.  `.
                   ,"   ,;"  ,"\../\  \:   \
                  (   ,"/   / \.,' :   ))  /
                   \  |/   / \.,'  /  // ,'
                    \_)\ ,' \.,'  (  / )/
                        `  \._,'   `"
                           \../
                           \../
                 ~        ~\../           ~~
          ~~          ~~   \../   ~~   ~      ~~
     ~~    ~   ~~  __...---\../-...__ ~~~     ~~
       ~~~~  ~_,--'        \../      `--.__ ~~    ~~
   ~~~  __,--'              `"             `--.__   ~~~
~~  ,--'                                         `--.
   '------......______             ______......------` ~~
 ~~~   ~    ~~      ~ `````---'''''  ~~   ~     ~~
        ~~~~    ~~  ~~~~       ~~~~~~  ~ ~~   ~~ ~~~  ~
     ~~   ~   ~~~     ~~~ ~         ~~       ~~   SSt
              ~        ~~       ~~~       ~

"""
]


    if all:
        for a in art: print(a)
    else:
        idx = int(len(art)*np.random.random_sample())
        print(art[idx])

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
        statsf = open(stats_file, 'r')
        print(f'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print(f' Hallo {username}! Blij je weer te zien!')
        print(f'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    
    return username, statsf



def prep_exercise():
    '''
    prepare exercise
    '''

    spec_table = int( input( 'Wil je oefenen met een specifieke tafel (1=ja, 0=nee)? ' ) )
    
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
        
        return first_fact, second_fact
    else:
        # do 10 random multiplications
        first_fact = np.copy( first_fact_all )
        np.random.shuffle( first_fact )
        second_fact = np.copy( first_fact_all )
        np.random.shuffle( second_fact )
        
        return first_fact, second_fact


def do_exercise(first_fact, second_fact):
    
    
    print('We beginnen eraan!')
    
    correct_results = first_fact * second_fact
    
    err_idx         = np.linspace(0,len(correct_results)-1,len(correct_results), dtype=int)
    your_res        = np.ones_like(correct_results, dtype=int)*(-1000)
    while not np.array_equal(correct_results, your_res):
        for idx,i in enumerate(err_idx):
            good_input = False
            while not good_input:
                inp = input(f'{first_fact[i]} x {second_fact[i]} = ' )
                try:
                    your_res[i] = int(inp)
                    good_input = True
                except:
                    print(f'Hmm, dat snap ik niet: {inp}. Probeer nog eens:')

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
        print('Dat snap ik niet {username}, we zullen stoppen voor nu.')
        print('Daaag, tot de volgende keer!')
        return False

        

if __name__ == '__main__':
    
    # first greet user
    username, statsf = greet_user()

    continue_exe = True
    while continue_exe:
        # prepare exercise
        first_fact, second_fact = prep_exercise()
        # execute exercise
        do_exercise(first_fact, second_fact)
        # finish or do another round
        continue_exe = finish_exercise(username)
        
    #print_ascii_art(all=True)
    #prep_exercise()

