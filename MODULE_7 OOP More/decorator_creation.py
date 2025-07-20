# decorator banayle bustbe inner fun lagbe
# aikhane @timer diyar karone jokhon get_fectirial call korchi tokhon get_fectoriyal
# perameter hisabe timer fun a work a geche then oi timer fun kaj kortecge..

def time(work):
    def inner():
       print('time started')
       work()
       print('time ended')
    return inner
@time
def get_fectoriyal():
    print('starting factorial')

get_fectoriyal()



#### perameter pathayle
  # এখন, get_fectoriyal হল inner ফাংশন। তাই, get_fectoriyal(10) কল করলে আসলে inner(10) কল হয়।
  # inner(10) এর ভিতরে:
  # 1.print('time started') হয়।
  # 2.work(10) কল হয়, যা মূল get_fectoriyal(10) ফাংশন।
  # 3.print('time ended') হয়।

def time(work):
    def inner(*args): #*args holo akadhik perameter pathanor jono
       print('time started')
       work(*args)
       print('time ended')
    return inner
@time
def get_fectoriyal(n):
    result=n*2
    print('starting factorial',result)

get_fectoriyal(10)
    