mylist = ['apple', 'banana', 'cherry']
print(mylist)
print(mylist[1])                                        # wyświetla element listy z indexem 1 (pamiętaj że liczy się od 0 co oznacza że 1 index to drugi element danej tablicy/listy)

thislist = ['apple', 'banana', 'cherry', 'cherry']
print(len(thislist))                                    # pokazuje ile elementów znajduje się w danej tablicy 

list1 = ['23', 'apple', 'True', 'male']                 # Tablica może przchowywać dane o różnych typach
print(type(list1))                                      # Wyświetla typy danych w tablicy <class 'list'>

ownlist = list(('apple', 'banana', 'cherry', 'cherry')) # inny sposób tworzenia tabilcy 
print(ownlist[2:3])                                     # wyświetla zakres wartości tablicy w polach o podanych indexach
 
thislist = list(('apple', 'banana', 'cherry', 'cherry'))
if 'apple' in thislist:
    print("Yes apple is in the fruit list")
    
# change the second item in list
thislist = ['Max', 'Filip', 'Marcin', 'Mateusz']
thislist[1] = 'Łukasz'
print(thislist)


