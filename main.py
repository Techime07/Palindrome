org_word = input("What text do you want to test: ")
rev_word = reversed(org_word)

if list(org_word) == list(rev_word):
    print("This text is a Palindrome")
elif list(org_word) != list(rev_word):
    print("This text is not a Palindrome")
