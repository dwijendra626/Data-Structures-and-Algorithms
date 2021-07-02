'''
Program for array rotation
Ex: 
    Input array = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    Output array = [3, 4, 5, 6, 7, 1, 2]
'''
def leftrotate(a,d):
    for i in range(0,d):
        a.append(a.pop(0))
    print(a)

if __name__ == '__main__':
    d=int(input("Enter rotate by elements: "))
    a=list(map(int,input().split()))
    leftrotate(a,d)