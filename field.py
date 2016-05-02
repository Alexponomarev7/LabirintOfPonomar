number = int(input())
def load(number):
    fin = open('level'+str(number)+'.txt','r')
    field = fin.readlines()
    for i in range(len(field)):
        field[i] = field[i].strip()
    print(field)
load(number)