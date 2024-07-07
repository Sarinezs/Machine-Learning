def f1():
    print("lkasga")

def f2(name, surname):
    print(name+" "+surname)

def f3():
    friend = ["arm", "foat", "pang", "force", "most", "due", "nine", "natch"]
    print(friend[-6:-2]) #ไม่นับตัวเลขหลัง
    print(friend[2:6])

def f4():
    friend = ["arm", "foat", "pang", "force"]
    friend2 = ["most", "due", "nine", "natch"]
    try:
        friend.remove("arm1")
        print(friend)
    except ValueError:
        print("there is no name")
    except:
        print("Something else went wrong")
    
def f5():
    friend = ["arm", "foat", "pang", "force", "most", "due", "nine", "natch"]
    [print(friend[i]) for i in range(0,2)]
    
def f6():
    friend = ["arm", "foat", "pang", "force", "most", "due", "nine", "natch"]
    
    newlist = []
    
    
    # for i in friend:
    #     if "f" in i:
    #         newlist.append(i)
    
    newlist = ["asdgklnasdg" for i in friend if "a" in i]

    print(newlist)
   
def f7():
    #sort
    friend = ["arm", "foat", "pang", "force", "most", "due", "nine", "natch"]
    friend.sort()
    print(friend)
    
    
f7()