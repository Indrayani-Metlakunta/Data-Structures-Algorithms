# creating dictionary
phone_no = {'Ram' : 1234,
            'Shyam' : 4564,
            'Mohan' : 5678,
            'Ram' : 8986 #cant have dups, the key gets updated with the latest assigned value
}
phone_no2 = phone_no.copy()
print(phone_no2)
# Accessing particular key
print(phone_no['Ram'])
print(phone_no)
phone_no['Mohan'] = 9999 #values are mutable but not keys
print(phone_no)
phone_no['Madhav'] = {1233,4564,6544} # we can add new key and value and value can be list as well
print(phone_no)
phone_no['Mohan'] = {'Mohan work':3454, 'Mohan Home':7878} #  value can be dictionary as well
print(phone_no)
#we cn remove element using pop and del functions
del phone_no['Ram']
phone_no.pop('Shyam')
print(phone_no)
# popitem deletes last added pair and returns key and value
print(phone_no.popitem()) 
# to access only keys
print(phone_no.keys()) 
print(phone_no.values()) 
print(phone_no.items()) 
# looping through dict
for i in phone_no:
    print(i)
    print(phone_no[i])



