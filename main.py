
with open('word.txt', 'r') as file:
    word = file.read().strip().lower()

hidden = ['_'] * len(word)
tries = 6
used_letters = set()

while tries > 0 and '_' in hidden:
    guess = str(input('Type a letter: ')).lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print('Please insert a valid value!')
        continue
    if guess in used_letters:
        print('This letter has already been typed! Try again.')
        continue

    found = False

    used_letters.add(guess)

    for i in range(len(word)):
        if word[i] == guess:
            hidden[i] = guess
            found = True

    if not found:
        tries -= 1
        print('Wrong letter!')
        print(f'You still have {tries} tries. ')
        
    else:
        print('Good guess!')

    print('Word: ', ''.join(hidden))
    print(f"Tries: {tries}")
    print()

if not '_' in hidden:
    print(f'Congrats! You won with {tries} tries left!')
else:
    print(f'Unfortunately you lost! The word was {word}')






