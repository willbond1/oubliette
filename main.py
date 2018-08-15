from classes import *

def welcome():
    print("-" * 200)
    print("""
    Welcome to Oubliette!
    You are the local hero of your tiny feudal village, pop. ~50. Lately, some unseen monster has been terrorizing
    your village. You have it on faith that it lives in the nearby ancient temple ruins. Do you have what it takes
    to take up your sword and do your duty?
    """)
    print("-" * 200)

def main():
    welcome()

    slime = Creature("Slime", hp=10, atk=2, shield=1, desc='A slimy slime.')
    print(slime.__repr__())
    print(slime)
    return

if __name__ == "__main__":
    main()