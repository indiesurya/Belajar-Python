sebuah_list = ['Zorin OS','Ubuntu','Free BSD','NetBSD','OpenBSD','Backtrack','Fedora','Slackwave']
sebuah_tuple = (0,1,2,3,4,5,6,7,8,9)
sebuah_dictionary = {'nama':'Wiro Sableng','prodi':'ilmu komputer','email':'wirosableng@gmail.com','website':'www.google.com'}
print(sebuah_list)
print(sebuah_tuple)
print(sebuah_dictionary)

print(sebuah_tuple[8])
print(sebuah_list[2])
print(sebuah_dictionary['email'])

print(sebuah_list[2:5])
print(sebuah_tuple[3:9])

for i in sebuah_list :
    print(i)

for j in sebuah_tuple :
    print(j)

for k in sebuah_dictionary :
    print(k,':',sebuah_dictionary[k])