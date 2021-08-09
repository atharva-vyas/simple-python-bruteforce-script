from itertools import product
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*

#test this script
def test():
    input_word = input('enter test password to be cracked: ')
    range_from = input('enter minimum length of the password: ')
    range_to = input('enter maximum length of the password: ')
    letters = input('enter characters to be brute forced (eg: 123abcefg): ')

    def allwords(chars, length):
        for letters in product(chars, repeat=length):
            yield ''.join(letters)

    def main():
        i = 0
        print('\nthis may take some time...\n')
        for wordlen in range(int(range_from), int(range_to)):
            for word in allwords(letters, wordlen):
                if word == input_word:
                    print('success: ', word)
                    print('in tries: ', i)
                    break
                else:
                    i += 1
    main()

#for piping and coustom logic
def logic():
    range_from = input('enter minimum length of the password: ')
    range_to = input('enter maximum length of the password: ')
    letters = input('enter characters to be brute forced (eg: 123abcefg): ')

    def allwords(chars, length):
        for letters in product(chars, repeat=length):
            yield ''.join(letters)

    def main():
        # i = 0
        for wordlen in range(int(range_from), int(range_to)):
            for word in allwords(letters, wordlen):
                #ENTER COUSTOM LOGIC HERE FOR PIPING
                #ENTER COUSTOM LOGIC HERE FOR PIPING
                #ENTER COUSTOM LOGIC HERE FOR PIPING
                #ENTER COUSTOM LOGIC HERE FOR PIPING
                print('please add coustom logic')
                break
                #EXAMPLE:-
                # if word == password:
                #     print('success', word)
                #     print('in tries: ', i)
                #     break
                # else:
                #     i += 1
    main()

#writes to a txt file
def txt():
    file_name = input('enter file name: ')
    range_from = input('enter minimum length of the password: ')
    range_to = input('enter maximum length of the password: ')
    letters = input('enter characters to be brute forced (eg: 123abcefg): ')

    def allwords(chars, length):
        for letters in product(chars, repeat=length):
            yield ''.join(letters)

    def main():
        i = 0
        print('\nthis may take some time...\n')
        f = open(file_name + '.txt', "a")
        for wordlen in range(int(range_from), int(range_to)):
            for word in allwords(letters, wordlen):
                f.write(word + '\n')
                i += 1
    main()

#main menu
menu = input('\n1) test this script \n2) coustom logic(piping) \n3) save as text file\n\n')
if menu == '1':
    test()
elif menu == '2':
    logic()
elif menu == '3':
    txt()
else:
    print('invalid input')