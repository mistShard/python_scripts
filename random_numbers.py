import random

def main():
    numbers = [16.2, 34.4, 87.99]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 2)
    print(numbers)
    words = ['joy', 'ben', 'ken']
    print(words)
    append_random_words(words)
    print(words)
    append_random_words(words, 2)
    print(words)

def append_random_numbers(alist, quantity=1):
    for _ in range(quantity):
        num = round(random.uniform(1, 2**8), 2)
        alist.append(num)

def append_random_words(alist, quantity=1):
    for _ in range(quantity):
        words = ['blow', 'dang', 'minute', 'cap', 'gang', 'game']
        word = random.choice(words)
        alist.append(word)

if __name__ == "__main__":
    main()