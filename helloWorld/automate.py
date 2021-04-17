
# try and except error
def divideby(divide):
    try:
        return 42 / divide
    except:
        print('Error: 42 is not divisible by 0!')

print(divideby(2))      
print(divideby(0))            
print(divideby(12))      
print(divideby(42))


hello = ['alba', 'world', 'space', 'tulay']

hello[:3] = 'juls'

print(hello)




for num in range(0,100):
    if num % 2 != 0:
        
        print(num, end= " ")
        


       