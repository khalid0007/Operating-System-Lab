'''
   #                             #####
  # #    #####   #####          #     #   ####   #        ####   #    #  #####
 #   #   #    #  #    #         #        #    #  #       #    #  #    #  #    #
#     #  #    #  #    #         #        #    #  #       #    #  #    #  #    #
#######  #    #  #    #         #        #    #  #       #    #  #    #  #####
#     #  #    #  #    #         #     #  #    #  #       #    #  #    #  #   #
#     #  #####   #####           #####    ####   ######   ####    ####   #    #


                                  #####   ####
                                    #    #    #
                                    #    #    #
                                    #    #    #
                                    #    #    #
                                    #     ####

                        ######
    #    #    #         #     #   #   #   #####  #    #   ####   #    #
    #    ##   #         #     #    # #      #    #    #  #    #  ##   #
    #    # #  #         ######      #       #    ######  #    #  # #  #
    #    #  # #         #           #       #    #    #  #    #  #  # #
    #    #   ##         #           #       #    #    #  #    #  #   ##
    #    #    #         #           #       #    #    #   ####   #    #
'''

'''
To make some of your text more readable, you can use ANSI escape codes to change the 
colour of the text output in your python program. A good use case for this is to to highlight errors.

Example: print("\033[1;32;40m Bright Green  \n")

The above ANSI escape code will set the text colour to bright green. The format is;
\033[  Escape code, this is always the same
1 = Style, 1 for normal.
32 = Text colour, 32 for bright green.
40m = Background colour, 40 is for black.


'''

## https://ozzmaker.com/add-colour-to-text-in-python/
'''
TEXTCOLOR   CODE	    TEXT STYLE      CODE	        BACKGROUND COLOR    CODE
Black       30	        No effect	    0	            Black	            40
Red	        31	        Bold	        1	            Red	                41
Green	    32	        Underline	    2	            Green	            42
Yellow	    33	        Negative1	    3	            Yellow	            43
Blue	    34	        Negative2	    5	            Blue	            44
Purple	    35			                                Purple	            45
Cyan	    36			                                Cyan	            46
White	    37			                                White	            47
'''

textColorDictonary = {
    'noEffect':    0,
    'Black'   :    30,
    'Red'	  :    31,
    'Green'	  :    32,
    'Yellow'  :	   33,
    'Blue'	  :    34,
    'Purple'  :	   35,
    'Cyan'    :	   36,
    'White'	  :    37,
}

textStyleDictonary = {
    'noEffect' : 0,
    'bold'     : 1,
    'undeline' : 2,
    'Negative1': 3,
    'Negative2': 5,
}

backgroundColorDictonary = {
    'noEffect'  :       0,
    'Black'	    :       40,
    'Red'       :       41,
    'Green'	    :       42,
    'Yellow'    :       43,
    'Blue'      :       44,
    'Purple'    :       45,
    'Cyan'      :       46,
    'White'	    :       47,
}

# color = {
#     'white':    "\033[1,37m",
#     'yellow':   "\033[1,33m",
#     'green':    "\033[1,32m",
#     'blue':     "\033[1,34m",
#     'cyan':     "\033[1,36m",
#     'red':      "\033[1,31m",
#     'magenta':  "\033[1,35m",
#     'black':    "\033[1,30m",
#     'darkwhite':  "\033[0,37m",
#     'darkyellow': "\033[0,33m",
#     'darkgreen':  "\033[0,32m",
#     'darkblue':   "\033[0,34m",
#     'darkcyan':   "\033[0,36m",
#     'darkred':    "\033[0,31m",
#     'darkmagenta':"\033[0,35m",
#     'darkblack':  "\033[0,30m",
#     'off':        "\033[0,0m"
# }

def wrapTextWithStyle(text='', textcolor='noEffect', backgroundcolor='noEffect', style='noEffect'):
    wrappedText = f"\033[{textStyleDictonary[style]};{textColorDictonary[textcolor]};{backgroundColorDictonary[backgroundcolor]}m{text} \033[0;0;0m"

    return wrappedText


if __name__ == '__main__':

    x = wrapTextWithStyle('Hello', 'White', 'Red', 'bold')
    print(x)