sebuah_list = ['Zorin OS','Ubuntu','Free BSD','NetBSD','OpenBSD','Backtrack','Fedora','Slackwave']
sebuah_tuple = (0,1,2,3,4,5,6,7,8,9)
sebuah_dictionary = {'nama':'Wiro Sableng','prodi':'ilmu komputer','email':'wirosableng@gmail.com','website':'www.google.com'}

print(sebuah_list)
list_baru = sebuah_list+['Windows','PC Linux OS','IGOS','OpenSUSE']
print(list_baru)
print(sebuah_tuple)
tuple_baru = sebuah_tuple + (100,200,300)
print(tuple_baru)
print(sebuah_dictionary)
dictionary_baru = {'telepon':'089654323185','alamat':'jalan batanta'}
sebuah_dictionary.update(dictionary_baru)
print(dictionary_baru)