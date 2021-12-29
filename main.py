org_word = input("What text do you want to test: ").lower()
rev_word = reversed(org_word)

if list(org_word) == list(rev_word):
    print( org_word.capitalize() + " is a Palindrome")
elif list(org_word) != list(rev_word):
    print( org_word.capitalize() + " is not a Palindrome")
