name = "kamil"

print(len(name))                # liczy ilość znaków w podanej zmiennej 
print(name.capitalize)          # metoda ta zamienia pierwszą literę na dużą literę 
print(name.upper)               # wszystkie litery zamienia na duże litery
print(name.lower)               # wszystkie litery zamienia na małe


print(name[0])                  # wyświetla pierwszą litere warotści zmiennej
print(name[0:4])                #wyświetla litery w przedziale 0-4
channel = "Jak nauczyć się programowania" 
print(channel.split(" "))

join_string = " " 
print(join_string.join(['jak', 'nauczyć', 'sie', 'programowania']))

print(name.startswith("K"))
print(name.startswith("k"))
print(name.rstrip("l"))
print(name.strip("l"))

name = "    Kamil "
print(name)
print(name.strip())             # usuwa nadmierne spacje

first_name = "kamil"
last_name = "kowalski"
print(first_name + " " + last_name)
join_string = " "
print(join_string.join([first_name, last_name]))
james_bond = 7
print(str(james_bond).zfill(3))

