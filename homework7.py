
def display_quote():
    print('''"Don't compare yourself with anyone in this world.
if you do so, you are insulting yourself."
         Bill Gates''')

display_quote()


def print_even_numbers(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i)


print_even_numbers(1, 10)


def draw_square(size, symbol, filled):
    for i in range(size):
        if filled or i == 0 or i == size - 1:
            print(symbol * size)
        else:
            print(symbol + ' ' * (size - 2) + symbol)

draw_square(5, '*', True)
draw_square(5, '#', False)

def find_minimum(a, b, c, d, e):
    return min(a, b, c, d, e)

print(find_minimum(3, 7, 2, 9, 5))

def count_digits(number):
    return len(str(abs(number)))

print(count_digits(3456))


def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

print(is_palindrome(12321)) 
print(is_palindrome(421987)) 
