print("What is your Word")
d1 = {"mutable":"can change", "immutable":"cannot change", "severe":"intense",
"unimaginable":"unthinkable", "Chcolate":{"A":"B", "C":"D", "E":"F"}}
word1 = input()

print("The meaning of your word is :", d1.get(word1))
