#1
name = "Kenny"
last_name = "Aragón"
full_name = name + last_name
print(full_name) #console wrote: KennyAragón

#2
number = 12
#add_str_int = name + number
#print(add_str_int) 
# #console wrote: TypeError: can only concatenate str (not "int") to str

#3
#add_int_str = number + name
#print(add_int_str) 
# #console wrote: TypeError: unsupported operand type(s) for +: 'int' and 'str'

#4 
numbers = [12, 13, 14]
names = ["Kenny", "John", "Micheal"]
add_list_list = numbers + names
print(add_list_list) #console wrote: [12, 13, 14, 'Kenny', 'John', 'Micheal']

#5
#add_str_list = name + names
#print(names) 
# #console wrote: TypeError: can only concatenate str (not "list") to str

#6
decimal = 5.2
add_float_int = decimal + number
print(add_float_int) #console wrote: 17.2

#7
yes = True
no = False
add_bool_bool = yes + no
print(add_bool_bool) #console wrote: 1

#aprendí que cuando se hace una operación aritmetica, true se interpreta como 1 y false 0
#en otras palabras: 1 + 0 = 1