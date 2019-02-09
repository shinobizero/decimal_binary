# -*- coding: utf-8 -*-

print('Decimal To Binary Converter')
decimal = int(input('Please input a Number: '))
bin_list = []
while decimal > 0:
    if decimal % 2 == 0:
        bin_list.append(0)
    else:
        bin_list.append(1)
    decimal = decimal//2
bin_seq_rev = ''
for digit in bin_list:
    bin_seq_rev += str(digit)
print(bin_seq_rev[::-1])