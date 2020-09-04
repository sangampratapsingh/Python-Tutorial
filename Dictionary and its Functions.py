#for denoting dictonary we use curly brackets:{}
#Lets take the following example:-
d1 = {"mutable":"can change", "immutable":"cannot change", "severe":"intense",
"unimaginable":"unthinkable", "Chcolate":{"A":"B", "C":"D", "E":"F"}}
print(type(d1))
print(d1)
print(d1["mutable"])
print(d1["Chcolate"] ["A"])


#The following are dictonary functions
#clear():Removes all the elements from the dictionary
#copy():Returns a copy of the dictionary
#fromkeys():Returns a dictionary with the specified keys and value
#get():Returns the value of the specified key
#items():Returns a list containing a tuple for each key value pair
#keys():Returns a list containing the dictionary's keys
#pop():Removes the element with the specified key
#popitem():Removes the last inserted key-value pair
#setdefault():Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update():Updates the dictionary with the specified key-value pairs
#values():Returns a list of all the values in the dictionary
