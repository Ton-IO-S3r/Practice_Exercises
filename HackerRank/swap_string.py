# def swap_case(s):
#     swap = ''
#     for char in s:
#         if char.isupper():
#             swap += f'{char.lower()}'
#         else:
#             swap += f'{char.upper()}'
        
#     return swap
def swap_case(s):
  swap=''
  return swap.join([char.lower() if char.isupper() else char.upper() for char in s ])
        
print(swap_case('Hola Mundo'))