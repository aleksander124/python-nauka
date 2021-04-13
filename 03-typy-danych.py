name = "Alek's project"             # można używać apostrofy w pomiedzy znakami cudzysłowia ale nie można używać enterów
name2 = 'Olek'                      # wyświetla tekst ale nie można używać apostrofów na przykłąd 'alek's channel' bo python tego nie zinterpretuje
name3 = """Alek's project

"""                                 # pomiędzy cudzysłowami można używać enterów i tekst zostanie wyświetlony w takiej samej formie co został zapisany 
print(name)

a = 10 
b = 2.5

print(a + b)

a = 1_000_000                       # zapis taki ułatwia znacząco czytanie liczb pyhon wyświetla bez podkreśleń

is_sky_blue = True
is_sun_blue = False                 # podczas gdy zmienna składa się z paru wyrazów rozdzielamy je "_" is_sky_blue

print(type(name))
print(type(a))
print(type(is_sky_blue))

first = 2 
secound = "3"

print(first + int(secound))        # konwersja zmiennej typu string na int czyli typ liczbowy 
