length1 = int(input('Length1 : '))
breadth1= int(input('breadth1 : '))
length2 = int(input('Length2: '))
breadth2= int(input('breadth2 : '))
area1= length1* breadth1
area2= length2*breadth2
perimeter = 2 * (length1 + breadth1)
print('Perimeter of the Rectangle : ',perimeter)
if area1 > area2:
        print()
        print('The area of rectangle one is: ', area1)
        print('The area of rectangle two is: ', area2)
        print('Rectangle one\'s area is greater.')
elif area1 < area2:
        print()
        print('The area of rectangle one is: ', area1)
        print('The area of rectangle two is: ', area2)
        print('Rectangle two\'s area is greater.')
elif area1 == area2:
        print()
        print('The area of rectangle one is: ', area1)
        print('The area of rectangle two is: ', area2)
        print('Rectangle\'s areas are equal.')
        print('Perimeter of the Rectangle : ',perimeter)

