# name = 'Rümeysa Besli'

# for letter in name:
#     if letter=='a':
#         break       #a harfinde durup sonlanır
#         #continue   #sadece a harini es geçip döngüyü tamamlıyor
#     print(letter)
#####################
# x=0

# while x<5:
#     if x==2:
#         continue    #ikide takılı kalıp arttırılmadığı için break gibi işlev görür, çünkü arttırma breakten sonra okutuluyor
#     print(x)
#     x+=1
#########################


#1-100e kadar tek sayıların toplamı
x=0
sum=0
while x<=100:
    sum+=x
    x+=1
    if x%2==0:
        continue
print(sum)
