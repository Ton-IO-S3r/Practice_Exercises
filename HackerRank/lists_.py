my_list=[]
N = int(input())
for _ in range(N):
  instruction = input().split()
  cmd = instruction[0]
  args = instruction[1:]
  if cmd=='print':
    print(my_list)
  else:
    my_method = f'{cmd}({",".join(args)})'
    eval(f'my_list.{my_method}')