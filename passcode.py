import random


def crack_passcode(passcode):
    character_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                      'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                      'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
                      'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                      's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2',
                      '3', '4', '5', '6', '7', '8', '9']
    guess_passcode = ''
    tries = 0
    while guess_passcode != passcode:
        guess_passcode = random.choices(character_list, k=len(passcode))
        passcode_list = list(passcode)
        print(f'Decrypting passcode: {guess_passcode}')
        tries += 1
        if guess_passcode == passcode_list:
            guess_passcode = ''.join(guess_passcode)
            print(f'Your passcode is {guess_passcode} and it took {tries} times to guess it.')
            break


if __name__ == '__main__':
    user_passcode = input("Enter a passcode using letters & numbers: ")
    crack_passcode(user_passcode)
