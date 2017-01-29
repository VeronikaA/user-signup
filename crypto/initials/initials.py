#### initials.py ####


def get_initials(fullname):
    """ Given a person's name, return the person's initials (uppercase) """
    fullnames = fullname.split()
    initials = ''.join(letter[0].upper() for letter in fullname.split()) 
    print (initials)
    return initials

def main():    
    # fullname = get_initials(input('What is your name?\n'))
    fullname = get_initials("veronika alexander")
if __name__ == '__main__':
    main()









  






