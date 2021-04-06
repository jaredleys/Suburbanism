import random
import re

def title_page():
    print("---------------------------------------------------")
    print("Welcome to the SUBURBANISM Text-Based Adventure Game!")
    print("Original story and game design by Jared Leys.")
    print("---------------------------------------------------")

def intro():
    print("---------------------------------------------------")
    print("Suburbanism is a tale told in Seven Movements.")
    print("---------------------------------------------------")
    print("--First Movement--")
    print("Suburbanism: A Tale of Pride, Courage, and a Boy Name Greeny/n/nOnce upon a time, there was a boy named Greeny.  He was very popular, but nobody really knew why, including himself. He lived high on a hill in the middle of Nowhere. Nowhere was a mostly peaceful and harmless land. Except for Greeny. He believed in Suburbanism.")
    print("What is Suburbanism? Well, nobody really knew the answer to that question outside of Greeny and his brother. But the meaning doesn’t really matter to this story except to say that it was a problem.  And not a problem for Greeny, but for the people of Nowhere.  They did not understand Suburbanism, so they did not like it.")


ready_input = input("Are you ready to begin your adventure? ")

# if re.search("no|No|NO|nO") != None:
#     print("No problem! Let's start over.")
#     title_page()
# else:
#     intro()

title_page()
intro()
