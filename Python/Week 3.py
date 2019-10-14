

s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]



i= input("Enter student's name ")

if i == 'Ahmad' :

    for x in s1 :
        w= sum (s1[1:])
    print (i,w)

elif i == 'Sami':
    for x in s2 :
        w= sum (s2[1:])
    print (i,w)

elif i == 'Faris':
        for x in s3 :
            w= sum (s3[1:])
        print (i,w)

else:
    print('Student is not recorded 0')
