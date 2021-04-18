def minion_game(string):
    length = len(string)

    the_vowel = "AEIOU"

    kiven = 0
    stuart = 0
    for i in range(length):
        if ( string[i] in the_vowel):
            kiven = kiven + length - i
        else:
            stuart = stuart + length - i

    if kiven > stuart:
        print ("Kevin %d" % kiven)
    elif kiven < stuart:
        print ("Stuart %d" % stuart)
    else:
        print ("Draw")