def dobule_decker():
    print('Starting the double decker')
    def inner_fun(name):
        print('inside the inner',name)
    return inner_fun #aikhane inner fun retun hocche
dobule_decker() #sudu double_decker ke call korteche
dobule_decker()('siyam') #aivabe inner call kora jay
#or 
work=dobule_decker() #aivabe o inner call kora jay
work("rahim")





## akhon fun er moode perametter hisabe arek fun patihe call
def do_something(perameter):
    perameter()

def coding():
    print('coding in python')

do_something(coding) #aikhane coding fun ke perametter hisabe pathaylam