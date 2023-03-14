def f(x,y,delit):
    if x%delit == 0 and y%delit == 0:
        global count
        count=delit
        if delit < min(x,y):
            return f(x,y,delit)
        else:
            return count
    else:
        if delit<min(x,y):
            return f(x,y,delit+1)
delit=2
count=0
x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
print(f(x,y,delit))



#конь ходит буквой Г на поле 8
pole = [i for i in range(36)]#игровое поле
visited=[]#где конь был
x1 = int(input('Введите положение коня по x: '))
y1 = int(input('Введите положение коня по y: '))
x2 = int(input('Введите куда прийдет конь по х:'))
y2 = int(input('Введите куда прийдет конь по y:'))
dx = (abs(x1-x2)) #модуль разницы координат х
dy = (abs(y1-y2)) #модуль разницы координат y
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('Yes')
else:
    print('No')
# конь 2 вариант
# Посещение нужно для того чтобы:
#1. Хранить список посещений
#2. Хранить клетки для возможного хода коня
visited = [[0 for i in range(N)] for y in range(N)]
pos = 1
#клетки из 8 вариаций хода коня
row = [2,1,-1,-2,-2,-1,1,2,2]
col =[1,2,2,1,-1,-2,-2,-1,1]

#является ли (х,у) правильными координатами доски
def isvalid(x,y):
    return not (x<0 or y<0 or x>=N or y>=N) # N-длина доски
def horse(visited,x,y,pos):
    visited[x][y] = pos
    if pos>=N*N:
        for i in visited:
            print(i)
        print()
        visited[x][y]=0
        return
#Проверка всех восьми возможных ходов
    for i in range(8):
        #новая позиция коня из текущей клетки
        newX=x+row[i]
        newY=y+col[i]
        #Если позиция действительная и не посещена
        if isvalid(newX,newY) and visited[newX][newY] == 0:
            horse(visited,newX,newY,pos+1)
    visited[x][y]=0

horse(visited,0,0,pos)#вместо нулей х и у можно передать данный пользователя о начальном положении коня