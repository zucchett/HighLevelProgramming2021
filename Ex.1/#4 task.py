import string
s = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
def counting_letter(s):
    alphabet_string_lowecase = string.ascii_lowercase
    alphabet_list_lowecase = list(alphabet_string_lowecase)
    alphabet_string_uppercase = string.ascii_uppercase
    alphabet_list_uppercase = list(alphabet_string_uppercase)
    for i in range(26):
        print(alphabet_list_lowecase[i], end=': ')
        print(s.count(alphabet_list_lowecase[i]) + s.count(alphabet_list_uppercase[i]))

counting_letter(s)