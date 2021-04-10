print("*******Here is Palindrome(Words) Checker********")


def word_checker(word):
    word = input("Enter the word here: ").lower()
    back = word[::-1]
    if len(word) > 1:
        if word == back:
            print(f"This word is Palindromic. It says {True}")
            recheck = input("Would you like to recheck (y) or (n): ")
            if recheck == 'y':
                word_checker(word)
            elif recheck == 'n':
                print("Thanks for using our mini checker")
                exit()
            else:
                print("Your option was invalid!!!")
                word_checker(word)
        else:
            print(f"This word isn't Palindromic. It says {False}")
            word_checker(word)
    else:
        print(f"A letter can't be Palindromic. It says {False}")
        word_checker(word)


print(word_checker(''))
