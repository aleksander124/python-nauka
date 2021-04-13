light = input("Jakie jest światło? (red, green, yellow): ")

if light == 'red':
    print("Czekaj!")
elif light == 'yellow':
    print("przygotuj się!")
elif light == 'green':
    print("Jedź!")
else:
    print("Niewłaściwa wartość")
    
print("Jedź!") if light == 'green' else print("Czekaj!")
