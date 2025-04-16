#task 1

filtered_numbers = [x for x in range(1, 101) if x % 3 == 0 and x % 5 != 0]
   print(filtered_numbers)

#task 2

celsius = [0, 10, 20, 30, 40, 100]
fahrenheit = [c * 9 / 5 + 32 for c in celsius]
   print(fahrenheit)


#task 3

even_squares = [x**2 for x in range(1, 51) if x % 2 == 0]
   print(even_squares)


#task 4

text = "Python is amazing and powerful language"
word_lengths = [len(word) for word in text.split()]
   print(word_lengths)


#task 5

composite_numbers = [n for n in range(2, 101)
                     if len([d for d in range(1, n + 1) if n % d == 0]) > 2]
   print(composite_numbers)
