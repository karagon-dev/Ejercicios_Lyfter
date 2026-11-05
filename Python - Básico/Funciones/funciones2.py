#1
def func1(parameter):
    local_variable = parameter
print(local_variable)
#NameError: name 'local_variable' is not defined
func1(10)
#2
global_variable = 10

def func2():
    global global_variable
    global_variable = 10+10
func2()
print(global_variable)