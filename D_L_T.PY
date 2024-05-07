a=[{'jeans':('bootcut', 'baggy', 'skinny' , 'regular'),},{"waist":('high rise' , 'mid rise ' , 'low waist')},
   {'color':('black ', 'blue' , 'navy blue' , 'denim blue' )}]
print("wellcome to the jeans store ")
print(a[0]['jeans'])
b=int(input("choose the jeans by entering the number which is before the jeans type for example if want to choose type (bootcut) enter its position number which is 1 "))
print('now for',a[0]['jeans'][b-1],'jeans choose the waist type ')
print(a[1]['waist'])
c=int(input())

print("lastly choose the color ",a[2]['color'])
d=int(input())
print("excellent combination ")
print("your order is ",a[2]['color'][d-1],a[0]['jeans'][b-1],"jeans of",a[1]['waist'][c-1] )
print("thank you")
